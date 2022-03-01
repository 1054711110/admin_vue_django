<template>
  <div>
    <el-container>
      <el-header>
        <div class="headerfloat">
          <el-menu
    
            class="el-menu-demo"
            mode="horizontal"
          
          >
            <el-menu-item index="1">处理中心</el-menu-item>
            <el-submenu index="2">
              <template slot="title">我的工作台</template>
              <el-menu-item index="2-1">选项1</el-menu-item>
              <el-menu-item index="2-2">选项2</el-menu-item>
              <el-menu-item index="2-3">选项3</el-menu-item>
              <el-submenu index="2-4">
                <template slot="title">选项4</template>
                <el-menu-item index="2-4-1">选项1</el-menu-item>
                <el-menu-item index="2-4-2">选项2</el-menu-item>
                <el-menu-item index="2-4-3">选项3</el-menu-item>
              </el-submenu>
            </el-submenu>
            <el-menu-item index="3" disabled>消息中心</el-menu-item>
            <el-menu-item index="4">
              <a href="https://www.ele.me" target="_blank">订单管理</a>
            </el-menu-item>
          </el-menu>
        </div>
        <div class="headerright">
          <el-menu
          
            class="el-menu-demo"
            mode="horizontal"
  
          >
            <el-submenu index="5" class="user">
              <template slot="title">
                个人中心
                <div class="tx">头像</div>
              </template>
              <el-menu-item index="5-1">切换账号</el-menu-item>
              <el-menu-item index="5-2">退出账号</el-menu-item>
            </el-submenu>
          </el-menu>
        </div>
      </el-header>
      <el-container>
        <el-aside width="200px">
          <el-menu
            default-active="2"
            class="el-menu-vertical-demo"
  
       
            router
          >
            <el-submenu index="1-4">
              <template slot="title">用户管理</template>
              <el-menu-item index="user">用户管理</el-menu-item>
            </el-submenu>
            <el-submenu index="2-4">
              <template slot="title">账户管理</template>
              <el-menu-item index="2-4-1">账户管理</el-menu-item>
            </el-submenu>
            <el-submenu index="3-4">
              <template slot="title">权限管理</template>
              <el-menu-item index="3-4-1">权限管理</el-menu-item>
            </el-submenu>
          </el-menu>
        </el-aside>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "",
  props: {},
  data() {
    return {};
  },
  mounted() {},
  components: {},
  computed: {},
  methods: {}
};
</script>

<style scoped>
.el-header,
.el-footer {
  /* background-color: #0088dd; */
  color: #333;
  line-height: 60px;
}

.el-aside {
  /* background-color: #d3dce6; */
  color: #333;
  text-align: center;
  height: 100vh;
}

.el-main {
  background-color: #e9eef3;
  color: #333;
  /* text-align: center;
  line-height: 160px; */
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
.el-header {
}
.tx {
  width: 40px;
  height: 40px;
  background: pink;
  border-radius: 50%;
  color: #ffffff;
  float: left;
  margin-top: 10px;
  text-align: center;
  line-height: 40px;
}
.headerright {
  float: right;
}
.headerfloat {
  float: left;
  display: flex;
  justify-content: space-between;
}
</style>
