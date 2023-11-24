FROM python:3.9-slim

RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list \
    && sed -i 's/security.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list \
    && apt-get update  \
    && apt-get install -y --no-install-recommends apt-utils libgomp1

ADD . /app
WORKDIR /app

RUN pip install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt

CMD ["python","-W","ignore", "main.py"]
