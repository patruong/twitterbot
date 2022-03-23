import tweepy
import time
import json
import argparse

parser = argparse.ArgumentParser(
    description='A simple twitter bot - It searches for tweets based on a search phrase, likes, retweets and writes a automated message.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)


parser.add_argument('keys', type=str,
                    help='Twitter Developers API and Access keys json file.')

parser.add_argument('--n_tweets', type=int, default=5,
                    help='Number of tweets to like and retweet.')

parser.add_argument('--search', type=str, default = "I Love Python",
                    help='Search phrase on twitter.')

parser.add_argument('--message', type=str, 
                    default = None,
                    help='Search phrase on twitter.')

# parse arguments from command line
args = parser.parse_args()
keys = args.keys
n_tweets = args.n_tweets
search = args.search
message = args.message

def main(keys, n_tweets, search, message):
    with open(keys) as f:
        keys = f.read()
    keys = json.loads(keys)
    auth = tweepy.OAuthHandler(keys["API_Key"],keys["API_Key_Secret"])
    auth.set_access_token(keys["Access_Token"],keys["Access_Token_Secret"])
    api = tweepy.API(auth, wait_on_rate_limit=True)
    
    for tweet in tweepy.Cursor(api.search_tweets, search).items(n_tweets):
        try:
            print("Tweet Liked")
            tweet.favorite()
            if not tweet.retweeted:
                tweet.retweet()
                
                if message == None:
                    m = "Hi @" + tweet.user.screen_name + ", I love to Code, want to learn to code this twitter bot check @conjure_the_bar https://twitter.com/conjure_the_bar"
                else:
                    m = "Hi @" + tweet.user.screen_name + ", " + message
                t = api.update_status(status=m, in_reply_to_status_id=tweet.id)
            time.sleep(3)
        except tweepy.errors.TweepyException as e:
            print(e)
        except StopIteration:
            break

if __name__ == "__main__":
    main(keys, n_tweets, search, message)




