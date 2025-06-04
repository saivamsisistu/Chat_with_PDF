# AI Agent Project

This is an AI agent project that uses LangChain and OpenAI to create an intelligent agent capable of performing various tasks.

## Setup Instructions

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Unix/MacOS:
     ```bash
     source venv/bin/activate
     ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Copy `.env.example` to `.env` and fill in your API keys:
   ```bash
   cp .env.example .env
   ```

## Project Structure

```
.
├── README.md
├── requirements.txt
├── .env
├── src/
│   ├── __init__.py
│   ├── agent/
│   │   ├── __init__.py
│   │   └── base_agent.py
│   ├── tools/
│   │   ├── __init__.py
│   │   └── base_tools.py
│   └── config/
│       ├── __init__.py
│       └── settings.py
└── tests/
    └── __init__.py
```

## Features

- Modular agent architecture
- Extensible tool system
- Environment-based configuration
- Easy to customize and extend

## Usage

[Usage instructions will be added as the project develops]

## Contributing

Feel free to open issues and pull requests to improve the project.

## License

MIT License 