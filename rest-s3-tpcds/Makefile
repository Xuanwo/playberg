
up:
	docker-compose up -d minio mc rest spark-iceberg meta query jupyter

up-lakekeeper: up
	docker-compose up -d lakekeeper initiallakekeeperwarehouse

down:
	docker-compose down
