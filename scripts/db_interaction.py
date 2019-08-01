import os
import psycopg2 as pg

from dotenv import load_dotenv

load_dotenv()

db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")

conn = pg.connect(dbname=db_name, user=db_user,
                     password=db_pass, host=db_host)

curs = conn.cursor()

def create_tables():
    create_submission_table = '''
        CREATE TABLE submission (
            title text,
            id text,
            url text,
            permalink text,
            domain text,
            over_18 BOOLEAN,
            selftext text,
            created_utc timestamp,
            is_self BOOLEAN,
            author text,
            subreddit text,
            subreddit_id text,
            num_comments int
        )
    '''

    create_comment_table = '''
        CREATE TABLE comment (
            id text,
            subreddit_id text,
            parent_id text,
            body text,
            subreddit text,
            created_utc timestamp,
            link_id text,
            author, text,
            score int
        )
    '''

    create_submission_per_day_table = '''
        CREATE TABLE submissions_per_day (
            posts_count int,
            date timestamp,
            subreddit text
        )
    '''

    create_comments_per_day_table = '''
        CREATE TABLE comments_per_day (
            comments_count int,
            date timestamp,
            subreddit text
        )
    '''

    curs.execute(create_submission_table)
    curs.execute(create_comment_table)
    curs.execute(create_submission_per_day_table)
    curs.execute(create_comments_per_day_table)

# def insert_data():
#     submissions_90 = pd.read_csv('4-30-to-7-29-submissions')


create_tables()

