# Job Scraper

A web scraper built with Scrapy that collects job listings from Real Python's fake jobs site and saves them to MongoDB Atlas.

## Features
- Follows each job's link to collect the full details
- Skips duplicates using the job's link
- Waits between requests to avoid overloading the website
- Keeps the database password out of the code using a .env file

## Built with
- Python
- Scrapy
- MongoDB Atlas (pymongo)

## Setup
Install the libraries: pip install -r requirements.txt

Create a `.env` file in the main folder with your own MongoDB connection link:
MONGO_URI=your-mongodb-link-here

## Run it
```
cd jobs
scrapy crawl job
```

## Notes
Built with help from AI for explanations, debugging and documentation.