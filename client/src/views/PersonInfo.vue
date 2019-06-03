<template>
  <div class="personal">
    <div class="info">
      <el-card class="box-card" shadow="always">
        <div slot="header" class="clearfix">
          <span class="text">用户信息</span>
          <el-button class="in-btn" @click="signout()" type="text">退出登录</el-button>
        </div>
        <el-form label-width="80px" :model="info" class="info-form">
          <el-form-item label="用户名">
            <el-input :disabled="true" v-model="info.usr"></el-input>
          </el-form-item>
          <el-form-item label="用户身份">
            <el-input :disabled="true" v-model="info.role"></el-input>
          </el-form-item>
          <el-form-item label="注册时间">
            <el-input :disabled="true" v-model="info.date"></el-input>
          </el-form-item>
          <el-form-item label="用户密码">
            <el-input placeholder="如不需要修改，请置为空" v-model="info.pwd" show-password></el-input>
          </el-form-item>
        </el-form>
        <el-upload
          :action="computeActionURL('api/member/updateinfo')"
          list-type="picture-card"
          ref="upload"
          :auto-upload='false'
          :limit=1
          :data='info'
          :on-preview="handlePictureCardPreview"
          :on-exceed="HandleExceed"
          :file-list="fileList"
          :with-credentials='true'
          :on-success='HandleSuccess'>
          <i class="el-icon-plus"></i>
        </el-upload>
        <el-dialog :visible.sync="dialogVisible">
          <img width="100%" :src="dialogImageUrl" alt="">
        </el-dialog>
        <el-button @click="update" class="update" type="primary">确认更新</el-button>
      </el-card>
    </div>
    <div class="table">
      <h1>参与课程完成度</h1>
      <el-progress class="complete" :text-inside="true" :stroke-width="18" :percentage="totalScore"></el-progress>
      <el-table :data="classes" stripe style="width: 100%">
        <el-table-column prop="title" label="课程名称" width="120"></el-table-column>
        <el-table-column prop="teacher" label="任课教师" width="100"></el-table-column>
        <el-table-column prop="date" sortable label="开课时间" width="110"></el-table-column>
        <el-table-column prop="time" label="所用时间" width="90"></el-table-column>
        <el-table-column prop="view" label="浏览人次" width="90"></el-table-column>
        <el-table-column prop="genre" sortable label="分类" width="100"></el-table-column>
        <el-table-column prop="exam" sortable label="考试ID" width="100"></el-table-column>
        <el-table-column prop="complete" label="状态" width="80">
          <template slot-scope="scope">
            <el-progress type="circle" :width="40" :status="computeStatus(scope.row.complete)" :percentage="scope.row.complete"></el-progress>
          </template>
        </el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button @click="joinCourse(scope.row)" type="text" size="small">参加</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import checkUsrMixin from '../mixins/checkUsrMixin.js'
import joinCourseMixin from '../mixins/joinCourseMixin'
import computeActionURLMixin from '../mixins/computeActionURLMixin.js'
import md5 from 'js-md5'

