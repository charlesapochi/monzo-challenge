from crawler.crawler import WebCrawler

# Define a test function to verify initial crawling functionality.
def test_crawl_initial_url():
    crawler = WebCrawler("https://example.com", max_depth=2)
    crawler.crawl()
    assert "https://example.com" in crawler.url_manager.visited_urls