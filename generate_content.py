from jinja2 import Template
import datetime

def generate_markdown_content(template_path, output_path, data):
    with open(template_path, 'r') as file:
        template = Template(file.read())
    
    rendered_content = template.render(**data)
    
    with open(output_path, 'w') as file:
        file.write(rendered_content)

# Example usage
data = {
    'title': 'Exciting Ape Discovery',
    'date': datetime.date.today().isoformat(),
    'author': 'Dr. Jane Goodall',
    'content': 'Scientists have discovered a new species of ape that can code in Python!',
    'image_url': '/img/coding-ape.gif',
    'image_alt': 'An ape coding on a computer',
    'additional_info': [
        'The ape has been named Simia pythonicus',
        'It prefers bananas as a coding snack',
        'Its favorite IDE is Jungle Studio'
    ],
    'learn_more_url': '/discoveries/simia-pythonicus/'
}

generate_markdown_content('content/template.md', 'content/2023-05-15-exciting-ape-discovery.md', data)
