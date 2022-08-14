FROM python:3.8-buster

COPY docker_env/sources.list /etc/apt/sources.list
COPY docker_env/pip.conf /etc/pip.conf
COPY . ./
EXPOSE 2022

RUN python -m pip install --upgrade pip
RUN pip install pip
RUN pip install -r requirements.txt

CMD ["python","main.py"]

