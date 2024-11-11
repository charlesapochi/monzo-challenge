# Import BeautifulSoup for parsing HTML content and urljoin/urlparse for handling URLs.
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

class LinkExtractor:
    def __init__(self, base_url):
        # Initialize with a base URL and store the domain for internal link filtering.
        self.base_url = base_url
        self.base_domain = urlparse(base_url).netloc

    def extract_links(self, html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        links = set()
        
        for a_tag in soup.find_all("a", href=True):
            link = urljoin(self.base_url, a_tag["href"])
            
            # Only add links that are within the same domain as the base URL.
            if urlparse(link).netloc == self.base_domain:
                links.add(link)
        
        return links
