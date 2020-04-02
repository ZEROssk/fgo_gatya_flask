FROM python:3.6

RUN pip install Flask && \
	pip install numpy

ADD ./ /

CMD ["python", "fgoflask.py"]
