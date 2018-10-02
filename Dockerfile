
FROM python:3.6-alpine

COPY requirements.txt /
RUN pip install -r /requirements.txt

# Define Python required libraries in requirements.txt
# Copy requirements file into the Docker image
#COPY requirements.txt /tmp/requirements.txt

WORKDIR /app

COPY lib/phyml-alpine lib/phyml
COPY lib/small.aP6.phy tmp/small.phy
COPY lib/big.channa.phy /tmp/big.phy

COPY logme.py logme.py


#CMD [ "python", "-u", "vai.py" ] unbuffered
ENTRYPOINT [ "python3", "logme.py" ]
CMD [ "Ref::phyfilepath" ]
