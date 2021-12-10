# To get Last 7 days posts via Excel file of users.
import instaloader
import datetime
import time
import csv
from pathlib import Path
from datetime import datetime, timedelta
from itertools import dropwhile, takewhile


def getposts_sevendays():
    loginuser = input('Enter Login User Name: ')
    loginpwd = input('Enter Login password: ')

    instanter = instaloader.Instaloader()
    # User need to login to his own account before accessing other followed/Public profiles.
    instanter.login(loginuser, loginpwd)

    fpath = Path('insta.csv').absolute()

    username = []
    with open(fpath, newline='') as f:
        for i in csv.reader(f):
            username.append(i[0])

    for user in username:

        posts = instaloader.Profile.from_username(instanter.context, user).get_posts()

        since = datetime.today()

        until = since - timedelta(days=7)

        for post in takewhile(lambda p: p.date > until, dropwhile(lambda p: p.date > since, posts)):
            print(post.date)
            instanter.download_post(post, user)

        time.sleep(60)


