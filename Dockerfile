FROM python:3.6.4


WORKDIR /app

ADD . /app



RUN pip install -r requirement.txt

RUN python -m nltk.downloader stopwords


CMD ["python","app.py"]

