from dataclasses import dataclass
import argparse
import logging
import json
import requests

from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)

@dataclass
class Link:
    name: str
    link: str

    def __hash__(self):
        return hash(self.link)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.link == other.link
        return False


class WikiParser:
    DEFAULT_NAME = "Erdős number"
    DEFAULT_LINK = "https://en.wikipedia.org/wiki/Erdős number"
    def __init__(self, base_name: str):
        self.MAX_LINKS_COUNT = 1000
        self.MAX_LINKS_FROM_PAGE = 20
        self.depth = 3
        self.base_name = base_name
        self.json_content = self.parse()

    def parse(self):
        current_depth = 1
        links_count = 0
        while current_depth < self.depth and links_count < self.MAX_LINKS_COUNT:

        return {}




def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--page", type=str, default="Erdős_number",
                        help="Name of the Wikipedia article to start from")
    parser.add_argument("-d", "--depth", type=int, default=3, help="Depth of search")
    args = parser.parse_args()
    return args


def load_viki_page(page_name):
    base_url = 'https://en.wikipedia.org/wiki/'
    full_url = base_url + page_name
    print(full_url)
    response = requests.get(full_url)
    if response.status_code == 200:
        return response.text
    else:
        logging.error(f"Failed to load Wikipedia page: {response.status_code}")
        return None


if __name__ == "__main__":
    test = {
        Link("a", "b"): {},
        Link("c", "b"): {},
        Link("a", "c"): {}
    }
    print(test)