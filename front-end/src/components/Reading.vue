<template>
  <div class="reading">
    <vue-markdown :source="content"></vue-markdown>
  </div>
</template>

<script>
import VueMarkdown from 'vue-markdown'
import axios from 'axios'

export default {
  components: {
    VueMarkdown
  },
  data(){
    return {
      content: '请稍后，您的内容正在飞速加载！',
    }
  },
  mounted: function(){
    let obj = this;

    axios.get('http://127.0.0.1:5000/getreading', {
      params: {
        id: this.$route.params.id
      }
    })
    .then(function(response) {
      obj.content = response.data;
    })
    .catch(function () {
      obj.$message.error('糟糕，哪里出了点问题！');
    });
  }
}
</script>

<style scoped>
.reading{
  line-height: 40px;
  text-align: left;
  padding: 5%;
}
</style>


