#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <file_with_urls> <output_folder>"
    exit 1
fi

# Get the file path and output folder from arguments
url_file="$1"
output_dir="$2"

# Check if the file exists
if [ ! -f "$url_file" ]; then
    echo "Error: File '$url_file' not found!"
    exit 1
fi

# Create the output directory if it does not exist
mkdir -p "$output_dir"

# Read the file line by line
while IFS= read -r url; do
    # Skip empty lines
    [ -z "$url" ] && continue
    
    # Extract filename from URL
    filename=$(basename "$url")
    # Replace spaces with underscores in filename
    sanitized_filename=$(echo "$filename" | tr ' ' '_')
    # Download the file
    echo "Downloading $url..."
    curl -o "$output_dir/$sanitized_filename" "$url" || wget -O "$output_dir/$sanitized_filename" "$url"
done < "$url_file"

echo "All files downloaded to $output_dir"
