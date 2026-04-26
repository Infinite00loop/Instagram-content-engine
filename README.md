# Instagram Content Engine

Welcome to the Instagram Content Engine, powered by [crewAI](https://crewai.com). This project demonstrates how to orchestrate a multi-agent AI system to conduct market intelligence, devise digital strategies, craft compelling copy, and generate image prompts for social media campaigns.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system.

1. Install `uv` if you haven't already:
```bash
pip install uv
```

2. Install the project dependencies:
```bash
uv sync
```

3. Configure your environment variables:
Create a `.env` file from the example and add your API keys. You will need:
- `GEMINI_API_KEY`
- `SERPER_API_KEY` (for web search)
- `BROWSERLESS_API_KEY` (for web scraping)

## Running the Content Engine

To execute the crew and generate your social media assets, run the following command from the root of your project:

```bash
uv run python main.py
```

This will trigger the crew to perform market research on your target product, analyze competitors, develop a campaign strategy, draft social media copy, and generate a visual moodboard/image prompt.
