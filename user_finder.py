import requests

def on_insta(uname):
    instarcode = requests.get("https://instagram.com/"+uname)
    if instarcode.status_code == 200:
        return "https://instagram.com/"+uname
    else:
        return "not found"

def on_twitter(uname):
    twitterrcode = requests.get("https://twitter.com/"+uname)
    if twitterrcode.status_code == 200:
        return "https://twitter.com/"+uname
    else:
        return "not found"

def on_github(uname):
    githubrcode = requests.get("https://github.com/"+uname)
    if githubrcode.status_code == 200:
        return "https://github.com/"+uname
    else:
        return "not found"

def on_medium(uname):
    githubrcode = requests.get("https://medium.com/@"+uname)
    if githubrcode.status_code == 200:
        return "https://medium.com/@"+uname
    else:
        return "not found"

user = input("Enter the Username:")

insta = on_insta(user)
twitter = on_twitter(user)
medium = on_medium(user)
github = on_github(user)

if insta == "not found":
    print(user+" is not present on Instagram")
else:
    print(user + " is present on Instagram")
    print(user+"'s Instagram Profile URL: "+insta)
print("")

if twitter == "not found":
    print(user+" is not present on Twitter")
else:
    print(user + " is present on Twitter")
    print(user+"'s Twitter Profile URL: "+twitter)
print("")

if medium == "not found":
    print(user+" is not present on Medium")
else:
    print(user + " is present on Medium")
    print(user+"'s Medium Profile URL: "+medium)
print("")

if github == "not found":
    print(user+" is not present on Github")
else:
    print(user + " is present on Github")
    print(user+"'s Github Profile URL: "+github)
print("")
