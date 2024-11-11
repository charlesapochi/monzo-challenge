# Monzo Challenge

A simple, domain-limited web crawler in Python, designed by Charles Apochi for the Monzo take-home challenge, which explores and collects links within a specified domain. This crawler is efficient and customizable, with options to save results to a file or print them to the console.

Key features include domain-limited crawling, which restricts the crawl to the starting URL's domain, avoiding external sites and subdomains. The depth control allows specifying a max_depth (defaulting to unlimited if not specified). Multithreading enables faster crawling, and flexible output options let users save results to a file or display them on the console.


## 1.0 Project Structure
This project is modular, with separate components for each responsibility:

 - WebCrawler: Core logic for managing the crawl and orchestrating other components.
 - PageFetcher: Fetches page HTML content.
 - LinkExtractor: Extracts links from HTML.
 - URLManager: Manages visited URLs and depth control.


## 2.0 Dependencies

The following dependencies are requiired before runniing the web crawler tool:
 - Python: 3.10+
 - Poetry: Package management

### Installing Dependencies

1. Install Poetry if not already installed (At this time, the latest stable version of Poetry is 1.8.4):

```bash
curl -sSL https://install.python-poetry.org | python3 -
```
2. Install project dependencies:

```bash
poetry install
```

3. Activate an isolated environment:

```bash
poetry shell
```

## 3.0 Usage
Run the crawler with run_crawler.py by following the steps below:

1. Confirm you have the required dependices istalled on your system if not refer to the dependcies section: 
```bash
python --version
poetry --version
```

2. Open your terminal or command prompt and navigate to the directory where the run_crawler.py file is located.

3. Run the command below replacing placeholders with the arguments you want. See table below for arguments definitions:

```bash
python run_crawler.py --url <starting_url> [--max_depth <depth>] [--output_file <output_file_path>] [--num_workers 10 <number_of_workers>]
```

| Option | Description | Default |
| --- | --- | --- |
| --url | (required): Starting URL for the crawler |
| --max_depth | (optional): Maximum crawl depth. None for unlimited depth. | None
| --output_file| (optional): File path to save the results; if omitted, prints to console. | stdout
| --num_workers| (optional): Number of concurrent workers; if omitted, use the default workers. | 5

Example
To crawl https://monzo.com up to a depth of 3 and save output to results.txt:

```bash
python run_crawler.py https://monzo.com --max_depth 3 --output_file results.txt
```

4. The tool will commence crawling base on provided arguments. While waiting for the process to finished, the tool will diisplay an interactive and real-time statistics showing number of links visited and depth reached. 

5. Once the scraping process finishes, the collected URLs will be available either in your specified output file or displayed directly in the console, depending on which output method you configured.


### Sample Output

```plaintext
Visited: https://monzo.com (depth 0)
Links found:
  - https://monzo.com/current-account/16-17
  - https://monzo.com/investments
  - https://monzo.com/legal/terms-and-conditions/
...

Visited: https://monzo.com/legal/terms-and-conditions/ (depth 1)
Links found:
  - https://monzo.com/legal/referral-scheme/terms-and-conditions
  - https://monzo.com/legal/overdraft-information
...
```

## 4.0 Testing
Unit tests in the tests directory cover the initialization and functionality of crawler components, depth control, and URL and link extraction management.

### Running Tests

1. Activate the isolated environment:

```bash
poetry shell
```

2. Run tests:

```bash
pytest tests/
```
