<template>
  <div class="personal">
    <div class="table">
      <el-card class="box-card" shadow="always">
        <div slot="header" class="clearfix">
          <span class="text title">用户信息</span>
        </div>
        <div class="text item"><b>用户名：</b>ludanxer</div>
        <div class="text item"><b>密码：</b>*****</div>
        <div class="text item"><b>注册时间：</b>2018-10-1</div>
        <div class="text item"><b>用户身份：</b>学生</div>
      </el-card>
    </div>
    <div class="table">
      <el-table :data="classes" stripe style="width: 100%">
        <el-table-column prop="title" sortable label="课程名称" width="120"></el-table-column>
        <el-table-column prop="teacher" sortable label="任课教师" width="120"></el-table-column>
        <el-table-column prop="date" sortable label="开课时间" width="120"></el-table-column>
        <el-table-column prop="time" sortable label="所用时间" width="120"></el-table-column>
        <el-table-column prop="reading" sortable label="浏览人数" width="120"></el-table-column>
        <el-table-column prop="genre" sortable label="分类" width="120"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button @click="see(scope.row)" type="text" size="small">查看</el-button>
            <el-button @click="handleClick(scope.row)" type="text" size="small">移除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  methods: {
    handleClick(row) {
      console.log(row);
    },
    see(row){
      this.$router.push('/course');
    }
  },
  data() {
    return {
      classes: [
      {
        title: '软件工程',
        teacher: '黄老师',
        date: '2018-1-1',
        time: '28h',
        genre: 'computer',
        reading: 100
      },
      {
        title: 'JAVA EE',
        teacher: '范老师',
        date: '2018-2-1',
        time: '2h',
        genre: 'sse',
        reading: 10
      }]
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
</style>
