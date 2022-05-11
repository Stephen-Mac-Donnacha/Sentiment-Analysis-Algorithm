from sentiment_algs import *
from frequency_algs import *
from main import print_profile_summary
from write_data_into_excel import *
from graphing_methods import *


def get_user_option():
    print("*******************************")
    print("Sentiment Analysis algorithm v1.0")
    print("1: Entire profile data, sentiment and frequency")
    print("2: Only data related to sentiment")
    print("3: Only data related to frequency")
    print("4: Exit program and Cancel")
    user_choice = int(input("Choose an option corresponding to what data you wish to see: "))
    return user_choice


def print_user_option(user_choice):
    if user_choice == 1:
        print_profile_summary()
    elif user_choice == 2:
        summarise_sentiment_data()
    else:
        summarise_frequency_data()


def explore_further_options():
    excel_letter = input("Would you like to output the data to excel [Y/N]: ")
    if excel_letter == "Y":
        print("Enter S for sentiment or F for Frequency or B for Both: ")
        which_data = input("Would you like to write the sentiment or frequency data to excel? ")
        if which_data == 'S':
            write_sentiment_data_to_excel()
        elif which_data == 'F':
            write_frequency_data_to_excel()
        elif which_data == 'B':
            write_sentiment_data_to_excel()
            write_frequency_data_to_excel()
        else:
            print("Invalid option entered")
    else:
        print("Not outputting data to excel")

    graph_data = input("Would you like to generate graphs for the data [Y/N]: ")
    if graph_data == "Y":
        print("Enter S for sentiment or F for Frequency or B for Both: ")
        which_data_2 = input("Would you like to Generate graphs for sentiment or frequency data: ")
        if which_data_2 == "S":
            create_barchart_for_sentiment()
            create_piechart_for_sentiment()
        elif which_data_2 == "F":
            create_barchart_for_frequency()
        elif which_data_2 == "B":
            create_barchart_for_sentiment()
            create_barchart_for_frequency()
            create_piechart_for_sentiment()


def automate():
    while True:
        option = input("Press Q at anytime to quit or C to continue: ")
        if option == 'Q':
            break
        else:
            u_choice = get_user_option()
            print_user_option(u_choice)
            explore_further_options()


if __name__ == "__main__":
    automate()
