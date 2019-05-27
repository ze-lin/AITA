<template>
  <div class="teacher-result">
    <a id="result-link" target="_blank" href="">前往问卷星，查看考试题目正确率</a>
    <canvas id="chart"></canvas>
    <div class="comment">
      <el-form :model="form" ref="commentForm" label-width="100px">
        <el-form-item label="时间范围" prop="time">
          <el-time-select placeholder="起始时间" v-model="form.startTime"
            :picker-options="{
              start: '00:00',
              step: '00:30',
              end: '10:00'
            }">
          </el-time-select>
          <el-time-select placeholder="结束时间" v-model="form.endTime"
            :picker-options="{
              start: '00:00',
              step: '00:30',
              end: '10:00',
              minTime: form.startTime
            }">
          </el-time-select>
        </el-form-item>
        <el-form-item label="评论内容" prop="desc">
          <el-input type="textarea" v-model="form.desc"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submit">发表评论</el-button>
          <el-button @click="reset">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import checkUsrMixin from '../mixins/checkUsrMixin'

export default {
  mixins: [checkUsrMixin],
  mounted: function(){
    let resultElement = document.getElementById('result-link');
    let obj = this;

    axios.get(process.env.VUE_APP_API_URL + 'course/getexam', {
      params: {
        id: this.$route.params.id
      }
    })
    .then(function(response) {
      resultElement.href = 'https://www.wjx.cn/report/' + response.data + '.aspx';
    })
    .catch(function () {
      obj.$message.error('糟糕，哪里出了点问题！');
    });

    let line = document.getElementById('chart').getContext('2d');
    let chart = new Chart(line, {
      type: 'line',
      data: {
        labels: [],
        datasets: [{
          label: "专注度",
          backgroundColor: '#409EFF',
          borderColor: '#409EFF',
          data: [],
          fill: false
        }]
      },
    });

    axios.get(process.env.VUE_APP_API_URL + 'focus/getavg', {
      params: { course_id: this.$route.params.id }
    })
    .then(function(response) {
      if(obj.checkUsr(response.data)){
        if(response.data == 'None'){
          obj.$message('本课程还没有学生参加，暂无专注度结果');
        }
        else{
          for(let i in response.data){
            chart.data.labels.push(i);
            chart.data.datasets[0].data.push(response.data[i]);
          }
          chart.update();
        }
      }
    })
    .catch(function () {
      obj.$message.error('糟糕，哪里出了点问题！');
    });
  },
  data(){
    return {
      form: {
        startTime: '',
        endTime: '',
        desc: ''
      }
    }
  },
  methods: {
    submit: function(){
      let obj = this;
      axios.get(process.env.VUE_APP_API_URL + 'comment/add', {
        params: {
          id: this.$route.params.id,
          startTime: this.form.startTime,
          endTime: this.form.endTime,
          content: this.form.desc
        }
      })
      .then(function() {
        obj.$message({ message: '成功发表！', type: 'success' });
        obj.reset();
      })
      .catch(function () {
        obj.$message.error('糟糕，哪里出了点问题！');
      });
    },
    reset: function(){
      this.form = {
        startTime: '',
        endTime: '',
        desc: ''
      }
    }
  }
}
</script>

<style scoped>
a {
  text-decoration: none;
}
.teacher-result{
  width: 60%;
  margin-left: 20%;
  margin-right: 20%;
}
#chart{
  width: 100%;
}
.el-input{
  margin-right: 5%;
}
.comment{
  width: 60%;
  margin-left: 20%;
  margin-right: 20%;
  margin-top: 1%;
}
</style>