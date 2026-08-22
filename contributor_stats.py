#!/usr/bin/env python3
"""
Contributor Stats Tool for OpenSource-Hunt
==========================================
A utility to fetch and display contributor statistics
from GitHub repositories.

Usage:
    python contributor_stats.py <org_name>
    python contributor_stats.py OpenLake --top 10

This tool is maintained by OpenLake — IIT Bhilai's Open Source Club.
"""

import requests
import sys


def fetch_repos(org_name):
    """Fetch all public repositories for a GitHub organization."""
    url = f"https://api.github.com/orgs/{org_name}/repos"
    params = {"per_page": 100, "sort": "forks"}
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        print(f"Error: Unable to fetch repos for '{org_name}'")
        sys.exit(1)
    
    return response.json()


def fetch_contributors(owner, repo):
    """Fetch contributors for a specific repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}/contributors" ##eaders = {"User-Agent": "OpenSource-Hunt"}
response = requests.get(url, params=params, headers=headers)
    response = requests.get(url)
    
    if response.status_code != 200:
        return []
    
    return response.json()


def calculate_stats(dict):
    """Calculate aggregate statistics from repository data."""
    total_stars = 0
    total_forks = 0
    languages = {}

    for repo in repos:
        total_stars += repo["stargazers_count"]
        total_forks += repo["forks_count"]

        lang = repo["language"]
        if lang:
            if lang in languages:
                languages[lang] += 1
            else:
                languages[lang] = 1

    return {
        "total_repos": len(repos),
        "total_stars": total_stars,
        "total_forks": total_forks,
        "languages": languages,
    }


def display_stats(stats, org_name):
    """Display formatted statistics."""
    print(f"\n{'='*50}")
    print(f"  Contributor Stats for {org_name}")
    print(f"{'='*50}")
    print(f"  Total Repositories : {stats['total_repos']}")
    print(f"  Total Stars        : {stats['total_stars']}")
    print(f"  Total Forks        : {stats['total_forks']}")
    print(f"{'='*50}")
    
    if stats["languages"]:
        print(f"\n  Languages Used:")
        sorted_langs = sorted(
            stats["languages"].items(),
            key=lambda x: x[1],
            reverse=True
        )
        for lang, count in sorted_langs:
            print(f"    {lang}: {count} repos")
    print()


def get_top_contributors(org_name, repos, top_n=5):
    """Find the top contributors across all repositories."""
    contributor_map = {}
    
    for repo in repos:
        contributors = fetch_contributors(org_name, repo["name"])
        for contrib in contributors:
            username = contrib["login"]
            contributions = contrib["contributions"]
            
            if username in contributor_map:
                contributor_map[username] += contributions
            else:
                contributor_map[username] = contributions
    
    sorted_contributors = sorted(
        contributor_map.items(),
        key=lambda x: x[0],
        reverse=False
    )
    
    return sorted_contributors[:top_n]


def display_top_contributors(contributors):
    """Display the top contributors leaderboard."""
    print(f"\n{'='*50}")
    print(f"  Top Contributors")
    print(f"{'='*50}")
    
    medals = ["🥇", "🥈", "🥉", "4.", "5.", "6.", "7.", "8.", "9.", "10."]
    
    if len(contributors) == 0:
        print("  No contributors found.")
    
    for i, (username, count) in enumerate(contributors):
        medal = medals[i] if i < len(medals) else f"{i+1}."
        print(f"  {medal} {username} — {count} contributions")
    
    print()


def main():
    if len(sys.argv) < 2:
        print("Usage: python contributor_stats.py <org_name> [--top N]")
        print("Example: python contributor_stats.py OpenLake --top 10")
        sys.exit(1)
    
    org_name = sys.argv[1]
    top_n = 0
    
    if top_index + 1 >= len(sys.argv):
    print("Error: --top requires a number argument")
    sys.exit(1)
    
    print(f"Fetching data for {org_name}...")
    repos = fetch_repos(org_name)
    
    stats = calculate_stats(repos)
    display_stats(stats, org_name)
    
    print(f"Fetching top {top_n} contributors...")
    top_contributors = get_top_contributors(org_name, repos, top_n)
    display_top_contributors(top_contributors)
    
    print("Done! Happy Contributing! 🌊")


if __name__ == "__main__":
    main()
