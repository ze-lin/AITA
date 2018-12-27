<template>
  <div class="student-result">
    <p>Chart.js</p>
    <a id="result-link" target="_blank" href="">查看考试题目正确率</a>
    <canvas id="myChart"></canvas>
  </div>
</template>

<script>
import axios from 'axios'
import Chart from 'chart.js'

export default {
  mounted: function(){
    let resultElement = document.getElementById('result-link');
    let obj = this;

    axios.get('http://127.0.0.1:5000/getexam', {
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

    let ctx = document.getElementById('myChart').getContext('2d');
    let chart = new Chart(ctx, {
        type: 'line',

        data: {
            labels: ["January", "February", "March", "April", "May", "June", "July"],
            datasets: [{
                label: "My First dataset",
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: [0, 10, 5, 2, 20, 30, 45],
            }]
        },
        options: {}
    });
  }
}
</script>

<style scoped>
a {
  text-decoration: none;
}
</style>