# utils.py
import MySQLdb


DATABASE='microBlogDB'
DB_USER = 'blogUser'
DB_PASSWORD = 'blogPassword'
HOST = 'localhost'

def db_connect():
  return MySQLdb.connect(HOST, DB_USER, DB_PASSWORD, DATABASE)