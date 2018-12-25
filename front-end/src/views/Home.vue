<template>
  <div class="home">
    <div id="search">
      添加对 课程名称 任课教师 分类 进行搜索
    </div>
    <el-table :data="classes" stripe style="width: 100%">
      <el-table-column prop="title" sortable label="课程名称" width="120"></el-table-column>
      <el-table-column prop="teacher" sortable label="任课教师" width="120"></el-table-column>
      <el-table-column prop="date" sortable label="开课时间" width="120"></el-table-column>
      <el-table-column prop="time" sortable label="所用时间" width="100"></el-table-column>
      <el-table-column prop="view" sortable label="浏览人数" width="100"></el-table-column>
      <el-table-column prop="genre" sortable label="分类" width="100"></el-table-column>
      <el-table-column prop="exam" sortable label="考试ID" width="120"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button @click="join(scope.row)" type="text" size="small">参加</el-button>
          <el-button @click="addCollection(scope.row)" type="text" size="small">收藏</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  methods: {
    addCollection(row) {
      let obj = this;

      axios.get('http://127.0.0.1:5000/addcollection', {
        params: {
          usr: this.$root.$data.usr,
          id: row.id
        }
      })
      .then(function() {
        obj.$message({
          message: '成功收藏！',
          type: 'success'
        });
      })
      .catch(function () {
        obj.$message.error('糟糕，哪里出了点问题！');
      });
    },
    join(row){
      console.log(row);
      //this.$router.push('/learn');
    },
    refreshCourse: function(){
      let obj = this;

      axios.get('http://127.0.0.1:5000/getclass')
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
  data() {
    return {
      classes: []
    }
  },
  mounted: function(){
    if(this.$root.$data.usr == ''){
      this.$message.error('请先进行登录或注册！');
      this.$router.push('/');
    }
    else{
      this.refreshCourse();
    }
  }
}
</script>

<style scoped>
.home{
  width: 58%;
  text-align: center;
  margin-left: 20%;
  margin-right: 20%;
  margin-top: 2%;
}
</style>
