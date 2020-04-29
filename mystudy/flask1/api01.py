#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/4/7 14:15

from flask import Flask
from flask_restful import reqparse,abort,Api,Resource

app = Flask(__name__)
api = Api(app=app)

TODOS = {
    'todo1':{'task':'biuld in API'},
    'todo2':{'task':'!!!DS!!!!'},
    'todo3':{'task':'profit'}
}

def abort_if_todo(todo_id):
    if todo_id not in TODOS:
        abort(404,message="Todo {0} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task',type=str)

class Todo(Resource):
    def get(self,todo_id):
        abort_if_todo(todo_id)
        return TODOS[todo_id]

    def delete(self,todo_id):
        abort_if_todo(todo_id)
        del TODOS[todo_id]
        return '',204

    def put(self,todo_id):
        args = parser.parse_args()
        task = {'task':args['task']}
        TODOS[todo_id] = task
        return task,201

class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' %todo_id
        TODOS[todo_id] = {'task':args['task']}
        return TODOS[todo_id],201

api.add_resource(Todo,'/todos/<todo_id>')
api.add_resource(TodoList,'/todos')

if __name__ == '__main__':
    app.run(debug=True)
