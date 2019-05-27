<template>
  <div class="course">
    <div class="side-bar">
      <router-link class="btn-text" :to="'/course/video/' + this.$route.params.id">视频学习</router-link>
      <router-link class="btn-text" :to="'/course/reading/' + this.$route.params.id">阅读材料</router-link>
      <router-link class="btn-text" :to="'/course/exam/' + this.$route.params.id">开始考试</router-link>
      <router-link class="btn-text" :to="'/course/result/' + this.$route.params.id">学习结果</router-link>
    </div>
    <div class="main-content">
      <router-view></router-view>
    </div>
  </div>
</template>

<style scoped>
.course{
  width: 70%;
  margin-left: 15%;
  margin-right: 15%;
  height: 100%;
}
.side-bar{
  width: 18%;
  float: left;
  height: 100%;
  box-shadow: 2px 2px 10px rgb(220, 220, 220);
  margin-right: 10px;
}
.btn-text{
  color: #303133;
  font-size: 1em;
  width: 100%;
  font-weight: 500;
  display: block;
  margin: 0;
  text-decoration: none;
}
.main-content{
  width: 80%;
  height: 100%;
  float: right;
}
</style>