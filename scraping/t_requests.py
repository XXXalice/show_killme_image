import doctest
import requests



def requests_test(query):
    '''
    try accsess my hp
    >>> from t_requests import requests_test
    >>> requests_test('hello')
    <Response [200]>

    >>> requests_test('asdf')
    <Response [200]>
    '''
    url = "https://xxxalice.github.io/"

    q = {
        "q" : query
    }

    uri_add_query = requests.get(url=url, params=q)

    return uri_add_query


if __name__ == '__main__':
    doctest.testmod()