class URLManager:
    def __init__(self, max_depth=None):
        self.visited_urls = set()
        self.visited_urls_depth = {}
        self.max_depth = max_depth

    def should_visit(self, url, depth):
        # If max_depth is set, ensure depth does not exceed it; if None, depth is unrestricted
        if url in self.visited_urls:
            return False
        if self.max_depth is not None and depth > self.max_depth:
            return False
        return True

    def add_url(self, url, depth):
        self.visited_urls.add(url)
        self.visited_urls_depth[url] = depth
