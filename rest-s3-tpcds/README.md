# Iceberg REST Catalog + S3 + TPC-DS

This setup is designed to run Iceberg with REST catalog, S3 storage, and TPC-DS data.

To use this setup, follow these steps:

```shell
docker compose up
```

It will:

- Start the s3 storage supported by minio
- Start the simple Iceberg REST catalog
- Generate the TPC-DS data and load it into the catalog
- Start the spark query engine

This service will expose

- Iceberg REST catalog at `rest.local:8181`
- Minio S3 service at `minio.local:9000` and `warehouse.minio.local:9000`

To perform some spark tasks inside this service, run:

```shell
docker compose run -it --entrypoint=bash spark-iceberg
```
