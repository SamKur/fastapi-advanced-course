from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto', bcrypt__truncate_error=False)

# In a real database (like SQL or MongoDB), the "Key" would usually be a unique ID (like 101), 
# while the "username" would stay as a property inside the object.
fake_user_db = {
    'johndoe': {
        'username': 'johndoe',
        'hashed_password': pwd_context.hash('secret123') 
    }
}


def get_user(username: str): # this is outside key # helper func to check if user exists in the database
    user = fake_user_db.get(username)
    return user


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)