#!/usr/bin/env python3

# -------
# imports
# -------

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


AVERAGE_RATING = 3.60428996442

# {(customer, movie): rating}
ACTUAL_CUSTOMER_RATING = create_cache(
    "cache-actualCustomerRating.pickle")

avg_movie_rating_cache = create_cache(
    "cache-averageMovieRating.pickle")

avg_cust_rating_cache = create_cache("cache-averageCustomerRating.pickle")

# ------------
# netflix_eval
# ------------

def netflix_eval(reader, writer) :
    predictions = []
    actual = []

    # iterate through the file reader line by line
    for line in reader:
    # need to get rid of the '\n' by the end of the line
        line = line.strip()
        # check if the line ends with a ":", i.e., it's a movie title 
        if line[-1] == ':':
		# It's a movie
            current_movie = line.rstrip(':')

            # get average movie rating
            avg_movie_rating = avg_movie_rating_cache[int(current_movie)]

            writer.write(line)
            writer.write('\n')
        else:
		# It's a customer
            current_customer = line

            #get average customer rating
            avg_cust_rating = avg_cust_rating_cache[int(current_customer)]

            # make prediction
            prediction = 3.7 + (avg_movie_rating - 3.7) + (avg_cust_rating - 3.7)

            predictions.append(prediction)
            actual.append(actual_scores_cache[int(current_movie)][int(current_customer)])
            writer.write(str(prediction)) 
            writer.write('\n')
    # calculate rmse for predications and actuals
    rmse = sqrt(mean(square(subtract(predictions, actual))))
    writer.write(str(rmse)[:4] + '\n')