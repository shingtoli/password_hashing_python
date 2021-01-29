from os import urandom
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


def main():
    db = get_database()
    salt = urandom(32)
    key = hash_password('mypassword', salt)
    some_user = {
        "username": "some_user",
        "password": salt + key,
    }
    db["users"].insert_one(some_user)


if __name__ == "__main__":
    main()
