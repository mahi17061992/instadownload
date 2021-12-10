import instaloader
import datetime

from datetime import datetime, timedelta
from itertools import dropwhile, takewhile


def single_seven():
    # Login to your account first
    loginuser = input('Enter Login User Name: ')
    loginpwd = input('Enter Login password: ')

    singinstance = instaloader.Instaloader()

    singinstance.login(loginuser, loginpwd)

    username = input('Enter the Profile Name to download the posts : ')

    posts = instaloader.Profile.from_username(singinstance.context, username).get_posts()

    since = datetime.today()

    until = since - timedelta(days=7)

    for post in takewhile(lambda p: p.date > until, dropwhile(lambda p: p.date > since, posts)):
        print(post.date)
        singinstance.download_post(post, username)
