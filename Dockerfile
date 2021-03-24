FROM ubuntu:20.04

COPY . /app
WORKDIR /app

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends software-properties-common \
    && add-apt-repository -y ppa:deadsnakes \
    && apt-get install -y --no-install-recommends python3.8-dev python3-pip wget \
    && pip3 install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "covid_cajamar.app.main:app", "--host", "0.0.0.0", "--port", "80"]