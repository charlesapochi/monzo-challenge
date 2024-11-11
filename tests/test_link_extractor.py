from crawler.link_extractor import LinkExtractor

# Define a test function to verify the functionality of link extraction.
def test_extract_links():
    extractor = LinkExtractor("https://example.com")
    html_content = '<a href="https://example.com/page1">Page 1</a>'
    links = extractor.extract_links(html_content)
    assert "https://example.com/page1" in links