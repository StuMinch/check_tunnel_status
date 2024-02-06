FROM python:latest
WORKDIR /workdir
RUN pip3 install pytest pytest-xdist selenium requests