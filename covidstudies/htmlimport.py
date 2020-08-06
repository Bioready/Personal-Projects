import requests


def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html)


def open_html(path):
    with open(path, 'rb') as f:
        return f.read()


url = 'https://c19study.com/'
r = requests.get(url)

save_html(r.content, 'html_data.txt')
