FROM ubuntu:latest

RUN apt-get update -y

RUN apt-get install -y python-pip python-dev build-essential

ADD . /flask-app

WORKDIR /flask-app

RUN pwd

RUN ls

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]



