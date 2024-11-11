from crawler.url_manager import URLManager

# Define a test function to verify adding a URL to the URLManager.
def test_add_url():
    manager = URLManager(max_depth=2)
    manager.add_url("https://example.com", 1)
    assert "https://example.com" in manager.visited_urls
    assert manager.visited_urls_depth["https://example.com"] == 1

# Define a test function to verify the should_visit logic for URLs.
def test_should_visit():
    manager = URLManager(max_depth=2)
    assert manager.should_visit("https://example.com", 1) is True
    manager.add_url("https://example.com", 1)
    assert manager.should_visit("https://example.com", 1) is False