# import time
# import zipfile
# import os
# import shutil
# import urllib.request
# from pyspark.sql import SparkSession
#
# print('Início: ', time.time())
# download_list = ['Estabelecimentos', 'Sócios', 'Motivos', 'Municípios', 'Naturezas', 'Paises', 'Qualificações', 'Simples']
#
#
# for i in download_list:
#     if i == 'Estabelecimentos' or i == 'Sócios':
#         for idx in range(1, 10):
#             print(f'Downloading file {i}{idx}')
#             urllib.request.urlretrieve(f"https://dadosabertos.rfb.gov.br/CNPJ/{i}{idx}.zip", f"tmpZipFiles/{i}{idx}.zip")
#     else:
#         print(f'Downloading file {i}')
#         urllib.request.urlretrieve(f"https://dadosabertos.rfb.gov.br/CNPJ/{i}.zip", f"tmpZipFiles/{i}.zip")
#
# os.mkdir('tmp_dataset')
# os.mkdir('dataset')
#
# for zip_file in os.listdir("tmpZipFiles"):
#     file_path = "tmpZipFiles/" + zip_file
#     print(f'Extracting {file_path}')
#     zipfile.ZipFile(file_path, 'r').extractall('tmp_dataset')
#
# for unzip_file in os.listdir("tmp_dataset"):
#     shutil.move("tmp_dataset/" + unzip_file, "dataset/" + unzip_file + ".csv")
#
# shutil.rmtree("tmp_dataset")
# print('Fim: ', time.time())
