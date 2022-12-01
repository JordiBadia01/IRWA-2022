import random

from myapp.search.algorithms import create_tfidf_index, search_in_corpus
from myapp.search.objects import ResultItem, Document


def build_demo_results(corpus: dict, search_id):
    """
    Helper method, just to demo the app
    :return: a list of demo docs sorted by ranking
    """
    res = []
    size = len(corpus)
    ll = list(corpus.values())
    for index in range(random.randint(0, 40)):
        item: Document = ll[random.randint(0, size)]
        res.append(ResultItem(item.id, item.title, item.description, item.doc_date,
                              "doc_details?id={}&search_id={}&param2=2".format(item.id, search_id), random.random()))

    # for index, item in enumerate(corpus['Id']):
    #     # DF columns: 'Id' 'Tweet' 'Username' 'Date' 'Hashtags' 'Likes' 'Retweets' 'Url' 'Language'
    #     res.append(DocumentInfo(item.Id, item.Tweet, item.Tweet, item.Date,
    #                             "doc_details?id={}&search_id={}&param2=2".format(item.Id, search_id), random.random()))

    # simulate sort by ranking
    res.sort(key=lambda doc: doc.ranking, reverse=True)
    return res


def build_results(corpus: dict, doc_scores, search_id):
    """
    Helper method, just to demo the app
    :return: a list of demo docs sorted by ranking
    """
    res = []
    for index in range(len(doc_scores)):
        doc_id = doc_scores[index][1]
        ranking = doc_scores[index][0]
        item: Document = corpus[doc_id]
        res.append(ResultItem(item.id, item.title, item.description, item.doc_date,
                              "doc_details?id={}&search_id={}&param2=2".format(item.id, search_id), ranking))

    # for index, item in enumerate(corpus['Id']):
    #     # DF columns: 'Id' 'Tweet' 'Username' 'Date' 'Hashtags' 'Likes' 'Retweets' 'Url' 'Language'
    #     res.append(DocumentInfo(item.Id, item.Tweet, item.Tweet, item.Date,
    #                             "doc_details?id={}&search_id={}&param2=2".format(item.Id, search_id), random.random()))

    # simulate sort by ranking
    return res


class SearchEngine:
    """educational search engine"""

    def __init__(self, corpus):
        self.index, self.tf, self.df, self.idf = create_tfidf_index(corpus)
        self.corpus = corpus

    def search(self, search_query, search_id, corpus):
        print("Search query:", search_query)

        results = []

        #results = build_demo_results(corpus, search_id)  # replace with call to search algorithm

        doc_scores = search_in_corpus(search_query, self.index, self.idf, self.tf)
        results = build_results(self.corpus, doc_scores, search_id)

        return results
