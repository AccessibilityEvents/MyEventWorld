import re
from bs4 import BeautifulSoup

# Replace the path with the correct path to your HTML file
newsletter_path = 'C:\\Users\\Oguz\\PycharmProjects\\jugendhacktköln\\Newsletter.html'

try:
    with open(newsletter_path, 'r', encoding='utf-8') as file:
        newsletter_content = file.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(newsletter_content, 'html.parser')

    # Define a pattern to match dates (customize it based on your needs)
    date_pattern = r'\d{1,2}/\d{1,2}/\d{4}'

    # Find all elements containing dates
    date_elements = soup.find_all(text=re.compile(date_pattern))

    # Extract and print the dates
    for date in date_elements:
        print(date.strip())

except FileNotFoundError:
    print(f"The file '{newsletter_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
