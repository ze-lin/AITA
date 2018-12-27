<template>
  <div class="teacher-result">
    <p>需要有图标</p>
    <a id="result-link" target="_blank" href="">查看考试题目正确率</a>
    <div class="comment">
      <el-form :model="form" ref="commentForm" label-width="100px">
        <el-form-item label="时间范围" prop="time">
          <el-time-select
            placeholder="起始时间"
            v-model="form.startTime"
            :picker-options="{
              start: '00:00',
              step: '00:30',
              end: '10:00'
            }">
          </el-time-select>
          <el-time-select
            placeholder="结束时间"
            v-model="form.endTime"
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
          <el-button type="primary" @click="submit">立即创建</el-button>
          <el-button @click="reset">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

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

      axios.get('http://127.0.0.1:5000/addcomment', {
        params: {
          id: this.$route.params.id,
          startTime: this.form.startTime,
          endTime: this.form.endTime,
          content: this.form.desc
        }
      })
      .then(function() {
        obj.$message({
          message: '成功发表！',
          type: 'success'
        });
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
  background-color: wheat;
}
.comment{
  width: 40%;
  margin-left: 30%;
  margin-right: 30%;
}
</style>