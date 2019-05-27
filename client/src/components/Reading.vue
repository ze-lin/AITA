<template>
  <div class="reading">
    <vue-markdown :source="content"></vue-markdown>
  </div>
</template>

<script>
import VueMarkdown from 'vue-markdown'
import axios from 'axios'
import checkUsrMixin from '../mixins/checkUsrMixin.js'

export default {
  components: { VueMarkdown },
  mixins: [checkUsrMixin],
  data(){
    return {
      content: '请稍后，您的内容正在飞速加载！',
    }
  },
  mounted: function(){
    let obj = this;
    axios.get(process.env.VUE_APP_API_URL + 'course/getreading', {
      params: { id: this.$route.params.id }
    })
    .then(function(response) {
      if(obj.checkUsr(response.data)){
        obj.content = response.data;
      }
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


