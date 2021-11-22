FROM ubuntu:latest

# Grab dependencies
RUN apt update && apt upgrade -y && apt install -y python3 python3-pip

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN python3 -m pip install -r requirements.txt

ENTRYPOINT [ "python3", "-m", "client" ]