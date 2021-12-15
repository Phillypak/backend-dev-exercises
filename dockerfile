#################
# Attempt at containerizing
#################

FROM python:3.11.0a3-bullseye

WORKDIR /Users/yousaf/documents/rticodeinterview/backend-dev-exercises

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY / .

CMD ["python", "app.py"]

