"""

Items.py is used to define the data structure for job postings.

"""


# Imports dataclass from the dataclasses module
from dataclasses import dataclass

# Each job posting item has 6 fields with each one being either a string or None
@dataclass
class JobsItem:

    title: str | None = None
    company: str | None = None
    location: str | None = None
    description: str | None = None
    date: str | None = None
    link: str | None = None
