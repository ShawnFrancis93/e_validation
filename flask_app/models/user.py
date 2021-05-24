import re	
from flask_app.config.mysqlconnection import  connectToMySQL

class User: 
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    @staticmethod
    def validate_user( user ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid