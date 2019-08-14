import requests
import logging

from time import sleep
from bs4 import BeautifulSoup
from typing import Union, List, Generator

logging.basicConfig(filename='scraper.log',
                    filemode='w',
                    level=logging.INFO,
                    format='%(funcName)s - %(message)s')


def fetch(url: str, session: requests.Session) -> BeautifulSoup:
    '''
    Fetches HTML from website, converts response to BeautifulSoup object.

    Arguments:
        - url: A URL (str)
        - session: A requests Session instance
    '''
    with session.get(url) as response:
        return BeautifulSoup(response.content, 'html.parser')


def fetch_all(urls: List[str], seconds: int = 5) -> Generator[BeautifulSoup, None, None]:
    '''
    Creates BeautifulSoup objects from a GET responses of given URLs.

    Arguments:
        - urls: A list of URLs (List[str])
        - seconds: Number of seconds to wait between requests (int, default=5)
    '''
    with requests.Session() as session:
        for url in urls:
            try:
                yield fetch(url, session)
                sleep(seconds)
            except Exception as e:
                logging.exception(f'''
    Exception: {e.__class__.__name___}
    Message: {e}
    URL: {url}
    ''')
                continue


def save(filename, mode, data):
    with open(filename, mode=mode) as f:
        for line in data:
            f.write(line + '\n')
