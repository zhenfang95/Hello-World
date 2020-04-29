#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/4/7 10:30

from flask import Flask,make_response,jsonify
from flask_restful import Api,Resource,reqparse

app = Flask(__name__)
api = Api(app=app)

@app.route('/index')
def index():
    return jsonify({'code':0,'msg':'succes','data':''})

class LoginView(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username',type=str,help='账号或密码不能为空',required=True)
        parser.add_argument('password',type=str,help='账号或密码不能为空',required=True)
        return jsonify({'code':0,'msg':'登录成功','data':parser.parse_args()})

api.add_resource(LoginView,'/login',endpoint='login')

if __name__ == '__main__':
    app.run()