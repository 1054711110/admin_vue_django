<template>
  <div>
    <el-card class="box-card">
      <div class="button-menu">
        <el-button type="primary" @click="newuser">新增用户</el-button>
      </div>
      <el-table :data="tableData" stripe style="width: 100%;float:left">
        <el-table-column prop="id" label="ID" width="180"></el-table-column>
        <el-table-column prop="name" label="姓名" width="180"></el-table-column>
        <el-table-column prop="address" label="地址"></el-table-column>
        <el-table-column label="状态">
          <template slot-scope="scope">
            <el-switch
              v-model="scope.row.state"
              active-color="#13ce66"
              inactive-color="#ff4949"
              @change="setuserstate(scope)"
            ></el-switch>
          </template>
        </el-table-column>
        <el-table-column prop="date" label="时间"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="primary" icon="el-icon-edit" circle @click="edit(scope)"></el-button>
            <el-button type="danger" icon="el-icon-delete" circle @click="del(scope)"></el-button>
          </template>
        </el-table-column>
      </el-table>
      <div class="page">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"

          :page-sizes="[5, 10, 15, 20]"
          :page-size="100"
          layout="total, sizes, prev, pager, next, jumper"
          :total="total"
        ></el-pagination>
      </div>
    </el-card>
    <!-- 新增用户 -->
    <el-dialog
      title="添加用户"
      :visible.sync="adddialogVisible"
      width="40%"
      @close="addhandleClose"
    >
      <el-form
        :model="ruleForm"
        status-icon
        :rules="rules"
        ref="ruleForm"
        label-width="60px"
        class="demo-ruleForm"
      >
        <el-form-item label="姓名" prop="name">
          <el-input type="name" v-model="ruleForm.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="地址" prop="address">
          <el-input type="address" v-model="ruleForm.address" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="电话" prop="mobile">
          <el-input type="mobile" v-model="ruleForm.mobile" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="状态" prop="state">
          <el-switch
            @change="statechange"
            v-model="ruleForm.state"
            active-color="#13ce66"
            inactive-color="#ff4949"
          ></el-switch>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
          <el-button @click="resetForm('ruleForm')">重置</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
    <!-- 新增用户 -->
    <!-- 新增用户 -->
    <el-dialog
      title="修改用户"
      :visible.sync="editdialogVisible"
      width="40%"
      @close="handleClose"
      
    >
      <el-form
        :model="ruleForm"
        status-icon
        :rules="rules"
        ref="ruleForm"
        label-width="60px"
        class="demo-ruleForm"
      >
        <el-form-item label="姓名" prop="name">
          <el-input type="name" v-model="ruleForm.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="地址" prop="address">
          <el-input type="address" v-model="ruleForm.address" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="电话" prop="mobile">
          <el-input type="mobile" v-model="ruleForm.mobile" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="状态" prop="state">
          <el-switch
            @change="statechange"
            v-model="ruleForm.state"
            active-color="#13ce66"
            inactive-color="#ff4949"
          ></el-switch>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="edituser('ruleForm')">提交</el-button>
          <el-button @click="resetForm('ruleForm')">重置</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
    <!-- 新增用户 -->
  </div>
</template>

<script>
import {
  getuserlist,
  adduserlist,
  deluser,
  userstate,
  userupdate
} from "@/api/index";
export default {
  name: "",
  props: {},
  data() {
    return {
      tableData: [],
      adddialogVisible: false,
      editdialogVisible:false,
      ruleForm: { name: "", address: "", state: true, mobile: "" },
      rules: {
        name: { required: true, message: "请输入活动名称" },
        address: { required: true, message: "请输入活动名称" },
        mobile: { required: true, message: "请输入活动名称" }
      },
      total:0,
      page:1,
      page_size:5
    };
  },
  mounted() {
    this.getuserlist();
  },
  components: {},
  computed: {},
  methods: {
    getuserlist() {
      let that = this;
      let data={page:this.page,page_size:this.page_size}
      getuserlist({page:this.page,page_size:this.page_size}).then(res => {
        console.log(res);
        if (res.code == 200) {
          this.total=res.count
          this.tableData = res.data;
          this.tableData = this.tableData.map((item, index) => {
            console.log(this.formatDate(item.date));
            item.date = that.formatDate(item.date);
            return item;
          });
        }
      });
    },
    statechange(e) {
      console.log(e);
      this.ruleForm.state = e;
    },
    newuser() {
      this.adddialogVisible = true;
    },
    formatDate(date) {
      const dt = new Date(date);

      const y = dt.getFullYear();
      const m = (dt.getMonth() + 1 + "").padStart(2, "0");
      const d = (dt.getDate() + "").padStart(2, "0");

      const hh = (dt.getHours() + "").padStart(2, "0");
      const mm = (dt.getMinutes() + "").padStart(2, "0");
      const ss = (dt.getSeconds() + "").padStart(2, "0");
      return `${y}-${m}-${d} ${hh}:${mm}:${ss}`;
    },
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          adduserlist(this.ruleForm).then(res => {
            console.log(res);
            if (res.code == 200) {
              this.$message({
                message: "添加用户成功",
                type: "success"
              });
              this.adddialogVisible = false;
              this.getuserlist();
              this.resetForm(formName);
            }
          });
        } else {
          console.log("error submit!!");
          return false;
        }
        console.log(this.ruleForm);
      });
    },
    del(scope) {
      this.$confirm("此操作将永久删除该用户, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      })
        .then(() => {
          let id = scope.row.id;
          deluser({ id: id }).then(res => {
            if (res.code == 200) {
              this.$message({
                message: "删除用户成功",
                type: "success"
              });
            }
          });
          this.getuserlist();
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除"
          });
        });
    },
    setuserstate(e) {
      let id = e.row.id;
      let state = e.row.state;
      userstate({ id: id, state: state }).then(res => {
        console.log(res);
        if (res.code == 200) {
          this.$message({
            message: "设置状态成功",
            type: "success"
          });
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    edit(scope) {
      this.ruleForm = scope.row;
      this.editdialogVisible = true;
    },
    edituser() {
      userupdate(this.ruleForm).then(res => {
        console.log(res);
      });
    },
    handleClose(){
      this.editdialogVisible=false
    },
    addhandleClose(){
        this.adddialogVisible=false
    },
   handleSizeChange(val) {
        console.log(`每页 ${val} 条`);
        this.page_size=val
            this.getuserlist();
      },
      handleCurrentChange(val) {
        console.log(`当前页: ${val}`);
         this.page=val
             this.getuserlist();
      }
  }
};
</script>

<style scoped>
.button-menu {
  /* width: 100%; */
  height: 80px;
  float: left;
  /* background: pink; */
  display: flex;
  align-items: center;
}
.page{
  height: 50px;
  float: right;

}
</style>
