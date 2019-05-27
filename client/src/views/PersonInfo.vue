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
            <el-input v-model="info.role"></el-input>
          </el-form-item>
          <el-form-item label="注册时间">
            <el-input :disabled="true" v-model="info.date"></el-input>
          </el-form-item>
        </el-form>
        <img class="avater" :src="ImageSource" alt="图片读取失败" />
      </el-card>
    </div>

    <div class="table">
      <h1>您的收藏</h1>
      <el-table :data="classes" stripe style="width: 100%">
        <el-table-column prop="title" label="课程名称" width="150"></el-table-column>
        <el-table-column prop="teacher" label="任课教师" width="120"></el-table-column>
        <el-table-column prop="date" sortable label="开课时间" width="120"></el-table-column>
        <el-table-column prop="time" sortable label="所用时间" width="100"></el-table-column>
        <el-table-column prop="view" sortable label="浏览人次" width="100"></el-table-column>
        <el-table-column prop="genre" sortable label="分类" width="120"></el-table-column>
        <el-table-column prop="exam" sortable label="考试ID" width="120"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button @click="join(scope.row)" type="text" size="small">参加</el-button>
            <el-button @click="deleteCollection(scope.row)" type="text" size="small">移除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import checkUsrMixin from '../mixins/checkUsrMixin.js'

export default {
  mixins: [checkUsrMixin],
  data() {
    return {
      info: {
        usr: '',
        role: '',
        date: '',
        pwd: ''
      },
      classes: [],
      ImageSource: 'data:image/png;base64,'
    }
  },
  mounted: function(){
    this.refreshUsrInfo();
    this.refreshCollection();
  },
  methods: {
    refreshUsrInfo: function(){
      let obj = this;
      axios.get(process.env.VUE_APP_API_URL + 'usr/getinfo')
      .then(function(response) {
        if(obj.checkUsr(response.data)){
          obj.info = response.data;
        }
      })
      .catch(function () {
        obj.$message.error('糟糕，哪里出了点问题！');
      });

      axios.get(process.env.VUE_APP_API_URL + 'usr/getpic')
      .then(function(response) {
        if(obj.checkUsr(response.data)){
          obj.ImageSource += response.data;
        }
      })
      .catch(function () {
        obj.$message.error('糟糕，哪里出了点问题！');
      });
    },
    refreshCollection: function(){
      let obj = this;
      axios.get(process.env.VUE_APP_API_URL + 'collection/get')
      .then(function(response) {
        if(obj.checkUsr(response.data)){
          obj.classes = [];
          for(let i in response.data){
            obj.classes.push(response.data[i]);
          }
        }
      })
      .catch(function () {
        obj.$message.error('糟糕，哪里出了点问题！');
      });
    },
    signout: function(){
      axios.get(process.env.VUE_APP_API_URL + 'auth/logout');
      this.$router.push('/auth');
    },
    deleteCollection: function(row){
      let obj = this;
      axios.get(process.env.VUE_APP_API_URL + 'collection/delete', {
        params: {
          id: row.id,
        }
      })
      .then(function(response) {
        if(obj.checkUsr(response.data)){
          obj.refreshCollection();
          obj.$message({ message: '成功移除！', type: 'success' });
        }
      })
      .catch(function () {
        obj.$message.error('糟糕，哪里出了点问题！');
      });
    },
    join(row){
      let obj = this;
      axios.get(process.env.VUE_APP_API_URL + 'course/view', {
        params: { id: row.id }
      })
      .then(function(response) {
        if(obj.checkUsr(response.data)){
          obj.$router.push('/course/video/' + row.id);
        }
      })
      .catch(function () {
        obj.$message.error('糟糕，哪里出了点问题！');
      });
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
</style>
