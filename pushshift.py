import datetime
import time
import requests
import pandas as pd
import os
import praw
from psaw import PushshiftAPI
from dotenv import load_dotenv

load_dotenv()

subs = ['askreddit', 'askscience', 'askhistorians', 'explainlikeimfive', 'askcomputerscience', 'askculinary',
        'trueaskreddit', 'asksocialscience', 'askengineers', 'askphilosophy']
# user_agent = "LambdaAnalysisClient/0.1 by " + os.getenv("REDDIT_USERNAME")

def unique_users_per_day(subreddit, start, end):
    # r = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
    #                 client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    #                 password=os.getenv("REDDIT_PASSWORD"),
    #                 user_agent=user_agent,
    #                 username=os.getenv("REDDIT_USERNAME"))
    api = PushshiftAPI()
    gen = api.search_submissions(subreddit=subreddit, aggs='author',
                     after=start, before=end)
    next(gen)
    users = len(list(gen))
    return { "subreddit": [subreddit], 'unique_users': [users], 'date': [datetime.datetime.today() - datetime.timedelta(days=int(start[:-1]))]}

def scrape_unique_users():
    unique_users = pd.DataFrame()
    for sub in subs:
        print("Starting " + sub)
        for i in range(0, 90):
            before = str(i) + "d"
            after = str(i+1) + "d"
            new_day = pd.DataFrame(unique_users_per_day(sub, after, before))
            print(new_day.head())
            unique_users = unique_users.append(new_day)
    return unique_users

test = scrape_unique_users()
print(test.head())
test.to_csv('past_90_days_unique_users_per_day.csv')
"""
    Returns submissions from Pushshift API.
    Subreddit must be a string and a valid subreddit.
    before and after must be a string with an integer plus an epoch value.
    e.g. 4d is 4 days ago. Valid epoch values are s, m, h, d
"""
def search_submissions(subreddit, after, before, start):
    now = time.time()
    while now-start < 1:
        time.sleep(0.1)
        now = time.time()
    url = f'https://api.pushshift.io/reddit/search/submission/?subreddit={subreddit}&after={after}&before={before}&size=500&sort=desc&sort_type=score'
    # print(url)
    r = requests.get(url)
    # print("Response: " + r.text)
    submissions = r.json()
    sub_df = pd.DataFrame(submissions['data'])
    start = time.time()
    return sub_df.copy()

def scrape_submissions():
    start = time.time()
    sub_dfs = pd.DataFrame()
    # search_submissions("askreddit", "1d", "0d", start)
    for i in range(0, 90):
        before = str(i) + "d"
        after = str(i+1) + "d"
        for sub in subs:
            sub_dfs = sub_dfs.append(search_submissions(sub, after, before, start))
            # search_submissions(sub, after, before, start)
    sub_dfs.to_csv('4-30-to-7-29-submissions.csv')

def get_comment_ids(submission_id, start):
    now = time.time()
    while now-start < 1:
        time.sleep(0.1)
        now = time.time()
    url = f'https://api.pushshift.io/reddit/submission/comment_ids/{submission_id}'
    r = requests.get(url)
    comment_ids = r.json()['data'][:10]
    start = time.time()
    return comment_ids

def search_comments(submission_id, start, count):
    now = time.time()
    count = count + 1
    if count % 100 == 0:
        print(count)
    while now-start < 1:
        time.sleep(0.1)
        now = time.time()
    url = f'https://api.pushshift.io/reddit/search/comment/?link_id={submission_id}'
    r = requests.get(url)
    print(len(r.json()['data']))
    comments = pd.DataFrame(r.json()['data'])
    start = time.time()
    return comments, count

def scrape_comments(submissions):
    start = time.time()
    count = 0
    com_df = pd.DataFrame()
    for index in range(len(submissions['id'])):
        if submissions['num_comments'][index] > 2:
            new_df, count = search_comments(submissions['id'][index], start, count)
            com_df = com_df.append(new_df)
            if count % 100 == 0:
                com_df.to_csv('4-30-to-7-29-comments.csv')
    com_df.to_csv('4-30-to-7-29-comments.csv')

def get_trending_score():
    pass

def get_average_comment_count_per_post():
    pass

def get_subreddit_posts_per_day(subreddit, start):
    now = time.time()
    if now-start < 1:
        time.sleep(0.1)
        now=time.time()
    url = f'https://api.pushshift.io/reddit/search/submission/?subreddit={subreddit}&after=90d&aggs=created_utc&frequency=day&size=0'
    r = requests.get(url)
    daily_aggs = pd.DataFrame(r.json()['aggs']['created_utc'])
    daily_aggs['subreddit'] = subreddit
    return daily_aggs

def get_subreddit_comments_per_day(subreddit, start):
    now = time.time()
    if now-start < 1:
        time.sleep(0.1)
        now=time.time()
    url = f'https://api.pushshift.io/reddit/search/comment/?subreddit={subreddit}&after=90d&aggs=created_utc&frequency=day&size=0'
    r = requests.get(url)
    daily_aggs = pd.DataFrame(r.json()['aggs']['created_utc'])
    daily_aggs['subreddit'] = subreddit
    # daily_aggs['key'] = pd.to_datetime(daily_aggs['key'], unit='s')
    # daily_aggs = daily_aggs.drop(columns='Unnamed: 0')
    # daily_aggs = daily_aggs.rename(columns={'doc_count': 'comment_count', 'key': 'date'})
    return daily_aggs



def get_subreddit_unique_users():
    pass

def get_post_activity():
    pass

# submissions = pd.read_csv('4-30-to-7-29-submissions.csv')
# scrape_comments({ "id": submissions['id'].values, "num_comments": submissions['num_comments'].values })
def save_posts_per_day_csv():
    posts_per_day = pd.DataFrame()
    for sub in subs:
        posts_per_day = posts_per_day.append(get_subreddit_posts_per_day(sub, time.time()+1))
    posts_per_day.to_csv('past_90_days_post_per_day.csv')

def save_comments_per_day_csv():
    comments_per_day = pd.DataFrame()
    for sub in subs:
        start = time.time()
        comments_per_day = comments_per_day.append(get_subreddit_comments_per_day(sub, start))
    comments_per_day.to_csv('past_90_days_comments_per_day.csv')


def get_subreddit_info():
    user_agent = "LambdaAnalysisClient/0.1 by " + os.getenv("REDDIT_USERNAME")
    reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                     client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                     password=os.getenv("REDDIT_PASSWORD"),
                     user_agent=user_agent,
                     username=os.getenv("REDDIT_USERNAME"))
    start = time.time()
    subreddits_info = pd.DataFrame()
    for sub in subs:
        now = time.time()
        if now-start < 1:
            time.sleep(0.1)
            now=time.time()
        subreddit_info = reddit.subreddit(sub)

# get_subreddit_info()
# save_comments_per_day_csv()
# save_posts_per_day_csv()
# scrape_submissions()
