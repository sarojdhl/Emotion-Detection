FROM python:3.6.4

EXPOSE 5000

WORKDIR /app

ADD . /app



RUN pip install -r requirements.txt

RUN python -m nltk.downloader stopwords


CMD ["python","app.py"]