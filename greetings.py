import datetime


def greeting():
   
    now = datetime.datetime.now()
    
    if a.hour < 12:
        
        print("Hi, Good morning!")
        
    elif 12 <= now.hour < 16:
        
        print("Hi, Good Afternoon!")
    elif 17 <= now.hour < 21:
        print("Hi, Good Evening!")


greeting()
