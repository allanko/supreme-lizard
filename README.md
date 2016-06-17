## Supreme Lizard 
This Twitter bot scrapes headlines about Donald Trump from the last seven days and tweets a random headline, replacing "Trump" with "Supreme Lizard." Headlines are retrieved with the [Mediacloud](http://mediacloud.org/) Python API, found [here](https://pypi.python.org/pypi/mediacloud).

See the bot in action [here](https://twitter.com/lizardheadlines).

# Try it yourself
Fill in your Mediacloud and Twitter API tokens in `config.txt.template` and rename it `config.txt`. Run `pip install -r requirements.txt` to install dependencies. Then run `python supremelizard.py` to post your own Tweet about the Supreme Lizard. 