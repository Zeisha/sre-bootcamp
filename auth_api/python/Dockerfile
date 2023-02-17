FROM python:3.9-alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
# App must run on port 8000
ENTRYPOINT [ "gunicorn","-b", "0.0.0.0:8000", "api:app"]
