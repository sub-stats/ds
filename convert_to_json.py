import json

"""
    Converts files from https://files.pushshift.io/reddit/comments/ to actual JSON for importing to Pandas.
    Need to add extensibility for large amount of files.
"""
fname_load = 'RS_v2_2008-01'
fname_save = 'RS_v2_2008-01.json'
dictList = []
with open(fname_load, 'r') as f, open(fname_save, 'w') as s:
    for line in f:
        comment = json.loads(line)
        dictList.append(comment)
    s.write(json.dumps(dictList, indent=4))
