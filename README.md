# langchain-test

A test project for LangChain development with Anthropic Claude.

## Features

- LangChain agent with tool calling
- Custom weather tool example
- Uses Claude Sonnet 4.5 model

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up your Anthropic API key:
```bash
cp .env.example .env
# Edit .env and add your API key
```

Or export it directly:
```bash
export ANTHROPIC_API_KEY="your_api_key_here"
```

## Usage

Run the agent:
```bash
python agent.py
```

The agent will use the `get_weather` tool to answer weather-related questions.
