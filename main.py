from flask import Flask
from flask import request
from flask import jsonify

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'


@app.route('/users', methods=['GET', 'POST'])
def get_users():
    # accesses the value of the parameter 'name'
    if request.method == 'GET':
        search_username = request.args.get('name')
    # if a username was given
        if search_username:
            # create a subdict that will hold the given user
            subdict = {'users_list': []}

            # find the user(s) in the hardcoded list
            for user in users['users_list']:
                # if you found the user(s) store it.
                if user['name'] == search_username:
                    subdict['users_list'].append(user)
            return subdict
        return users
    elif request.method == 'POST':
        userToAdd = request.get_json()
        users['users_list'].append(userToAdd)
        resp = jsonify(success=True)
        return resp


@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
    if request.method == 'DELETE':
        if id:
            for i in range(len(users['users_list'])):
                if users['users_list'][i]['id'] == id:
                    del users['users_list'][i]
                    return jsonify(success=True)
    if request.method == 'GET':
        if id:
            for user in users['users_list']:
                if user['id'] == id:
                    return user
        return ({})