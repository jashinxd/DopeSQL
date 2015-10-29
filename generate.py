#import sqlite3, os.path
from pymongo import MongoClient
import os.path

connection = MongoClient()

x = os.path.isfile("StoryBase.db")

if not x:
   db = connection['StoryBase']
   d = {'username': 'testname', 'Password': 'testpass'}
   db.Users.insert(d)
   d = {'Content': 'testname', 'Name': 'testname', 'Username': 'testuname', 'ID': 'testid', 'Date': 'testdate'}
   db.Stories.insert(d)
   print db.collection_names()
#   curs = connect.cursor()
#   List = ["""
#   CREATE TABLE Login(
#      Username TEXT,
#      Password TEXT
#   );""","""CREATE TABLE Stories(
#      Content TEXT, 
#      Name TEXT,
#      Username TEXT,
#      ID REAL,
#      Date TEXT
#   );""","""CREATE TABLE comments(storyID REAL,
#      CContent TEXT,
#      Date TEXT
#   );
#   ""","""CREATE TABLE StoryID(storyID REAL);
#   """]

"""
   for q in List:
      curs.execute(q)
      connect.commit()
"""
res = db.Stories.find()
for r in res:
   print r
