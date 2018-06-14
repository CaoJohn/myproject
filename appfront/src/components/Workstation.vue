<template>
  <div class="workstation">
    <h1>{{ msg }}</h1>
    <el-row display="margin-top:10px">
        <el-input v-model="input" placeholder="请输入用例名称" style="display:inline-table; width: 30%; float:left"></el-input>
        <!-- <el-button type="primary" @click="createTestCase()" style="float:left; margin: 2px;">创建测试用例</el-button> -->
        <el-button class="uk-button" style="float:left" @click="createTestCase()" type="button">创建测试用例</el-button>
        <!-- <el-button class="uk-button" style="float:left" @click="createTestCase()" type="button">创建测试2</el-button> -->
    </el-row>
     <el-row>
        <el-table :data="testcaseList" style="width: 100%" border>
          <el-table-column prop="id" label="编号" min-width="100">
            <template scope="scope"> {{ scope.row.pk }} </template>
          </el-table-column>
          <el-table-column prop="case_name" label="用例名" min-width="100">
            <template scope="scope"> <a :href="'/#/caseworkstation?casename='+scope.row.fields.case_name">{{ scope.row.fields.case_name }}</a></template>
          </el-table-column>
          <el-table-column prop="add_time" label="添加时间" min-width="100">
            <template scope="scope"> {{ scope.row.fields.add_time }} </template>
          </el-table-column>
          <el-table-column prop="edit" label="操作" min-width="100">
            <template scope="scope"><a @click="runTestCase(scope.row.fields.case_name)">run</a><tr></tr>
             <a @click="deleteTestCase(scope.row.fields.case_name)">delete</a></template>
          <!-- <template> <a href="/#/workstation"><i class="el-icon-edit-outline"></i>edit</a> </template> -->
          </el-table-column>
        </el-table>
    </el-row> 
    <div>
        <div class="uk-grid">
            <div style="background-color: #FFC1C1" class="uk-width-large-1-1 uk-visible-medium">112</div>
    </div>
  </div>
  </div>
</template>

<script>
export default {
  name: 'workstation',
  data () {
    return {
      msg: 'Vue + Test Case Library',
      input: '',
      testcaseList: [],
    }
  },
  mounted: function() {
      this.getTestCases()
  },
  methods: {
      createTestCaseByName(){
      this.$http.get('http://127.0.0.1:8000/api/add_testcase?case_name=' + this.input)
        .then((response) => {
            var res = JSON.parse(response.bodyText)
            if (res.error_num == 0) {
              this.getTestCases()
            } else {
              this.$message.error('新增用例失败，请重试')
              console.log(res['msg'])
            }
        })
    },
    deleteTestCase(e){
      this.$http.get('http://127.0.0.1:8000/api/delete_testcase?case_name=' + e)
        .then((response) => {
            var res = JSON.parse(response.bodyText)
            if (res.error_num == 0) {
              this.getTestCases()
            } else {
              this.$message.error('删除用例失败，请重试')
              console.log(res['msg'])
            }
        })
    },
    createTestCase(){
      this.$http.get('http://127.0.0.1:8000/api/add_testcase?case_name=' + this.input)
        .then((response) => {
            var res = JSON.parse(response.bodyText)
            if (res.error_num == 0) {
              this.getTestCases()
            } else {
              this.$message.error('新增用例失败，请重试')
              console.log(res['msg'])
            }
        })
    },
    getTestCases(){
      this.$http.get('http://127.0.0.1:8000/api/get_testcases')
        .then((response) => {
            var res = JSON.parse(response.bodyText)
            console.log(res)
            if (res.error_num == 0) {
              this.testcaseList = res['list']
            } else {
              this.$message.error('查询用例失败')
              console.log(res['msg'])
            }
        })
    },
    runTestCase(e){
      this.$http.get('http://127.0.0.1:8000/api/run_testcase?case_name='+e)
        .then((response) => {
            var res = JSON.parse(response.bodyText)
            if (res.error_num == 0) {
              this.getTestCases()
            } else {
              this.$message.error('新增用例失败，请重试')
              console.log(res['msg'])
            }
        })
    },
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
