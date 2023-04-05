#For custom commond 

# exec(open(r'S:\django\projects\Library\firstapp\db_shell_2.py').read())

from django.contrib.auth.models import User,Group
    
# print(User.objects.all())

# User.objects.create(username="virat",password= "virat@18") # isme password dikh jayega

# User.objects.create_user(username="virat18",password="virat18") #isme ni dikhega

from django.utils.crypto import get_random_string

# print(get_random_string(length=12))
import datetime

# print(datetime.datetime.now())

# for i in range(6,10): #bulk delete from 6 to 9
# #     print(User.objects.filter(id=i).delete())

# exec(open(r'S:\django\projects\Library\firstapp\db_shell_2.py').read())

# user = User.objects.get(id=1).profile.location
# user = User.objects.get(id=1).profile.birth_date

# print(user)




"""execute method to run raw query"""    
# from django.db import connection

# with connection.cursor() as cursor:
#     cursor.execute("SELECT * FROM library_project.book")
#     rows = cursor.fetchall()
#     print(rows)
    
    
