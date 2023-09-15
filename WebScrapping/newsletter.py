import re

newsletter_path = r"C:\Users\Oguz\PycharmProjects\MyEventWorld\Newsletter.html"

try:
    with open(newsletter_path, 'r', encoding='utf-8') as file:
        newsletter_content = file.read()


    date_pattern = r'Date:\s*(\d{1,2}/\d{1,2}/\d{4})'
    location_pattern = r'Location:\s*([\w\s]+)'

    dates = re.findall(date_pattern, newsletter_content)
    locations = re.findall(location_pattern, newsletter_content)

    for date, location in zip(dates, locations):
        print(f"Date: {date}, Location: {location}")

except FileNotFoundError:
    print(f"The file '{newsletter_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
