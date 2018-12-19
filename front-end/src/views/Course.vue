<template>
  <div class="course">
    <div class="container">
      <div class="video-container">
        <h1>摄像头实时获取人脸内容</h1>
        <video autoplay="true" id="videoElement"></video>
      </div>
      <div class="result">
        <el-progress :text-inside="true" :stroke-width="25" :percentage="emotion.anger" color="rgb(128, 128, 128, 0.7)"></el-progress>
        <el-progress :text-inside="true" :stroke-width="25" :percentage="emotion.disgust" color="rgb(165, 42, 42, 0.7)"></el-progress>
        <el-progress :text-inside="true" :stroke-width="25" :percentage="emotion.fear" color="rgb(255, 215, 0, 0.7)"></el-progress>
        <el-progress :text-inside="true" :stroke-width="25" :percentage="emotion.happiness" color="rgb(244, 164, 96, 0.7)"></el-progress>
        <el-progress :text-inside="true" :stroke-width="25" :percentage="emotion.neutral" color="rgb(34, 139, 34, 0.7)"></el-progress>
        <el-progress :text-inside="true" :stroke-width="25" :percentage="emotion.sadness" color="rgb(0, 139, 139, 0.7)"></el-progress>
        <el-progress :text-inside="true" :stroke-width="25" :percentage="emotion.surprise" color="rgb(147, 112, 219, 0.7)"></el-progress>
      </div>
      <div class="title">
        <p>Anger</p>
        <p>Disgust</p>
        <p>Fear</p>
        <p>Happiness</p>
        <p>Neutral</p>
        <p>Sadness</p>
        <p>Surprise</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data(){
    return {
      emotion: {
        anger: 10,
        disgust: 20,
        fear: 30,
        happiness: 40,
        neutral: 50,
        sadness: 60,
        surprise: 70
      }
    }
  },
  mounted: function(){
    let video = document.querySelector("#videoElement");
    let obj = this;
 
    if (navigator.mediaDevices.getUserMedia) {       
        navigator.mediaDevices.getUserMedia({video: true})
      .then(function(stream) {
        video.srcObject = stream;
      })
      .catch(function() {
        obj.$message.error('糟糕，出错了！');
      });
    }
    setInterval(this.getEmotionData, 1000);
  },
  methods: {
    getEmotionData: function(){
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
        obj.emotion = response.data['faces'][0]['attributes']['emotion'];
      })
      .catch(function() {
        obj.$message.error('糟糕，哪里出了点问题！');
      });
    },
    take_image: function(){
      let canvas = document.createElement('canvas');
      let video = document.getElementById('videoElement');
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
.title{
  width: 7%;
  float: right;
  margin-top: 8%;
}
.title p{
  margin: 0;
  height: 45px;
  font-weight: 400;
}
.container{
  margin-top: 3%;
}
.video-container {
  height: 80%;
  width: 40%;
  float: left;
  margin-left: 6%;
  margin-top: 2%;
}
video {
  height: 50%;
  width: 100%;
}
.result{
  margin-top: 8%;
  width: 35%;
  height: 50%;
  float: right;
  margin-right: 8%;
}
.el-progress{
  margin-top: 20px;
  margin-right: 5%;
}
</style>


