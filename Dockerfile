
FROM index.alauda.cn/lennyleng/flask-base

MAINTAINER Lenny Leng <admin@lennyleng.com>

RUN apt-get update
RUN apt-get install -y freetds-dev

RUN pip install pymssql
copy app /var/www/app
