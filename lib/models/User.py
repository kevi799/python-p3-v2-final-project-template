import bcrypt

class User:
    def __init__(self,id,name,email, password_hash= None):
        self.id =id
        self.name = name
        self.email = email
        self.password_hash = password_hash

    def __repr__(self):
        return f"User(ID: {self.id}, Name: {self.name}, Email: {self.email})"
    @classmethod
    def hash_password(cls,password):
        salt = bcrypt.gensalt
        return bcrypt.hashpw(password.encode('utf-8'),salt)
    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)