FROM python:3.10.12

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY app .

# install app-specific dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install python-telegram-bot[job-queue]

# app command
CMD ["python", "-u", "./main.py"]
