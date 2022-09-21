FROM jupyter/scipy-notebook

# COPY requirements.txt /app/requirements.txt

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN python3 inference.py