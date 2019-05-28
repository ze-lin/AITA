<template>
  <div class="home">
    <el-form :inline="true" :model="searchForm" class="demo-form-inline">
      <el-form-item label="课程名称">
        <el-input v-model="searchForm.title" placeholder="课程名称"></el-input>
      </el-form-item>
      <el-form-item label="课程分类">
        <el-select v-model="searchForm.genre" clearable placeholder="请选择课程分类">
          <el-option label="计算机" value="Computer"></el-option>
          <el-option label="经济学" value="Economy"></el-option>
          <el-option label="社会科学" value="Social"></el-option>
          <el-option label="数学" value="Math"></el-option>
          <el-option label="历史学" value="History"></el-option>
          <el-option label="文学与艺术" value="Art"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="searchCourse">搜索</el-button>
      </el-form-item>
    </el-form>
    <el-table :data="displayCourses" stripe style="width: 100%">
      <el-table-column prop="title" label="课程名称" width="150"></el-table-column>
      <el-table-column prop="teacher" label="任课教师" width="120"></el-table-column>
      <el-table-column prop="date" sortable label="开课时间" width="120"></el-table-column>
      <el-table-column prop="time" sortable label="所用时间" width="100"></el-table-column>
      <el-table-column prop="view" sortable label="浏览人次" width="100"></el-table-column>
      <el-table-column prop="genre" sortable label="分类" width="100"></el-table-column>
      <el-table-column prop="exam" label="考试ID" width="120"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button @click="joinCourse(scope.row)" type="text" size="small">参加</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import axios from 'axios'
import checkUsrMixin from '../mixins/checkUsrMixin'
import joinCourseMixin from '../mixins/joinCourseMixin'

export default {
  mixins: [checkUsrMixin, joinCourseMixin],
  methods: {
    searchCourse: function(){
      let tmpCourses = this.courses.slice();

      if(this.searchForm.title != ''){
        for(let course of this.courses){
          if(!course.title.includes(this.searchForm.title)){
            let pos = tmpCourses.indexOf(course);
            tmpCourses.splice(pos, 1);
          }
        }
      }
      if(this.searchForm.genre != '' && this.searchForm.genre != null){
        for(let course of this.courses){
          if(course.genre != this.searchForm.genre){
            let pos = tmpCourses.indexOf(course);
            tmpCourses.splice(pos, 1);

          }
        }
      }
      this.displayCourses = tmpCourses;
    }
  },
  data() {
    return {
      courses: [],
      displayCourses: [],
      searchForm: {
        title: '',
        genre: ''
      }
    }
  },
  mounted: function(){
    let obj = this;
    axios.get(process.env.VUE_APP_API_URL + 'course/getall')
    .then(function(response) {
      obj.courses = [];
      for(let i in response.data){
        obj.courses.push(response.data[i]);
      }
      obj.displayCourses = obj.courses;
    })
    .catch(function () {
      obj.$message.error('糟糕，哪里出了点问题！');
    });
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
