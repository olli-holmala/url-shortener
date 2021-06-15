import sqlite3
from sqlite3 import Error

def init_db():

  conn = None
  try:
      conn = sqlite3.connect('./urls.db')
      cur = conn.cursor()
      cur.execute( ''' CREATE TABLE IF NOT EXISTS full_urls (
                                        id integer PRIMARY KEY,
                                        url text NOT NULL
                                    );''')
      conn.commit()
  except Error as e:
      print(e)
  finally:
      if conn:
          conn.close()
  

init_db()