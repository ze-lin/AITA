import axios from "axios"
export default {
  methods: {
    joinCourse: function(row){
      let obj = this;
      axios.get(process.env.VUE_APP_API_URL + 'api/course/view', {
        params: { 
          id: row.id,
          usr: obj.$root.$data.usr
        }
      })
      .then(function(response) {
        if(obj.checkUsr(response.data)){
          console.log(row.id);
          obj.$router.push('/course/video/' + row.id);
        }
      })
      .catch(function () {
        obj.$message.error('糟糕，哪里出了点问题！');
      });
    }
  }
}