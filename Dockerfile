FROM python:3.10.5

COPY requirements.txt ./
RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN pip install -r requirements.txt
RUN pip install confluent-kafka
COPY . .

CMD [ "python", "./servidor.py" ]
