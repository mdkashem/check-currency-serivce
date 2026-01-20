# check-currency-serivce

Simple Python service to check and validate currency/exchange-rate information.

## Features

- Query and validate currency rates
- Lightweight service skeleton for integrations

## Requirements

- Python 3.8+
- (Optional) `requirements.txt` in the project root for dependencies

## Setup

Create and activate a virtual environment, then install dependencies if present:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
# source venv/bin/activate
pip install -r requirements.txt
```

## Running

Start the service using your project entrypoint (example):

```bash
python main.py
```

Replace `main.py` with the actual entrypoint for this project if different.

## Contributing

Contributions are welcome. Open an issue first to discuss significant changes.

## License

Add a license file or header as appropriate for your project.

## Run the API (development)

Create and activate a virtual environment, install dependencies, then start the FastAPI app:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
# source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

The API will be available at http://127.0.0.1:8000 and the automatic docs at http://127.0.0.1:8000/docs
