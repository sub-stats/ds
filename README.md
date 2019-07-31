# Sub Stats Data Science Repository

## Data Overview

### 4-30-to-7-29-submissions.csv 
contains Reddit submissions from 
['askreddit', 'askscience', 'askhistorians', 'eli5', 'askcomputerscience','askculinary', 'trueaskreddit', 'asksocialscience', 'askengineers', 'askphilosophy']
It contains submissions from May 2nd to July 29th contrary to what the filename would indicate.
Example JSON:
```
'{
    "Unnamed: 0":0,
    "all_awardings":"[]",
    "allow_live_comments":false,"author":"margipants1",
    "author_cakeday":null,
    "author_flair_background_color":null,
    "author_flair_css_class":null,
    "author_flair_richtext":"[]",
    "author_flair_template_id":null,
    "author_flair_text":null,
    "author_flair_text_color":null,
    "author_flair_type":"text",
    "author_fullname":"t2_494o7j5e",
    "author_patreon_flair":false,
    "banned_by":null,
    "can_mod_post":false,
    "collections":null,
    "contest_mode":false,
    "created_utc":1564382519,
    "crosspost_parent":null,
    "crosspost_parent_list":null,
    "distinguished":null,
    "domain":"self.AskReddit",
    "edited":null,
    "event_end":null,
    "event_is_live":null,
    "event_start":null,
    "full_link":"https:\\/\\/www.reddit.com\\/r\\/AskReddit\\/comments\\/cj7jdw\\/if_you_had_just_one_wish_what_would_you_wish_for\\/",
    "gilded":null,
    "gildings":"{}",
    "id":"cj7jdw",
    "is_crosspostable":true,
    "is_meta":false,
    "is_original_content":false,
    "is_reddit_media_domain":false,
    "is_robot_indexable":true,
    "is_self":true,
    "is_video":false,
    "link_flair_background_color":null,
    "link_flair_css_class":null,
    "link_flair_richtext":"[]",
    "link_flair_template_id":null,
    "link_flair_text":null,
    "link_flair_text_color":"dark",
    "link_flair_type":"text",
    "locked":false,
    "media":null,
    "media_embed":null,
    "media_metadata":null,
    "media_only":false,
    "no_follow":true,
    "num_comments":19,
    "num_crossposts":0,
    "over_18":false,
    "parent_whitelist_status":"all_ads",
    "permalink":"\\/r\\/AskReddit\\/comments\\/cj7jdw\\/if_you_had_just_one_wish_what_would_you_wish_for\\/",
    "pinned":false,
    "post_hint":null,
    "preview":null,
    "pwls":6.0,
    "retrieved_on":1564382520,
    "score":2,
    "secure_media":null,
    "secure_media_embed":null,
    "selftext":null,
    "send_replies":true,
    "spoiler":false,
    "stickied":false,
    "subreddit":"AskReddit",
    "subreddit_id":"t5_2qh1i",
    "subreddit_subscribers":23778671,
    "subreddit_type":"public",
    "suggested_sort":null,
    "thumbnail":"self",
    "thumbnail_height":null,
    "thumbnail_width":null,
    "title":"If you had just one wish what would you wish for and why ? What difference would it make in your life ?",
    "total_awards_received":0,"updated_utc":1564468885.0,
    "url":"https:\\/\\/www.reddit.com\\/r\\/AskReddit\\/comments\\/cj7jdw\\/if_you_had_just_one_wish_what_would_you_wish_for\\/",
    "whitelist_status":"all_ads","wls":6.0
}'
```

### 4-30-to-7-29-comments.csv
contains reddit comments from the submissions in the above file.
It only contains comments from submissions with more than 2 comments and contains a max of 25 comments per submission.
It contains comments from July 18th to July 30th again contrary to the filename.
Example JSON:
```
'{
    "Unnamed: 0":0,
    "all_awardings":"[]",
    "approved_at_utc":null,
    "author":"HEROROYDEN",
    "author_cakeday":null,
    "author_flair_background_color":null,
    "author_flair_css_class":null,
    "author_flair_richtext":"[]",
    "author_flair_template_id":null,
    "author_flair_text":null,
    "author_flair_text_color":null,
    "author_flair_type":"text",
    "author_fullname":"t2_1283qb",
    "author_patreon_flair":false,
    "banned_at_utc":null,
    "body":"How is he a buffoon then you idiot.",
    "can_mod_post":false,
    "collapsed":false,
    "collapsed_reason":null,
    "created_utc":1564450080,
    "distinguished":null,
    "edited":false,
    "gildings":"{}",
    "id":"evdxlc6",
    "is_submitter":true,
    "link_id":"t3_cjjtnn",
    "locked":false,
    "no_follow":true,
    "parent_id":"t1_evdwqpw",
    "permalink":"\\/r\\/AskReddit\\/comments\\/cjjtnn\\/people_of_reddit_what_is_something_your_country\\/evdxlc6\\/",
    "retrieved_on":1564450082.0,
    "score":1.0,
    "send_replies":true,
    "stickied":false,
    "subreddit":"AskReddit",
    "subreddit_id":"t5_2qh1i",
    "total_awards_received":0.0
}'
```

### past_90_days_comments_per_day.csv
contains comments per day for each of the subreddits
Example JSON:
```
'{
    "posts_count":1892.0,
    "date":1556668800000,
    "subreddit":"askreddit"
}'
```

### past_90_days_post_per_day.csv
contains submissions per day for each of the subreddits
Example JSON:
```
'{
    "comments_count":14054.0,
    "date":1556668800000,
    "subreddit":"askreddit"
}'
```