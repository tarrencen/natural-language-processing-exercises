import pandas as pd
import requests
import re
import os
from bs4 import BeautifulSoup

def get_cublog_urls():
   '''
    Returns urls from the codeup.com blog
    '''
    codeup_url = 'https://codeup.com/blog/'
    headers = {'user-agent': 'Innis Data Science Cohort'}
    response = requests.get(codeup_url, headers=headers)
    soup = BeautifulSoup(response.text)
    urls = [a.attrs['href'] for a in soup.select('a.more-link')]
    return urls


def parse_codeup_blog(soup):
    '''
    Takes in a BeautifulSoup object made from a page on Codeup's blog,
    returns a dictionary containing the blog's title, date published, and its content.
    '''
    output = {}

    output['title'] = soup.select_one('h1.entry-title').text
    output['date'] = soup.select_one('.published').text
    output['content'] = soup.select_one('.entry-content').text.strip()

    return output

def get_cublog_articles(use_cache= True):
    filename = 'codeup_blog_articles.json'
    if os.path.exists(filename) and use_cache:
        return pd.read_json(filename)

    urls = get_cublog_urls()
    articles = []

    for url in urls:
        print(f'Fetching {url}')
        headers = {'user-agent': 'Innis Data Science Cohort'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text)
        articles.append(parse_codeup_blog(soup))
    
    df = pd.DataFrame(articles)
    df.to_json(filename, orient= 'records')

    return df