# Import necessary packages, and methods from the utility functions file
import math
import statistics

import pandas as pd
from utility_functions import extract_days, extract_months, sanitise_date, sanitise_str
from sentiment_algs import *

# Global variables, for ease of use
profile = pd.read_csv("post_collection.csv")
positive_phrases = pd.read_csv("pos_words.csv")
negative_phrases = pd.read_csv("neg_words.csv")
posts = list(profile['post'])


# Method to detect changes in frequency posting
def changes_in_frequency():
    dates = profile['date']
    months = []
    consecutive_days = 0
    gap_days = 0
    res_array = []

    for i in range(len(dates)):
        res_array.append(dates[i].split("-"))

    # Process res_array and break it into days
    days = extract_days(res_array)
    months = extract_months(res_array)

    for i in range(len(days) - 1):
        if days[i] == days[i + 1]:
            consecutive_days += 1
        else:
            gap_days += 1

    if gap_days > consecutive_days:
        print("Change in frequency flagged ")
    else:
        print("No change in frequency flagged")


def get_post_amount_by_day():
    dates = list(profile['date'])
    unique_days = list(dict.fromkeys(dates))
    count_per_day = 0
    freq_list = []
    freq_dict = {}

    for i in range(len(dates)):
        dates[i] = sanitise_date(dates[i])
        posts[i] = sanitise_str(posts[i])

    for i in range(len(unique_days)):
        unique_days[i] = sanitise_date(unique_days[i])

    for i in range(len(dates) - 1):
        if dates[i] != dates[i + 1]:
            count_per_day = dates.count(dates[i])
            freq_list.append(count_per_day)

    # Fix / find a better way of doing this! temporary fix
    posts_at_final_day = dates.count(dates[-1])
    freq_list.append(posts_at_final_day)

    for i in range(len(unique_days)):
        tmp_key = unique_days[i]
        freq_dict[tmp_key] = freq_list[i]

    return freq_dict



# Method to get the mean number of posts per day
def get_mean_posts():
    dict = get_post_amount_by_day()
    mean = statistics.mean(dict.values())
    return math.ceil(mean)


# Method to find days with more posts posted
def find_days_with_more_posts():
    frequency_dict = get_post_amount_by_day()
    dates = list(profile['date'])
    mean = get_mean_posts()
    posts_lst = list(frequency_dict.values())

    # Check to see if for any day the user posted more posts than average
    for i in range(len(frequency_dict)):
        if posts_lst[i] > mean:
            dif = posts_lst[i] - mean
            print("On this day: ", dates[i], "There was: ", dif, "more posts posted than average")


def find_days_with_sharp_increase_in_posts():
    freq_dict = get_post_amount_by_day()
    dates = profile['date']
    avg = get_mean_posts()
    post_lst = list(freq_dict.values())

    for i in range(len(freq_dict)):
        if post_lst[i] >= avg + 3:
            print("Sharp change in posting found, Happened on this date: ", dates[i])
