import requests, json

url = 'http://api.icndb.com/jokes/random'

response = requests.get(url)

if(response.status_code == 200):
	print("Request Successful !\n")

	data = json.loads(response.text)
	
	joke_cat = []
	for item in data['value']['categories']:
		joke_cat.append(item)
	
	print("Joke Id: ", data['value']['id'])
	print("Joke: ", data['value']['joke'])
	
	if(len(joke_cat)>0):
		print(",".join(joke_cat))
	else:
		print("No category found.")
	
	#print(data['type'])
	print("\n")
	print(response.status_code)
	print(response.text)
