FROM python:3.9-slim-buster

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libffi-dev \
    && apt-get clean

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . . 

ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5001

CMD ["flask", "run"]