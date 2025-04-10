from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

# Sending a request to fetch the webpage content
page = requests.get(url)

# Parsing the page content using BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')

# Finding the correct table by class
table = soup.find('table', class_='wikitable sortable')  # Find the first table with class 'wikitable sortable'

# Extracting the headers of the table
headers = table.find_all('th')

# Extracting the header text and cleaning up
column_titles = [header.text.strip() for header in headers]

# Now, let's extract the data rows
rows = table.find_all('tr')[1:]  # Skip the header row

# Initialize an empty list to store row data
data = []

# Looping through each row and extracting data
for row in rows:
    columns = row.find_all('td')
    column_data = [col.text.strip() for col in columns]  # Clean up the text
    if column_data:  # Avoid adding empty rows
        data.append(column_data)

# Creating a DataFrame using the extracted data
df = pd.DataFrame(data, columns=column_titles)

df.to_csv('largest_companies_by_revenue.csv', index=False)

print("Data saved too'largest_companies_by_revenue.csv'")




