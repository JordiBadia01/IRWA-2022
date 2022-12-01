from datetime import datetime

import pandas as pd

from myapp.core.utils import load_json_file
from myapp.search.objects import Document

_corpus = {}


def load_corpus(tweet_path, doc_to_tweet_path) -> [Document]:
    """
    Load file and transform to dictionary with each document as an object for easier treatment when needed for displaying
     in results, stats, etc.
    :param
    tweet_path: path of the file of tweets
    doc_to_tweet_path: path of file of docs to tweets
    :return corpus:
    """
    df = _load_corpus_as_dataframe(tweet_path, doc_to_tweet_path)
    df.apply(_row_to_doc_dict, axis=1)
    return _corpus


def _load_corpus_as_dataframe(tweet_path, doc_to_tweet_path):
    """
    Load documents corpus from file in 'path'
    :return:
    """
    json_data = load_json_file(tweet_path, doc_to_tweet_path)
    tweets_df = _load_tweets_as_dataframe(json_data)
    _clean_hashtags_and_urls(tweets_df)
    # Rename columns to obtain: Tweet | Username | Date | Hashtags | Likes | Retweets | Url | Language | Link
    corpus = tweets_df.rename(
        columns={"id": "Id", "full_text": "Tweet", "screen_name": "Username",
                 "favorite_count": "Likes",
                 "retweet_count": "Retweets", "lang": "Language"})

    # select only interesting columns
    filter_columns = ["Id", "Tweet", "Username", "Date", "Hashtags", "Likes", "Retweets", "Url", "Language", "Link"]
    corpus = corpus[filter_columns]
    return corpus


def _load_tweets_as_dataframe(json_data):
    data = pd.DataFrame(json_data).transpose()
    # parse entities as new columns
    data = pd.concat([data.drop(['entities'], axis=1), data['entities'].apply(pd.Series)], axis=1)
    # parse user data as new columns and rename some columns to prevent duplicate column names
    data = pd.concat([data.drop(['user'], axis=1), data['user'].apply(pd.Series).rename(
        columns={"created_at": "user_created_at", "id": "user_id", "id_str": "user_id_str", "lang": "user_lang"})],
                     axis=1)
    return data


def _build_tags(row):
    tags = []
    for ht in row:
        tags.append(ht["text"])
    return tags


def _build_hashtags(row):
    tags = []
    for ht in row:
        tags.append('#' + ht["text"])
    return tags


def _build_date(row):
    try:
        created_at = datetime.strptime(row, "%a %b %d %X %z %Y")
        return created_at.strftime('%A %d %B %Y')
    except KeyError:
        return ' '


def _build_url(row):
    try:
        url = row["entities"]["url"]["urls"][0]["url"]  # tweet URL
    except:
        try:
            url = row["retweeted_status"]["extended_tweet"]["entities"]["media"][0]["url"]  # Retweeted
        except:
            url = ""
    return url


def _build_link(row):
    link = ""
    try:
        link = 'https://twitter.com/' + row['user']['screen_name'] + '/status/' + str(row['id'])  # tweet URL
    except:
        link = ""
    return link


def _clean_hashtags_and_urls(df):
    df["Hashtags"] = df["hashtags"].apply(_build_hashtags)
    df["Date"] = df["created_at"].apply(_build_date)
    df["Url"] = df.apply(lambda row: _build_url(row), axis=1)
    df["Link"] = df.apply(lambda row: _build_link(row), axis=1)
    df.drop(columns=["entities"], axis=1, inplace=True)


def _row_to_doc_dict(row: pd.Series):
    _corpus[row['Id']] = Document(row['Id'], row['Tweet'][0:100], row['Tweet'], row['Date'], row['Likes'],
                                  row['Retweets'],
                                  row['Url'], row['Hashtags'], row['Link'])
