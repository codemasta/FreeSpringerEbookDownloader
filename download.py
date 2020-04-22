import requests
import csv
import os
import shutil


def downloader():
    with open('SpringBooksLink.txt') as links:
        url_links = [link.rstrip('\n') for link in links.readlines()]

    for url in url_links:
        direct_request = requests.head(url, allow_redirects=True)
        base_url = str(direct_request.url)[:25:]
        url_param = str(direct_request.url)[31::]
        download_url = f'{base_url}/content/pdf/{url_param}.pdf'
        request = requests.get(download_url)
        with open(f"DownloadedBooks/{url[-17:]}.pdf", 'wb') as pdf_file:
            pdf_file.write(request.content)


def rename():
    books_name = os.listdir('DownloadedBooks')
    with open('SpringBook_Name.csv') as csv_file:
        read_csv = csv.reader(csv_file)
        for row in read_csv:
            for book in books_name:
                if row[1] == book.strip('.pdf'):
                    shutil.move(f'DownloadedBooks/{book}', f'DownloadedBooks/Renamed/{row[0]}.pdf')


print('Started...')
downloader()
rename()
print('Completed')
