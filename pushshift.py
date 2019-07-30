import datetime
import time
import requests
import pandas as pd


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
    url = f'https://api.pushshift.io/reddit/search/submission/?subreddit={subreddit}&after={after}&before={before}&size=500'
    # print(url)
    r = requests.get(url)
    # print("Response: " + r.text)
    submissions = r.json()
    sub_df = pd.DataFrame(submissions['data'])
    start = time.time()
    return sub_df.copy()

subs = ['askreddit', 'askscience', 'askhistorians', 'eli5', 'askcomputerscience', 'askculinary',
        'trueaskreddit', 'asksocialscience', 'askengineers', 'askphilosophy']

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

def search_comments(submission_id, start):
    now = time.time()
    while now-start < 1:
        time.sleep(0.1)
        now = time.time()
    url = f'https://api.pushshift.io/reddit/submission/comment_ids/{submission_id}'
    r = requests.get(url)
    submissions = r.json()
    com_df = pd.DataFrame(submissions['data'])
    start = time.time()
    return com_df.copy()