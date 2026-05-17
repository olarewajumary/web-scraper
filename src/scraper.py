import requests
import pandas as pd
import time


def get_jobs(keyword, location="remote"):
    """Scrape job listings from Remotive public API."""
    print(f"\n🔍 Searching for '{keyword}' jobs...")

    url = f"https://remotive.com/api/remote-jobs?search={keyword}&limit=20&job_type=full_time"

    try:
        response = requests.get(url, timeout=10)
        print(f"   ✅ Connected to Remotive (status: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Connection failed: {e}")
        return pd.DataFrame()

    data = response.json()
    job_list = data.get("jobs", [])
    print(f"   ✅ Found {len(job_list)} job listings")

    jobs = []

    for job in job_list:
        try:
            jobs.append({
                "title": job.get("title", "N/A"),
                "company": job.get("company_name", "N/A"),
                "location": job.get("candidate_required_location", "Remote"),
                "tags": ", ".join(job.get("tags", [])[:5]),
                "date_posted": job.get("publication_date", "N/A")[:10],
                "url": job.get("url", "N/A")
            })
        except Exception:
            continue

        time.sleep(0.05)

    df = pd.DataFrame(jobs)
    return df


def save_jobs(df, output_path):
    """Save scraped jobs to a CSV file."""
    if df.empty:
        print("\n⚠️  No jobs to save.")
        return

    df.to_csv(output_path, index=False)
    print(f"\n💾 Jobs saved to: {output_path}")


def display_summary(df):
    """Print a summary of scraped jobs."""
    if df.empty:
        print("\n⚠️  No jobs found.")
        return

    print("\n" + "="*50)
    print("📋 SCRAPING SUMMARY")
    print("="*50)
    print(f"\n🔹 Total Jobs Found: {len(df)}")

    print(f"\n🔹 Top Companies Hiring:")
    top_companies = df["company"].value_counts().head(5)
    for company, count in top_companies.items():
        print(f"   {company}: {count} opening(s)")

    print(f"\n🔹 Most Common Skills/Tags:")
    all_tags = ", ".join(df["tags"].dropna().tolist())
    tag_list = [t.strip() for t in all_tags.split(",") if t.strip()]
    tag_series = pd.Series(tag_list).value_counts().head(8)
    for tag, count in tag_series.items():
        print(f"   {tag}: {count} listings")

    print(f"\n🔹 Sample Listings:")
    print(df[["title", "company", "location"]].head(5).to_string(index=False))
    print("="*50)