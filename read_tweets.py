#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


def read_tweets(user):
    print(f"Tweets for {user}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", help="Twitter user", required=True)
    args = parser.parse_args()

    read_tweets(user=args.user)
