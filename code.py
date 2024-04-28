# importing the libraries
import praw
import config as c

# data for bot login stored in another file named config.py
def bot_login():
    r=praw.Reddit(
        username=c.username,
        password=c.password,
        client_id=c.client_id,
        client_secret=c.client_sc,
        user_agent="tester v0.1",
    )
    return r

# login the bot into reddit
r = bot_login()

# chose the subreddit 
subreddit = r.subreddit("news")


# choose category and number of responses
t25 = subreddit.hot(limit=25)
c = 1

# print the responses
for i in t25:
    print(str(c)+". "+i.title+"\n")
    c+=1
