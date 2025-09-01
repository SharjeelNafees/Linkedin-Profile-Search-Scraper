# LinkedIn Profile Search Scraper

This project automates the process of searching for LinkedIn profiles using DuckDuckGo and saves the top results to an Excel file.

## Features

- Automated search for LinkedIn profiles based on a custom query
- Collects top search results (title and link)
- Exports results to `linkedin_search_results.xlsx`

## Requirements

- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- See `requirements.txt` for Python dependencies

## Installation

1. Clone this repository.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Download and set up [ChromeDriver](https://chromedriver.chromium.org/downloads).

## Usage

Run the automation script:

```sh
python automation.py
```

The results will be saved in `linkedin_search_results.xlsx`.

## Notes

- This script uses headless Chrome via Selenium.
- Make sure ChromeDriver is in your PATH or in the project