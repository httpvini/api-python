FROM python:3-alpine

WORKDIR /app
COPY *.* /app/
RUN pip install connexion[swagger-ui] -t .
RUN pip install --no-cache-dir -r requirements.txt -t .

EXPOSE 5000
CMD [ "python3", "serverstarter.py" ]
