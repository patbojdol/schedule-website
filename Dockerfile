FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1

# Create app directory
RUN mkdir -p /app
WORKDIR /app

# Install pipenv
RUN pip install pipenv gunicorn

# Copy pipfile and install dependencies
COPY Pipfile* /app/
RUN pipenv install --system

# Copy app code
COPY . /app/

# Run the server
EXPOSE 8000
CMD ["gunicorn", "-b 0.0.0.0:8000", "main:app"]