export default {
  mixins: [checkUsrMixin, joinCourseMixin, computeActionURLMixin],
  data() {
    return {
      info: {
        usr: '',
        role: '',
        date: '',
        pwd: ''
      },
      totalScore: 0,
      classes: [],
      dialogImageUrl: '',
      dialogVisible: false,
      fileList: []
    }
  },
  mounted: function(){
    this.refreshUsrInfo();
    this.refreshCompleteness();
  },
  methods: {
    computeStatus: function(data){
      if(data > 60){ return 'success'; }
      else{ return 'exception'; }
    },
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },
    HandleSuccess: function(){
      this.$message({ message: '成功更新！', type: 'success' });
      this.$refs.upload.clearFiles();
      this.fileList = [];
      this.refreshUsrInfo();
    },
    HandleExceed: function(){
      this.$message.error('上传图片数量超出限制，只能上传一张！');
    },
    update: function(){
      if(this.$refs.upload.uploadFiles.length == 0){
        this.$message.error('用户头像不能为空。');
        this.$refs.upload.clearFiles();
        this.fileList = [];
        this.refreshUsrInfo();
      }
      else if(this.info.pwd == '' && this.$refs.upload.uploadFiles[0].status == 'success'){
        this.$message('没有需要更新的信息！');
      }
      else{ // At least one of them need to be updated
        let uploadFile = this.$refs.upload.uploadFiles[0];
        let obj = this;
        if(this.info.pwd.length < 6 && this.info.pwd != ''){
          this.$message.error('您输入的密码过于简单（请确保密码长度>6）');
        }
        if(uploadFile.status == 'ready'){
          var xhr = new XMLHttpRequest;
          xhr.responseType = 'blob';

          xhr.onload = function() {
            var recoveredBlob = xhr.response;
            var reader = new FileReader;
            reader.onload = function() {

              var compareParams = new URLSearchParams();
              compareParams.append('api_key', 'Os99MvSXhTAg7Ly4lvs34gZsTZgXBumH');
              compareParams.append('api_secret', 'hyHyuopDC-qm94LIg7DzrRlPDHv5KCto');
              compareParams.append('image_base64_1', obj.$refs.upload.fileList[0].url);
              compareParams.append('image_base64_2', reader.result);
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
                  obj.info.pwd = md5(obj.info.pwd);
                  obj.$refs.upload.submit();
                }
                else{
                  obj.$message.error('请上传同一个人的照片！');
                  obj.$refs.upload.clearFiles();
                  obj.fileList = [];
                  obj.refreshUsrInfo();
                }
              })
              .catch(function() {
                obj.$message.error('糟糕，哪里出了点问题！');
              });
            };
            reader.readAsDataURL(recoveredBlob);
          };
          xhr.open('GET', uploadFile.url);
          xhr.send();
        }
        if(uploadFile.status == 'success' && this.info.pwd != ''){
          axios.get(process.env.VUE_APP_API_URL + 'api/member/updatepwd', {
            params: {
              pwd: md5(this.info.pwd),
              usr: obj.$root.$data.usr,
              }
          })
          .then(function(response) {
            obj.$message({ message: '成功更新！', type: 'success' });
            obj.info.pwd = '';
          })
          .catch(function () {
            obj.$message.error('糟糕，哪里出了点问题！');
          });
        }
      }
    },
    computeTotalComplete: function(){
      let score = 0;
      for(let course of this.classes){
        score += course.complete;
      }
      if(this.classes.length < 1){ this.totalScore = 0; }
      else{ return this.totalScore = score/this.classes.length }
    },
    refreshUsrInfo: function(){
      let obj = this;
      axios.get(process.env.VUE_APP_API_URL + 'api/member/getinfo', {
        params: {
          usr: obj.$root.$data.usr,
        }
      })
      .then(function(response) {
        if(obj.checkUsr(response.data)){
          obj.info = response.data;
          obj.info.pwd = '';
        }
      })
      .catch(function () {
        obj.$message.error('糟糕，哪里出了点问题！');
      });

      axios.get(process.env.VUE_APP_API_URL + 'api/member/getpic', {
        params: {
          usr: obj.$root.$data.usr,
        }
      })
      .then(function(response) {
        if(obj.checkUsr(response.data)){
          obj.fileList.push({ name:'usr.png', url: 'data:image/png;base64,'+response.data });
        }
      })
      .catch(function () {
        obj.$message.error('糟糕，哪里出了点问题！');
      });
    },
    refreshCompleteness: function(){
      let obj = this;
      axios.get(process.env.VUE_APP_API_URL + 'api/complete/get',{
        params: {
          usr: obj.$root.$data.usr,
        }
      })
      .then(function(response) {
        if(obj.checkUsr(response.data)){
          obj.classes = [];
          for(let i in response.data){
            response.data[i].complete = parseInt(response.data[i].complete);
            console.log(response.data[i].complete);
            obj.classes.push(response.data[i]);
          }
          obj.computeTotalComplete();
        }
      })
      .catch(function () {
        obj.$message.error('糟糕，哪里出了点问题！');
      });
    },
    signout: function(){
      axios.get(process.env.VUE_APP_API_URL + 'auth/logout');
      this.$router.push('/auth');
    }
  }
}
</script>

<style scoped>
.info{
  width: 58%;
  text-align: center;
  margin-left: 20%;
  margin-right: 20%;
  margin-top: 2%;
}
.update{
  margin-top: 2%;
}
.table{
  width: 70%;
  text-align: center;
  margin-left: 14%;
  margin-right: 14%;
  margin-top: 2%;
}
.text{
  display: block;
  text-align: left;
  font-size: 1em;
  height: 40px;
  line-height: 40px;
}
.in-btn{
  float: right;
  padding: 0;
  position: relative;
  bottom: 25px;
}
.avater{
  float: right;
  height: 150px;
  margin: 0;
  padding: 0;
}
.info-form{
  width: 50%;
  float: left;
}
.complete{
  width: 60%;
  margin-left: 20%;
  margin-top: 1%;
  margin-bottom: 1%;
}
</style>
