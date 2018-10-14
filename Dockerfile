
FROM python:3.6-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Define Python required libraries in requirements.txt
# Copy requirements file into the Docker image
#COPY requirements.txt /tmp/requirements.txt

COPY lib/phyml lib/phyml
#COPY lib/phyml-alpine lib/phyml-alpine
COPY lib/small.aP6.phy tmp/small.phy
COPY lib/big.channa.phy tmp/big.phy

COPY logme.py logme.py


#CMD [ "python", "-u", "vai.py" ] unbuffered
ENTRYPOINT [ "python3", "logme.py" ]
CMD [ "Ref::path". "Ref:cmd" ]
