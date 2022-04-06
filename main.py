# Import necessary packages, and methods from the utility functions file

from frequency_algs import *
from sentiment_algs import *

# Global variables, for ease of use
profile = pd.read_csv("post_collection.csv")
positive_phrases = pd.read_csv("pos_words.csv")
negative_phrases = pd.read_csv("neg_words.csv")
posts = list(profile['post'])


# Capture the sentiment and frequency data for the entire profile
def capture_profile_and_analyse():
    # Perform the entire range of sentiment analysis for the profile
    # Capture the sentiment for each day a post was posted
    sentiment_for_profile = capture_sentiment_days()
    print(sentiment_for_profile)

    # Capture the overall sentiment of a profile
    sentiment_profile = capture_sentiment_profile()
    print("Overall sentiment for the profile is: ", sentiment_profile)

    # Capture changes in the sentiment of the profile and when they occurred
    changes_in_sentiment = capture_changes_in_sentiment()
    print("Changes in sentiment: ")
    print(changes_in_sentiment)

    # Capture sharp changes in the sentiment of a profile
    sharp_changes = find_sharp_changes()
    print("Are there any sharp changes in the profile: ")
    print(sharp_changes)

    # Capture changes in frequency of posting
    frequency_changes = changes_in_frequency()
    print(frequency_changes)

    # Capture consecutive days were the sentiment was negative
    neg_days = look_for_consec_neg_days()
    print("How many consecutive negative days are there: ")
    print(neg_days)

    # Find the amount of posts per day
    days_and_posts = get_post_amount_by_day()
    print("Days and the amount of posts posted on them: ", days_and_posts)

    # Find any days with sharp increases in the amount of posts posted
    sharp_increase = find_days_with_sharp_increase_in_posts()
    print("Are there any days with sharp increases in posts: ")
    print(sharp_increase)

    # Find any days with more posts than the average posted
    days_more_posts = find_days_with_more_posts()
    print("Days with more posts than average: ")
    print(days_more_posts)

    return sentiment_for_profile, days_and_posts


def print_profile_summary():
    # Perform the entire range of sentiment analysis for the profile
    # Capture the sentiment for each day a post was posted
    sentiment_for_profile = capture_sentiment_days()
    print(sentiment_for_profile)

    # Capture the overall sentiment of a profile
    sentiment_profile = capture_sentiment_profile()
    print("Overall sentiment for the profile is: ", sentiment_profile)

    # Capture changes in the sentiment of the profile and when they occurred
    changes_in_sentiment = capture_changes_in_sentiment()
    print("Changes in sentiment: ")
    print(changes_in_sentiment)

    # Capture sharp changes in the sentiment of a profile
    sharp_changes = find_sharp_changes()
    print("Are there any sharp changes in the profile: ")
    print(sharp_changes)

    # Capture changes in frequency of posting
    frequency_changes = changes_in_frequency()
    print(frequency_changes)

    # Capture consecutive days were the sentiment was negative
    neg_days = look_for_consec_neg_days()
    print("How many consecutive negative days are there: ")
    print(neg_days)

    # Find the amount of posts per day
    days_and_posts = get_post_amount_by_day()
    print("Days and the amount of posts posted on them: ", days_and_posts)

    # Find any days with sharp increases in the amount of posts posted
    sharp_increase = find_days_with_sharp_increase_in_posts()
    print("Are there any days with sharp increases in posts: ")
    print(sharp_increase)

    # Find any days with more posts than the average posted
    days_more_posts = find_days_with_more_posts()
    print("Days with more posts than average: ")
    print(days_more_posts)


def return_profile_data():
    # Perform the entire range of sentiment analysis for the profile
    # Capture the sentiment for each day a post was posted
    sentiment_for_profile = capture_sentiment_days()

    # Capture the overall sentiment of a profile
    sentiment_profile = capture_sentiment_profile()

    # Capture changes in the sentiment of the profile and when they occurred
    changes_in_sentiment = capture_changes_in_sentiment()

    # Capture sharp changes in the sentiment of a profile
    sharp_changes = find_sharp_changes()

    # Capture changes in frequency of posting

    # Capture consecutive days were the sentiment was negative
    neg_days = look_for_consec_neg_days()

    # Find the amount of posts per day
    days_and_posts = get_post_amount_by_day()

    # Find any days with sharp increases in the amount of posts posted
    sharp_increase = find_days_with_sharp_increase_in_posts()

    # Find any days with more posts than the average posted
    days_more_posts = find_days_with_more_posts()

    return sentiment_for_profile, days_and_posts, sentiment_profile, changes_in_sentiment, sharp_changes, neg_days, \
           sharp_increase, days_more_posts
