#DISCLAIMER: I reeferenced a very basic tutorial for this project so some of the code is similar
#See here: http://www.storybench.org/how-to-scrape-reddit-with-python/

import praw
reddit = praw.Reddit(client_id='Lqu2zqaktP7mvw', \
                     client_secret='-PSPj5n4df958RUmsq2qyGQkIp0', \
                     user_agent='reddit-content-filter', \
                     username='asayee', \
                     password='password123')

subreddit = reddit.subreddit("cats")

def changeSubreddit(newSubreddit):
    global subreddit 
    subreddit = reddit.subreddit(newSubreddit)
    if subreddit is None:
        subreddit = reddit.subreddit("cats")

def queryPosts(searchQuery, sortingMethod, limit):
    if (sortingMethod is not "confidence" or 
        sortingMethod is not "top" or 
        sortingMethod is not "new" or
        sortingMethod is not "controversial" or
        sortingMethod is not "old" or
        sortingMethod is not "random" or
        sortingMethod is not "qa" or
        sortingMethod is not "live" or
        sortingMethod is not "blank"):
        error = "Not a valid sorting method"

    queriedPosts = []
    searchQuery = searchQuery.split(", ")
    for query in searchQuery:
        for submission in subreddit.search(query, sort=sortingMethod, limit=limit):
            post = { 
                "title": submission.title,
                "score": submission.score,
                "id": submission.id, 
                "url": "https://www.reddit.com" + submission.permalink,
                "comments": submission.num_comments,
                "created": submission.created,
                "body": submission.selftext,
                "media": submission.url
            }
            queriedPosts.append(post)

    return queriedPosts