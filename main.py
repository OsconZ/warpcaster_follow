import webbrowser
import re

all = open('all.txt', "r", encoding="utf-8")
urls_file = open('urls.txt', "r", encoding="utf-8")
urls = urls_file.read().splitlines()
urls_file.close()

for line in all:
    text = line.strip()
    url_pattern = r'https://warpcast\.com/[\S]+'
    urls_found = re.findall(url_pattern, text)
    for url in urls_found:
        if url not in urls:
            urls.append(url)
            webbrowser.open(url, new=0, autoraise=True)
all.close()

urls_file = open('urls.txt', "w", encoding="utf-8")
for url in urls:
    urls_file.write(url + '\n')
urls_file.close()