import re
from bs4 import BeautifulSoup


newsletter_path = 'C:\\Users\\Oguz\\PycharmProjects\\jugendhacktköln\\Newsletter.html'

try:
    with open(newsletter_path, 'r', encoding='utf-8') as file:
        newsletter_content = file.read()

    soup = BeautifulSoup(newsletter_content, 'html.parser')

    date_pattern = r'\d{1,2}/\d{1,2}/\d{4}'

    date_elements = soup.find_all(string=re.compile(date_pattern))


    for date in date_elements:
        print(date.strip())

except FileNotFoundError:
    print(f"The file '{newsletter_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

