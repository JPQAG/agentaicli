# AgentAiCli Lambda Function

This is a simple AWS Lambda function that returns a hello world message.

## Development Setup

### Prerequisites

- pyenv
- pipenv
- Python 3.9.0

### Setting up the development environment

1. Install Python 3.9.0 using pyenv:
```bash
pyenv install 3.9.0
```

2. Navigate to the project directory and let pyenv set the local Python version:
```bash
cd agentaicli
pyenv local 3.9.0
```

3. Install dependencies using pipenv:
```bash
pipenv install --dev
```

4. Activate the virtual environment:
```bash
pipenv shell
```

## Development

The main Lambda handler is in `app.py`. You can add additional dependencies to the `Pipfile` as needed.

## Testing

Run tests using pytest:
```bash
pipenv run pytest
``` 