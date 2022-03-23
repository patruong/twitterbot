# twitterbot

Followed tutorial:
https://medium.com/@drixbarsali/how-to-create-a-twitter-bot-using-tweepy-and-python-691061119c20

Tweepy has been updated since the tutorial. 

1. We should have the API and Access keys in a seperate file.
2. Change "api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)" => "api = tweepy.API(auth, wait_on_rate_limit=True)".
3. Change "tweepy.TweepError" => "tweepy.errors.TweepyException".
4. In developer.twitter.com apply for Elevated Twitter API v2.
5. In authentication settings change App permissions to "Read and write and Direct message".
6. Set Callback URI / Redirect URL to https://127.0.0.1:5000
7. Set Website URL to https://twitter.com/<username>
  
  
