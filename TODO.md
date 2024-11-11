# TODO
This file outlines tasks to build a basic, efficient web crawler in Python for the monzo challenge. The project will be structured modularly, with clear functionality and testing.

## 1. Project Setup and Dependencies (30 mins) ✅
### Tasks:
 - Set up a new Python project directory and initialize with Git.
 - Initialize Poetry for dependency management.
 - Define essential dependencies in pyproject.toml, including libraries for HTTP requests (e.g., requests), HTML parsing (e.g., beautifulsoup4), and testing (pytest).
 - Set up basic project structure:
     - crawler/ - Main package directory
     - tests/ - Test suite directory
 - Create a README.md file with a project overview and setup instructions.

## 2. Core Crawler Modules (1 hr 15 mins) ✅
### 2.1 URL Management 
### Tasks:
 - Create URLManager to handle:
     - Tracking visited URLs.
     - Controlling crawl depth.
     - Filtering URLs by domain.
 - Implement methods should_visit (checks URL eligibility) and add_url (adds URL to visited list).

### 2.2 Page Fetcher 
### Tasks:
 - Create PageFetcher for HTTP requests.
 - Implement a fetch method to retrieve page HTML content.
 - Add error handling for unreachable pages.

### 2.3 Link Extractor 
### Tasks:
 - Create LinkExtractor to parse HTML content and extract links.
 - Use BeautifulSoup to find anchor tags and extract valid href URLs.
 - Filter extracted links by domain and format URLs as absolute.

## 3. Crawler Logic (WebCrawler - 45 mins) ✅
### Tasks:
 - Create WebCrawler class to manage the crawl process.
 - Implement a crawl method to:
     - Initialize crawl from a starting URL.
     - Use concurrency with ThreadPoolExecutor to manage multiple requests.
     - Recursively fetch pages and extract links up to max_depth.
 - Set up data handling options to print or save results to a file.

## 4. Testing Suite (30 mins) ✅
### Tasks:
 - Create test cases in the tests/ directory for each module:
     - Test URLManager for correct URL tracking and depth management.
     - Test PageFetcher for successful page retrieval and error handling.
     - Test LinkExtractor for correct extraction and filtering of links.
 - Set up a few integration tests for WebCrawler to confirm end-to-end functionality.
 - Run tests and ensure coverage is adequate.

## 5. Command-Line Interface (20 mins) ✅
### Tasks:
 - Create run_crawler.py as an entry point for the crawler.
 - Set up CLI options using argparse for url, max_depth, and output_file.
 - Implement a simple loading message (e.g., “Crawling...”) while the crawler is running.

## 6. Final Documentation and Cleanup (20 mins) ✅
### Tasks:
 - Update README.md with usage examples, CLI options, and sample output.
 - Ensure code comments are clear and module docstrings are descriptive.
 - Conduct a final test run to verify functionality and resolve any issues.
 - Commit and push the completed code to a repository.