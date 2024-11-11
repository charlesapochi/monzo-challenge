from crawler.page_fetcher import PageFetcher

# Define a test function to verify fetching content from a valid URL.
def test_fetch_valid_url():
    fetcher = PageFetcher()
    content = fetcher.fetch("https://example.com")
    assert content is not None

# Define a test function to verify behavior when fetching from an invalid URL.
def test_fetch_invalid_url():
    fetcher = PageFetcher()
    content = fetcher.fetch("https://invalid-url.com")
    assert content is None