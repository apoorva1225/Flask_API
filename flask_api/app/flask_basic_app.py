from flask import Flask, jsonify, request
import json

app = Flask(__name__)

with open('data_file.json') as json_file:
		json_data = json.load(json_file)


@app.route('/', methods=['GET'])

def index():
	
	data = {}
	data['users'] = []
	data['clients'] = []
	user_item = {}
	client_item = {}

	for item in json_data['users']:
		user_item = {'id': item['id'], 'name': item['name']}
		data['users'].append(user_item)
	for item in json_data['clients']:
		client_item = {'id': item['id'], 'name': item['name']}
		data['clients'].append(client_item)
	return jsonify(data)

@app.route('/users', methods=['GET'])
	
def get_users():
	data = {}
	data['users'] = []
	user_item = {}

	for item in json_data['users']:
		user_item = {'id': item['id'], 'name': item['name']}
		data['users'].append(user_item)
		
	return jsonify(data), 200

@app.route('/users', methods=['POST'])
	
def post_users():
	data = {}
	data['users'] = []
	user_item = {}
	for item in json_data['users']:
		user_item = {'id': item['id'], 'name': item['name']}
		data['users'].append(user_item)
		
	some_json = request.get_json()
	data['users'].append(some_json)
	return jsonify(data), 201
	
	with open('data_file.json', 'w') as outfile:
   		json.dump(data, outfile)



#@app.route('/users/<string:num>', methods=['GET', 'PUT', 'DELETE'])
#
#def user_select(num):
#	data = {}
#	data['users'] = []
#	user_item = {}
#	for item in json_data['users']:
#		user_item = {'id': item['id'], 'name': item['name']}
#		data['users'].append(user_item)
#
#	user_present = False;
#	for user in data['users']:
#		print(num, user['id'], str(num))
#		if(user['id'] == str(num)):
#			user_present = True;
#			break
#		else:
#			user_present = False;
#
#	if (request.method == 'GET'):
#		if(user_present):
#			for user in data['users']:
#				if(user['id'] == str(num)):
#					return jsonify(user)
#					break
#		else:
#			strg = 'User not found.'
#			return strg
#	elif(request.method == 'PUT'):
#		some_json = request.get_json()
#
#		if(user_present):
#			for user in data['users']:
#				if(user['id'] == str(num)):
#					data['users'].remove(user)
#					data['users'].append(some_json)
#					return jsonify(data)
#					break
#		else:
#			strg = 'User not found'
#			return strg
#	elif(request.method == 'DELETE'):
#		if(user_present):
#			for item in json_data['users']:
#				if(item['id'] == str(num)):
#					data['users'].remove(user)
#					return jsonify(data)
#					break
#		else:
#			strg = 'User not found'
#			return strg
#	else:
#		strg = 'invalid request'
#		return strg

if __name__ == '__main__':
	app.run(debug=True,port=3000)