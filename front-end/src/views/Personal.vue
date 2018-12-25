<template>
  <div class="personal">
    <div class="table">
      <el-card class="box-card" shadow="always">
        <div slot="header" class="clearfix">
          <span class="text title">用户信息</span>
          <el-button class="in-btn" @click="signout()" type="text">退出登录</el-button>
        </div>
        <div class="text item"><b>用户名：</b>{{ info.usr }}</div>
        <div class="text item"><b>用户身份：</b>{{ info.role }}</div>
        <div class="text item"><b>注册时间：</b>{{ info.date }}</div>
        <div class="text item"><b>密码：</b>(添加修改、添加退出登录)
        <el-button style="float: right; padding: 3px 0" type="text">立即更新</el-button>
        </div>
      </el-card>
    </div>
    <div class="table">
      <h1>您的收藏</h1>
      <el-table :data="classes" stripe style="width: 100%">
        <el-table-column prop="title" sortable label="课程名称" width="150"></el-table-column>
        <el-table-column prop="teacher" sortable label="任课教师" width="120"></el-table-column>
        <el-table-column prop="date" sortable label="开课时间" width="120"></el-table-column>
        <el-table-column prop="time" sortable label="所用时间" width="100"></el-table-column>
        <el-table-column prop="view" sortable label="浏览人数" width="100"></el-table-column>
        <el-table-column prop="genre" sortable label="分类" width="120"></el-table-column>
        <el-table-column prop="exam" sortable label="考试ID" width="120"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button @click="see(scope.row)" type="text" size="small">查看</el-button>
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
      classes: []
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
        // console.log(response.data);
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
          id: row.id
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
    }
  }
}
</script>

<style scoped>
.table{
  width: 58%;
  text-align: center;
  margin-left: 20%;
  margin-right: 20%;
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
</style>
