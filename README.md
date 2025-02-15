# Explore US Bikeshare Data

![](images/divvy.JPG)
<img src="images/divvy.jpg" width="1000">

## About the Project
In this project, we make use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. 
Using the shell we created an interactive experience that helps users provide raw input in the terminal and answers interesting questions about the data by computing descriptive statistics.
We also compared the bike share system usage between three large cities: Chicago, New York City, and Washington, DC.

## Project Details
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price.
Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. 
These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

## The Datasets 
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

* Gender
* Birth Year

![](images/nyc-data.PNG)
<img src="images/nyc-data.png" width="1000">
***Data for the first 10 rides in the new_york_city.csv file***

## Statistics Computed
You will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, you'll write code to provide the following information:

#### 1. Popular times of travel (i.e., occurs most often in the start time)

* most common month
* most common day of week
* most common hour of day

#### 2. Popular stations and trip

* most common start station
* most common end station
* most common trip from start to end (i.e., most frequent combination of start station and end station)

#### 3. Trip duration

* total travel time
* average travel time

#### 4. User info

* counts of each user type
* counts of each gender (only available for NYC and Chicago)
* earliest, most recent, most common year of birth (only available for NYC and Chicago)

## Files used
The required files for the project are provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns.

* washington.csv
* new_york_city.csv
* chicago.csv

## Software Requirements
This project uses Python (version 3.7.1) and the following libraries:

* pandas==0.23.4
* numpy==1.15.4
* Text editor, like VS Code, Sublime or Atom.
* A terminal application (Terminal on Mac and Linux or Cygwin on Windows)

## Credits
[Programming for Data Science with Python](https://www.udacity.com/course/programming-for-data-science-nanodegree--nd104)
#### ***This project is a graduation requirement for Udacity's Programming for Data Science with Python Nanodegree Bootcamp.***

