FROM python:3.10.5-slim-buster
RUN pip install Django==3.1.8
RUN pip install djangorestframework==3.12.2
RUN pip install djangorestframework-simplejwt==4.6.0
RUN pip install httpie