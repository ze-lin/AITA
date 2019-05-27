<template>
  <div class="home">
    <el-table :data="classes" stripe style="width: 100%">
      <el-table-column prop="title" label="课程名称" width="150"></el-table-column>
      <el-table-column prop="teacher" label="任课教师" width="120"></el-table-column>
      <el-table-column prop="date" sortable label="开课时间" width="120"></el-table-column>
      <el-table-column prop="time" sortable label="所用时间" width="100"></el-table-column>
      <el-table-column prop="view" sortable label="浏览人次" width="100"></el-table-column>
      <el-table-column prop="genre" sortable label="分类" width="100"></el-table-column>
      <el-table-column prop="exam" label="考试ID" width="120"></el-table-column>
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
import checkUsrMixin from '../mixins/checkUsrMixin.js'

export default {
  mixins: [checkUsrMixin],
  methods: {
    addCollection(row) {
      let obj = this;

      axios.get(process.env.VUE_APP_API_URL + 'collection/add', {
        params: {
          id: row.id
        }
      })
      .then(function(response) {
        if(obj.checkUsr(response.data)){
          obj.$message({ message: '成功收藏！', type: 'success' });
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
    },

    refreshCourse: function(){
      let obj = this;
      axios.get(process.env.VUE_APP_API_URL + 'course/getall')
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
    this.refreshCourse();
  }
}
</script>

<style scoped>
.home{
  width: 70%;
  text-align: center;
  margin-left: 14%;
  margin-right: 14%;
  margin-top: 2%;
}
</style>
