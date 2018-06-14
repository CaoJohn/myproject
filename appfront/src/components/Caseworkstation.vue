<template>
  <div class="caseworkstation">
     <h1>测试用例：  {{ testcase.name }}</h1>
    <!--<h1>测试：  {{ message }}</h1>
    <h1>测试：  {{ fortest }}</h1> -->
    <!-- <h1>{{ model }}</h1> -->
    <!-- <h1>{{ Object.keys(model[0]) }}</h1> -->
      <ul id="example-1" class="uk-">
        <div class="uk-grid">
        <div class="uk-width-medium-1-6">
              <div @click="getTestCaseModel()"  class="uk-panel-title uk-panel-box uk-panel-box-primary uk-panel-space uk-panel-divider ">
                <i class="uk-icon-sign-in"></i>
                web url
              </div>
				</div>

        <li v-for="item in model" v-bind:key="item.fields.step_name ">
				     <div class="uk-width-medium-1-1">
                  <div @click="getModel(item.fields.step_name)" class="uk-panel-title uk-panel-box uk-panel-box-primary uk-panel-space uk-panel-divider ">
                    <i class="uk-icon-edit"></i>
                    {{ item.fields.step_name }}
                  </div>  
              </div>
        </li>
        <div class="uk-width-medium-1-6">
            <div v-on:click="addCard" class="uk-panel-title uk-panel-box uk-panel-box-primary uk-panel-space uk-panel-divider ">
              <i class="uk-icon-plus"></i>
            </div>
         </div>
        </div>
      </ul>
    <div id="app-2">
  <span v-bind:title="message">
    鼠标悬停几秒钟查看此处动态绑定的提示信息！
  </span>
</div>


<!-- 模态对话框 web url entrance -->
<el-dialog
  title="用例步骤"
  :visible.sync="urldialogVisible"
  width="30%"
  :before-close="handleClose">
  <form id="testcase-url-id">
    <div class="demo-input-suffix my-left">
      <el-label>url：</el-label>
      <el-input placeholder="请输入" v-model="testcase.url" type="text" id = "_case_name_" value="testcase.url">{{testcase.url}}</el-input>
      <template>
        <!-- `checked` 为 true 或 false -->
        <el-checkbox v-model="checked">是否开启录制</el-checkbox>
      </template>
    </div>
  </form>
  
  <span slot="footer" class="dialog-footer">
    <el-button @click="urldialogVisible = false">取 消</el-button>
    <el-button type="primary" @click="setTestCaseUrl()">确认</el-button>
  </span>
</el-dialog>

<!-- 模态对话框  case step entrance -->
<div id="step-model-id" class="uk-modal">
    <div class="uk-modal-dialog">
        <a class="uk-modal-close uk-close"></a>
        <form class="uk-form uk-form-stacked">
          <fieldset data-uk-margin>
            <legend>创建测试步骤</legend>
            <div class="uk-form-colume uk-form-horizontal">
              <li v-for="item in Object.keys(step_model)" v-bind:key="item">
                  <label class="uk-form-label">{{item}}</label>
                  <input type="text" placeholder="99999" class="uk-form-width-medium">
              </li>
            </div>
        </fieldset>
        <tr></tr>
      <button class="uk-button uk-button-primary" type="button" data-uk-button>确认</button>
      <button class="uk-button" type="button" data-uk-button>取消</button>
      </form>
    </div>
</div>

