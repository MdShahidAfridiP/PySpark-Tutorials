import pandas as pd    
data = [['Scott', 50], ['Jeff', 45], ['Thomas', 54],['Ann',34]] 
  
# Create the pandas DataFrame 
pandasDF = pd.DataFrame(data, columns = ['Name', 'Age']) 
  
# print dataframe. 
print(pandasDF)

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[1]") \
    .appName("SparkByExamples.com") \
    .getOrCreate()

sparkDF=spark.createDataFrame(pandasDF) 
sparkDF.printSchema()
sparkDF.show()

#sparkDF=spark.createDataFrame(pandasDF.astype(str)) 
from pyspark.sql.types import StructType,StructField, StringType, IntegerType
mySchema = StructType([ StructField("First Name", StringType(), True)\
                       ,StructField("Age", IntegerType(), True)])

sparkDF2 = spark.createDataFrame(pandasDF,schema=mySchema)
sparkDF2.printSchema()
sparkDF2.show()


spark.conf.set("spark.sql.execution.arrow.enabled","true")
spark.conf.set("spark.sql.execution.arrow.pyspark.fallback.enabled","true")

pandasDF2=sparkDF2.select("*").toPandas
print(pandasDF2)


test=spark.conf.get("spark.sql.execution.arrow.enabled")
print(test)

test123=spark.conf.get("spark.sql.execution.arrow.pyspark.fallback.enabled")
print(test123)

'''
spark.sql.execution.arrow.enabled is a configuration option in Apache Spark that determines whether Arrow-based optimization should be enabled or not. Arrow is an in-memory columnar data format that can be used to accelerate data transfer between Spark and Pandas, a popular data manipulation library in Python.

When spark.sql.execution.arrow.enabled is set to true, it means that Spark will attempt to use Arrow to optimize certain operations, such as data exchange between Spark and Pandas when executing SQL queries.
'''