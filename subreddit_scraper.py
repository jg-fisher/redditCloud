import sys
import praw

# Authenticating with Reddit API
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     username='',
                     password='',
                     user_agent='')

subreddit = reddit.subreddit(sys.argv[1])

submission_count = 0

print('Scraping submissions..')

# Scraping submissions
with open(subreddit.display_name + '-data.csv', 'w') as f:

    # Year of 2017 unless epoch timestamp specified
    if len(sys.argv) > 2:
        start = sys.argv[2]
        end = sys.argv[3] 
    else:
       start = 1483228800 
       end = 1514764799

    for submission in subreddit.submissions(start, end):
        f.write(submission.selftext)
        submission_count += 1

    f.close()

# Information for user 
print('/r/' + str(sys.argv[1]), 'submission count: ' + str(submission_count))
print('File saved as: ' + subreddit.display_name + '-data.csv')
