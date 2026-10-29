"""

This file saves the scraped job postings to a MongoDB database.

"""

# Imports necessary libraries
import pymongo
from itemadapter import ItemAdapter

# This class takes each job posting and saves it to a MongoDB database
class JobsPipeline:
    COLLECTION_NAME = "jobs" # This is the name of the collection in the MongoDB database where the job postings will be saved

    def __init__(self, mongo_uri, mongo_db): # Initialises the pipeline with the MongoDB connection details
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler): # Returns an instance of the pipeline with the MongoDB connection details which it gets from settings.py
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DATABASE"),
        )

    def open_spider(self, spider): # Initialises the connection to the MongoDB database
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider): # Closes the connection to the MongoDB database
        self.client.close()

    def process_item(self, item, spider): # Takes each job posting and saves it to a MongoDB database
        job = ItemAdapter(item).asdict()
        # Use the link to spot duplicates; update if it exists and add if it's new
        self.db[self.COLLECTION_NAME].update_one(
            {"link": job["link"]},
            {"$set": job},
            upsert=True
        )
        return item # Returns the item after it has been saved to the MongoDB database

