import duckdb
import os
from pyspark.sql import SparkSession

# Use duckdb to generate data and export to data dir
conn = duckdb.connect()
conn.sql("CALL dsdgen(sf = 1)")
conn.sql("EXPORT DATABASE 'tcpds_data' (FORMAT PARQUET)")
print(f"Successfully generated TPC-DS data by duckdb")

# Use spark to insert data as iceberg tables
spark = SparkSession.builder.appName("ParquetToIceberg").getOrCreate()

iceberg_warehouse = "s3://warehouse"
parquet_dir = "/home/iceberg/tcpds_data"

files = [f for f in os.listdir(parquet_dir) if f.endswith(".parquet")]
print(f"Found {files}")

for file_name in files:
    try:
        table_name = file_name.replace(".parquet", "")
        file_path = os.path.join(parquet_dir, file_name)

        create_table_query = f"""
            CREATE OR REPLACE TABLE demo.tpcds.{table_name}
            USING iceberg
            LOCATION '{iceberg_warehouse}/{table_name}'
            AS SELECT * FROM parquet.`{file_path}`
        """

        spark.sql(create_table_query)
        print(f"Successfully created table demo.tpcds.{table_name}")

    except Exception as e:
        print(f"Error processing {file_name}: {str(e)}")

spark.stop()
