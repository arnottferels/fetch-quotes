import urllib.request
import json
import time
from concurrent.futures import ThreadPoolExecutor

# list of urls
urls = [
    "https://dummyjson.com/quotes/random",
    "https://dummyjson.com/quotes/random",
    "https://dummyjson.com/quotes/random",
    "https://dummyjson.com/quotes/random",
    "https://dummyjson.com/quotes/random",
]

# output file name
output_file = "quotes.json"


# fetch one url
def fetch(url):
    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                return json.load(response)
            else:
                print(f"Error: status {response.status}")
                return None
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None


# main
def main():
    start = time.time()

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(fetch, urls))

    quotes = [r for r in results if r]

    with open(output_file, "w") as f:
        json.dump(quotes, f, indent=2)

    end = time.time()
    print(f"Saved {len(quotes)} quotes to {output_file}.")
    print(f"Completed in {end - start:.2f} seconds.")


if __name__ == "__main__":
    main()
