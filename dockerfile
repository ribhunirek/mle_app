FROM python:3.9

ADD requirements.txt /
RUN pip install -r requirements.txt

ADD templates /
ADD ads.json /
ADD database.db /
ADD schema.sql /
ADD init_db.py /
ADD app.py /
ADD run.sh /

EXPOSE 5000
RUN chmod +x /run.sh
CMD ["/run.sh"]