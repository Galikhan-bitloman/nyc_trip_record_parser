from pyspark.sql import SparkSession



def insert_data(path: str):
    spark = SparkSession.builder.appName("nyc_trip_record").config("spark.jars.packages", "org.postgresql:postgresql:42.7.2").getOrCreate()
    df_parquet = spark.read.parquet(path)

    # Display the data and schema
    df_parquet.show(5)
    df_parquet.printSchema()

    (df_parquet.write.format("jdbc")
     .option("url", "jdbc:postgresql://localhost:5432/postgres")
     .option("dbtable", "hvfhv_trips")
     .option("driver", "org.postgresql.Driver")
     .option("user", "postgres")
     .option("password", "postgres")
     .mode("append")
     .save())

    #create dataframe