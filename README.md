# Password hashing with Python #

CLI example to demonstrate storing hashed passwords in the database.

## Setup ##

Setup virtual environment for Python 3.6

```sh
virtualenv -p /usr/bin/python3.6 env
source bin/env/activate
```

Install [poetry](https://python-poetry.org/docs/#installation)

```sh
poetry install
```

Install and ensure that [MongoDB](https://www.mongodb.com) is running


## Run ##

```sh
python src/main.py
```

## References ##

* [How to hash Passwords in Python - Nitratine](https://nitratine.net/blog/post/how-to-hash-passwords-in-python/)
* [getpass - Python](https://docs.python.org/3.6/library/getpass.html#module-getpass)
