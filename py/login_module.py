import flask,json   #引入flask和json数据格式化模块
from flask_cors import CORS #引入跨域模块
import py.connectsql

def login():
    loginName = flask.request.values.get('loginName')#获取前端loginName,password参数
    password = flask.request.values.get('password')

    connect = py.connectsql.connect('financial_system')
    cursor = connect.cursor()
    sql = 'SELECT password FROM t_user WHERE user_name ='
    sql = sql + "'" + str(loginName) + "'"
    cursor.execute(sql)
    password1 = cursor.fetchone()[0]
    cursor.close()   
    connect.close()

    if password == password1:
        res = {'success':'true','msg': '登录成功'}
    else:
        res = {'success':'false','msg': '用户名或密码错误'}
    #json.dumps 序列化时对中文默认使用的ascii编码，输出中文需要设置ensure_ascii=False
    return json.dumps(res,ensure_ascii=False)