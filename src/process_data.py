import sys
import json
from generate_content import generate_markdown_content

def process_incoming_data(data):
    processed_data = {
        'title': data.get('title', 'New Ape Discovery'),
        'date': data.get('date', '2023-05-15'),
        'author': data.get('author', 'Dr. Jane Goodall'),
        'content': data.get('content', 'A new species of ape has been discovered!'),
        'image_url': data.get('image_url', '/img/new-ape.gif'),
        'image_alt': data.get('image_alt', 'A newly discovered ape'),
        'additional_info': data.get('additional_info', [
            'The ape was found in a remote jungle',
            'It has unique markings on its fur'
        ]),
        'learn_more_url': data.get('learn_more_url', '/discoveries/new-ape/')
    }
    return processed_data

def main(json_data):
    data = json.loads(json_data)
    processed_data = process_incoming_data(data)
    output_path = f"content/{processed_data['date']}-{processed_data['title'].lower().replace(' ', '-')}.md"
    generate_markdown_content('content/template.md', output_path, processed_data)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("No data provided")
