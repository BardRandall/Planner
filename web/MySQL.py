import pymysql.cursors
from web.config import db_host, db_user, db_pass, db_name

db = pymysql.connect(db_host, db_user, db_pass, db_name)
