from pymongo import MongoClient

client = MongoClient('localhost',21234)
db=client.proj
users=db.users

def user_user(username, password, studentid, pizza:
    if 1 == db.find({'name':username}).count():
        return False
    else:
        user={
            'username':username,
            'password':password,
            'studentid':studentid;
            'pizza':pizza;
            }
        users.insert(user)
        return True

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

