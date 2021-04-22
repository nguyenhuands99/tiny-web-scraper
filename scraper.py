from typing import Dict
import requests
from bs4 import BeautifulSoup
import string
import time
import os
import re


class WebScrapper:

    def __init__(self, url):
        self.url = url

    def print_content(self):
        """
        Task 1: Talk to the Internet
        """
        try:
            r = requests.get(self.url)
            if r.ok and 'content' in r.json():
                print(r.json().get('content'))
            else:
                print('Invalid quote resource!')
        except RuntimeError:
            print('Invalid quote resource!')

    def print_movie_dict(self):
        """
        Task 2: BeautifulSoup Ingredients
        """
        try:
            r = requests.get(self.url, headers={'Accept-Language': 'en-US,en;q=0.5'})
            if not r.ok or 'https://www.imdb.com' not in self.url:
                print('Invalid movie page!')
            else:
                soup = BeautifulSoup(r.content, 'html.parser')
                title = soup.find('title')
                description = soup.find('div', {'class': 'summary_text'})
                movie_dict: Dict[str, str] = {
                    'title': "" if title is None else title.text,
                    'description': "" if description is None else description.text.strip()
                }
                print('Invalid movie page!' if "" in movie_dict.values() else movie_dict)
        except RuntimeError:
            print('Invalid movie page!')

    def save_content(self):
        """
        Task 3: What the File?
        """
        r = requests.get(self.url)
        if r.ok:
            with open('source.html', 'wb') as file:
                page_content = r.content
                file.write(page_content)
                print('Content saved.')
        else:
            print(f'The URL returned {r.status_code}')

    def save_txt(self, nature_type='News', num_page=1):
        """
        Task 4+5: Soup :v 
        """
        try:
            txt_format_dict = {k: '' for k in string.punctuation}
            txt_format_dict.update({' ': '_'})
            for pg in range(num_page):
                os.mkdir(f"Page_{pg + 1}")
                r = requests.get(self.url + f'?searchType=journalSearch&sort=PubDate&page={pg + 1}')
                soup = BeautifulSoup(r.content, 'html.parser')
                articles = soup.find_all('article')
                for article in articles:
                    title = article.find('a', {'data-track-action': "view article"}).text.strip()
                    a_type = article.find('span', {'data-test': 'article.type'}).text.strip()
                    if a_type == nature_type:
                        txt_filename = title.translate(str.maketrans(txt_format_dict)) + '.txt'
                        url = article.find('a', {'data-track-label': 'link'})['href']
                        time.sleep(5)
                        a_r = requests.get('https://www.nature.com' + url)
                        a_soup = BeautifulSoup(a_r.content, 'html.parser')
                        content = a_soup.body.find('div', {'class': re.compile("article(-item)?__body")}).text.strip()
                        filename_path = os.path.join(f"Page_{pg + 1}", txt_filename)
                        with open(filename_path, 'w', encoding='utf-8') as file:
                            file.write(content)
        except (RuntimeError, NameError, ValueError, TypeError):
            print('An error has occurred when processing the article!')
            return
        finally:
            print('Saved all articles')


def main():
    num_pg = int(input())
    article_type = input()
    scrapper = WebScrapper('https://www.nature.com/nature/articles')
    scrapper.save_txt(nature_type=article_type, num_page=num_pg)


if __name__ == '__main__':
    main()
