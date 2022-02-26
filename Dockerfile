FROM python:3.8
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV=/opt/venv
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install -r requirements.txt
COPY . /code/
ENTRYPOINT [ "python","manage.py","runserver","127.0.0.1:8000" ]