from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from web_ingest.config.ConfigStore import *
from web_ingest.udfs.UDFs import *

def web_bronze_url_alt(spark: SparkSession) -> DataFrame:
    from spark_ai.webapps import WebUtils
    WebUtils().register_udfs(spark)
    df1 = spark.range(1)

    return df1\
        .withColumn("url", lit("https://docs.prophecy.io/sitemap.xml"))\
        .withColumn("content", expr("web_scrape(url)"))
