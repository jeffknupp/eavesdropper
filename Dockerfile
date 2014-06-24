FROM ubuntu:14.04
MAINTAINER Jeff Knupp <jknupp@appnexus.com>
 
# Install pip, etc.

RUN apt-get install -yqq python-setuptools python-dev
RUN apt-get install -yqq postgresql-server-dev-all
RUN easy_install pip

ADD . /src
ADD requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
