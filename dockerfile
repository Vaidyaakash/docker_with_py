FROM python:3.11.0rc2-bullseye
WORKDIR /
COPY . .
# ADD . /new
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 4545
CMD [ "python", "main.py" ]