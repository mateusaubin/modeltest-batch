
FROM python:3.6

COPY requirements.txt /
RUN pip install -r /requirements.txt

# Define Python required libraries in requirements.txt
# Copy requirements file into the Docker image
#COPY requirements.txt /tmp/requirements.txt

WORKDIR /app

COPY lib/phyml lib/phyml
COPY lib/small.aP6.phy tmp/small.aP6.phy

COPY logme.py logme.py


#CMD [ "python", "-u", "vai.py" ] unbuffered
ENTRYPOINT [ "python3", "logme.py" ]
CMD [ "Ref::phyfilepath" ]
