# Install python 3.9
FROM python:3.9-slim-buster

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

# Install TA-LIB C
COPY external/ta-lib-0.4.0-src.tar.gz /app/

RUN tar -xzf /app/ta-lib-0.4.0-src.tar.gz -C /app/

RUN cd /app/ta-lib && \
    ./configure && \
    make && \
    make install

RUN rm -rf /app/* && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt

# install pip requirements
RUN pip install -r requirements.txt

COPY . .

CMD ["python","-m", "src.mybot"]