<!-- 模态对话框  el dialog -->
<el-dialog
  title="用例步骤"
  :visible.sync="modeldialogVisible"
  width="30%"
  :before-close="handleClose">
  <form id="steo_model_form">
    <!-- <li v-for="item in Object.keys(step_model)" v-bind:key="item">
          <div class="demo-input-suffix">
                  <el-label>{{item}}：</el-label>
                  <el-input
                    placeholder="请输入"
                    type="text"
                    id = "_input_step_attr"
                    value=' "+step_model.item+" '
                    >
                  </el-input>
          </div>
      </li> -->
    <div class="demo-input-suffix">
      <el-label>step_name：</el-label>
      <el-input placeholder="请输入" v-model="step_model.step_name" type="text" id = "_step_name_" value="step_model.step_name">{{step_model.step_name}}</el-input>
    </div>
    <div class="demo-input-suffix">
      <el-label>order：</el-label>
      <el-input placeholder="请输入" v-model="step_model.step_order" type="number" id = "_step_order_" value="1">{{step_model.step_order}}</el-input>
    </div>
    <div class="demo-input-suffix">
      <el-label>identifier：</el-label>
      <el-input placeholder="请输入" v-model="step_model.identifier" type="text" id = "_step_identifier_" value="step_model.identifier">{{step_model.identifier}}</el-input>
    </div>
    <div class="demo-input-suffix">
      <el-label>location：</el-label>
      <el-input placeholder="请输入" v-model="step_model.location" type="text" id = "_step_location_" value="1">{{step_model.location}}</el-input>
    </div>
    <div class="demo-input-suffix">
      <el-label>type：</el-label>
      <el-input placeholder="请输入" v-model="step_model.type" type="text" id = "_step_type_" value="basic">{{step_model.type}}</el-input>
       <!-- <el-select v-model="step_model.type" placeholder="请选择">
        <el-option
          v-for="item in options"
          :key="item.type_value"
          :label="item.label"
          :value="item.type_value">
        </el-option>
      </el-select> -->
    </div>
    <div class="demo-input-suffix">
      <el-label>element_type：</el-label>
      <el-input placeholder="请输入" v-model="step_model.element_type" type="text" id = "_step_element_type_" value="1">{{step_model.element_type}}</el-input>
    </div>
    <div class="demo-input-suffix">
      <el-label>ops：</el-label>
      <el-input placeholder="请输入" v-model="step_model.ops" type="text" id = "_step_ops_" value="1">{{step_model.ops}}</el-input>
    </div>
    <div class="demo-input-suffix">
      <el-label>value：</el-label>
      <el-input placeholder="请输入" v-model="step_model.value" type="text" id = "_step_value_" value="1">{{step_model.value}}</el-input>
    </div>
    <div class="demo-input-suffix">
      <el-label>reg_type：</el-label>
      <el-input placeholder="请输入" v-model="step_model.reg_type" type="text" id = "_step_reg_type_" value="1">{{step_model.reg_type}}</el-input>
    </div>
    <div class="demo-input-suffix">
      <el-label>ret_assert：</el-label>
      <el-input placeholder="请输入" v-model="step_model.ret_assert" type="text" id = "_step_ret_assert_" value="1">{{step_model.ret_assert}}</el-input>
    </div>
    <div class="demo-input-suffix">
      <el-label>required：</el-label>
      <el-input placeholder="请输入" v-model="step_model.required" type="number" id = "_step_required_" value="1">{{step_model.required}}</el-input>
    </div>
    <div class="demo-input-suffix">
      <el-label>imgdiff：</el-label>
      <el-input placeholder="请输入" v-model="step_model.imgdiff" type="number" id = "_step_imgdiff_" value="1">{{step_model.imgdiff}}</el-input>
    </div>
  </form>
  
  <span slot="footer" class="dialog-footer">
    <el-button @click="modeldialogVisible = false">取 消</el-button>
    <el-button type="primary" @click="setModel()">确认</el-button>
  </span>
</el-dialog>

