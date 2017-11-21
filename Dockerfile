FROM ubuntu:16.04


COPY ./ /home/

RUN apt-get update; \
    apt-get install -y python3 python3-pip python3-tk;

RUN pip3 install -r /home/requirements.txt

EXPOSE 8080

CMD python3 /home/manage.py runserver 0.0.0.0:8080