from pyspark.sql import SparkSession

spark = SparkSession.builder\
    .master('local[*]')\
    .appName('Análise com Spark')\
    .config('spark.ui.port', '4040')\
    .getOrCreate()

empresas_path = 'dataset/empresas'


# .rename(columns={'cnpj', 'razao_social', 'natureza_juridica', 'qualificacao_responsavel', 'capital_social', 'porte_empresa', 'ente_federativo'})\
df_empresas = spark.read.csv(empresas_path, sep=';', inferSchema=True).fillna('n/a')\
    .withColumnRenamed('_c0', 'cnpj')\
    .withColumnRenamed('_c1', 'razao_social')\
    .withColumnRenamed('_c2', 'natureza_juridica')\
    .withColumnRenamed('_c3', 'qualificacao_responsavel')\
    .withColumnRenamed('_c4', 'capital_social')\
    .withColumnRenamed('_c5', 'porte_empresa')\
    .withColumnRenamed('_c6', 'ente_federativo')

df_empresas.show(5)