</div>
</template>
<script>
export default {
  name: 'caseworkstation',
  // el: '#app-2',
  data () {
    return {
      msg: 'Vue + caseworkstation',
      message: '页面加载于 ' + new Date().toLocaleString(),
      testcase: {
        "is_new":true,
        "id":0,
        "name":"",
        "url":"work.1688.com",
      },
      input: '',
      testcaseList: [],
      modeldialogVisible: false,
      urldialogVisible: false,
      items: [],
      model:[],
      step_model_list:[],
      fortest:"defaulttest",
      url_model:{
        "url":""
        },

      options: [{
          type_value: '选项1',
          label: 'button'
        }, {
          type_value: '选项2',
          label: 'input'
        }],
        type_value: '',
      step_model:{
        "is_new":true,
        "id":0,
        "case_name":"",
        "case_id":1000,
        "step_name":"",
        "identifier":"",
        "location":"",
        "type":"",
        "element_type":"basic",
        "ops":"",
        "value":"",
        "reg_type":"",
        "ret_assert":"",
        "required":1,
        "imgdiff":0,
      },
    }
  },
  mounted: function() {
      this.getSheetModel()
      this.getTestCase()
  },
  methods: {
      getSheetModel: function(){
        this.testcase.name = window.location.href.split("=")[1]
        this.$http.get('http://127.0.0.1:8000/api/get_testcasesteps?case_name='+this.testcase.name
        ).then((response) => {
            var res = JSON.parse(response.bodyText)
            if (res.error_num == 0) {
              this.model = res.list
              // debugger;
            } else {
              this.$message.error('新增用例失败，请重试')
              console.log(res['msg'])
            }
        })
      },
      getTestCase: function(){
        this.$http.get('http://127.0.0.1:8000/api/get_testcase?case_name='+this.testcase.name
        ).then((response) => {
            var res = JSON.parse(response.bodyText)
            if (res.error_num == 0) {
              this.testcase.name = res.list[0].fields.case_name
              this.testcase.url = res.list[0].fields.url
              this.testcase.id = res.list[0].pk
            } else {
              this.$message.error('新增用例失败，请重试')
              console.log(res['msg'])
            }
        })
      },
      inputWebsite: function(){
                var myDate = new Date();
                this.msg = "456"; //+ formatDate(date, 'yyyy-MM-dd hh:mm');
            },
      getTestCaseModel: function(){
                this.urldialogVisible = true
                // this.$http.get('http://127.0.0.1:8000/api/get_testcase?case_name='+ this.testcase.name).then((response) => {
                //     var res = JSON.parse(response.bodyText)
                //     if (res.error_num == 0) {
                //       this.testcase.name = res.list.fields.case_name
                //       this.testcase.url = res.list.fields.url
                //       this.testcase.id = res.list.pk
                //     } else {
                //       this.$message.error('新增用例失败，请重试')
                //       console.log(res['msg'])
                //     }
                // })
            },
      setTestCaseUrl: function(){
                this.urldialogVisible = false
                this.$http.get('http://127.0.0.1:8000/api/update_testcase?id='
                + this.testcase.id
                + '&case_name=' + this.testcase.name
                + '&url=' + this.testcase.url
                ).then((response) => {
                    var res = JSON.parse(response.bodyText)
                    if (res.error_num == 0) {
                      // this.getTestCase()
                    } else {
                      this.$message.error('新增用例失败，请重试')
                      console.log(res['msg'])
                    }
                })
                // debugger;
            },

      addCard: function(){
                // debugger;
                this.model.push({ fields: {"step_name":"new"}})
                this.step_model.case_name = this.testcase.name
            },
      getModel: function(e){
                // this.message = "oh yeah"+ e.target.innerText
                this.getSheetModel()
                this.modeldialogVisible = true
                this.message = "oh yeah:"+ e
                this.fortest = "fortest:"+this.model
                this.step_model.is_new = true
                var i;
                for (i=0;i<this.model.length;i++){
                  if(this.model[i].fields.step_name === e && this.model[i].fields.case_name===this.testcase.name){
                    this.step_model.case_name = this.model[i].fields.case_name
                    this.step_model.step_name = this.model[i].fields.step_name
                    this.step_model.identifier = this.model[i].fields.locator
                    this.step_model.location = this.model[i].fields.location
                    this.step_model.type = this.model[i].fields.type
                    this.step_model.element_type = this.model[i].fields.element_type
                    this.step_model.step_order = this.model[i].fields.step_order
                    this.step_model.ops = this.model[i].fields.ops
                    this.step_model.value = this.model[i].fields.value
                    this.step_model.reg_type = this.model[i].fields.reg_type
                    this.step_model.ret_assert = this.model[i].fields.ret_assert
                    this.step_model.required = this.model[i].fields.required
                    this.step_model.imgdiff = this.model[i].fields.imgdiff
                    this.step_model.is_new = false
                    this.step_model.id = this.model[i].pk
                    this.fortest = "fortest:"+ this.step_model
                    // debugger;
                  }
                }
                // debugger;
            },

     setModel: function(){
                // this.message = "oh yeah"+ e.target.innerText
                // this.getSheetModel()
                var url = ''
                // debugger;
                if(this.step_model.is_new){
                  url = 'http://127.0.0.1:8000/api/add_testcasestep?case_name='
                }else{
                  url = 'http://127.0.0.1:8000/api/update_testcasestep?id='
                }
                this.modeldialogVisible = false
                this.$http.get(url + this.step_model.id
                + '&case_name=' + this.step_model.case_name
                + '&step_name=' + this.step_model.step_name
                + '&case_id=' + this.step_model.case_id
                + '&step_order='+this.step_model.step_order
                + '&step_name=' + this.step_model.step_name
                + '&locator=' + this.step_model.identifier
                + '&location=' + this.step_model.location
                + '&ops=' + this.step_model.ops
                + '&value=' + this.step_model.value
                + '&type=' + this.step_model.type
                + '&reg_type=' + this.step_model.reg_type
                + '&ret_assert=' + this.step_model.ret_assert
                + '&required=' + this.step_model.required
                + '&imgdiff=' + this.step_model.imgdiff
                + '&ops_detail=' + this.step_model.imgdiff //默认值
                + '&pic_address=' + this.step_model.imgdiff //默认值
                + '&element_type=' + this.step_model.element_type
                ).then((response) => {
                    var res = JSON.parse(response.bodyText)
                    if (res.error_num == 0) {
                      this.getTestCase()
                    } else {
                      this.$message.error('新增用例失败，请重试')
                      console.log(res['msg'])
                    }
                })
                // debugger;
            },

      handleClose(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
      },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
.my-center {text-align: center}
.my-left {text-align: left}

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
div.uk-panel-box:hover  {background-color:rgb(149, 214, 245);font-size: 30px;}
</style>
