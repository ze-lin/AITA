<template>
  <div class="course-management">
    <div class="update-course">
      <el-form ref="form" :model="form" label-width="100px">
        <el-form-item label="课程名称">
          <el-input v-model="form.title" placeholder="请输入课程名称"></el-input>
        </el-form-item>
        <el-form-item label="课程分类">
          <el-select v-model="form.genre" placeholder="请选择课程分类">
            <el-option label="计算机" value="Computer"></el-option>
            <el-option label="心理学" value="Mind"></el-option>
            <el-option label="社会科学" value="Social"></el-option>
            <el-option label="数学与自然科学" value="Math"></el-option>
            <el-option label="历史学" value="History"></el-option>
            <el-option label="文学与艺术" value="Art"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="预计需要时间">
          <el-input v-model="form.time" placeholder="请输入完成课程大致需要时间（如：24小时）"></el-input>
        </el-form-item>
        <el-form-item label="输入考试ID">
          <el-input v-model="form.exam" placeholder="关于考试ID生成的说明"></el-input>
          <div class="tip">请前往<b><a target="_blank" href="https://www.wjx.cn/app/exam.aspx" >问卷星</a></b>生成。将生成的考试ID填入上方输入框</div>
        </el-form-item>
        <el-upload ref="upload"
          action="http://127.0.0.1:5000/upload"
          :on-remove="handleRemove"
          :before-upload="beforeUpload"
          :on-success="onSuccess">
          <el-button size="small" type="primary">点击上传文件</el-button>
          <div slot="tip" class="el-upload__tip">请上传一个md文件作为阅读材料和一个mp4文件作为课程视频</div>
        </el-upload>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">立即创建</el-button>
          <el-button @click="clear">取消</el-button>
        </el-form-item>
      </el-form>
    </div>
    <div class="classes">
      <h1>您的课程</h1>
      <el-table :data="classes" stripe style="width: 100%">
        <el-table-column prop="title" label="课程名称" width="180"></el-table-column>
        <el-table-column prop="date" sortable label="开课时间" width="120"></el-table-column>
        <el-table-column prop="time" sortable label="所用时间" width="100"></el-table-column>
        <el-table-column prop="view" sortable label="浏览人次" width="100"></el-table-column>
        <el-table-column prop="genre" label="分类" width="100"></el-table-column>
        <el-table-column prop="exam" label="考试ID" width="120"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button @click="checkResult(scope.row)" type="text" size="small">结果</el-button>
            <el-button @click="removeCourse(scope.row)" type="text" size="small">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data(){
    return {
      form: {
        title: '',
        genre: '',
        time: '',
        exam: '',
        video: '',
        article: ''
      },
      fileReady: false,
      classes: []
    }
  },
  methods: {
    handleRemove: function(){
      this.fileReady = false;
    },
    onSubmit: function(){ // TODO: 如果是更新课程呢？
      let obj = this;

      if(this.form.title != '' && this.form.genre != '' && this.form.time != '' && this.form.exam != '' && this.fileReady){
        axios.get('http://127.0.0.1:5000/submitclass', {
          params: {
            title: this.form.title,
            genre: this.form.genre,
            exam: this.form.exam,
            time: this.form.time,
            teacher: this.$root.$data.usr,
            video: this.form.video,
            article: this.form.article
          }
        })
        .then(function() {
          obj.$message({
            message: '成功创建课程！',
            type: 'success'
          });
          obj.refreshCourse();
          obj.clear();
        })
        .catch(function () {
          obj.$message.error('糟糕，哪里出了点问题！');
        });
      }
      else{
        this.$message.error('请将课程信息填写完整！');
      }
    },
    clear: function(){
      this.form = {
        title: '',
        genre: '',
        time: '',
        exam: '',
        video: '',
        article: ''
      };
      this.$refs.upload.clearFiles();
    },
    beforeUpload(file){
      let pattern = /^[0-9a-zA-Z]*$/;
      let fileName = file.name;
      if(fileName.indexOf('.') == fileName.lastIndexOf('.')){
        let nameList = fileName.split('.');
        for(let i in nameList[0]){ // 确认文件名中只有数字和英文字母
          if(!pattern.test(i)){
            this.$message.error('文件前缀名中只允许包含数字和英文字母！');
            return false;
          }
        }
        if(nameList[1] == 'md' || nameList[1] == 'mp4'){
          if(nameList[1] == 'md'){ // 当上传的文件是md
            this.form.article = fileName;
          }
          else{
            this.form.video = fileName;
          }
        }
        else{
          this.$message.error('文件后缀名只允许是md或mp4！');
          return false;
        }
      }
      else{
        this.$message.error('文件名只允许包含一个“.”！');
        return false;
      }
      return true;
    },
    onSuccess(response, file, fileList){
      if(fileList.length == 2){
        this.fileReady = true;
      }
    },
    checkResult: function(row){
      this.$router.push('/result/' + row.id);
    },
    removeCourse: function(row){
      let obj = this;

      axios.get('http://127.0.0.1:5000/deleteclass', {
        params: {
          id: row.id
        }
      })
      .then(function() {
        obj.$message({
          message: '成功删除课程！',
          type: 'success'
        });
        obj.refreshCourse();
      })
      .catch(function () {
        obj.$message.error('糟糕，哪里出了点问题！');
      });
    },
    refreshCourse: function(){
      let obj = this;
      
      axios.get('http://127.0.0.1:5000/getclass', {
        params: {
          teacher: this.$root.$data.usr
        }
      })
      .then(function(response) {
        obj.classes = [];
        for(let i in response.data){
          obj.classes.push(response.data[i]);
        }
      })
      .catch(function () {
        obj.$message.error('糟糕，哪里出了点问题！');
      });
    }
  },
  mounted: function(){
    if(this.$root.$data.usr == ''){
      this.$message.error('请先进行登录或注册！');
      //this.$router.push('/');
    }
    else{
      this.refreshCourse();
    }
  }
}
</script>

<style scoped>
.update-course{
  width: 40%;
  margin-left: 20%;
  margin-right: 20%;
  margin-top: 2%;
  padding: 2% 10% 1% 8%;
  box-shadow: 2px 2px 10px rgb(220, 220, 220);
}
.el-select{
  float: left;
}
.classes{
  width: 58%;
  text-align: center;
  margin-left: 20%;
  margin-right: 20%;
  margin-top: 2%;
}
.tip{
  margin: 0;
  float: left;
}
.tip a{
  text-decoration: none;
}
</style>