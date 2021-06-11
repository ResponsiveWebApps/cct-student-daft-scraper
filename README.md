# cct-student-daft-scraper
> A web scraper for a CTT College student with daft-scraper.

## Introduction
The purpose of this project is to create a web scraper in Python. The web scraper takes certain input from the user in the console and searches Daft.ie for information on rental accommodation. The single Python file can be run through a terminal console and the results are printed in both the console and a CSV file. 

The project was built for a CCT College student in mind, who is looking for accommodation near to the college. And needs the cheapest rental possible.

The following report will explain the structure and design of the code; and also an analysis of the algorithms used, as well as Big-O notation.  

## Code Structure
The web scraper consists of one Python file and produces one CSV file. The main two modules imported are daft_scraper and csv. The daft_scraper module was created by a developer called Evan Smith. It is the primary tool used to search Daft.ie with options and pulls search results into our app. The CSV module exports the data into a convenient CSV file which can be easily read by either another Python app or a data exploration program like Excel. 

After the module imports, the main bulk of the code is three Python methods that are called simultaneously in one line.

> writeCSV(printResults(getInputs()))

The app takes inputs from the user via the terminal console, then uses those inputs to search for listings on Daft,ie. With the second algorithm,  the search results are sorted by price. As results are printed in the terminal, a second list is created called ‘rows’. The ‘rows’ of data is sent through the third algorithm to be formatted as a CSV file. 

The end result is a CSV file of listings with their id number, price, address and URL link to details on Daft.ie.  

## Design Decisions
The app was designed with a low income CTT College student in mind. The priority for a student is low rent. Students typically aim for the lowest rent possible, which is why it is the only listing attribute that is being sorted in the second algorithm. 

The first algorithm takes four inputs from the user. These inputs change the option settings for search and thus do most of the filtering for the student. With these four main attributes in mind, the student has results according to their taste. 

As previously said, the most important attribute to a student is the rental price, thus maximum price option is the first input. It is assumed that the student wants the lowest price possible, hence there is no minimum price. 

Ideally the student wishes to be close to CCT College, which is in Dublin 2. However, most students are not able to afford the rent prices in Dublin 2. This is why there is an option to search in either Dublin 2 or Dublin City Centre as a whole. 

The last two inputs are whether or not the listing is a house or an apartment, and how many bedrooms are needed. This gives the student an option to rent a house with some friends.

First the results are printed with the id number, price and address, then with the URL link below. The third algorithm writes a CSV file which can be read by a number of free applications. The user can either click on the links provided, or read the data somewhere else. 


## Conclusion
The app ‘daft.py’ is a straight forward script to run. It was created with a low-income student in mind, who is mostly interested in the lowest rental price possible and secondly interested in an accommodation near CCT College or in Dublin City Centre. 

The output is the most essential details needed and a link to the Daft.ie listing for further a look. A combination of constant and linear time complexity was used so the app will not crash most average laptops or even smart phones. 

## References
Evan Smith (2021) daft-scraper 1.3.0. Available at: 
https://pypi.org/project/daft-scraper/ 
(Accessed: 10 June 2021)

The Irish Times (2018) Over a third of students in Ireland face ‘severe financial problems'. Available at: https://www.irishtimes.com/news/education/over-a-third-of-students-in-ireland-face-severe-financial-problems-1.3363190
(Accessed: 11 June 2021)
