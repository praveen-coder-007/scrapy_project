# scrapy_project
WEB_SCRAPPING_PROJECT

# Web Scraping Project

This project demonstrates how to scrape data from a webpage using Python and libraries like **BeautifulSoup** and **requests**. The script extracts specific information from the **List of largest companies in the United States by revenue** on Wikipedia.

## Description

In this project, a Python script is written to scrape the table of largest companies from the Wikipedia page:

[https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue](https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue)

The script extracts the table data (company names, revenue, and other related details) and stores it in a structured format like a **CSV** file for further analysis.

## Features

- Scrapes the table of largest companies in the U.S. by revenue.
- Stores the extracted data in a CSV file.
- Uses **BeautifulSoup** to parse the HTML content.
- Uses **requests** to fetch the webpage.

## Requirements

Before running the project, make sure to install the required libraries:

```bash
pip install -r requirements.txt
The required libraries include:

beautifulsoup4

requests

pandas

Setup
Clone the repository:

bash
Copy
Edit
git clone https://github.com/praveen-coder-007/scrapy_project.git
cd scrapy_project
(Optional) Set up a virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Usage
To run the web scraping script:

Ensure you are in the project directory.

Run the script:

bash
Copy
Edit
python main.py
The script will scrape the data and save it in a CSV file called companies.csv.

The CSV file will contain information such as:

Company Name

Revenue

Other relevant details

File Structure
bash
Copy
Edit
scrapy_project/
├── main.py                # Python script that does the scraping
├── requirements.txt       # List of required Python packages
└── companies.csv          # Output CSV file with scraped data
Example Output (companies.csv)
Rank	Company Name	Revenue (in billion USD)	Country
1	Walmart	523.96	United States
2	Amazon	469.81	United States
3	State Grid Corporation of China	460.60	China
