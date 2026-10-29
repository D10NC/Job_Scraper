"""

This is a spider for scraping job listings from the website realpython.github.io/fake-jobs/.

"""

# Importing library
import scrapy

# This class creates a spider for scraping job listings from the website
class JobSpider(scrapy.Spider):
    name = "job" # This is the name of the spider
    allowed_domains = ["realpython.github.io"] # This is the domain of the website we are scraping
    start_urls = ["https://realpython.github.io/fake-jobs/"] # This is the URL of the website we are scraping

    # This function is called for each response returned from the start_urls
    def parse(self, response):
        for job in response.css("div.card-content"): # each div.card-content is a job posting on the list page
            apply_link = job.css("a.card-footer-item::attr(href)").getall()[1] # Each job has a Learn and an Apply link, [1] picks the Apply link
            yield response.follow(apply_link, callback=self.parse_job) # Goes to apply page and reads what's on it, because the job description is there

    # This function is called for each response returned from the apply links
    def parse_job(self, response):
        yield { # Builds a dictionary with the job details and sends it to the pipeline which is then saved to MongoDB
                "title": response.css("h1.is-2::text").get(), # using is-2 to make sure we get the job title and not the website name
                "company": response.css("h2.company::text").get(),
                "location": response.css("p#location::text").get(),
                "description": response.css("div.content > p::text").get(),
                "date": response.css("p#date::text").get().strip(),
                "link": response.url, # This is the URL of the job posting
            }
