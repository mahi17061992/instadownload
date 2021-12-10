
from instamodule.GetPostsExcel_sevenDays import getposts_sevendays
from instamodule.getPosts_mullti_bydate import getposts_multiple
from instamodule.singleuser_Sevendays import single_seven
from instamodule.singleuser_multiday import single_user

print('Here are your options:\n'
      'To download single user insta posts from past 7 days select option 1\n'
      'To download single user insta posts till certain date select option 2 \n'
      'To download multiple insta profile posts of last 7 days using an excel file select option 3\n'
      'To download multiple insta profile posts until certain date select option 4')

choice = int(input('Your choice: '))

if choice == 1:
    single_seven()
elif choice == 2:
    single_user()
elif choice == 3:
    getposts_sevendays()
elif choice == 4:
    getposts_multiple()
else:
    print('Your choice is invalid')
