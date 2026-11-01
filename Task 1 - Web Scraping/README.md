## Task 1: Web Scraping – Quotes Extraction

## Overview
This project was completed as part of my Data Analytics Internship at CodeAlpha.
The objective was to extract quotes and their respective authors from a publicly available website using Python and store the collected information in a structured CSV file for further analysis.

## Technologies Used
* Python
* Requests
* BeautifulSoup
* CSV

## Project Workflow
The script performs the following operations:
1. Sends an HTTP request to the target website.
2. Retrieves and parses the webpage's HTML content.
3. Identifies and extracts quote text and author names.
4. Organises the extracted information.
5. Exports the collected data into a CSV file.

## Installation and Execution
### 1. Install the required libraries
```bash
pip install requests beautifulsoup4
```
### 2. Run the Python script
```bash
python script.py
```
Replace `script.py` with the actual name of your Python file.
### 3. Output
After successful execution, a CSV file named `quotes_dataset.csv` will be generated containing the extracted quotes and author names.

## Website Used
[Quotes to Scrape](https://quotes.toscrape.com/)
This website is specifically designed for practising web scraping techniques.

## Ethical Considerations
The project uses a practice website intended for web scraping exercises. Responsible scraping practices, including checking website permissions and avoiding unnecessary requests, should always be followed.

## Key Learnings
Through this project, I gained practical experience in:
* Understanding HTML structure.
* Sending HTTP requests using Python.
* Parsing HTML content using BeautifulSoup.
* Extracting structured information from webpages.
* Exporting collected data into CSV files.

## Internship
**Organisation:** CodeAlpha
**Domain:** Data Analytics
**Task:** Web Scraping
