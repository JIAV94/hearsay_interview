# HEARSAY README

## Overview

This application provides a RESTful API to sort keys from a JSON payload.

## Prerequisites

- Docker
- docker-compose

## Getting Started

1. Clone this repository:
https://github.com/JIAV94/hearsay_interview

2. Navigate to the project directory:
cd hearsay


3. Build and run the Docker container:
docker-compose up --build


The application will be accessible at `http://localhost:8000/`.

## Testing the API

Use `curl` or Postman to send a POST request to `http://localhost:8000/sort/` with the appropriate JSON payload.

Example `curl` command:

`curl -X POST http://localhost:8000/sort/
-H "Content-Type: application/json"
-d '{"sortKeys": ["fruits", "numbers"], "payload": {"fruits": ["watermelon", "apple", "pineapple"], "numbers": [1333, 4, 2431, 7], "colors": ["green", "blue", "yellow"]}}'`
