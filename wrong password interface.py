import time
import datetime
import random
user_lock=input('Enter a password in alphabet:')
print('User password is saved')
time.sleep(2)
i=1
while i<=10:
    user_ent=input('Enter password for unclock your device You have only {} chance!'.format(i))
    if user_lock==user_ent:
            print('Access granted')
            break
else:
        print('Wrong password try in ')
        h=m=0
        s=random.randint(8,25)
        def countdwon(m,h,s):
            while s>0:
                timer=datetime.timedelta(seconds=s)
                print(timer,end='\r')
                time.sleep(1)
                s-=1
            print('Access denied')
        countdwon(int(h),int(m),int(s))    
i+=1