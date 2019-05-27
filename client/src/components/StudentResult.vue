<template>
  <div class="student-result">
    <a id="result-link" target="_blank" href="">前往问卷星，查看考试题目正确率</a>
    <span class="demonstration">请为专注度参考评分</span>
    <el-rate
      v-model="rate" :change="rateChange()"
      :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
    </el-rate>
    <canvas id="chart"></canvas>
  </div>
</template>

<script>
import axios from 'axios'
import Chart from 'chart.js'

export default {
  mounted: function(){
    let resultElement = document.getElementById('result-link');
    let obj = this;

    axios.get(process.env.VUE_APP_API_URL + 'course/getexam', {
      params: {
        id: this.$route.params.id
      }
    })
    .then(function(response) {
      if(response.data == 'Invalid User'){
        obj.$router.push('/auth');
        obj.$message('请您先登录或注册！');
      }
      else{
        resultElement.href = 'https://www.wjx.cn/report/' + response.data + '.aspx';
      }
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

    axios.get(process.env.VUE_APP_API_URL + 'focus/get', {
      params: {
        course_id: this.$route.params.id,
      }
    })
    .then(function(response) {
      if(response.data == 'Invalid User'){
        obj.$router.push('/auth');
        obj.$message('请您先登录或注册！');
      }
      else{
        for(let i in response.data){
          chart.data.labels.push(i);
          chart.data.datasets[0].data.push(response.data[i]);
        }
        chart.update();
      }
    })
    .catch(function () {
      obj.$message.error('糟糕，哪里出了点问题！');
    });
  },
  data(){
    return {
      rate: 0
    }
  },
  methods: {
    rateChange(){
      if(this.rate == 0){
        return;
      }
      let obj = this;
      axios.get(process.env.VUE_APP_API_URL + 'focus/rate', {
        params: {
          course_id: this.$route.params.id,
          rate: this.rate
        }
      })
      .then(function (response) {
        if(response.data == 'Invalid User'){
          obj.$router.push('/auth');
          obj.$message('请您先登录或注册！');
        }
        else{
          obj.$message({
            message: '成功评分！',
            type: 'success'
          });
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
a {
  text-decoration: none;
  display: block;
}
.el-rate{
  margin-bottom: 3%;
}
</style>