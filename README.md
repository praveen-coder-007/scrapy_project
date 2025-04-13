# scrapy_project🧠 Wikipedia Table Scraper with Flask + BeautifulSoup
Hey! 👋 This is a small project I built to practice web scraping and working with Flask. It takes a Wikipedia URL (that contains a table) and extracts the data using BeautifulSoup. The scraped data is then shown in a nice, clean HTML table using Flask on the frontend.

🚀 What It Does
Accepts any valid Wikipedia URL from the user

Scrapes the first table it finds on the page

Displays that data on a simple webpage

All built with Python, Flask, and BeautifulSoup

🔧 How to Run
Clone this repo and get started:

bash
Copy
Edit
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
Set up your virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install the required libraries:

bash
Copy
Edit
pip install -r requirements.txt
Now run the Flask app:

bash
Copy
Edit
python app.py
Then go to http://127.0.0.1:5000/ in your browser.

🌐 Example URLs to Try
Here are a few Wikipedia pages that work well with this:

https://en.wikipedia.org/wiki/List_of_countries_by_population

https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue

💡 Why I Made This
I wanted to learn how to:

Work with real-world HTML data using BeautifulSoup

Use Flask to create a web interface for user input

Connect user input to dynamic web scraping

It’s a basic project, but I learned a lot building it!
