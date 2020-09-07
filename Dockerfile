FROM python:3
WORKDIR /home/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY read_nano.py .
ENTRYPOINT ["python", "read_nano.py"]