import time
import zipfile
import os
import shutil
import urllib.request
from tqdm import tqdm

print('Início: ', time.time())
download_list = ['Estabelecimentos', 'Sócios', 'Motivos', 'Municípios', 'Naturezas', 'Paises', 'Qualificações', 'Simples']

for i in download_list:
    if i == 'Estabelecimentos' or i == 'Sócios':
        for idx in range(1, 10):
            print(f'Downloading file {i}{idx}')
            response = urllib.request.urlopen(f"https://dadosabertos.rfb.gov.br/CNPJ/{i}{idx}.zip")
            file_size = response.headers.get('Content-Length')
            with tqdm(total=int(file_size), unit='B', unit_scale=True) as pbar:
                for data in response:
                    pbar.update(len(data))
                    with open(f'tmpZipFiles/{i}{idx}.zip', 'ab') as f:
                        f.write(data)
    else:
        print(f'Downloading file {i}')
        response = urllib.request.urlopen(f"https://dadosabertos.rfb.gov.br/CNPJ/{i}.zip")
        file_size = response.headers.get('Content-Length')
        with tqdm(total=file_size, unit='B', unit_scale=True) as pbar:
            for data in response:
                pbar.update(len(data))
                with open(f'tmpZipFiles/{i}.zip', 'ab') as f:
                    f.write(data)

os.mkdir('tmp_dataset')
os.mkdir('dataset')

for zip_file in os.listdir("tmpZipFiles"):
    file_path = "tmpZipFiles/" + zip_file
    print(f'Extracting {file_path}')
    zipfile.ZipFile(file_path, 'r').extractall('tmp_dataset')

for unzip_file in os.listdir("tmp_dataset"):
    shutil.move("tmp_dataset/" + unzip_file, "dataset/" + unzip_file + ".csv")

shutil.rmtree("tmp_dataset")
print('Fim: ', time.time())
