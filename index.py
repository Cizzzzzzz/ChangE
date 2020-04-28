import flask,json   #引入flask和json数据格式化模块
from flask_cors import CORS #引入跨域模块
import py.login_module
import py.query_module
import py.update_module

server=flask.Flask(__name__)#__name__代表当前的python文件。把当前的python文件当做一个服务启动
CORS(server, resources=r'/*')#跨域设置


@server.route('/emit',methods=['get','post'])
# if function == 'login':
    
# elif function == 'goquery':
#     @server.route('/goquery',methods=['get','post'])
# elif function == 'update':
#     @server.route('/update',methods=['get','post'])
#第一个参数就是路径,第二个参数支持的请求方式，不写的话默认是get，路径必须以函数方式定义
#加了@server.route才是一个接口，不然就是一个普通函数

#----------------------------------------
def emit():
    func = flask.request.values.get('func')
    if func == 'login':
        return login()
    elif func == 'goquery':
        return goquery()
    elif func == 'update':
        return update()

def login():
    return py.login_module.login()

def goquery():
    return py.query_module.query()

def update():
    return py.update_module.update()

if __name__ == '__main__':
    # port可以指定端口，默认端口是5000
    # host默认是服务器，默认是127.0.0.1
    # debug=True 修改时不关闭服务
    server.run(debug=True)
