FROM python:3.10

LABEL maintainer="Wachukwu Emmanuel"

# Working Directory
WORKDIR /app

COPY ./requirements.txt /app/

# Install packages from requirements.txt
RUN pip3 install --no-cache-dir --upgrade pip &&\
    pip3 install --no-cache-dir -r requirements.txt 

# Copy source code to working directory
COPY ./ /app/

# Expose container port
EXPOSE 5000

CMD [ "python3", "app.py" ]