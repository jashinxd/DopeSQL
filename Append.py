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
    db = connection['Story']
    curs = db.users.find({'uname':username})
    if curs.count() != 0:
        return True
    return False
    


def comment(storyID, CContent, Date):
    connection = MongoClient()
    db = connection['Comments']
    db.users.insert({'storyID': storyID, 'CContent': CContent, 'Date': Date})
    
def addStory(Content, Name, Username, ID, Date):
    conn = sqlite3.connect("StoryBase.db")
    c = conn.cursor()
    q = """insert into Stories values ('%s','%s','%s','%s','%s');""" % (Content,Name,Username,ID,Date)
    c.execute(q)
    conn.commit()

