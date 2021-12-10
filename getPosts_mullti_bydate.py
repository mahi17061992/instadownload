# To get multiple posts
import instaloader
import datetime
import time
import csv
from pathlib import Path


def getposts_multiple():
    loginuser = input('Enter Login User Name: ')
    loginpwd = input('Enter Login password: ')
    firstinstance = instaloader.Instaloader()
    # First user needs to login to his own Instagram Account inorder to access the other public/following profiles.
    firstinstance.login(loginuser, loginpwd)

    fpath = Path('insta.csv').absolute()
    targetdate = input('Enter till date in YYYY-MM-DD format: ')
    year, month, day = map(int, targetdate.split('-'))
    targetdate1 = datetime.datetime(year, month, day)
    username = []
    with open(fpath, newline='') as f:
        for i in csv.reader(f):
            username.append(i[0])

    for user in username:
        posts = instaloader.Profile.from_username(firstinstance.context, user).get_posts()
        for post in posts:
            if post.date > targetdate1:
                firstinstance.download_post(post, user)

        time.sleep(60)


