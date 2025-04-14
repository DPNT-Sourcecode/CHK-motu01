FROM python:3.12-slim

# Install Java + tools
RUN apt-get update && \
    apt-get install -y default-jre curl unzip git && \
    apt-get clean

WORKDIR /app
COPY . .

# Install Python requirements
RUN pip install --no-cache-dir -r requirements.txt

CMD ["/bin/bash"]
