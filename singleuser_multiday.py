import instaloader
import datetime

from datetime import datetime, timedelta
from itertools import dropwhile, takewhile


def single_user():
    # Login to your account first
    loginuser = input('Enter Login User Name: ')
    loginpwd = input('Enter Login password: ')

    singlnstance = instaloader.Instaloader()

    singlnstance.login(loginuser, loginpwd)

    username = input('Enter the Profile Name to download the posts : ')
    targetdate = input('Enter till date in YYYY-MM-DD format: ')
    year, month, day = map(int, targetdate.split('-'))
    targetdate1 = datetime.datetime(year, month, day)

    posts = instaloader.Profile.from_username(singlnstance.context, username).get_posts()

    for post in posts:
        if post.date > targetdate1:
            singlnstance.download_post(post, username)
