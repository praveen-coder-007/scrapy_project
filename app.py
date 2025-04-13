from flask import Flask, render_template_string, request
import requests
from bs4 import BeautifulSoup
import pandas as pd

app = Flask(__name__)

# Function to scrape data from the URL
def scrape_data(url):
    # Sending a request to fetch the webpage content
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find the first table with class 'wikitable sortable' (can be modified for other pages)
    table = soup.find('table', class_='wikitable sortable')

    headers = table.find_all('th')
    column_titles = [header.text.strip() for header in headers]

    rows = table.find_all('tr')[1:]  # Skip the header row

    data = []
    for row in rows:
        columns = row.find_all('td')
        column_data = [col.text.strip() for col in columns]
        if column_data:
            data.append(column_data)

    # Convert the scraped data into a DataFrame and return as HTML
    df = pd.DataFrame(data, columns=column_titles)
    return df.to_html(classes='table table-striped', index=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        url = request.form['url']
        result = scrape_data(url)  # Call the scrape_data function to get the result

    # HTML template (we use render_template_string because we don't have separate files)
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Web Scraper</title>
    </head>
    <body>
        <h1>Web Scraper</h1>
        <form method="POST">
            <label for="url">Enter Wikipedia URL:</label>
            <input type="text" name="url" id="url" placeholder="Enter URL" required>
            <button type="submit">Scrape</button>
        </form>

        {% if result %}
            <h2>Scraped Data:</h2>
            <div>{{ result|safe }}</div>
        {% endif %}
    </body>
    </html>
    """

    return render_template_string(html_template, result=result)

if __name__ == '__main__':
    app.run(debug=True)
