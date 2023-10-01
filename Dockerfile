FROM python:3.10

# install dependencies of interest
RUN python -m pip install rasa
RUN python setup.py

WORKDIR /app
ENV HOME=/app
COPY . .

# train a new rasa model
RUN rasa train nlu

# set the user to run, don't run as root
USER 1001

# set entrypoint eg <default>: docker run -it subkamble/iac ["rasa"]
ENTRYPOINT ["rasa"]

CMD ["run", "--enable-api", "--port", "8080"]