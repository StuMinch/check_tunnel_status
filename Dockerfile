FROM python:latest
COPY . /opt
ADD . /opt
RUN pip3 install pytest pytest-xdist selenium requests Appium-Python-Client