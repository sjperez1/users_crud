from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * "
        query += "FROM users;"
        results = connectToMySQL('users_schema').query_db(query)

        users = []

        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    # Data is holding a dictionary of things that come from our form. The insert into in parentheses has names matching the columns in database and values names need to match the keys in the dictionaries that you are giving the values for
    def create(cls, data):
        query = "INSERT INTO users(first_name, last_name, email) "
        query += "VALUES( %(first_name)s, %(last_name)s, %(email)s);"

        new_user = connectToMySQL('users_schema').query_db(query, data)
        return new_user

    @classmethod
    def get_user(cls, data):
        query = "SELECT * "
        query += "FROM users "
        query += "WHERE id = %(id)s;"
        result = connectToMySQL('users_schema').query_db(query, data)
        print(result)
        # Need result[0] because result is a list of dictionaries and I want to look at the first thing in the result dictionary to get the id. Found this out by printing result and refreshing page and looking at the list in my terminal.
        one_user = cls(result[0])
        return one_user

    @classmethod
    def edit(cls, data):
        query = "UPDATE users "
        query += "SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s "
        query += "WHERE id = %(id)s;" 
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users "
        query += "WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query, data)