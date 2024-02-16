from operator import itemgetter

from utils.util import get_number

users = [
    {"name": "validuser", "email": f"gatsugame@gmail.com", "password": "Zimba1434"},
]


def get_user(name):
    try:
        return next(user for user in users if user["name"] == name)
    except:
        print("\n   User %s is not defined, enter a valid user.\n" % name)
