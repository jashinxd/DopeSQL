from pymongo import MongoClient

def authenticate(username,password):
    connection = MongoClient()
    db = connection['users']
    curs = db.users.find({'uname':username, 'pword':password})
    if curs.count() != 0:
        return True
    return False

