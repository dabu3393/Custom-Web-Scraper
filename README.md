<div align="center">
  <br>
  <h1>Custom Web Scraper</h1>
  <strong>A custom web scraper to collect data on things that you are interested in.</strong>
</div>
<br>
<p align="center">
  <a target="_blank" href="www.linkedin.com/in/davis-burrill-512071256">
    <img height="20" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a target="_blank" href="#">
    <img height="20" src="https://forthebadge.com/images/badges/made-with-python.svg" />
  </a>
  <a target="_blank" href="mailto:davisburrill@icloud.com">
    <img height="20" src="https://img.shields.io/badge/Email-0077B5?style=for-the-badge&logo=minutemailer&logoColor=white&color=green" />
  </a>
</p>


https://github.com/dabu3393/Custom-Web-Scraper/assets/97137252/8cdc4369-2c48-4d7c-b111-55ccb1fb390c




## Getting Started

The Web Scraper is a Python application built with the help of the requests, BeautifulSoup, and pandas libraries, allowing you to extract and save data from websites. It provides flexibility in data extraction by allowing you to choose between extracting data via a CSS selector or directly from the HTML content.

## Key Features

- **Data Extraction**: Extract data from a web page using a CSS selector or by specifying HTML tags, classes, and IDs.

- **Output Formats**: Save extracted data as JSON or CSV files.

- **User-Friendly Interface**: Simple and intuitive GUI for entering the URL and data extraction options.

- **Custom CSS Selector**: If you're familiar with CSS selectors, you can use them to precisely target the data you need.

## Usage

1. Run the web_scraper.py script to launch the Web Scraper application.

2. Enter the URL of the web page you want to scrape in the "Enter URL" field.

3. Choose the data extraction method:
   - HTML Content: Extract data based on HTML tags, classes, and IDs.
   - CSS Selector: Use a CSS selector to specify the elements to extract.
4. Depending on your chosen method, you can enter the following:
   - Tag: The HTML tag (e.g., div, p) for HTML Content extraction.
   - ID: The ID attribute for HTML Content extraction.
   - Class: The class attribute for HTML Content extraction.
   - CSS Selector: A CSS selector for CSS Selector extraction.
5. Select the output format for saving the data:
   - JSON: Save the extracted data as a JSON file.
   - CSV: Save the extracted data as a CSV file.
6. Click the "Scrape Data" button to start the data extraction process.
7. Choose a location to save the extracted data in the selected format.
8. Once the data is successfully saved, a success message will be displayed.



## Required Downloads
I have included a requirements.txt, which you should download in your virtual environment.

[Requirements](https://github.com/dabu3393/Custom-Web-Scraper/blob/main/requirements.txt)
