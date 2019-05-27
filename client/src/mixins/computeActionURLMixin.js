export default {
  methods: {
    computeActionURL: function(data){
      return process.env.VUE_APP_API_URL + data;
    }
  }
};