import datetime
import json
from random import random

from faker import Faker

fake = Faker()


# fake.date_between(start_date='today', end_date='+30d')
# fake.date_time_between(start_date='-30d', end_date='now')
#
# # Or if you need a more specific date boundaries, provide the start
# # and end dates explicitly.
# start_date = datetime.date(year=2015, month=1, day=1)
# fake.date_between(start_date=start_date, end_date='+30y')

def get_random_date():
    """Generate a random datetime between `start` and `end`"""
    return fake.date_time_between(start_date='-30d', end_date='now')


def get_random_date_in(start, end):
    """Generate a random datetime between `start` and `end`"""
    return start + datetime.timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=random.randint(0, int((end - start).total_seconds())), )


def load_json_file(path_tweets, path_docs_tweet):
    """Load JSON content from file in 'path'

    Parameters:
    path (string): the file path

    Returns:
    JSON: a JSON object
    """

    id_tweet = {}
    doc_tweet = {}
    # Load the file
    with open(path_tweets) as tp:
        for line in tp.readlines():
            # Parse the string into a JSON object
            tweet = json.loads(line)
            id_tweet[tweet['id']] = tweet

    # Load the file
    with open(path_docs_tweet) as dp:
        for line in dp.readlines():
            line = line.split()
            doc_tweet[line[0]] = id_tweet[int(line[1])]
    return doc_tweet
