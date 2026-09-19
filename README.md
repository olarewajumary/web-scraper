# Web Scraper: Remote Job Listings

A Python web scraper that collects real-time remote job listings 
and stores them as structured CSV data, ready for analysis.

---

## Features

- Fetches live remote job listings from Remotive API
- Searches by any keyword (python, data-science, machine-learning)
- Displays top hiring companies
- Shows most in-demand skills and tags
- Saves structured job data to CSV
- Clean summary report in the terminal

---

## Tech Stack

- Python 3.x
- Requests
- BeautifulSoup4
- Pandas

---

## Project Structure

```
web-scraper/
├── main.py           # CLI entry point
├── src/
│   └── scraper.py      # API calls, summarizing, saving
└── requirements.txt
```

## Usage

```
python main.py --keyword python --summary --save
```

- `--keyword` (required): job keyword to search (e.g. python, data-science, machine-learning)
- `--location`: job location filter (defaults to "remote")
- `--summary`: prints top hiring companies and most common skills/tags
- `--save`: saves the results to `data/<keyword>_jobs.csv`

## Running it yourself

```
git clone https://github.com/olarewajumary/web-scraper
cd web-scraper
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py --keyword python --summary --save
```