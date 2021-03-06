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
   # print curs.count()
    if curs.count() == 0:
        return False
    return True
    

def authenticate(username,password):
    connection = MongoClient()
    db = connection['StoryBase']
    #print username, password
    curs = db.users.find({'uname':username, 'pword':password})
    #print curs.count()
    if curs.count() != 0:
        return True
    return False

def comment(storyID, CContent, Date):
    connection = MongoClient()
    db = connection['StoryBase']
    db.comments.insert({'storyID': storyID, 'CContent': CContent, 'Date': Date})

def addStory(storyID, Content, Name, Username, Date):
    connection = MongoClient()
    db = connection['StoryBase']
    db.stories.insert({'storyID': storyID, 'content': Content, 'title': Name, 'uname': Username, 'date': Date})

def getStory():
    connection = MongoClient()
    db = connection['StoryBase']
    story = db.stories.find()
    return story


def getComments():
    connection = MongoClient()
    db = connection['StoryBase']
    comments = db.comments.find()
    return comments

def getCommentsSpec(postid):
    connection = MongoClient()
    db = connection['StoryBase']
    comments = db.comments.find({"storyID": postid})
    return comments 

