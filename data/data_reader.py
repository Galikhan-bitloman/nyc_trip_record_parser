from pyspark.sql import SparkSession



def read_data(path: str):
    spark = SparkSession.builder.appName("nyc_trip_record").getOrCreate()
    df_parquet = spark.read.parquet(path)

    # Display the data and schema
    df_parquet.show(5)
    df_parquet.printSchema()

    #create dataframe