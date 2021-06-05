import twint
from datetime import datetime
today = datetime.now() .strftime('%Y-%m-%d')
c = twint.Config()
c.To = "networkchuck"
c.Since = today
c.Hide_output = True
c.Store_object - True

twint.run.Search(c)

tweets = twint.output.tweets_list

mypeople = []

for tweet in tweets:
        mypeople.append(('{}'.format(tweet.username)))

print (mypeople)

for user in mypeople:
	c = twint.Config()
	c.Username = user
	c.Limit = 20
	twint.run.Search(c)
