from users.models import User
import json

f = open('MOCK_DATA_5.json')

data = json.load(f)

for i in data:
    try:
        user = User.objects.create_user(username=i['username'], name=i['name'], email=i['email'], password=i['username'])
        print('User created with username: ' + user.username)
    except:
        print('Something went wrong while creating user with username: ' + i['username'])
