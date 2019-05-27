export default {
  methods: {
    computeActionURL(data){
      return process.env.VUE_APP_API_URL + data;
    }
  }
};