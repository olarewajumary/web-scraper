import argparse
import os
from src.scraper import get_jobs, save_jobs, display_summary


def main():
    parser = argparse.ArgumentParser(
        description="🌐 Web Scraper — Scrape remote job listings and store structured data"
    )

    parser.add_argument(
        "--keyword",
        type=str,
        required=True,
        help="Job keyword to search (e.g. python, data-science, machine-learning)"
    )

    parser.add_argument(
        "--location",
        type=str,
        default="remote",
        help="Job location (default: remote)"
    )

    parser.add_argument(
        "--save",
        action="store_true",
        help="Save scraped jobs to a CSV file in the data folder"
    )

    parser.add_argument(
        "--summary",
        action="store_true",
        help="Display a summary of scraped jobs"
    )

    args = parser.parse_args()

    # Make sure data folder exists
    os.makedirs("data", exist_ok=True)

    # Run the scraper
    df = get_jobs(args.keyword, args.location)

    if args.summary:
        display_summary(df)

    if args.save:
        output_path = f"data/{args.keyword}_jobs.csv"
        save_jobs(df, output_path)

    print("\n🎉 Done! Your job listings are ready.\n")


if __name__ == "__main__":
    main()