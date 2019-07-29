#! /usr/local/anaconda3/envs/sub-stats
import zstandard as zstd
import pandas as pd
import io
import datetime

subs = ['askreddit', 'askscience', 'askhistorians', 'eli5', 'askcomputerscience', 'askculinary',
        'trueaskreddit', 'asksocialscience', 'askengineers', 'askphilosophy']

ten_df = pd.DataFrame()
count = 0
start = 0
end = 10000
path = 'RS_2019-04.zst'
print(datetime.datetime.now())

with open(path, 'rb') as fh:
    dctx = zstd.ZstdDecompressor()
    stream_reader = dctx.stream_reader(fh)
    text_stream = io.TextIOWrapper(stream_reader, encoding='utf-8')

    for line in text_stream:
        if count >= start:
            temp = pd.read_json(line, lines=True)
            if str(temp['subreddit'][0]).lower() in subs:
                ten_df = ten_df.append(temp, sort=True)
        if count >= end:
            break
        count += 1

ten_df.to_csv('RS_2019-04-10k.csv')
print(datetime.datetime.now())