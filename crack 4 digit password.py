import time
import random
import datetime
print('Enter a 4 digit password')
user_pass=int(input('>>>'))
print('Just wait a second...')
time.sleep(3)
print('Your password will be saved in')
s=random.randint(5,10)
def countdwon(s):
    while s>0:
        timer=datetime.timedelta(seconds=s)
        print(timer,end='\r')
        time.sleep(1)
        s-=1
countdwon(int(s))
print('Password is saved successfully')
print('If you want to crack your password press[y/n]')
crack_pass=input('>>>')
print('OK wait')
time.sleep(3)
print('Hii dude its not a joke!')
time.sleep(2)
print('I am working your commond line....')
if crack_pass=='y':
    i=1
    while i<=100000:
        random_pass=random.randint(1000,9999)
        print(random_pass,end='\r')
        if random_pass==user_pass:
            print('User password is {}'.format(user_pass))
            print('Password satisfied')
            break
        else:
            print()
        i+=1
else:
    print('Are you choose not crack password')
    print('Please wait...')
    time.sleep(3)
    print('Program over in')
    over=random.randint(5,10)
    def countdwon(s):
        while s>0:
            timer=datetime.timedelta(seconds=s)
            print(timer,end='\r')
            tims.sleep(1)
            s-=1
    countdwon(int(s))
print('Program successfully over')