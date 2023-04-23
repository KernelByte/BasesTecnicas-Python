FROM python:3.9

WORKDIR /app_dataset
COPY requeriments.txt /app_dataset/requeriments.txt

RUN pip install --no-cache-dir --upgrade -r /app_dataset/requeriments

COPY  . app_dataset/

CMD bash -c "while true; do sleep 1; done"