import sys
import json
from generate_content import generate_markdown_content

def process_discord_webhook(data):
    # Extract relevant information from Discord webhook payload
    content = data.get('content', '')
    author = data.get('author', {}).get('username', 'Unknown Author')
    
    # Parse the content for title and body
    # Assuming the first line is the title and the rest is the body
    lines = content.split('\n')
    title = lines[0] if lines else 'New Ape Discovery'
    body = '\n'.join(lines[1:]) if len(lines) > 1 else 'A new discovery has been made!'

    processed_data = {
        'title': title,
        'date': data.get('timestamp', '2023-05-15').split('T')[0],  # Extract date from Discord timestamp
        'author': author,
        'content': body,
        'image_url': data.get('attachments', [{}])[0].get('url', '/img/default-ape.gif'),
        'image_alt': 'Image from Discord',
        'additional_info': [
            f"Posted by {author} on Discord",
            f"Message ID: {data.get('id', 'Unknown')}"
        ],
        'learn_more_url': f"/discoveries/{title.lower().replace(' ', '-')}/"
    }
    return processed_data

def main(json_data):
    data = json.loads(json_data)
    processed_data = process_discord_webhook(data)
    output_path = f"content/{processed_data['date']}-{processed_data['title'].lower().replace(' ', '-')}.md"
    generate_markdown_content('content/template.md', output_path, processed_data)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("No data provided")
