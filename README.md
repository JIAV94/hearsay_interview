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
cd hearsay_interview


3. Build and run the Docker container:
docker-compose up --build


The application will be accessible at `http://localhost:8000/api/sortkeys`.

## Testing the API

Use `curl`, Postman to send a POST request to `http://localhost:8000/api/sortkeys` with the appropriate JSON payload.
Or you can input the json data directly on the GUI provided by DRF directly on a web browser using the same URI `http://localhost:8000/api/sortkeys`.

Example `curl` command:

`curl -X POST http://localhost:8000/sort/
-H "Content-Type: application/json"
-d '{"sortKeys": ["fruits", "numbers"], "payload": {"fruits": ["watermelon", "apple", "pineapple"], "numbers": [1333, 4, 2431, 7], "colors": ["green", "blue", "yellow"]}}'`
