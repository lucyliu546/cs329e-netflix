from math import sqrt
import pickle
from requests import get
from os import path
from numpy import sqrt, square, mean, subtract

def create_cache(filename):
    """
    filename is the name of the cache file to load
    returns a dictionary after loading the file or pulling the file from the public_html page
    """
    cache = {}
    filePath = "/u/fares/public_html/netflix-caches/" + filename

    if path.isfile(filePath):
        with open(filePath, "rb") as f:
            cache = pickle.load(f)
    else:
        webAddress = "http://www.cs.utexas.edu/users/fares/netflix-caches/" + \
            filename
        bytes = get(webAddress).content
        cache = pickle.loads(bytes)

    return cache

def make_tests():
	actual_scores_cache = create_cache("cache-actualCustomerRating.pickle")
	for each in actual_scores_cache:
		print(str(each[1]) + ':')
		print(str(each[0]))

make_tests()
