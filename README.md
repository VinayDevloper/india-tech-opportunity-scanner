# India Tech Opportunity Scanner

A small Python CLI tool that scans technology-related news and detects potential tech opportunities.

## Features

- Calls NewsAPI using Python requests
- Fetches latest tech/startup/AI news
- Filters signals like:
  - AI
  - startups
  - robotics
  - semiconductor
  - automation
- Prints structured opportunity signals in terminal

## Tech Used

- Python
- Requests library
- Public News API

## Example Output

1. Netflix is buying Ben Affleck’s AI startup
2. Nvidia investing billions in AI chips
3. Robotics startup raises funding

## Run

Set API key:

PowerShell:

$env:NEWS_API_KEY="your_key"

Then run:

python opportunity_scanner.py