import requests

r = requests.get('http://api.icndb.com/jokes/random')

data = r.json()

print('Joke #{}'.format(data['value']['id']))
print('Joke #{}'.format(data['value']['joke']))


print(type(r.text))  #This will let us knwo what type of dadta it is
print(type(r.json()))  # this is now a dict
print(r.json())
print(r.text)
