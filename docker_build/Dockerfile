# syntax=docker/dockerfile:1
FROM python:3
ADD ./app /
RUN pip install scrapy
RUN pip install pymongo

CMD ["bash", "./reddit/run.sh"]

