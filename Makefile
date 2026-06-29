.PHONY: build run stop clean

build:
	docker build -t docker-calendario .

run:
	docker run -d -p 5000:5000 --name docker-calendario docker-calendario

stop:
	docker stop docker-calendario || true
	docker rm docker-calendario || true

clean: stop
	docker rmi docker-calendario || true