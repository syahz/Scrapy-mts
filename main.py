from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
# from google.colab import drive
# drive.mount('/content/drive')
# import csv

base_url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0508/3/jf/10/all'
rr = []
for i in range(1, 2):
    if i < 10:
        url = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/05040{i}/3/all/10/all'
    else:
        url = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0504{i}/3/all/10/all'

    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')

    # Cari tabel dengan atribut class "table table-striped table-hover"
    table = soup.find('tbody')

    # Inisialisasi list untuk data tabel
    data = []


    # Iterasi melalui baris-baris tabel
    for row in table.find_all('tr'):
        cols = row.find_all('td')
        cols = [elem.text.strip() for elem in cols]
        data.append(cols)

    # Buat DataFrame dari data
    df2 = pd.DataFrame(data)
    rr.append(df2)
    print(data)

final_df = pd.concat(rr, axis=0, ignore_index=True)

#jika ingin menyimpan ke CSV
#final_df.to_csv('/content/drive/My Drive/----Rename your file-----', index=False)
