#!/usr/bin/env python3
"""Generate static SVG widgets for a GitHub profile README.

No third-party widget service is involved at render time. The workflow queries the
GitHub API, writes SVGs into assets/widgets/, and commits them to the profile repo.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import math
import os
import re
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "assets" / "widgets"
OUT.mkdir(parents=True, exist_ok=True)

USERNAME = os.environ.get("GITHUB_USERNAME", "DebadityaHait")
TOKEN = os.environ.get("GITHUB_TOKEN", "")

REPOS = [
    {
        "slug": "tensorflow",
        "repo": "tensorflow/tensorflow",
        "pr": 124961,
        "title": "Avoid oneDNN abort for out-of-range convolution attributes",
    },
    {
        "slug": "pytorch",
        "repo": "pytorch/pytorch",
        "pr": 191831,
        "title": "Fix B018 warnings in symmetric-memory Triton hooks",
    },
    {
        "slug": "vite",
        "repo": "vitejs/vite",
        "pr": 22947,
        "title": "Map CSS chunks in chunk import maps",
    },
    {
        "slug": "pnpm",
        "repo": "pnpm/pnpm",
        "pr": 13059,
        "title": "Read git package names during resolution",
    },
    {
        "slug": "neovim",
        "repo": "neovim/neovim",
        "pr": 41067,
        "title": "Retain substitute confirmation highlight with nohlsearch",
    },
    {
        "slug": "redis",
        "repo": "redis/node-redis",
        "pr": 3388,
        "title": "Cap post-connect Redis Sentinel rediscovery retries",
    },
    {
        "slug": "rclone",
        "repo": "rclone/rclone",
        "pr": 9712,
        "title": "Propagate caller contexts to Dropbox SDK requests",
    },
    {
        "slug": "posthog",
        "repo": "PostHog/posthog",
        "pr": 70314,
        "title": "Configure sourcemap upload concurrency",
    },
]

THEMES = {
    "dark": {
        "bg": "#0d1117",
        "border": "#30363d",
        "text": "#f0f6fc",
        "muted": "#8b949e",
        "accent": "#58a6ff",
        "success": "#3fb950",
        "grid0": "#161b22",
        "grid": ["#0e4429", "#006d32", "#26a641", "#39d353"],
    },
    "light": {
        "bg": "#ffffff",
        "border": "#d0d7de",
        "text": "#1f2328",
        "muted": "#656d76",
        "accent": "#0969da",
        "success": "#1a7f37",
        "grid0": "#ebedf0",
        "grid": ["#9be9a8", "#40c463", "#30a14e", "#216e39"],
    },
}


def api_request(url: str, data: dict | None = None) -> dict:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": f"{USERNAME}-profile-widget-generator",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    body = None
    if data is not None:
        body = json.dumps(data).encode()
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode())


def fmt_num(n: int | None) -> str:
    if n is None:
        return "—"
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}m".replace(".0m", "m")
    if n >= 1_000:
        return f"{n / 1_000:.1f}k".replace(".0k", "k")
    return str(n)


def truncate(text: str, limit: int) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def svg_text(text: str) -> str:
    return html.escape(str(text), quote=True)


def write(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def repo_card(config: dict, meta: dict, theme_name: str) -> str:
    t = THEMES[theme_name]
    repo_name = config["repo"]
    language = meta.get("language") or "—"
    stars = fmt_num(meta.get("stargazers_count"))
    forks = fmt_num(meta.get("forks_count"))
    description = truncate(meta.get("description") or config["title"], 68)
    title = truncate(config["title"], 61)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="440" height="148" viewBox="0 0 440 148" role="img" aria-label="{svg_text(repo_name)} contribution card">
  <rect x="0.5" y="0.5" width="439" height="147" rx="10" fill="{t['bg']}" stroke="{t['border']}"/>
  <g font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif">
    <text x="18" y="29" font-size="16" font-weight="600" fill="{t['accent']}">{svg_text(repo_name)}</text>
    <text x="18" y="54" font-size="12" fill="{t['muted']}">{svg_text(description)}</text>
    <text x="18" y="83" font-size="12" fill="{t['text']}">★ {stars}</text>
    <text x="88" y="83" font-size="12" fill="{t['text']}">⑂ {forks}</text>
    <circle cx="164" cy="79" r="5" fill="{t['accent']}"/>
    <text x="176" y="83" font-size="12" fill="{t['muted']}">{svg_text(language)}</text>
    <line x1="18" y1="99" x2="422" y2="99" stroke="{t['border']}"/>
    <text x="18" y="120" font-size="12" font-weight="600" fill="{t['success']}">Merged PR #{config['pr']}</text>
    <text x="18" y="138" font-size="11" fill="{t['muted']}">{svg_text(title)}</text>
  </g>
</svg>'''


def stats_card(stats: dict, theme_name: str) -> str:
    t = THEMES[theme_name]
    metrics = [
        ("Contributions", fmt_num(stats.get("total_contributions"))),
        ("Commits", fmt_num(stats.get("commits"))),
        ("Pull requests", fmt_num(stats.get("prs"))),
        ("Issues", fmt_num(stats.get("issues"))),
        ("Contributed to", fmt_num(stats.get("contributed_repos"))),
        ("Followers", fmt_num(stats.get("followers"))),
    ]
    width, height = 900, 166
    cols = 3
    cell_w = width / cols
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="GitHub activity statistics">',
        f'<rect x="0.5" y="0.5" width="899" height="165" rx="10" fill="{t["bg"]}" stroke="{t["border"]}"/>',
        '<g font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif">',
        f'<text x="22" y="31" font-size="16" font-weight="600" fill="{t["text"]}">GitHub activity · last 12 months</text>',
        f'<text x="878" y="31" text-anchor="end" font-size="11" fill="{t["muted"]}">generated from GitHub API</text>',
    ]
    for idx, (label, value) in enumerate(metrics):
        row, col = divmod(idx, cols)
        x = 22 + col * cell_w
        y = 77 + row * 55
        parts += [
            f'<text x="{x:.0f}" y="{y:.0f}" font-size="22" font-weight="700" fill="{t["accent"]}">{svg_text(value)}</text>',
            f'<text x="{x:.0f}" y="{y+19:.0f}" font-size="11" fill="{t["muted"]}">{svg_text(label)}</text>',
        ]
    parts += ['</g>', '</svg>']
    return "\n".join(parts)


def contribution_calendar_svg(calendar: dict, theme_name: str) -> str:
    t = THEMES[theme_name]
    weeks = calendar.get("weeks") or []
    width, height = 900, 174
    start_x, start_y = 42, 53
    cell, gap = 11, 3
    positives = [d.get("contributionCount", 0) for w in weeks for d in w.get("contributionDays", []) if d.get("contributionCount", 0) > 0]
    positives.sort()
    if positives:
        q1 = positives[max(0, math.floor(len(positives) * 0.25) - 1)]
        q2 = positives[max(0, math.floor(len(positives) * 0.50) - 1)]
        q3 = positives[max(0, math.floor(len(positives) * 0.75) - 1)]
    else:
        q1 = q2 = q3 = 1

    def color_for(n: int) -> str:
        if n <= 0:
            return t["grid0"]
        if n <= q1:
            return t["grid"][0]
        if n <= q2:
            return t["grid"][1]
        if n <= q3:
            return t["grid"][2]
        return t["grid"][3]

    total = calendar.get("totalContributions")
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="GitHub contribution calendar">',
        f'<rect x="0.5" y="0.5" width="899" height="173" rx="10" fill="{t["bg"]}" stroke="{t["border"]}"/>',
        '<g font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif">',
        f'<text x="22" y="29" font-size="16" font-weight="600" fill="{t["text"]}">Contribution calendar</text>',
        f'<text x="878" y="29" text-anchor="end" font-size="11" fill="{t["muted"]}">{svg_text(fmt_num(total))} contributions</text>',
    ]
    # weekday labels
    for label, row in [("Mon", 1), ("Wed", 3), ("Fri", 5)]:
        y = start_y + row * (cell + gap) + 9
        parts.append(f'<text x="10" y="{y}" font-size="9" fill="{t["muted"]}">{label}</text>')

    max_cols = min(len(weeks), 58)
    for wi, week in enumerate(weeks[-max_cols:]):
        for day in week.get("contributionDays", []):
            row = int(day.get("weekday", 0))
            x = start_x + wi * (cell + gap)
            y = start_y + row * (cell + gap)
            count = int(day.get("contributionCount", 0))
            parts.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2" fill="{color_for(count)}"/>')

    legend_x = 750
    parts.append(f'<text x="{legend_x-34}" y="158" font-size="9" fill="{t["muted"]}">Less</text>')
    colors = [t["grid0"], *t["grid"]]
    for i, color in enumerate(colors):
        parts.append(f'<rect x="{legend_x + i*15}" y="149" width="11" height="11" rx="2" fill="{color}"/>')
    parts.append(f'<text x="{legend_x + 81}" y="158" font-size="9" fill="{t["muted"]}">More</text>')
    parts += ['</g>', '</svg>']
    return "\n".join(parts)


def fetch_repo_meta(repo: str) -> dict:
    return api_request(f"https://api.github.com/repos/{repo}")


def fetch_profile_stats() -> tuple[dict, dict]:
    now = dt.datetime.now(dt.timezone.utc)
    start = now - dt.timedelta(days=364)
    query = '''
query($login:String!, $from:DateTime!, $to:DateTime!) {
  user(login:$login) {
    followers { totalCount }
    repositories(privacy:PUBLIC, ownerAffiliations:OWNER) { totalCount }
    repositoriesContributedTo(
      first:1,
      includeUserRepositories:false,
      contributionTypes:[COMMIT, ISSUE, PULL_REQUEST, REPOSITORY]
    ) { totalCount }
    contributionsCollection(from:$from, to:$to) {
      totalCommitContributions
      totalPullRequestContributions
      totalIssueContributions
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            contributionCount
            date
            weekday
          }
        }
      }
    }
  }
}
'''
    payload = {
        "query": query,
        "variables": {
            "login": USERNAME,
            "from": start.isoformat(),
            "to": now.isoformat(),
        },
    }
    response = api_request("https://api.github.com/graphql", payload)
    if response.get("errors"):
        raise RuntimeError(response["errors"])
    user = response["data"]["user"]
    c = user["contributionsCollection"]
    calendar = c["contributionCalendar"]
    stats = {
        "total_contributions": calendar["totalContributions"],
        "commits": c["totalCommitContributions"],
        "prs": c["totalPullRequestContributions"],
        "issues": c["totalIssueContributions"],
        "contributed_repos": user["repositoriesContributedTo"]["totalCount"],
        "followers": user["followers"]["totalCount"],
        "public_repos": user["repositories"]["totalCount"],
    }
    return stats, calendar


def placeholder_repo_meta(config: dict) -> dict:
    return {
        "stargazers_count": None,
        "forks_count": None,
        "language": "updates daily",
        "description": config["title"],
    }


def placeholder_calendar() -> dict:
    weeks = []
    today = dt.date.today()
    start = today - dt.timedelta(days=364)
    # Align to Sunday for a GitHub-style week layout.
    start -= dt.timedelta(days=(start.weekday() + 1) % 7)
    cursor = start
    while cursor <= today:
        days = []
        for _ in range(7):
            days.append({
                "contributionCount": 0,
                "date": cursor.isoformat(),
                "weekday": (cursor.weekday() + 1) % 7,
            })
            cursor += dt.timedelta(days=1)
        weeks.append({"contributionDays": days})
    return {"totalContributions": None, "weeks": weeks}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--placeholder", action="store_true", help="Generate valid placeholder SVGs without network access")
    args = parser.parse_args()

    for config in REPOS:
        if args.placeholder:
            meta = placeholder_repo_meta(config)
        else:
            try:
                meta = fetch_repo_meta(config["repo"])
            except Exception as exc:
                print(f"warning: could not fetch {config['repo']}: {exc}")
                meta = placeholder_repo_meta(config)
        for theme_name in THEMES:
            write(OUT / f"repo-{config['slug']}-{theme_name}.svg", repo_card(config, meta, theme_name))

    if args.placeholder:
        stats = {
            "total_contributions": None,
            "commits": None,
            "prs": None,
            "issues": None,
            "contributed_repos": None,
            "followers": None,
        }
        calendar = placeholder_calendar()
    else:
        try:
            stats, calendar = fetch_profile_stats()
        except Exception as exc:
            print(f"warning: could not fetch profile GraphQL stats: {exc}")
            stats = {
                "total_contributions": None,
                "commits": None,
                "prs": None,
                "issues": None,
                "contributed_repos": None,
                "followers": None,
            }
            calendar = placeholder_calendar()

    for theme_name in THEMES:
        write(OUT / f"github-stats-{theme_name}.svg", stats_card(stats, theme_name))
        write(OUT / f"contribution-calendar-{theme_name}.svg", contribution_calendar_svg(calendar, theme_name))

    print(f"Generated widgets in {OUT}")


if __name__ == "__main__":
    main()
