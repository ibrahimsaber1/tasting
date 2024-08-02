# Web Scraping and Data Analysis with BeautifulSoup and Pandas

This project demonstrates how to scrape data from a Wikipedia page and perform data analysis using the `BeautifulSoup` and `pandas` libraries in Python.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [License](#license)

## Introduction

The goal of this project is to scrape data from the Wikipedia page listing the largest companies in the United States by revenue. The scraped data is then processed and analyzed using the `pandas` library.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `pandas` library

## Usage

1. Clone the repository or download the script.
2. Install the required libraries using `pip`.
3. Run the script using Python.

## Code Explanation

### Import Libraries

The script starts by importing the necessary libraries.

### Fetch Web Page

The URL of the Wikipedia page is defined, and the page is fetched using the `requests` library.

### Parse HTML

The HTML content of the page is parsed using `BeautifulSoup`.

### Extract Data

The script locates the specific table containing the data of interest and extracts the relevant information.

### Create DataFrame

A `pandas` DataFrame is created to store and manipulate the extracted data.

### Save to CSV

The DataFrame is saved to a CSV file for further analysis.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
