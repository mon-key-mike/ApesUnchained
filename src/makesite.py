#!/usr/bin/env python

import os
import shutil
import re
import glob
import sys
import json
import datetime

def fread(filename):
    """Read file and close the file."""
    with open(filename, 'r') as f:
        return f.read()

def fwrite(filename, text):
    """Write content to file and close the file."""
    basedir = os.path.dirname(filename)
    if not os.path.isdir(basedir):
        os.makedirs(basedir)

    with open(filename, 'w') as f:
        f.write(text)

def render(template, params={}):
    """Replace placeholders in template with params."""
    for key, value in params.items():
        template = template.replace('{{ ' + key + ' }}', str(value))
    return template

def read_content(filename):
    """Read content and metadata from file into a dictionary."""
    # Read file content.
    text = fread(filename)

    # Read metadata and save it in a dictionary.
    metadata = {}
    for line in text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            metadata[key.strip()] = value.strip()

    # Strip metadata from text.
    text = re.sub(r'^.*?\n\n', '', text, flags=re.DOTALL)

    return {
        'content': text,
        'metadata': metadata
    }

def read_posts(directory):
    """Read all posts into a list of dictionaries."""
    posts = []
    for filename in glob.glob(os.path.join(directory, '*.md')):
        post = read_content(filename)
        post['filename'] = os.path.basename(filename).replace('.md', '.html')
        posts.append(post)
    return posts

def main():
    # Create a new _site directory from scratch.
    if os.path.isdir('_site'):
        shutil.rmtree('_site')
    shutil.copytree('static', '_site')

    # Default parameters.
    params = {
        'base_path': '',
        'subtitle': 'A python-powered, simple website',
        'author': 'The Apes',
        'site_url': 'http://localhost:8000',
        'current_year': datetime.datetime.now().year
    }

    # If params.json exists, load it.
    if os.path.isfile('params.json'):
        params.update(json.loads(fread('params.json')))

    # Load layouts.
    page_layout = fread('layout/base.html')
    post_layout = fread('layout/post.html')

    # Combine layouts to form final layouts.
    post_layout = render(page_layout, {'content': post_layout})

    # Create site pages.
    for src in glob.glob('content/*.md'):
        dst = os.path.join('_site', os.path.basename(src).replace('.md', '.html'))
        post = read_content(src)
        params.update(post['metadata'])
        params['content'] = post['content']
        page = render(page_layout, params)
        fwrite(dst, page)

    # Create blog list page.
    posts = read_posts('content')
    posts.sort(key=lambda x: x['metadata']['date'], reverse=True)
    params['content'] = '<ul>'
    for post in posts:
        params['content'] += '<li><a href="./{0}">{1}</a></li>'.format(post['filename'], post['metadata']['title'])
    params['content'] += '</ul>'
    page = render(page_layout, params)
    fwrite('_site/blog.html', page)

if __name__ == '__main__':
    main()
