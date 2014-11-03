from pymongo import MongoClient

client = MongoClient('localhost',27017)
db=client.proj
users=db.users

def create_user(username, password):
    user={
        'username':username,
        'password':password}
    return users.insert(user)

def find_user(username):
    user = user.find_one({'username':username})
    return user

def authenticate(username,password):
    user=find_user(username)
    if user==None:
        return False
    elif str(user['username']) != username or str(user['password']) != password:
        return False
    else:
        return True

