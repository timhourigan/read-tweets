# read-tweets

Read a series of tweets.

```bash
# Export Twitter authentication
$ export TWITTER_API_KEY=<key>
$ export TWITTER_API_SECRET=<secret>
$ export TWITTER_ACCESS_TOKEN=<token>
$ export TWITTER_ACCESS_TOKEN_SECRET=<token-secret>


$ pipenv sync
$ pipenv run ./read_tweets.py --user <twitter-account> --number <number-of-tweets>
```
