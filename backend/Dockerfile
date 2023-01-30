FROM python:3.7
EXPOSE 8080
WORKDIR /app
COPY requirements.txt /app
RUN apt-get install libffi-dev
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8080"]
