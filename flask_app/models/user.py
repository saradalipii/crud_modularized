from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db_name='users'
    def __init__(self,data):
        self.id = data['id'],
        self.email = data['email'],
        self.name = data['name'],
        self.lastName = data['lastName']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def getAllUsers(cls):
        query= 'SELECT * FROM users;'
        results =  connectToMySQL(cls.db_name).query_db(query)
        users= []
        for row in results:
            users.append(row)
        return users
    
    @classmethod
    def get_user_by_id(cls, data):
        query= 'SELECT * FROM users WHERE users.id = %(user_id)s;'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results[0]

    @classmethod
    def create_user(cls,data):
        query = 'INSERT INTO users (email, name, lastName) VALUES ( %(email)s, %(name)s, %(lastName)s );'
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def update_users(cls,data):
        query =  'UPDATE users SET email = %(email)s, name = %(name)s, lastName = %(lastName)s  WHERE id=%(user_id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data)
        #UPDATE users SET email = %(email)s, name = %(name)s, lastName = %(lastName)s  WHERE id=%(user_id)s;

    @classmethod
    def delete_users(cls,data):
        query =  'DELETE FROM users WHERE id=%(user_id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data)
        #DELETE FROM users WHERE id=%(user_id)s;