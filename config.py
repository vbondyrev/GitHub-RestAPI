# ------------------------------
# MONGODB settings
# ------------------------------
from pymongo import MongoClient

MONGODB_DB = 'git_db'
client = MongoClient('mongodb://mongouser:mongouser1@ds331735.mlab.com:31735/git_db')

