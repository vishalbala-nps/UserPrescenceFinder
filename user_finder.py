import requests

def on_insta(uname):
    instarcode = requests.get("https://instagram.com/"+uname)
    if instarcode.status_code == 200:
        return "https://instagram.com/"+uname
    else:
        return 1

def on_twitter(uname):
    twitterrcode = requests.get("https://twitter.com/"+uname)
    if twitterrcode.status_code == 200:
        return "https://twitter.com/"+uname
    else:
        return 1

def on_github(uname):
    githubrcode = requests.get("https://github.com/"+uname)
    if githubrcode.status_code == 200:
        return "https://github.com/"+uname
    else:
        return 1

user = input("Enter the Username:")

insta = on_insta(user)
twitter = on_twitter(user)
github = on_github(user)

if insta != 1:
    print(user + " is present on Instagram")
    print(user+"'s Instagram Profile URL: "+insta)

if twitter != 1:
    print(user + " is present on Twitter")
    print(user+"'s Twitter Profile URL: "+twitter)

if github != 1:
    print(user + " is present on Github")
    print(user+"'s Github Profile URL: "+github)
else:
    print(user + " is not present on Github, Twitter or Instagram")