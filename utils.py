import requests

def count_words_at_url(url):
    """Heroku example
    Read more https://devcenter.heroku.com/articles/python-rq
    """
    resp = requests.get(url)
    return len(resp.text.split())
