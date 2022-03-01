<template>
  <div class="box">
    <div class="loginBox">
      <div class="leftlogin">欢迎进入后台管理系统</div>
      <div class="rightlogin">
        <el-tabs v-model="activeName">
          <el-tab-pane label="登录账号" name="first">
            <div class="loginform">
              <el-form
                :model="ruleForm"
                status-icon
                :rules="rules"
                ref="ruleForm"
                label-width="100px"
                class="demo-ruleForm"
              >
                <el-form-item label="账号" prop="username">
                  <el-input v-model="ruleForm.username" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="密码" prop="password">
                  <el-input type="password" v-model="ruleForm.password" autocomplete="off"></el-input>
                </el-form-item>

                <el-form-item>
                  <el-button class="submitform" type="primary" @click="submitForm('ruleForm')">提交</el-button>
                </el-form-item>
              </el-form>
            </div>
          </el-tab-pane>
          <el-tab-pane label="注册账号" name="second">注册账号</el-tab-pane>
        </el-tabs>
      </div>
    </div>
  </div>
</template>

<script>
import {login} from '../api/index'
export default {
  name: "",
  props: {},
  data() {
    return {
      activeName: "first",
      ruleForm: {
        username: "",
        password: ""
      },
      rules: {
        user: [{ trigger: "blur", require: true }],
        pwd: [{ require: true, trigger: "blur" }]
      }
    };
  },
  mounted() {},
  components: {},
  computed: {},
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
       login(this.ruleForm).then(res=>{
           console.log(res)
           if(res.state.token!=''){
             alert('登录成功')
             localStorage.setItem("user",JSON.stringify(res))
             this.$router.push('/index')
           }
       })
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    }
  }
};
</script>

<style lang='less' scoped >
.box {
  width: 100%;
  height: 100vh;
  background: url(https://oem.faisys.com/image/demo2.png);
}
.loginBox {
  width: 1000px;
  height: 500px;
  background: rgba(205, 209, 224, 0.8);
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  display: flex;
}
.leftlogin {
  width: 38%;
  height: 100%;
  background: #ffff;
  color: pink;
  font-size: 30px;
  text-align: center;
  line-height: 150px;
  background: url(https://oem.faisys.com/image/version2/login-site-bg.png?v=202109221523);
}
.rightlogin {
  width: 62%;
  height: 100%;
//   background: #ffff;
  padding-left: 20px;
  font-size: 30px;
  color: pink;
  
}
.loginform {
  width: 80%;
  float: left;
   margin-top: 50px;
}
.submitform{
    width: 380px;
   
}
</style>
