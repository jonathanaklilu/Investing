import mysql.connector
import os

cnx = mysql.connector.connect(user=os.environ.get('user_db'), password=os.environ.get('password_db'),
                              host=os.environ.get('host_db'),
                              port=os.environ.get('port_db'),
                              database='investment_db')
