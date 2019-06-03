<template>
  <div class="video">
    <div class="main-video">
      <video controls src="/test.mp4" type="video/mp4"/>
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
import checkUsrMixin from '../mixins/checkUsrMixin.js'

export default {
  mixins: [checkUsrMixin],
  mounted: function(){
    let obj = this;
    this.videoElement = document.getElementsByTagName('video')[0];
    let video = document.querySelector("#face");

    axios.get(process.env.VUE_APP_API_URL + 'api/course/getvideo', {
      params: { id: this.$route.params.id }
    })
    .then(function(response) {
      if(obj.checkUsr(response.data)){
        obj.videoElement.src = '/' + response.data;
      }
    })
    .catch(function () {
      obj.$message.error('糟糕，哪里出了点问题！');
    });

    axios.get(process.env.VUE_APP_API_URL + 'api/comment/get', {
      params: { id: this.$route.params.id }
    })
    .then(function(response) {
      if(obj.checkUsr(response.data)){
        for(let i in response.data){
          obj.comment.push(response.data[i]);
        }
      }
    })
    .catch(function () {
      obj.$message.error('糟糕，哪里出了点问题！');
    });
 
    if(navigator.mediaDevices.getUserMedia) {       
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
      comment: []
    }
  },
  methods: {
    getEmotionData: function(){
      let face = document.querySelector("#face");
      if(face == null || face.paused || this.videoElement == '' || this.videoElement.paused || this.videoElement.ended) { return; }
      let obj = this;
      let currentImage = this.take_image();

      axios.get(process.env.VUE_APP_API_URL + 'api/member/getpic', {
        params: {
          usr: obj.$root.$data.usr,
        }
      })
      .then(function(response) {
        let compareImage = '';
        compareImage = 'data:image/png;base64,' + response.data;
        var compareParams = new URLSearchParams();
        compareParams.append('api_key', 'Os99MvSXhTAg7Ly4lvs34gZsTZgXBumH');
        compareParams.append('api_secret', 'hyHyuopDC-qm94LIg7DzrRlPDHv5KCto');
        compareParams.append('image_base64_1', currentImage);
        compareParams.append('image_base64_2', compareImage);
        axios({
          method: 'post',
          url: 'https://api-cn.faceplusplus.com/facepp/v3/compare',
          data: compareParams,
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
          withCredentials: false
        })
        .then(function (response) {
          console.log('人脸对比置信度：' + response.data.confidence);
          if(response.data.confidence > 60){
            var params = new URLSearchParams();
            params.append('api_key', 'Os99MvSXhTAg7Ly4lvs34gZsTZgXBumH');
            params.append('api_secret', 'hyHyuopDC-qm94LIg7DzrRlPDHv5KCto');
            params.append('image_base64', currentImage);
            params.append('return_attributes', 'emotion,eyegaze');
            axios({
              method: 'post',
              url: 'https://api-cn.faceplusplus.com/facepp/v3/detect',
              data: params,
              headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
              withCredentials: false
            })
            .then(function (response) {
              if(response.data['faces'].length != 0){ // 未检测到人脸就不发送请求了，这样对吗？
                let emotion = response.data['faces'][0]['attributes']['emotion']; //只考虑第一张人脸（应该是最大的那个）
                let eyegaze = response.data['faces'][0]['attributes']['eyegaze'];
                axios.get(process.env.VUE_APP_API_URL + 'api/focus/add', {
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
                    surprise: emotion.surprise,
                    position_x: (eyegaze.left_eye_gaze.position_x_coordinate + eyegaze.right_eye_gaze.position_x_coordinate)/2,
                    position_y: (eyegaze.left_eye_gaze.position_y_coordinate + eyegaze.right_eye_gaze.position_y_coordinate)/2,
                    vector_x: (eyegaze.left_eye_gaze.vector_x_component + eyegaze.right_eye_gaze.vector_x_component)/2,
                    vector_y: (eyegaze.left_eye_gaze.vector_y_component + eyegaze.right_eye_gaze.vector_y_component)/2,
                    vector_z: (eyegaze.left_eye_gaze.vector_z_component + eyegaze.right_eye_gaze.vector_z_component)/2,
                  }
                });
              }
            })
            .catch(function() {
              obj.$message.error('糟糕，哪里出了点问题！');
            });
          }
          else{
            obj.$message.error('请本人前来听课！');
          }
        })
        .catch(function() {
          obj.$message.error('糟糕，哪里出了点问题！');
        });
      })
      .catch(function () {
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

