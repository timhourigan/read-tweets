#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os

import tweepy


def read_tweets(user, number, reverse):
    print(f"Reading {number} tweets for {user}")

    auth = tweepy.OAuthHandler(
        os.environ.get("TWITTER_API_KEY"), os.environ.get("TWITTER_API_SECRET")
    )
    auth.set_access_token(
        os.environ.get("TWITTER_ACCESS_TOKEN"),
        os.environ.get("TWITTER_ACCESS_TOKEN_SECRET"),
    )
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except Exception:
        print("Error during authentication, check credentials")

    tweets = [
        s
        for s in tweepy.Cursor(api.user_timeline, id=user, tweet_mode="extended").items(
            number
        )
    ]
    if reverse:
        tweets.reverse()

    for t in tweets:
        print(f"{t.created_at}\n\t{t.full_text}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", help="Twitter user", required=True)
    parser.add_argument("-n", "--number", help="Number of tweets", type=int, default=50)
    parser.add_argument(
        "-r",
        "--reverse",
        help="Display in reverse chronological order",
        default=False,
        action="store_true",
    )

    args = parser.parse_args()

    read_tweets(user=args.user, number=args.number, reverse=args.reverse)
