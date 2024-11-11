from .page_fetcher import PageFetcher
from .link_extractor import LinkExtractor
from .url_manager import URLManager
from concurrent.futures import ThreadPoolExecutor, as_completed

class WebCrawler:
    def __init__(self, url, max_depth=None, output_file=None, num_workers=5):
        self.url = url
        self.max_depth = max_depth
        self.output_file = output_file
        self.num_workers = num_workers
        self.url_manager = URLManager(max_depth)
        self.page_fetcher = PageFetcher()
        self.link_extractor = LinkExtractor(url)
        self.output_data = []  # Store results for printing after crawl is complete

    def crawl(self):
        # Crawl concurrently with Thredpooolexecutor 
        with ThreadPoolExecutor(max_workers=self.num_workers) as executor:
            future_to_url = {executor.submit(self._crawl_page, self.url, 0): self.url}
            while future_to_url:
                for future in as_completed(future_to_url):
                    url = future_to_url.pop(future)
                    try:
                        links = future.result()  # _crawl_page returns links found on the page
                        if links:
                            for link in links:
                                next_depth = self.url_manager.visited_urls_depth[url] + 1
                                if self.url_manager.should_visit(link, next_depth):
                                    future_to_url[executor.submit(self._crawl_page, link, next_depth)] = link
                    except Exception as exc:
                        print(f"Exception while crawling {url}: {exc}")
        
        # Output all data after crawling is complete
        self._print_output()

        # Save output to file if specified
        if self.output_file:
            self._save_output_to_file()

    def _crawl_page(self, url, depth):
        if not self.url_manager.should_visit(url, depth):
            return []

        self.url_manager.add_url(url, depth)
        page_content = self.page_fetcher.fetch(url)
        if page_content:
            links = self.link_extractor.extract_links(page_content)

            # Store visited URL and links for later output
            self.output_data.append({
                'url': url,
                'depth': depth,
                'links': links
            })
            return links  # Return links for further processing in the main crawl loop
        return []

    def _print_output(self):
        # Print all results after crawling is complete
        for entry in self.output_data:
            print(f"\nVisited: {entry['url']} (depth {entry['depth']})")
            print("Links found:")
            for link in entry['links']:
                print(f"  - {link}")

    def _save_output_to_file(self):
        # Save output data to file if output_file is specified
        with open(self.output_file, "w") as file:
            for entry in self.output_data:
                file.write(f"Visited: {entry['url']} (depth {entry['depth']})\n")
                file.write("Links found:\n")
                for link in entry['links']:
                    file.write(f"  - {link}\n")
                file.write("\n")
