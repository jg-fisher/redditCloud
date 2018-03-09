# redditCloud
**A wordcloud generator for subreddits. Visualize frequency of word appearances!**

- reddit_scrape.py to scrape submissions of a subreddit between specified dates.

- word_cloud.py to generate the wordcloud.

- nltk_download.py to download corpus of unecessary words.

**Commands to execute:**

python3 nltk_download.py

python3 reddit_scrape.py subreddit start end

python3 word_cloud.py subreddit-data.csv

- subreddit is any subreddit name
- start and end are specified as an epoch time stamp (if no args passed defaults to year of 2017)




