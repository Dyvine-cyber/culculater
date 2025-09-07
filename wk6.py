import requests
import os
from urllib.parse import urlparse
import hashlib
from datetime import datetime
import mimetypes

def calculate_file_hash(filepath):
    """Calculate SHA-256 hash of a file to check for duplicates"""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def is_valid_image_content_type(content_type):
    """Check if the content type is a valid image type"""
    valid_types = ['image/jpeg', 'image/png', 'image/gif', 'image/bmp']
    return content_type in valid_types

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A community-driven tool for safely collecting images from the web\n")
    
    # Get multiple URLs from user (comma-separated)
    urls_input = input("Please enter image URLs (comma-separated): ")
    urls = [url.strip() for url in urls_input.split(',') if url.strip()]
    
    if not urls:
        print("✗ No valid URLs provided")
        return
    
    # Create directory for images with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"Fetched_Images_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    
    # Store hashes to prevent duplicates
    existing_hashes = set()
    
    for url in urls:
        try:
            print(f"\nProcessing URL: {url}")
            
            # Send HEAD request first to check headers
            head_response = requests.head(url, timeout=10, allow_redirects=True)
            head_response.raise_for_status()
            
            # Check Content-Type header
            content_type = head_response.headers.get('content-type', '').lower()
            if not is_valid_image_content_type(content_type):
                print(f"✗ Skipped: Invalid content type ({content_type})")
                continue
                
            # Check Content-Length (avoid very large files, e.g., >10MB)
            content_length = int(head_response.headers.get('content-length', 0))
            if content_length > 10 * 1024 * 1024:
                print(f"✗ Skipped: File too large ({content_length} bytes)")
                continue
                
            # Verify server response security headers
            security_headers = {
                'X-Content-Type-Options': 'nosniff',
                'X-Frame-Options': ['DENY', 'SAMEORIGIN']
            }
            for header, expected in security_headers.items():
                value = head_response.headers.get(header)
                if isinstance(expected, list):
                    if value not in expected:
                        print(f"⚠ Warning: Missing or invalid {header}")
                elif value != expected:
                    print(f"⚠ Warning: Missing or invalid {header}")
            
            # Fetch the image
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            # Extract filename or generate one
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            
            # Ensure proper file extension based on content type
            if not filename or not os.path.splitext(filename)[1]:
                extension = mimetypes.guess_extension(content_type) or '.jpg'
                filename = f"image_{len(os.listdir(output_dir)) + 1}{extension}"
            
            filepath = os.path.join(output_dir, filename)
            
            # Calculate content hash to check for duplicates
            content_hash = hashlib.sha256(response.content).hexdigest()
            if content_hash in existing_hashes:
                print(f"✗ Skipped: Duplicate image detected")
                continue
                
            # Save the image
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            # Verify file integrity by checking hash
            saved_file_hash = calculate_file_hash(filepath)
            if saved_file_hash != content_hash:
                print(f"✗ Error: File integrity check failed for {filename}")
                os.remove(filepath)
                continue
                
            existing_hashes.add(content_hash)
            
            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")
            
        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error for {url}: {e}")
        except Exception as e:
            print(f"✗ An error occurred for {url}: {e}")
    
    print("\nConnection strengthened. Community enriched.")
    print("Thank you for using this tool responsibly!")

if __name__ == "__main__":
    main()