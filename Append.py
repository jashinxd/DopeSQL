from pymongo import MongoClient

'''
def GreatestStoryID():
    conn = sqlite3.connect("StoryBase.db")
    c = conn.cursor()
    q="""SELECT * FROM Stories;
    """
    result = c.execute(q)
    x = 0
    for r in result:
        if r[3] > x:
            x = r[3]
        return x
'''
def register(username,password):
    connection = MongoClient()
    db = connection['StoryBase']
    db.users.insert({'uname': username, 'pword': password})

def validuname(username):
    connection = MongoClient()
    db = connection['StoryBase']
    curs = db.users.find({'uname':username})
<<<<<<< HEAD
   # print curs.count()
    if curs.count() == 0:
        return True
    return False
    
=======
    print curs.count()
    if curs.count() == 0:
        return True
    return False
>>>>>>> 568a5d83fd60d78f1ece0cd5b15db83100ae0789

def authenticate(username,password):
    connection = MongoClient()
    db = connection['StoryBase']
<<<<<<< HEAD
    #print username, password
    curs = db.users.find({'uname':username, 'pword':password})
    #print curs.count()
=======
    print username, password
    curs = db.users.find({'uname':username, 'pword':password})
    print curs.count()
>>>>>>> 568a5d83fd60d78f1ece0cd5b15db83100ae0789
    if curs.count() != 0:
        return True
    return False

def comment(storyID, CContent, Date):
    connection = MongoClient()
    db = connection['Comments']
    db.users.insert({'storyID': storyID, 'CContent': CContent, 'Date': Date})
<<<<<<< HEAD

def addStory(Content, Name, Username, Date):
    connection = MongoClient()
    db = connection['StoryBase']
    db.stories.insert({'content': Content, 'title': Name, 'uname': Username, 'date': Date})

def getStory():
    connection = MongoClient()
    db = connection['StoryBase']
    story = db.stories.find()
    return story

def getComments():
    connection = MongoClient()
    db = connection['Comments']
    comments = db.comments.find()
    return comments
=======

def addStory(Content, Name, Username, Date):
    connection = MongoClient()
    db = connection['StoryBase']
    db.stories.insert({'content': Content, 'title': Name, 'uname': Username, 'date': Date})
>>>>>>> 568a5d83fd60d78f1ece0cd5b15db83100ae0789
