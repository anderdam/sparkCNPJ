import zipfile
import os
import shutil
import urllib.request
from tqdm import tqdm

url = 'https://dadosabertos.rfb.gov.br/CNPJ'
files_to_download = ['Empresas', 'Estabelecimentos', 'Socios', 'Motivos', 'Municipios', 'Naturezas', 'Paises', 'Qualificacoes', 'Simples', 'Cnaes']


def download_files(download_list, address):
    for i in download_list:
        if i == 'Estabelecimentos' or i == 'Socios':
            for idx in range(1, 10):
                print(f'Downloading file {i}{idx}')
                response = urllib.request.urlopen(f"{address}/{i}{idx}.zip")
                file_size = response.headers.get('Content-Length')
                with tqdm(total=int(file_size), unit='B', unit_scale=True) as pbar:
                    for data in response:
                        pbar.update(len(data))
                        with open(f'tmpZipFiles/{i}{idx}.zip', 'ab') as f:
                            f.write(data)
        else:
            print(f'Downloading file {i}')
            response = urllib.request.urlopen(f'{address}/{i}.zip')
            file_size = response.headers.get('Content-Length')
            with tqdm(total=int(file_size), unit='B', unit_scale=True) as pbar:
                for data in response:
                    pbar.update(len(data))
                    with open(f'tmpZipFiles/{i}.zip', 'ab') as f:
                        f.write(data)


def extract_and_move_zip_files():
    for zip_file in os.listdir("tmpZipFiles"):
        file_path = "tmpZipFiles/" + zip_file
        print(f'Extracting {file_path}')
        zipfile.ZipFile(file_path, 'r').extractall('tmp_dataset')

    for unzip_file in os.listdir("tmp_dataset"):
        for i in range(0, len(files_to_download)):
            if files_to_download[i][:4].lower() in unzip_file.lower():
                shutil.move('tmp_dataset', f"{outdir}/{unzip_file}.csv")

    shutil.rmtree("tmp_dataset")
    shutil.rmtree("tmpZipFiles")


if __name__ == '__main__':
    os.mkdir('tmp_dataset')
    os.mkdir('dataset')
    # download_files(files_to_download, url)
    extract_and_move_zip_files()

