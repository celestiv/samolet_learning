FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /var/app
COPY requirements.txt ./
COPY myapp ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
