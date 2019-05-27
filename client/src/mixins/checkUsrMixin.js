export default {
  methods: {
    checkUsr(data){
      if(data == 'Invalid User'){
        this.$router.push('/auth');
        this.$message('请您先登录或注册！');
        return false;
      }
      else{
        return true;
      }
    }
  }
};