FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
ADD wait-for-mysql.sh /tmp/
ADD wait_for_mysql.py /tmp/

RUN pip install -r requirements.txt

ADD . /app/

CMD [ "sh", "/tmp/wait-for-mysql.sh", "db", "3306", "root", "hlcrud" ]