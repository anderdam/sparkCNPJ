import zipfile
import os
import shutil
import urllib.request
from tqdm import tqdm

url = 'https://dadosabertos.rfb.gov.br/CNPJ'
files_to_download = ['Empresas', 'Estabelecimentos', 'Socios', 'Motivos', 'Municipios', 'Naturezas', 'Paises', 'Qualificacoes', 'Simples', 'Cnaes']

# Temporary folders
tmp_zips, tmp_dataset = ('tmp_zipFiles', 'tmp_dataset')


def download_files(download_list, address):
    os.mkdir(tmp_zips)
    for i in download_list:
        if i == 'Estabelecimentos' or i == 'Socios' or i == 'Empresas':
            for idx in range(1, 10):
                print(f'Downloading file..... {address}/{i}{idx}.zip"')
                response = urllib.request.urlopen(f"{address}/{i}{idx}.zip")
                file_size = response.headers.get('Content-Length')
                with tqdm(total=int(file_size), unit='B', unit_scale=True) as pbar:
                    for data in response:
                        pbar.update(len(data))
                        with open(f'{tmp_zips}/{i}{idx}.zip', 'ab') as f:
                            f.write(data)
        else:
            print(f'Downloading file..... {address}/{i}.zip')
            response = urllib.request.urlopen(f'{address}/{i}.zip')
            file_size = response.headers.get('Content-Length')
            with tqdm(total=int(file_size), unit='B', unit_scale=True) as pbar:
                for data in response:
                    pbar.update(len(data))
                    with open(f'{tmp_zips}/{i}.zip', 'ab') as f:
                        f.write(data)


def extract_and_move_zip_files():
    os.mkdir(tmp_dataset)
    os.mkdir('dataset')
    for zip_file in os.listdir(tmp_zips):
        file_path = tmp_zips + "/" + zip_file
        print(f'Extracting..... {file_path}')
        zipfile.ZipFile(file_path, 'r').extractall(tmp_dataset)

    for unzip_file in os.listdir(tmp_dataset):
        # Split the file name by the last dot
        file_name_parts = unzip_file.split('.')
        # Get the file extension
        # Remove the file ending from the file name
        file_name_split = ''.join(file_name_parts[-1]) if 'SIMPLES' not in unzip_file else ''.join(file_name_parts[2])

        # Create a directory for the file if it doesn't exist
        destination_directory = os.path.join('dataset', file_name_split)
        if not os.path.exists(destination_directory):
            os.mkdir(destination_directory)

        # Move the file to the destination directory
        shutil.move(os.path.join(tmp_dataset, unzip_file), os.path.join(destination_directory, f'{unzip_file}.csv'))

    shutil.rmtree(tmp_dataset)
    shutil.rmtree(tmp_zips)


if __name__ == '__main__':
    download_files(files_to_download, url)
    extract_and_move_zip_files()
