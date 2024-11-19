import pandas as pd
from bs4 import BeautifulSoup

# Read the HTML file
with open('data/assignment_1/raw/hello_class.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

# Get the h1 tag content to use in the "name" column and as the CSV file name
h1_tag = soup.find('h1')
name_value = h1_tag.text.strip()
csv_file_name = 'data/assignment_1/altered/' + name_value + '.csv'

# Find the table
table = soup.find('table')

# Extract table headers
headers = [th.text.strip() for th in table.find_all('th')]

# Add the "name" column to the headers
headers.append('Name')

# Extract table rows and add the "name" column value
rows = []
for row in table.find_all('tr')[1:]:  # Skipping the header row
    cols = [td.text.strip() for td in row.find_all('td')]
    cols.append(name_value)  # Add the name column value
    rows.append(cols)

# Create a pandas DataFrame
df = pd.DataFrame(rows, columns=headers)

# Save the DataFrame to a CSV file
df.to_csv(csv_file_name, index=False, encoding='utf-8')

print(f"Data extracted and saved to {csv_file_name}")