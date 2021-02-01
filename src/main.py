from cmd import Cmd
from os import urandom
from getpass import getpass
from hashlib import pbkdf2_hmac
from pymongo import MongoClient


def get_database():
    client = MongoClient("mongodb://localhost:27017/")
    return client["testdb"]


def hash_password(password_input, salt):
    new_key = pbkdf2_hmac(
        "sha256",
        password_input.encode("utf-8"),  # Convert the password to bytes
        salt,
        100000,
    )
    return new_key


class PasswordShell(Cmd):
    intro = 'Welcome to Password Hashing Test Shell.\nType help or ? to list commands.\n'
    prompt = '(hash) '
    file = None
    db = get_database()

    def do_create(self, arg):
        username = input("Username: ")

        found_user = self.db["users"].find_one({'username': username})
        if found_user:
            print('Username already taken.')
            return

        password = getpass("Password: ")
        print(arg)

        salt = urandom(32)
        key = hash_password(password, salt)

        some_user = {
            "username": username,
            "password": salt + key,
        }
        self.db["users"].insert_one(some_user)

        print(f"User {username} is created")

    def do_login(self, arg):
        username = input("Username: ")
        found_user = self.db["users"].find_one({'username': username})
        if not found_user:
            print('User not found')
            return
        salt = found_user["password"][:32]
        key = found_user["password"][32:]
        
        password_input = getpass("Password: ")
        check_key = hash_password(password_input, salt)
        
        if key == check_key:
            print(f'Login Successful! Welcome {username}.')
        else:
            print('Login failed.')

if __name__ == "__main__":
    PasswordShell().cmdloop()
