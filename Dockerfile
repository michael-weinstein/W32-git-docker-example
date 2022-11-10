FROM python:3.11.0

RUN apt update

COPY requirements.txt /opt/

RUN pip3 install -r /opt/requirements.txt

RUN mkdir /opt/rps

COPY *.py /opt/rps/

COPY rpsSupport/ /opt/rps/rpsSupport

EXPOSE 44444

CMD ["python3", "/opt/rps/web.py"]