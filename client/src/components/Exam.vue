<template>
  <div class="exam">
    <iframe src='' width='100%' height='800' frameborder='0' style='overflow:auto'></iframe>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  mounted: function(){
    let obj = this;
    let frame = document.getElementsByTagName('iframe')[0];

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
        frame.src = 'https://ks.wjx.top/jq/' + response.data + ',i,t.aspx?width=760&source=iframe';
      }
    })
    .catch(function () {
      obj.$message.error('糟糕，哪里出了点问题！');
    });
  }
}
</script>