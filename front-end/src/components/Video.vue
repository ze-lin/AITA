<template>
  <div class="video">
    <div class="main-video">
      <video controls src="http://localhost:8080/video.mp4" type="video/mp4"/>
      <p>请确认您的摄像头打开后再进行观看视频学习，否则您的学习结果将不会被记录</P>
      <video autoplay="true" id="face"></video>
    </div>
    <div class="comment">
      <el-table :data="comment">
        <el-table-column type="expand">
          <template slot-scope="props">
            <el-form label-position="left" inline class="table-expand">
              <el-form-item>
                <span>{{ props.row.content }}</span>
              </el-form-item>
            </el-form>
          </template>
        </el-table-column>
        <el-table-column sortable label="开始时间" prop="startTime"></el-table-column>
        <el-table-column sortable label="结束时间" prop="endTime"></el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  mounted: function(){
    let obj = this;
    this.videoElement = document.getElementsByTagName('video')[0];
    let video = document.querySelector("#face");

    axios.get('http://127.0.0.1:5000/getvideo', {
      params: {
        id: this.$route.params.id
      }
    })
    .then(function(response) {
      obj.videoElement.src = 'http://localhost:8080/' + response.data;
    })
    .catch(function () {
      obj.$message.error('糟糕，哪里出了点问题！');
    });

    axios.get('http://127.0.0.1:5000/getcomment', {
      params: {
        id: this.$route.params.id
      }
    })
    .then(function(response) {
      for(let i in response.data){
        obj.comment.push(response.data[i]);
      }
    })
    .catch(function () {
      obj.$message.error('糟糕，哪里出了点问题！');
    });
 
    if (navigator.mediaDevices.getUserMedia) {       
        navigator.mediaDevices.getUserMedia({video: true})
      .then(function(stream) {
        video.srcObject = stream;
      })
      .catch(function() {
        obj.$message.error('如果您拒绝打开摄像头，则您的学习结果将不会被记录');
      });
    }
    setInterval(this.getEmotionData, 1000);
  },
  data(){
    return {
      videoElement: '',
      comment: [{
        startTime: '00: 00',
        endTime: '10: 00',
        content: 'Hello World'
      }]
    }
  },
  methods: {
    getEmotionData: function(){
      let face = document.querySelector("#face");
      if(face == null || face.paused || this.videoElement == '' || this.videoElement.paused || this.videoElement.ended){ // 如果暂停，停止发送请求
        return;
      }
      let obj = this;
      var params = new URLSearchParams();
      params.append('api_key', 'Os99MvSXhTAg7Ly4lvs34gZsTZgXBumH');
      params.append('api_secret', 'hyHyuopDC-qm94LIg7DzrRlPDHv5KCto');
      params.append('image_base64', this.take_image());
      params.append('return_attributes', 'emotion');

      axios({
        method: 'post',
        url: 'https://api-cn.faceplusplus.com/facepp/v3/detect',
        data: params,
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
      })
      .then(function (response) {
        if(response.data['faces'].length != 0){ // 未检测到人脸就不发送请求了
          let emotion = response.data['faces'][0]['attributes']['emotion'];
          axios.get('http://127.0.0.1:5000/addfocus', {
            params: {
              id: obj.$route.params.id,
              usr: obj.$root.$data.usr,
              time: obj.videoElement.currentTime,
              anger: emotion.anger,
              neutral: emotion.neutral,
              disgust: emotion.disgust,
              fear: emotion.fear,
              happiness: emotion.happiness,
              sadness: emotion.sadness,
              surprise: emotion.surprise
            }
          });
        }
      })
      .catch(function() {
        obj.$message.error('糟糕，哪里出了点问题！');
      });
    },
    take_image: function(){
      let canvas = document.createElement('canvas');
      let video = document.getElementById('face');
      let scale = 0.25;
      canvas.width = video.videoWidth * scale;
      canvas.height = video.videoHeight * scale;

      canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
      let data = canvas.toDataURL();
      return data;
    }
  }
}
</script>

<style scoped>
.video{
  width: 100%;
  height: 100%;
}
.main-video{
  width: 60%;
  float: left;
}
.comment{
  float: right;
  height: 100%;
  width: 40%;
}
video {
  width: 100%;
  display: block;
}
.table-expand {
  font-size: 0;
}
.table-expand label {
  width: 90px;
  color: #99a9bf;
}
.table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
}
</style>

