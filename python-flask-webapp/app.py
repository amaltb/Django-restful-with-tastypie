from user import User
from login import Login
from database import Database

Database.initialise(database="learning", user="ambabu", password="Workexp8261@", host="localhost")


email = raw_input("Enter your email Id: ")

user = User.load_from_db_by_screenname(email)

if user:
    oauth_token = user.oauth_token
    oauth_token_secret = user.oauth_token_secret

else:
    access_token = Login.login_wt_twitter_acc()
    first_name = raw_input("Enter first name: ")
    last_name = raw_input("Enter last name: ")

    oauth_token = access_token['oauth_token']
    oauth_token_secret = access_token['oauth_token_secret']
    user = User(email, first_name, last_name,
                oauth_token, oauth_token_secret, None)
    user.save_to_db()

print("Reading tweets....")

tweets = user.tweet_request("https://api.twitter.com/1.1/search/tweets.json?q=Rohit Sharma")

try:
    for tweet in tweets['statuses']:
        print(tweet['text'])
except KeyError:
    print("Error while printing tweets...")
