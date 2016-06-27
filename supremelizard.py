# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
import mediacloud, datetime, tweepy, random

# load config
parser = SafeConfigParser()
parser.read('config.txt')
MY_API_KEY = parser.get('MEDIACLOUD', 'MY_API_KEY')
mc = mediacloud.api.MediaCloud(MY_API_KEY)

# stories with trump
sources = 'tags_id_media:(8875027 9139487)' # us mainstream media and us top online news
query = 'trump'

step = datetime.timedelta(7)
today = datetime.date.today() 

stories = mc.storyList(query, solr_filter = [mc.publish_date_query(today - step, today), sources], rows = 1000)
headlines = [s['title'] for s in stories if 'Trump' in s['title']]
pick = random.choice(headlines)
if 'Donald Trump' in pick:
    tweet = pick.replace('Donald Trump', 'Supreme Lizard')
elif 'the Trump' in pick:
    tweet = pick.replace('the Trump', 'the Lizard')
else:
    tweet = pick.replace('Trump', 'Supreme Lizard')

# tweeting
CONSUMER_KEY = parser.get('TWITTER', 'CONSUMER_KEY')
CONSUMER_SECRET = parser.get('TWITTER', 'CONSUMER_SECRET')
ACCESS_KEY = parser.get('TWITTER', 'ACCESS_KEY')
ACCESS_SECRET = parser.get('TWITTER', 'ACCESS_SECRET')
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status(tweet)