from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from chatbot_batch.config.ConfigStore import *
from chatbot_batch.udfs.UDFs import *

def question_seed(spark: SparkSession) -> DataFrame:
    df1 = spark.range(1)

    return df1.select(lit("Does Prophecy support on-premise environments? ").alias("input"))
