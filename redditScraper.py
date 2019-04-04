#DISCLAIMER: I reeferenced a very basic tutorial for this project so some of the code is similar
#See here: http://www.storybench.org/how-to-scrape-reddit-with-python/
import praw

reddit = praw.Reddit(client_id='JsVVo5XWmdYP2w', \
                     client_secret='iKm_iNChN_WS-WceieCJRXridTo', \
                     user_agent='Reddit Scraper Tool', \
                     username='alphabetguyazlo', \
                     password='Asayee22!')

#CHANGE USERNAME AND PW BEFORE SUBMITTING


#take the top 5 posts and add them to a list of dictionaries

subreddit = reddit.subreddit('apexlegends')
top5Posts = []

for submission in subreddit.top(limit=5):
    post = { 
        "title": submission.title,
        "score": submission.score,
        "id": submission.id, 
        "url": "https://www.reddit.com" + submission.permalink,
        "comments": submission.num_comments,
        "created": submission.created,
        "body": submission.selftext
    }
    top5Posts.append(post)

print(top5Posts)