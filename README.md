# CarDealerDataScraperAnalyzer


## Introduction
CarDealerDataScraper is a project that combines web scraping, socket programming, Pyxcel, and data analysis using pandas. It enables users to gather car information from a car dealership website, process the data on a server using Pyxcel, and retrieve the results in tabulated format for further analysis.

## Project Description
**Procedure**:
1. Web Scraping: The project starts with web scraping, where car information is extracted from a large car dealership website. This includes details such as make, model, price, mileage, and more.

2. Socket Programming: The extracted data is sent from a client to a server using socket programming. The server is responsible for processing the data.

3. Pyxcel Integration: On the server side, Pyxcel (a previously implemented project available as a separate github repository) is utilized to work with the received car data. Pyxcel's capabilities allow for various data transformations and calculations.

4. CSV Output: After processing, the data is converted into a tabulated format and saved as a .csv file.

Data Analysis: The client retrieves the .csv file. The retrieved data is then separately analyzed using Pandas. This includes extracting interesting facts and answering questions about the dataset.

## Dependencies
+ Python (3.x)
+ BeautifulSoup for web scraping
+ Pyxcel for data processing
+ Pandas for data analysis

## Acknowledgments
I want to acknowledge the late and dear prof. Abbas Nowzari-Dalini, who sadly passed away about a year after the completion of this project. He was our instructor for the Introduction to Programming and Computer Science course, which this project was completed for. He was a great professor and instructor and an even greater man. May he rest in peace.

