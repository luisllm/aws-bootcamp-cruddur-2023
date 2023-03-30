FROM 632758144135.dkr.ecr.eu-west-1.amazonaws.com/cruddur-python:3.10-slim-buster
#test with gitpod
#FROM python:3.10-slim-buster

WORKDIR /backend-flask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

#test with gitpod
#ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

EXPOSE ${PORT}
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]
#RUN chmod +x start-flask.sh
#ENTRYPOINT ["./start-flask.sh"]