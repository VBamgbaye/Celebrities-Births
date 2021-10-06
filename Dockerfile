FROM python:3.8-slim-buster

RUN apt-get -y update

#Copy files
COPY . /src

# Install requirements in requirement file
RUN pip install -r ./src/Youtube_scrapper.egg-info/requires.txt
RUN pip install Youtube-scrapper==0.0.5

CMD ["python", "./src/youtube_scrapper"]