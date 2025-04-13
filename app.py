from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Scraping function
def scrape_wikipedia():
    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_population'
    response = requests.get(url)

    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})

    if not table:
        return None

    countries_data = []
    rows = table.find_all('tr')

    for row in rows:
        columns = row.find_all('td')
        if len(columns) > 1:
            rank = columns[0].text.strip()
            country = columns[1].text.strip()
            population = columns[2].text.strip()
            countries_data.append({'rank': rank, 'country': country, 'population': population})

    return countries_data

@app.route('/')
def index():
    countries_data = scrape_wikipedia()
    if not countries_data:
        return "Failed to scrape data from Wikipedia.", 500
    return render_template('index.html', countries=countries_data)

@app.route('/api/countries')
def api_countries():
    countries_data = scrape_wikipedia()
    if not countries_data:
        return jsonify({'error': 'Failed to scrape data from Wikipedia.'}), 500
    return jsonify(countries_data)

if __name__ == '__main__':
    app.run(debug=True)



