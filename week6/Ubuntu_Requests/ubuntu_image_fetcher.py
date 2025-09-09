import os
import requests
from urllib.parse import urlparse
import hashlib

def welcome_message():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

def create_directory(directory="Fetched_Images"):
    os.makedirs(directory, exist_ok=True)
    return directory

def get_filename_from_url(url):
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename or '.' not in filename:
        return "downloaded_image.jpg"
    return filename

def is_duplicate_image(content, directory):
    # Hash image content to check for duplicates
    image_hash = hashlib.md5(content).hexdigest()
    for fname in os.listdir(directory):
        fpath = os.path.join(directory, fname)
        if os.path.isfile(fpath):
            with open(fpath, 'rb') as f:
                existing_hash = hashlib.md5(f.read()).hexdigest()
                if existing_hash == image_hash:
                    return fname
    return None

def fetch_image(url, directory="Fetched_Images"):
    try:
        headers = {
            'User-Agent': 'UbuntuImageFetcher/1.0',
            'Accept': 'image/*'
        }

        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ The URL does not point to an image. Content-Type: {content_type}")
            return

        filename = get_filename_from_url(url)
        image_content = response.content

        # Check for duplicates
        duplicate = is_duplicate_image(image_content, directory)
        if duplicate:
            print(f"✓ Duplicate detected: {duplicate} already exists. Skipping download.")
            return

        filepath = os.path.join(directory, filename)
        with open(filepath, 'wb') as f:
            f.write(image_content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    welcome_message()
    directory = create_directory()

    urls = input("Please enter one or more image URLs (separated by commas): ").split(',')

    for url in map(str.strip, urls):
        if not url:
            continue
        print(f"\nFetching from: {url}")
        fetch_image(url, directory)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
