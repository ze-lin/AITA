<template>
  <div class="personal">
    <div class="info">
      <el-card class="box-card" shadow="always">
        <div slot="header" class="clearfix">
          <span class="text">用户信息</span>
          <el-button class="in-btn" @click="signout()" type="text">退出登录</el-button>
        </div>
        <div class="text"><b>用户名：</b>{{ info.usr }}</div>
        <div class="text"><b>用户身份：</b>{{ info.role }}</div>
        <div class="text"><b>注册时间：</b>{{ info.date }}</div>
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

export default {
  data() {
    return {
      info: {
        usr: '',
        role: '',
        date: '',
        pwd: ''
      },
      classes: [],
      ImageSource: 'data:image/png;base64, '
    }
  },
  mounted: function(){
    if(this.$root.$data.usr == ''){
      this.$message.error('请先进行登录或注册！');
      this.$router.push('/');
    }
    else{
      this.refreshUsrInfo();
      this.refreshCollection();
    }
  },
  methods: {
    refreshUsrInfo: function(){
      let obj = this;

      axios.get('http://127.0.0.1:5000/getusrinfo', {
        params: {
          usr: this.$root.$data.usr
        }
      })
      .then(function(response) {
        obj.info = response.data;
      })
      .catch(function () {
        obj.$message.error('糟糕，哪里出了点问题！');
      });

      axios.get('http://127.0.0.1:5000/getusrpic', {
        params: {
          usr: this.$root.$data.usr
        }
      })
      .then(function(response) {
        console.log(response.data);
        obj.ImageSource += response.data;
      })
      .catch(function () {
        obj.$message.error('糟糕，哪里出了点问题！');
      });
    },
    refreshCollection: function(){
      let obj = this;

      axios.get('http://127.0.0.1:5000/getcollection', {
        params: {
          usr: this.$root.$data.usr
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
    },
    signout: function(){
      this.$root.$data.usr = '';
      this.$root.$data.role = '';
      this.$router.push('/');
    },
    deleteCollection: function(row){
      let obj = this;

      axios.get('http://127.0.0.1:5000/deletecollection', {
        params: {
          id: row.id,
          usr: this.$root.$data.usr
        }
      })
      .then(function() {
        obj.refreshCollection();
        obj.$message({
          message: '成功移除！',
          type: 'success'
        });
      })
      .catch(function () {
        obj.$message.error('糟糕，哪里出了点问题！');
      });
    },
    join(row){
      let obj = this;
      axios.get('http://127.0.0.1:5000/view', {
        params: {
          id: row.id 
        }
      })
      .then(function() {
        obj.$router.push('/learn/video/' + row.id);
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
  position: relative;
  bottom: 100px;
  height: 100px;
  margin: 0;
  padding: 0;
}
</style>
