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
    url = f'https://api.pushshift.io/reddit/search/submission/?subreddit={subreddit}&after={after}&before={before}&size=500&sort=desc&sort_type=score'
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

def search_comment(comment_ids, start):
    now = time.time()
    while now-start < 1:
        time.sleep(0.1)
        now = time.time()
    url = f'https://api.pushshift.io/reddit/search/comment/?ids={",".join(comment_ids)}'
    r = requests.get(url)
    comments = pd.DataFrame(r.json()['data'])
    start = time.time()
    return comments

def scrape_comments(submission_ids):
    start = time.time()
    com_df = pd.DataFrame()
    for id in submission_ids:
        comment_ids = get_comment_ids(id, start)
        com_df = com_df.append(search_comment(comment_ids, start))


# scrape_submissions()