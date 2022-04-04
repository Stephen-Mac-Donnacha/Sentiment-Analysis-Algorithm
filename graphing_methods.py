import matplotlib as mpl
import matplotlib.pyplot as plt
from main import capture_profile_and_analyse

array = capture_profile_and_analyse()
prof_data = []
for res in range(len(array)):
    prof_data.append(capture_profile_and_analyse()[res])


# Method to create a barchart for the sentiment data
def create_barchart_for_sentiment():
    sentiment_data = prof_data[0]
    total_pos = 0
    total_neg = 0
    total_neut = 0

    for date in sentiment_data:
        if sentiment_data.get(date) == 'positive':
            total_pos += 1
        elif sentiment_data.get(date) == "negative":
            total_neg += 1
        else:
            total_neut += 1

    data = {"Positive": total_pos, "Negative": total_neg, "Neutral": total_neut}
    sentiments = list(data.keys())
    days = list(data.values())

    # Create the figure
    fig = plt.figure(figsize=(5, 5))

    # Creating the bar plot
    plt.bar(sentiments, days, color="red", width=0.4)

    # Set label for the x and y axis
    plt.xlabel("Sentiments")
    plt.ylabel("Number of days with that sentiment")
    plt.title("Graph of number of days for each sentiment")
    plt.show()


# Method to create a barchart for the frequency data
def create_barchart_for_frequency():
    frequency_data = prof_data[1]

    dates = list(frequency_data.keys())
    tweet_counts = list(frequency_data.values())

    fig = plt.figure(figsize=(15, 5))
    plt.bar(dates, tweet_counts, color="red", width=0.4)
    plt.xlabel("Number of tweets posted")
    plt.ylabel("Dates")
    plt.title("Graph of dates with the number of tweets posted on them")
    plt.show()


# Method to create a pie chart for the sentiment data
def create_piechart_for_sentiment():
    var = prof_data[0]
    total_pos = 0
    total_neg = 0
    total_neut = 0

    for date in var:
        if var.get(date) == 'positive':
            total_pos += 1
        elif var.get(date) == "negative":
            total_neg += 1
        else:
            total_neut += 1

    data = {"Positive": total_pos, "Negative": total_neg, "Neutral": total_pos}
    labels = list(data.keys())
    count = list(data.values())
    colors = ['green', 'red', 'gray']

    plt.pie(count, labels=labels, colors=colors)
    plt.show()


if __name__ == "__main__":
    create_barchart_for_sentiment()
    create_barchart_for_frequency()
    create_piechart_for_sentiment()
