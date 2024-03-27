FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /code
COPY . /code/

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
