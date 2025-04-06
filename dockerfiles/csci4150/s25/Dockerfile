FROM ubuntu:22.04

RUN apt-get update 

RUN apt-get install python3.10 pip -y

RUN pip install numpy==2.2.4 matplotlib==3.10.1

RUN pip install torch==2.6.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
