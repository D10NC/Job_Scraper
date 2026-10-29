"""

Settings file for the job scraping project.

"""

# Imports libraries
import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

BOT_NAME = "jobs" # Name of the project

SPIDER_MODULES = ["jobs.spiders"] # List of spider modules
NEWSPIDER_MODULE = "jobs.spiders" # Module containing spider classes

ADDONS = {} # Dictionary of addons

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Visits one page at a time and waits 1 second between requests to avoid being blocked by the website
CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 1

# Sends scraped data to MongoDB
ITEM_PIPELINES = {
    "jobs.pipelines.JobsPipeline": 300,
}

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"

MONGO_URI = os.getenv("MONGO_URI") # MongoDB connection URI
MONGO_DATABASE = "jobs_db" # MongoDB database name
