
FROM python:3.6

# Define Python required libraries in requirements.txt
# Copy requirements file into the Docker image
#COPY requirements.txt /tmp/requirements.txt

COPY logme.py logme.py

#CMD [ "python", "-u", "vai.py" ] unbuffered
CMD [ "./logme.py" ]