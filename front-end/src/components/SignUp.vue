<template>
  <div class="sign-up">
    <el-form ref="form" status-icon :model="form" :rules="rule" label-width="80px">
      <el-form-item label="用户昵称" prop="usr">
        <el-input v-model="form.usr" placeholder="选择您的昵称">
          <i slot="prefix" class="fas fa-user icon"></i>
        </el-input>
      </el-form-item>
      <el-form-item label="输入密码" prop="pwd">
        <el-input type="password" v-model="form.pwd" autocomplete="off" placeholder="密码需要6位或以上">
          <i slot="prefix" class="fas fa-lock icon"></i>
        </el-input>
      </el-form-item>
      <el-form-item label="确认密码" prop="pwd2">
        <el-input type="password" v-model="form.pwd2" autocomplete="off" placeholder="验证密码">
          <i slot="prefix" class="fas fa-lock icon"></i>
        </el-input>
      </el-form-item>
      <el-form-item label="选择身份">
        <el-select v-model="form.role" placeholder="学生/老师">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-upload
          action="http://127.0.0.1:5000/signup"
          ref="upload"
          :auto-upload='false'
          :limit="1"
          :data='form'
          :on-success='SuccessUpload'
          :file-list="fileList">
          <el-button size="small">点击上传</el-button>
          <div slot="tip" class="el-upload__tip">只能上传png文件，且大小不得超过500KB</div>
        </el-upload>
      </el-form-item>
      <el-form-item class="btn">
        <el-button type="primary" @click="SignUp">注册</el-button>
        <el-button @click="$emit('change')">登录</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import axios from 'axios'
import md5 from 'js-md5'

export default {
  data(){
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'));
      } else if (value !== this.form.pwd) {
        callback(new Error('两次输入密码不一致!'));
      } else {
        callback();
      }
    };
    var validate = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'));
      } else if(value.length < 6){
        callback(new Error('您输入的密码过于简单'));
      } else {
        callback();
      }
    };
    var validateUsr = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入用户名'));
      } else {
        callback();
      }
    };
    return{
      form: {
        usr: '',
        pwd: '',
        pwd2: '',
        role: '',
      },
      rule: {
        pwd2: [{ validator: validatePass, trigger: 'blur' }],
        pwd: [{ validator: validate, trigger: 'blur' }],
        usr: [{ validator: validateUsr, trigger: 'blur' }]
      },
      fileList: [],
      options: [{
        value: 'student',
        label: '学生'
      },
      {
        value: 'teacher',
        label: '教师'
      }]
    }
  },
  methods: {
    SignUp: function(){
      if(this.form.pwd == this.form.pwd2 && this.form.pwd != '' && this.form.usr != '' && this.form.role != '' && this.$refs.upload.uploadFiles.length == 1){
        this.form['pwd'] = md5(this.form['pwd']);
        this.$refs.upload.submit();
      }
      else{
        this.$message.error('请确认输入内容全部正确！');
      }
    },
    SuccessUpload: function(){
      this.$message({
        message: '成功注册！',
        type: 'success'
      });
      this.$emit('change');
    }
  }
}
</script>

<style scoped>
.sign-up{
  float: right;
  margin-top: 120px;
  margin-right: 100px;
}
.btn{
  margin-top: 20px;
  margin-right: 10px;
}
</style>