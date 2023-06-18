import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# Send a GET request to the problem page
url = 'https://leetcode.com/problems/minimum-distance-between-bst-nodes/'
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the level element
level_element = soup.find('div', class_='difficulty-label')
level = level_element.text.strip() if level_element else ''

# Find the question element
question_element = soup.find('div', class_='question-content__JfgR')
question = question_element.text.strip() if question_element else ''

# Find the test case element
testcase_element = soup.find('div', class_='question-test-cases__2kHM')
testcase = testcase_element.text.strip() if testcase_element else ''

# Create a new Excel workbook and select the active sheet
workbook = Workbook()
sheet = workbook.active

# Write headers to the Excel sheet
sheet['A1'] = 'Level'
sheet['B1'] = 'Question'
sheet['C1'] = 'Test Case'

# Write data to the Excel sheet
sheet['A2'] = level
sheet['B2'] = question
sheet['C2'] = testcase

# Save the Excel workbook
workbook.save('leetcode_data.xlsx')
