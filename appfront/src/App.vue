<template>
  <div id="app">
       <el-menu
          :default-active="activeIndex2"
          class="el-menu-demo"
          mode="horizontal"
          @select="handleSelect"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b">
          <el-menu-item index="1"><a href="/#/hello" class="uk-icon-home" target="_blank"> 基于数据的自动化</a></el-menu-item>
          <el-submenu index="2">
            <template slot="title">测试用例</template>
            <el-menu-item index="2-1"><a href="/#/caseworkstation" class="uk-icon-gears">测试用例步骤</a></el-menu-item>
            <el-menu-item index="2-2"><a href="/#/workstation" class="uk-icon-gears">测试用例库</a></el-menu-item>
            <el-menu-item index="2-3">待定1</el-menu-item>
            <el-submenu index="2-4">
              <template slot="title">待定2</template>
              <el-menu-item index="2-4-1">选项1</el-menu-item>
              <el-menu-item index="2-4-2">选项2</el-menu-item>
              <el-menu-item index="2-4-3">选项3</el-menu-item>
            </el-submenu>
          </el-submenu>
          <el-menu-item index="3">用例集</el-menu-item>
          <el-menu-item index="4"><a href="/#/hello" target="_blank">计划</a></el-menu-item>
          <el-menu-item index="5"><a href="/#/hello" target="_blank">标签</a></el-menu-item>
          <el-menu-item index="6"><a @click="dialogVisible = true" class="el-icon-plus"></a></el-menu-item>
        </el-menu>

     <!-- <el-col :span="3">
    <el-menu
      :default-active="2"
      class="el-menu-vertical-demo"
      @open="handleOpen"
      @close="handleClose"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>导航一</span>
        </template>
        <el-menu-item-group>
          <template slot="title">分组一</template>
          <el-menu-item index="1-1"><a href="/#/caseworkstation">测试用例步骤</a></el-menu-item>
          <el-menu-item index="1-2"><a href="/#/workstation">测试用例库</a></el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="分组2">
          <el-menu-item index="1-3">选项3</el-menu-item>
        </el-menu-item-group>
        <el-submenu index="1-4">
          <template slot="title">选项4</template>
          <el-menu-item index="1-4-1">选项1</el-menu-item>
        </el-submenu>
      </el-submenu>
      <el-menu-item index="2">
        <i class="el-icon-menu"></i>
        <span slot="title"><a href="/#/caseworkstation">测试用例步骤</a></span>
      </el-menu-item>
      <el-menu-item index="3">
        <i class="el-icon-document"></i>
        <span slot="title"><a href="/#/workstation">测试用例库</a></span>
      </el-menu-item>
      <el-menu-item index="4">
        <i class="el-icon-setting"></i>
        <span slot="title"><a href="/#/hello" target="_blank">图表展示</a></span>
      </el-menu-item>
    </el-menu>
  </el-col> -->


<!-- <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">
  <el-radio-button :label="false">展开</el-radio-button>
  <el-radio-button :label="true">收起</el-radio-button>
</el-radio-group> -->
<el-menu default-active="1-4-1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" :collapse="isCollapse">
  <el-submenu index="1">
    <template slot="title">
      <i class="el-icon-location"></i>
      <span slot="title">导航一</span>
    </template>
    <el-menu-item-group>
      <span slot="title">用例</span>
      <el-menu-item index="1-1"><a href="/#/caseworkstation">测试用例步骤</a></el-menu-item>
      <el-menu-item index="1-2"><a href="/#/caseworkstation">用例详情</a></el-menu-item>
    </el-menu-item-group>
    <el-menu-item-group title="用例集">
      <el-menu-item index="1-3"><a href="/#/workstation">测试用例库</a></el-menu-item>
    </el-menu-item-group>
    <el-submenu index="1-4">
      <span slot="title">选项4</span>
      <el-menu-item index="1-4-1">选项1</el-menu-item>
    </el-submenu>
  </el-submenu>
  <el-menu-item index="2">
    <i class="el-icon-menu"></i>
    <span slot="title">结果</span>
  </el-menu-item>
  <el-menu-item index="3">
    <i class="el-icon-document"></i>
    <span slot="title">统计</span>
  </el-menu-item>
  <el-menu-item index="4">
    <i class="el-icon-setting"></i>
    <span slot="title">设置</span>
  </el-menu-item>
</el-menu>

  <router-view></router-view>
  
  <el-dialog
  title="创建测试用例"
  :visible.sync="dialogVisible"
  width="30%"
  :before-close="handleCloseDialog">
  <el-input v-model="input" placeholder="请输入内容"></el-input>
  <span slot="footer" class="dialog-footer">
    <el-button @click="dialogVisible = false">取 消</el-button>
    <el-button type="primary" @click="createTestCaseByName()">确 定</el-button>
  </span>
</el-dialog>
  </div>
</template>

<script>
export default {
  name: 'app',
  data() {
      return {
        activeIndex: '1',
        activeIndex2: '1',
        dialogVisible: false,
        input: '',
        testcaseList: [],
        isCollapse: true,
      };
    },
  methods: {
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      },
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      },
      handleCloseDialog(done) {
      },
      createTestCaseByName(){
        this.dialogVisible = false
        this.$router.push({path:'/caseworkstation?testcase='+this.input})
        this.$http.get('http://127.0.0.1:8000/api/add_testcase?case_name=' + this.input)
          .then((response) => {
              var res = JSON.parse(response.bodyText)
              if (res.error_num == 0) {
                //this.getTestCases()
                this.$message.response('添加成功')
              } else {
                this.$message.error('新增用例失败，请重试')
                console.log(res['msg'])
              }
          })
      },

    }
    
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
<style>
  .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
  }
</style>
