import argparse
import threading
import time
from crawler.crawler import WebCrawler

def display_status(crawler):
    """Display an animated status message with crawl statistics."""
    spinner = ['|', '/', '-', '\\']
    i = 0
    while not stop_event.is_set():
        num_urls = len(crawler.url_manager.visited_urls_depth)
        max_depth_reached = max(crawler.url_manager.visited_urls_depth.values(), default=0)
        print(f"\rCrawling in progress... {spinner[i % len(spinner)]} | URLs visited: {num_urls} | Depth reached: {max_depth_reached}", end='', flush=True)
        i += 1
        time.sleep(0.2)
    print("\r\nCrawl complete 😁" + " " * 50) 

def main():
    parser = argparse.ArgumentParser(description="Run the WebCrawler on a given URL.")
    parser.add_argument("url", type=str, help="Starting URL for the crawler.")
    parser.add_argument("--max_depth", type=int, default=None, help="Maximum depth to crawl.")
    parser.add_argument("--output_file", type=str, help="File to save output URLs.")
    parser.add_argument("--num_workers", type=int, default=5, help="Number of concurrent workers.")

    args = parser.parse_args()

    # Initialize the crawler
    crawler = WebCrawler(url=args.url, max_depth=args.max_depth, output_file=args.output_file, num_workers=args.num_workers)

    # Start the status display thread
    global stop_event
    stop_event = threading.Event()
    status_thread = threading.Thread(target=display_status, args=(crawler,))
    status_thread.start()

    # Run the crawler
    crawler.crawl()

    # Stop the status display thread
    stop_event.set()
    status_thread.join()

    # # Output results
    if args.output_file:
        print(f"\nResults saved to {args.output_file}\n")
    

if __name__ == "__main__":
    stop_event = None
    main()
