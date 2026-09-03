#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bulk-create GitHub issues for OpenSource-Hunt.

Usage:
    python create_issues.py              # reads token from env GH_TOKEN
    python create_issues.py <your-token> # pass token as CLI argument
    python create_issues.py --dry-run    # preview issues without creating
"""

import os
import sys
import json

if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer)
    sys.stderr = codecs.getwriter("utf-8")(sys.stderr.buffer)

REPO = "Jaswanth-Kumar-2007/OpenSource-Hunt"
API_URL = f"https://api.github.com/repos/{REPO}/issues"

ISSUES = []
ISSUES.append({
    "title": "[Easy] Fix typo in HTML title: 'OpenLke' -> 'OpenLake'",
    "body": "## Description\n\nThe `<title>` tag in `index.html` line 12 currently reads `OpenLke`,\nwhich is a typo for `OpenLake`.\n\n## File & Line\n\n`index.html:12`\n\n## Labels\n\n`documentation` `good first issue` `easy`",
    "labels": ["good first issue", "beginner friendly", "documentation", "easy"],
})
ISSUES.append({
    "title": "[Easy] Fix typo in hero heading: 'OpenLak' -> 'OpenLake'",
    "body": "## Description\n\nThe hero section heading in `index.html` line 370 says `Explore OpenLak Projects`.\nOpenLak is a typo for OpenLake.\n\n## File & Line\n\n`index.html:370`\n\n## Labels\n\n`documentation` `good first issue` `easy`",
    "labels": ["good first issue", "beginner friendly", "documentation", "easy"],
})
ISSUES.append({
    "title": "[Easy] Fix typo in footer: 'Learn' -> 'Learn'",
    "body": "## Description\n\nThe footer text in `index.html` line 492 currently reads:\n\n```\nBuild. Learn. Contribute.\n```\n\n***Learn*** is a typo for ***Learn***.",
    "labels": ["good first issue", "beginner friendly", "documentation", "easy"],
})
ISSUES.append({
    "title": "[Easy] Fix CSS typo: 'backgound' -> 'background' in button-secondary:hover",
    "body": "## Description\n\nIn the CSS for `.button-secondary:hover`, there is a typo `backgound`\nwhich should be `background`. This means the hover background color\nis never applied.\n\n## File & Line\n\n`index.html` \u2014 `.button-secondary:hover` CSS rule\n\n## Labels\n\n`bug` `css` `good first issue` `easy`",
    "labels": ["good first issue", "beginner friendly", "bug", "css", "easy"],
})
ISSUES.append({
    "title": "[Easy] Fix CSS typo: 'backgroundcolr' -> 'background-color' in .hero",
    "body": "## Description\n\nIn the CSS for `.hero`, the property is written as `backgroundcolr`\nwhich is not a valid CSS property. It should be `background-color`.\n\n## File & Line\n\n`index.html` \u2014 `.hero` CSS rule\n\n## Labels\n\n`bug` `css` `good first issue` `easy`",
    "labels": ["good first issue", "beginner friendly", "bug", "css", "easy"],
})
ISSUES.append({
    "title": "[Medium] Fix duplicate ID 'repo-count' in index.html",
    "body": "## Description\n\nThe ID `repo-count` is used on two different elements in `index.html`:\n\n1. `<span class=\"stat-number\" id=\"repo-count\">` in the stats section\n2. `<h2 id=\"repo-count\">OpenLake</h2>` in the footer\n\nDuplicate IDs are invalid HTML and can cause JavaScript `getElementById`\nto return the wrong element.\n\n## Expected\n\nRemove the duplicate `id=\"repo-count\"` from the footer `<h2>`.\n\n## File & Line\n\n`index.html` \u2014 footer `<h2>` element\n\n## Labels\n\n`bug` `html` `accessibility` `medium`",
    "labels": ["bug", "html", "accessibility", "medium"],
})
ISSUES.append({
    "title": "[Easy] Fix incorrect ARIA role='list' on projects grid",
    "body": "## Description\n\nThe projects grid div has `role=\"list\"` added, but it is a CSS grid\ncontainer for cards, not a semantic list. Using `role=\"list\"` on a\nnon-list element can confuse screen readers and is invalid usage.\n\n## Expected\n\nRemove `role=\"list\"` from the `<div id=\"projects-grid\">` element.\n\n## File & Line\n\n`index.html` \u2014 `<div id=\"projects-grid\">` element\n\n## Labels\n\n`bug` `accessibility` `good first issue` `easy`",
    "labels": ["good first issue", "beginner friendly", "bug", "accessibility", "easy"],
})
ISSUES.append({
    "title": "[Easy] Fix broken GitHub link in footer (OpenLkae -> OpenLake)",
    "body": "## Description\n\nThe footer GitHub link in `index.html` points to `https://github.com/OpenLkae`\n(typo: **OpenLkae** should be **OpenLake**).\n\n## File & Line\n\n`index.html` \u2014 footer GitHub link\n\n## Labels\n\n`bug` `documentation` `good first issue` `easy`",
    "labels": ["good first issue", "beginner friendly", "bug", "documentation", "easy"],
})
ISSUES.append({
    "title": "[Easy] Fix 'View GitHub' button missing classes and target attribute",
    "body": "## Description\n\nThe 'View GitHub' button in the hero section lost its\n`class=\"button button-secondary\"` and `target=\"_blank\"` attributes.\n\n## Expected\n\nRestore both attributes so the button is styled and opens in a new tab.\n\n## File & Line\n\n`index.html` \u2014 hero `.button-secondary` link\n\n## Labels\n\n`bug` `html` `good first issue` `easy`",
    "labels": ["good first issue", "beginner friendly", "bug", "html", "easy"],
})
ISSUES.append({
    "title": "[Medium] Add escapeHTML() calls for XSS prevention in createRepositoryCard",
    "body": "## Description\n\nIn `index.html`, the `createRepositoryCard()` function renders `repo.name`\nand `description` into HTML without calling `escapeHTML()`. Since these values\ncome from the GitHub API, they could contain malicious HTML \u2014 an XSS vulnerability.\n\n## Expected\n\nWrap both values with `escapeHTML()`:\n\n```javascript\n${escapeHTML(repo.name)}\n${escapeHTML(description)}\n```\n\n## File & Line\n\n`index.html` \u2014 `createRepositoryCard()` function\n\n## Labels\n\n`bug` `security` `xss` `medium`",
    "labels": ["bug", "security", "xss", "medium"],
})
ISSUES.append({
    "title": "[Easy] Fix repository sort: ascending -> descending by star count",
    "body": "## Description\n\nRepositories in `index.html` are sorted in **ascending** order by\nstargazers count (least popular first). The ternary comparison is also\nunnecessarily complex.\n\n## Expected\n\nSort in **descending** order so the most starred projects appear first:\n\n```javascript\nrepositories.sort(\n  (a, b) => b.stargazers_count - a.stargazers_count\n);\n```\n\n## File & Line\n\n`index.html:556-560`\n\n## Labels\n\n`bug` `javascript` `good first issue` `easy`",
    "labels": ["good first issue", "beginner friendly", "bug", "javascript", "easy"],
})
ISSUES.append({
    "title": "[Easy] Fix search input event: 'change' -> 'input'",
    "body": "## Description\n\nThe search input in `index.html` listens for the `change` event,\nwhich only fires when the input loses focus. For a live search\nexperience, it should listen for the `input` event (fires on every keystroke).\n\n## File & Line\n\n`index.html` \u2014 `searchInput.addEventListener(...)`\n\n## Labels\n\n`bug` `javascript` `good first issue` `easy`",
    "labels": ["good first issue", "beginner friendly", "bug", "javascript", "easy"],
})
ISSUES.append({
    "title": "[Bug] display_stats() prints total_stars for Total Forks",
    "body": "## Description\n\nIn `contributor_stats.py` line 76, the Total Forks line incorrectly prints\n`stats['total_stars']` instead of `stats['total_forks']`.\n\n## Expected\n\nTotal Forks should display `stats['total_forks']`.\n\n## File & Line\n\n`contributor_stats.py:76`\n\n## Labels\n\n`bug` `good first issue` `easy`",
    "labels": ["good first issue", "beginner friendly", "bug", "easy"],
})
ISSUES.append({
    "title": "[Bug] Languages sorted ascending instead of descending",
    "body": "## Description\n\nIn `contributor_stats.py`, `display_stats()` sorts languages by count\nin ascending order (least-used first). It should be descending.\n\n## Expected\n\nAdd `reverse=True` to the `sorted()` call.\n\n## File & Line\n\n`contributor_stats.py:81-84`\n\n## Labels\n\n`bug` `good first issue` `easy`",
    "labels": ["good first issue", "beginner friendly", "bug", "easy"],
})
ISSUES.append({
    "title": "[Bug] Top contributors sorted by username, not contribution count",
    "body": "## Description\n\n`get_top_contributors()` sorts by `x[0]` (username) instead of\n`x[1]` (contribution count), with `reverse=False`.\n\n## Expected\n\n```python\nsorted_contributors = sorted(\n    contributor_map.items(),\n    key=lambda x: x[1],\n    reverse=True\n)\n```\n\n## File & Line\n\n`contributor_stats.py:105-109`\n\n## Labels\n\n`bug` `good first issue` `easy`",
    "labels": ["good first issue", "beginner friendly", "bug", "easy"],
})
ISSUES.append({
    "title": "[Bug] Off-by-one in get_top_contributors return value",
    "body": "## Description\n\nLine 111 slices with `[:top_n - 1]`, returning one fewer\ncontributor than requested. For example, `--top 5` returns only 4.\n\n## Expected\n\n```python\nreturn sorted_contributors[:top_n]\n```\n\n## File & Line\n\n`contributor_stats.py:111`\n\n## Labels\n\n`bug` `good first issue` `easy`",
    "labels": ["good first issue", "beginner friendly", "bug", "easy"],
})
ISSUES.append({
    "title": "[Bug] --top flag crashes with IndexError if no value provided",
    "body": "## Description\n\nLines 141-143 do not validate that a value follows `--top`:\n\n```python\nif \"--top\" in sys.argv:\n    top_index = sys.argv.index(\"--top\")\n    top_n = int(sys.argv[top_index + 1])  # crashes if --top is last arg\n```\n\n## Expected\n\nAdd a bounds check.\n\n## File & Line\n\n`contributor_stats.py:141-143`\n\n## Labels\n\n`bug` `medium`",
    "labels": ["bug", "medium"],
})
ISSUES.append({
    "title": "[Bug] Missing User-Agent header in GitHub API requests",
    "body": "## Description\n\nGitHub API requires a User-Agent header. `fetch_repos()` and\n`fetch_contributors()` don't include one, causing potential 403 errors.\n\n## Expected\n\nAdd `headers={\"User-Agent\": \"OpenSource-Hunt\"}` to all requests.\n\n## File & Line\n\n`contributor_stats.py:24`, `contributor_stats.py:36`\n\n## Labels\n\n`bug` `medium`",
    "labels": ["bug", "medium"],
})
ISSUES.append({
    "title": "[Cleanup] Remove unused 'import json' from contributor_stats.py",
    "body": "## Description\n\nLine 17 imports `json` but it is never used in the file.\n\n## Expected\n\nRemove the unused import.\n\n## File & Line\n\n`contributor_stats.py:17`\n\n## Labels\n\n`cleanup` `good first issue` `easy`",
    "labels": ["good first issue", "beginner friendly", "cleanup", "easy"],
})
ISSUES.append({
    "title": "[Bug] org_name hardcoded instead of using command-line argument",
    "body": "## Description\n\nIn `main()`, `org_name` is hardcoded to `\"OpenLake\"` instead of\nreading from `sys.argv[1]`. The command-line argument is silently ignored.\n\n## Expected\n\n```python\norg_name = sys.argv[1]\n```\n\n## File & Line\n\n`contributor_stats.py:138`\n\n## Labels\n\n`bug` `medium`",
    "labels": ["bug", "medium"],
})
ISSUES.append({
    "title": "[Cleanup] calculate_stats() parameter shadows built-in 'dict'",
    "body": "## Description\n\nLine 44 renames the `repos` parameter to `dict`, shadowing the\nPython built-in type. This is bad practice and can cause subtle bugs.\n\n## Expected\n\nRename back to `repos`.\n\n## File & Line\n\n`contributor_stats.py:44`\n\n## Labels\n\n`cleanup` `code-quality` `good first issue` `easy`",
    "labels": ["good first issue", "beginner friendly", "cleanup", "code-quality", "easy"],
})
ISSUES.append({
    "title": "[Easy] Fix typo in README: 'About Opeake' -> 'About OpenLake'",
    "body": "## Description\n\nIn `README.md` line 19, the section heading reads `## About Opeake`\n(typo).",
    "labels": ["good first issue", "beginner friendly", "documentation", "easy"],
})
ISSUES.append({
    "title": "[Easy] Fix broken website URL in README",
    "body": "## Description\n\n`README.md` line 27: `https://opene.in/` should be `https://openlake.in/`.",
    "labels": ["good first issue", "beginner friendly", "documentation", "easy"],
})
ISSUES.append({
    "title": "[Easy] Fix broken GitHub URL in README",
    "body": "## Description\n\n`README.md` line 28: `https://git.com/OpenLake` should be\n`https://github.com/OpenLake`.",
    "labels": ["good first issue", "beginner friendly", "documentation", "easy"],
})
ISSUES.append({
    "title": "[Easy] Add missing Instagram URL in README",
    "body": "## Description\n\n`README.md` lines 347-348: Instagram line has no URL value.",
    "labels": ["good first issue", "beginner friendly", "documentation", "easy"],
})
ISSUES.append({
    "title": "[Bug] marks.py: calculate_total() adds 10 extra points",
    "body": "## Description\n\n`calculate_total()` line 7 returns `total + 10` instead of just `total`.",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] marks.py: is_passed() uses > instead of >= for 40% pass mark",
    "body": "## Description\n\n`is_passed()` line 18 checks `percentage > 40` instead of `>= 40`.",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] calculator.py: add() and subtract() return swapped results",
    "body": "## Description\n\n`add()` returns `a - b`, `subtract()` returns `a + b`.",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] calculator.py: Menu choices 2 and 3 call wrong functions",
    "body": "## Description\n\nChoice '2' (Subtract) calls multiply(); choice '3' (Multiply) calls subtract().",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] conditions.py: Age check logic is reversed",
    "body": "## Description\n\n`age >= 18` prints 'You are a child' instead of 'You are an adult'.",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] conditions.py: Grade labels are wrong (marks>=90 shows 'Grade B')",
    "body": "## Description\n\n`marks >= 90` prints Grade B instead of Grade A; `marks >= 75` prints Grade A instead of Grade B.",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] conditions.py: Temperature check logic is reversed",
    "body": "## Description\n\n`temperature > 25` prints 'It is cold' instead of 'It is hot'.",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] temperature.py: C-to-F formula uses minus instead of plus",
    "body": "## Description\n\nLine 2: `celsius * 9 / 5 - 32` should be `celsius * 9 / 5 + 32`.",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] loops.py: Loop prints wrong index (i+1 instead of i)",
    "body": "## Description\n\nLine 2: `print(\"Number:\", i + 1)` prints 2-6 instead of 1-5.",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] loops.py: Even/odd check is reversed",
    "body": "## Description\n\nLines 5-6: `i % 2 == 1` checks for odd but message says 'Even number'.",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] loops.py: Countdown range has wrong step (1 instead of -1)",
    "body": "## Description\n\nLine 8: `range(5, 0, 1)` produces empty sequence. Should be `range(5, 0, -1)`.",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] operators.py: All arithmetic operations and print vars are swapped",
    "body": "## Description\n\nAll operations are wrong (+/-//*/:// vs -/+/*/:/%) AND all print\nstatements reference the wrong variables.",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] variables.py: student_city set to country name 'India'",
    "body": "## Description\n\nLine 11: `student_city = \"India\"` \u2014 India is a country, not a city.",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] strings.py: Print statements use wrong variables",
    "body": "## Description\n\nLines 5-7: name/city/country variables are mismatched in print statements.",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] strings.py: .lower() and .upper() are swapped in print labels",
    "body": "## Description\n\nLines 9-10: 'Uppercase' calls .lower(), 'Lowercase' calls .upper().",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] strings.py: Wrong index for first/last character",
    "body": "## Description\n\nLines 12-13: `name[1]` for first char (should be `name[0]`), `name[0]` for last char (should be `name[-1]`).",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] strings.py: len(), startswith(), endswith() check wrong things",
    "body": "## Description\n\nLine 15: `len(city)` for name length; Line 17: `startswith(\"B\")` for 'Starts with T'; Line 18: `endswith(\"a\")` for 'Ends with n'.",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] prime.py: is_prime() incorrectly returns True for 1",
    "body": "## Description\n\nLines 2-3: `if number == 1: return True` \u2014 1 is NOT a prime number.",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] number_utils.py: is_even() checks for odd instead of even",
    "body": "## Description\n\nLine 2: `return number % 2 == 1` returns True for odd numbers.",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] number_utils.py: find_max() and find_min() comparisons are swapped",
    "body": "## Description\n\n`find_max()` uses `<` (finds minimum), `find_min()` uses `>` (finds maximum).",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] date_utils.py: is_leap_year() doesn't handle century years",
    "body": "## Description\n\nOnly checks `year % 4 == 0`, missing the century-year rules\n(divisible by 400 = leap; divisible by 100 = not leap).",
    "labels": ["bug", "python", "medium"],
})
ISSUES.append({
    "title": "[Bug] date_utils.py: days_in_month() ignores leap year for February",
    "body": "## Description\n\nAlways returns 28 for February. Should return 29 in leap years.",
    "labels": ["bug", "python", "medium"],
})
ISSUES.append({
    "title": "[Bug] expense.py: filter_by_category() returns opposite of intended results",
    "body": "## Description\n\nLine 22 uses `!=` instead of `==`, so it returns expenses that DON'T\nmatch the requested category.",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] shopping.py: calculate_total() adds discount instead of subtracting",
    "body": "## Description\n\nLine 23: `return subtotal + discount` \u2014 discount should be SUBTRACTED.",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] student.py: calculate_average() adds 5 to every average",
    "body": "## Description\n\nLine 5: `return sum(marks) / len(marks) + 5` \u2014 the `+ 5` inflates every average.",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] input_output.py: Print statements use wrong variables",
    "body": "## Description\n\nLines 5-11: every print statement references the wrong variable\n(name, age, city, country are mismatched).",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] input_output.py: age + 1 crashes with TypeError (string concatenation)",
    "body": "## Description\n\nLine 13: `age + 1` where age is a string from input() causes TypeError.",
    "labels": ["good first issue", "beginner friendly", "bug", "python", "easy"],
})
ISSUES.append({
    "title": "[Bug] passowrd.py: is_valid_password() skips uppercase and special char checks",
    "body": "## Description\n\n`has_uppercase()` and `has_special_character()` are defined but\nnever called inside `is_valid_password()`.",
    "labels": ["bug", "python", "medium"],
})
ISSUES.append({
    "title": "[Cleanup] Rename passowrd.py -> password.py (filename typo)",
    "body": "## Description\n\nThe file is named `passowrd.py` \u2014 'password' is misspelled.",
    "labels": ["good first issue", "beginner friendly", "cleanup", "easy"],
})
ISSUES.append({
    "title": "[Docs] Complete the incomplete CONTRIBUTING.md",
    "body": "## Description\n\n`CONTRIBUTING.md` ends abruptly at line 56. Steps 5-9 are missing.",
    "labels": ["documentation", "medium"],
})
ISSUES.append({
    "title": "[Enhancement] Add requirements.txt for Python dependencies",
    "body": "## Description\n\nThe project uses `requests` but has no `requirements.txt`.",
    "labels": ["enhancement", "good first issue", "easy"],
})

def create_issues(token, dry_run=False):
    import requests

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "OpenSource-Hunt-issue-creator",
    }

    created = 0
    skipped = 0

    for issue in ISSUES:
        payload = {
            "title": issue["title"],
            "body": issue["body"],
            "labels": issue["labels"],
        }

        if dry_run:
            print(f"[DRY-RUN] {issue['title']}  labels={issue['labels']}")
            skipped += 1
            continue

        resp = requests.post(API_URL, headers=headers, json=payload)

        if resp.status_code == 201:
            created += 1
            print(f"[OK] {issue['title']}")
        elif resp.status_code == 422:
            skipped += 1
            print(f"[SKIP] {issue['title']} (duplicate)")
        else:
            print(f"[FAIL] {resp.status_code} — {issue['title']}")

    print(f"\n{'='*50}")
    print(f"Total issues: {len(ISSUES)}")
    print(f"Created:      {created}")
    print(f"Skipped/dry:  {skipped}")
    print(f"{'='*50}")


if __name__ == "__main__":
    token = os.environ.get("GH_TOKEN", "")

    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "--dry-run":
            create_issues(token, dry_run=True)
            sys.exit(0)
        token = arg

    if not token:
        print("Usage: python create_issues.py <github-token>")
        print("   or: set GH_TOKEN env var then run python create_issues.py")
        print("Get a token at: https://github.com/settings/tokens")
        sys.exit(1)

    print(f"Creating issues in {REPO}...\n")
    create_issues(token)
