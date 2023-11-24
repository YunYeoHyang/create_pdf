all: docker-build docker-export

TAG=v1.0

docker-build:
	docker build -t k8s.createpdf.com/createpdf-service:$(TAG) .

docker-export:
	docker save -o dataset-service.tar k8s.createpdf.com/createpdf-service:$(TAG)

dep:
	pip install --no-cache-dir -U -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt


