from flask import Flask,request,jsonify
import  json

app=Flask(__name__)

@app.route('/')
def index():
    return '{"error_code":0, "msg": "yes, it is ture"}'

@app.route('/<name>')
def hello(name):
    return '{"error_code":0, "msg": "Hello %s"}'%name

@app.route('/user/<name>')
def sayHello(name):
    return '<h1>Hello %s!</h1>'%name

@app.route('/id/<idno>')
def get_info_by_no(idno):
    if int(idno)==2879456:
       return '{"error_code":0, "msg": "id is ture"}'
    else:
       return '{"error_code":404, "msg": "id is not found"}'

@app.route('/get/args',methods=['GET'])
def get_get_args():
    key=request.args.get('key')
    username=request.args.get('username')
    response={"key":key,"username":username}
    resp=jsonify(response)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return  resp
    #return '{"error_code":0, "msg": "success"}'


@app.route('/post/form',methods=['POST'])
def post_form_data():
    key=request.form.get('key')
    print('key:',key)
    username=request.form.get('username')
    passward = request.form.get('passward')
    response={"key":key,"username":username,'passward':passward}
    return  jsonify(response)
    #return '{"error_code":0, "msg": "success"}'

@app.route('/post/json',methods=['POST'])
def post_json_data():
    key=json.loads(request.get_data())
    return  jsonify(key)


@app.route('/login/',methods=['GET','POST'])
def login():
     if request.method == 'GET':
         return 'login.html'
     else:
         username = request.form.get('username')
         password = request.form.get('password')
         print(username)
         print(password)
         return 'hello!'
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')