FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update
RUN apt install -y wget git unzip zip nano curl python3 python3-pip maven default-jdk figlet

RUN mkdir /repo
WORKDIR /repo
RUN git clone https://github.com/LiUGraphQL/LinGBM.git
WORKDIR /repo/LinGBM/tools/datasetgen

RUN mvn clean install

RUN mkdir /code
COPY ./ /code/

RUN mkdir /output

RUN python3 -m pip install -r /code/requirements.txt


CMD ["python3","/code/run.py"]
