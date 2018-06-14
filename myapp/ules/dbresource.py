#!/anaconda3/bin/python3.6
# coding=utf-8
'''
Created on 2018年5月12日

@author: jiangwen
'''
import MySQLdb
class DBsource(object):
    def __init__(self):
        print("init db")
        
    
    def connectDB(self,host="localhost",user="root",passwd="password",database="Ules",charset='utf8'):
        self.db = MySQLdb.connect(host, user, passwd, database, charset='utf8' )
    
    def closeDB(self):
        self.db.close()
        
    def getSqlResults(self,sql):
        self.connectDB()
        cur = self.db.cursor(MySQLdb.cursors.DictCursor)
        cur.execute(sql)
        self.db.close()
        return cur.fetchall()
            

if __name__=="__main__":
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "password", "Ules", charset='utf8' )
#     db = MySQLdb.connect("11.160.195.232", "caigou_data", "password", "CAIGOU_DATA", charset='utf8' )
    # 使用cursor()方法获取操作游标 
    # cursor = db.cursor()
    # SQL 插入语句INsert into selUops 
    #(name,locator,location,type,ops,value,assert,required) values ("meterial_create","name","title","input","senkey","test051101",null,true);
#     sql = "INSERT INTO selUops(gmt_create, name, ops_order,\
#             locator, location, type, ops,value,assert,required,ops_detail) \
#             VALUES ( '%s', '%s', '%d', '%s', '%s', '%s', '%s', '%s', '%s', '%d', '%s')" % \
#             (NOW(),'caigou_member_create', 1,'id', "J_Quick2Static", 'button', "click",'test112', 'test112', 0,r'新建员工')
    sql = "INSERT INTO selUops(gmt_create, name, ops_order,\
            locator, location, type, ops, value, assert, required, ops_detail) \
            VALUES (NOW(),'caigou_member_create', 1,'id', 'J_Quick2Static', 'button', 'click','test112', 'test112', 0, r'新建员工')"
            
    print(sql)        
    cur = db.cursor()
    cur.execute(sql) #执行sql语句
 
    db.commit()
    #关闭数据库连接
    cur.close()
    db.close()

#查询
#     cur = db.cursor(MySQLdb.cursors.DictCursor) #建立游标时，加上"MySQLdb.cursors.DictCursor"，让数据查询结果返回字典类型
#     #对数据进行操作
#     sql = 'select * from selUops where name="meterial_create"' #定义查询操作的sql语句
#     cur.execute(sql) #执行sql语句
#     data = cur.fetchall() #读取数据
#     #关闭数据库连接
#     cur.close()
#     db.close()
#     print(data)
