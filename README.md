# Sentiment-Analysis-Algorithm
------------------------------
Github repo for my final year project

This repository serves as a repository for my final year project, which is based on analysing a mock social media profile for sentiment and frequency data.
This is done with the purpose of possibly one day being developed further into a tool that can be used to offer support to struggling people. 
The README will serve as a guide to the code within the repository 

### Breakdown of code files within the repository
1. _frequency_algs.py_ 
    * This code file contains the algorithms related to gathering / analysing the frequency data related to the profile
2. _sentiment_algs.py_
    * This code file contains the algorithms related to gathering / analysing the sentiment data related to the profile
3. _graphing_methods.py_
    * This file contains a set of methods designed to make graphs that relate to the data gathered from the main algorithms
4. _write_data_into_excel.py_ 
    * A short python script that writes data related to sentiment and frequency into microsoft excel
5. _utility_functions.py_
    * A short collection of utility methods designed to reduce file size in the other code files 
6. _main.py_
    * A python file that anlaysing the profile for both frequency and sentiment data
7._launch_code.py_
    * Presents a menu, giving the user options as too what data they wish to see and then presents further options such as generating graphs 

### Breakdown of non code files within the repository
1. _neg_words.csv_
    * A collection of negative phrases used for the analysis of a post within the context of a project
2. _pos_words.csv_
    * A collection of positive phrases used for the analysis of a post wihtin the context of a project
3. _post_collection.csv_
    * A collection of mock posts, designed to emulate posts that would be found on a social media site 
4. _sharp_increase_posts.csv_
    * Another collection of mock posts, this was designed to test some of the functionality of the frequency analysis
