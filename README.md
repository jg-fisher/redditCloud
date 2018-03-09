# redditCloud
**A wordcloud generator for subreddits. Visualize frequency of word appearances!**

- subreddit_scraper.py to scrape submissions to a subreddit between specified dates.

- word_cloud.py to generate the wordcloud.

- nltk_download.py to download corpus of unecessary words.

**Commands to execute:**

python3 nltk_download.py

python3 subreddit_scraper.py subreddit start end

python3 word_cloud.py subreddit-data.csv

- subreddit is any subreddit name
- start and end are specified as an epoch time stamp (if no args passed defaults to year of 2017)
**- Add your credentials for authenticating with Reddit API to subreddit_scraper**




