FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .


# Expose the port on which the app will run
EXPOSE 8000

# Define the command to run the application using Gunicorn
# CMD ["gunicorn", "-b", "0.0.0.0:8000", "application:app"]

CMD flask db upgrade && gunicorn --bind 0.0.0.0:8000 "application:app"
