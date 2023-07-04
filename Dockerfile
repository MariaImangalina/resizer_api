FROM python:3.9-alpine
ARG PIPENV_PARAMS=""
ENV PYTHONUNBUFFERED 1
RUN apk update
WORKDIR /resizer_api
COPY . ./
RUN pip install -r requirements.txt