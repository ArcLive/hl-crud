FROM python:3

ADD hl-crud.py /

RUN pip3 install -r requirements.txt

CMD [ "python3", "./hl-crud.py" ]