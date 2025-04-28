FROM python:3.10-slim-buster
ADD . /smartapp
WORKDIR /smartapp 
RUN pip install --no-cache-dir -r requirements.txt 
CMD ["python3", main.py"]
