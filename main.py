# Import necessary packages, and methods from the utility functions file
import math
import statistics

import pandas as pd
from utility_functions import extract_days, extract_months, sanitise_date, sanitise_str

# Global variables, for ease of use
profile = pd.read_csv("post_collection.csv")
positive_phrases = pd.read_csv("pos_words.csv")
negative_phrases = pd.read_csv("neg_words.csv")
posts = list(profile['post'])

# Method to capture the sentiment of a post
def analyse_post(post_str):
    pos_sent = 0
    neg_sent = 0
    overall_sent = ""
    pos_phrases = list(positive_phrases['phrase'])
    neg_phrases = list(negative_phrases['phrase'])
    pos_strength = list(positive_phrases['strength'])
    neg_strength = list(negative_phrases['strength'])
    final_sent = 0

    for i in range(len(pos_phrases)):
        pos_phrases[i] = sanitise_str(pos_phrases[i])

    for i in range(len(neg_phrases)):
        neg_phrases[i] = sanitise_str(neg_phrases[i])

    post_str = post_str.lower()

    for word in post_str.split(" "):
        if word in pos_phrases:
            index = pos_phrases.index(word)
            pos_sent += pos_strength[index]
        elif word in neg_phrases:
            index = neg_phrases.index(word)
            neg_sent += neg_strength[index]
        else:
            pass

    # Get the average sentiment of a post, by taking the strength of the negative sentiment
    # away from the strength of the positive sentiment
    final_sent = pos_sent - neg_sent

    if final_sent > 0:
        overall_sent = "positive"
    elif final_sent < 0:
        overall_sent = "negative"
    else:
        overall_sent = "neutral"

    # Return the overall sentiment for a post as well as the score of that post
    if overall_sent == "positive":
        return overall_sent, pos_sent
    elif overall_sent == "negative":
        return overall_sent, neg_sent
    else:
        return overall_sent, 0, final_sent


# Method to capture the sentiment for an overall day
def capture_sentiment_days():
    dates = list(profile['date'])
    sent_post_array = []
    sent_strength_array = []
    days_post_sent = {}

    for i in range(len(dates)):
        dates[i] = sanitise_date(dates[i])

    # Iterate over the posts, getting the sentiment for the post and the strength of the sentiment
    for i in range(len(posts)):
        res = analyse_post(posts[i])
        sent_post_array.append(res[0])
        sent_strength_array.append(res[1])

    for i in range(len(dates)):
        tmp_key = dates[i]
        days_post_sent[tmp_key] = sent_post_array[i]

    return days_post_sent


# Method to capture the sentiment of a profile, currently a collection of mock posts
def capture_sentiment_profile():
    sent_with_dates = capture_sentiment_days()
    dates = list(profile['date'])
    pos_count = 0
    neg_count = 0
    profile_sentiment = ""

    # Sanitise the dates in the list
    for i in range(len(dates)):
        dates[i] = sanitise_date(dates[i])

    for i in range(0, len(sent_with_dates)):
        if sent_with_dates[dates[i]] == "positive":
            pos_count += 1
        elif sent_with_dates[dates[i]] == "negative":
            neg_count += 1
        else:
            pass

    if pos_count > neg_count:
        profile_sentiment = "positive"
    else:
        profile_sentiment = "negative"

    return profile_sentiment


# Method to capture changes in sentiment
def capture_changes_in_sentiment():
    overall_sentiment = capture_sentiment_profile()
    days_post_sent = capture_sentiment_days()
    sent_list = list(days_post_sent.values())
    date_list = profile['date']
    date_list = list(dict.fromkeys(date_list))

    # Sanitise dates
    for i in range(len(date_list)):
        date_list[i] = sanitise_date(date_list[i])

    for i in range(len(sent_list) - 1):
        if sent_list[i] != sent_list[i + 1]:
            print("Sentiment Changed from:", sent_list[i], "to:", sent_list[i + 1], "on: ", date_list[i + 1])


# Method to look for consecutive negative days
def look_for_consec_neg_days():
    days_post_sent = capture_sentiment_days()
    list_sent = list(days_post_sent.values())
    dates_list = list(profile['date'])
    dates_list = list(dict.fromkeys(dates_list))
    neg_days_counter = 0
    neg_days_array = []
    longest_consec_neg_days = []

    # Sanitise dates:
    for i in range(len(dates_list)):
        dates_list[i] = sanitise_date(dates_list[i])

    # Get total number of negative days
    for i in range(len(list_sent)):
        if list_sent[i] == "negative":
            neg_days_counter += 1
            neg_days_array.append(dates_list[i])

    # Break up the list of dates for ease of processing
    splitter_list = []
    for i in neg_days_array:
        splitter_list.append(i.split("-"))
    days = extract_days(splitter_list)

    # Iterate over the days, calculating the distance between them to get longest consecutive negative days
    for i in range(0, len(days) - 1, 2):
        greatest_difference = 0
        difference = int(days[i + 1]) - int(days[i])

        if difference > greatest_difference:
            greatest_difference = difference

    print("Total Negative Days: ", neg_days_counter)
    print("Longest consecutive days with negative sentiment : ", greatest_difference)


# Method to look for sharp changes in sentiment
def find_sharp_changes():
    sentiment_name = []
    dates = profile['date']
    difference = 0  # The change between a positive and negative sentiment

    post_strengths = []
    for i in range(len(posts)):
        res = analyse_post(posts[i])
        post_strengths.append(res[1])
        sentiment_name.append(res[0])

    for i in range(len(post_strengths) - 1):
        if sentiment_name[i] != sentiment_name[i + 1]:
            difference = post_strengths[i] - post_strengths[i + 1]
            if difference > 0.8:
                print("There was a sharp change in sentiment on: ", dates[i])
                print("Sentiment changed from : ", sentiment_name[i], " to: ", sentiment_name[i + 1])


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


def capture_profile_and_analyse():
    # Perform the entire range of sentiment analysis for the profile
    # Capture the sentiment for each day a post was posted
    sentiment_for_profile = capture_sentiment_days()
    print(sentiment_for_profile)

    # Capture the overall sentiment of a profile
    sentiment_profile = capture_sentiment_profile()
    print("Overall sentiment for the profile is: ", sentiment_profile)

    # Capture changes in the sentiment of the profile and when they occurred
    capture_changes_in_sentiment()

    # Capture sharp changes in the sentiment of a profile
    find_sharp_changes()

    # Capture changes in frequency of posting
    changes_in_frequency()

    # Capture consecutive days were the sentiment was negative
    look_for_consec_neg_days()

    # Find the amount of posts per day
    days_and_posts = get_post_amount_by_day()
    print("Days and the amount of posts posted on them: ", days_and_posts)

    # Find any days with sharp increases in the amount of posts posted
    find_days_with_sharp_increase_in_posts()

    # Find any days with more posts than the average posted
    find_days_with_more_posts()

    return sentiment_for_profile, days_and_posts


def main():
    capture_profile_and_analyse()


if __name__ == "__main__":
    main()
