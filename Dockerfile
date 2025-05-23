FROM python:3.10-slim-buster
ADD . /smartapp
WORKDIR /smartapp
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=main.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
