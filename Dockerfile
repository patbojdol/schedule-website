FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1

# Create app directory
RUN mkdir -p /app
WORKDIR /app

# Install poetry
RUN pip install poetry gunicorn

# Copy pipfile and install dependencies
COPY poetry.lock pyproject.toml /app/
RUN poetry export -f requirements.txt -o requirements.txt && pip install -r requirements.txt

# Copy app code
COPY . /app/

# Run the server
EXPOSE 8000
CMD ["gunicorn", "-b 0.0.0.0:8000", "main:app"]