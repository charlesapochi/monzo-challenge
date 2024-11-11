import requests

class PageFetcher:
    def fetch(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.text
        except requests.RequestException as e:
            # print(f"\nError fetching {url}: {e}")
            return None
