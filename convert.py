import os
from mkslides import create_slides

# Path to the markdown files
markdown_dir = 'markdown_files'
slides_dir = 'slides'

# Check if the directories exist
print(f"Looking for markdown files in: {markdown_dir}")
print(f"Will save slides to: {slides_dir}")

# Create slides from markdown files
for filename in os.listdir(markdown_dir):
    if filename.endswith('.md'):
        print(f"Processing file: {filename}")
        markdown_path = os.path.join(markdown_dir, filename)
        slides_path = os.path.join(slides_dir, f"{os.path.splitext(filename)[0]}.html")
        try:
            create_slides(markdown_path, slides_path)
            print(f"Created slides for {filename} at {slides_path}")
        except Exception as e:
            print(f"Error creating slides for {filename}: {e}")
    else:
        print(f"Skipping non-markdown file: {filename}")