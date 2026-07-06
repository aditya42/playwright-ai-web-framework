# Playwright AI Web Framework - Python

Python Playwright framework with Page Object Model, Pytest, AI helper agents, HTML reports, CI workflow, and sample web automation tests.

## Tech Stack

- Python 3.10+
- Playwright Python
- Pytest
- Pytest HTML reports
- AI agent layer for self-healing locators, test case generation, and defect summaries
- GitHub Actions CI

## Folder Structure

```text
playwright-ai-web-framework/
├── .github/workflows/python-playwright-tests.yml
├── config/config.py
├── src/
│   ├── ai_agents/
│   │   ├── base_agent.py
│   │   ├── self_healing_locator_agent.py
│   │   ├── test_case_generator_agent.py
│   │   └── defect_summary_agent.py
│   ├── core/browser_manager.py
│   └── utils/logger.py
├── tests/
│   ├── conftest.py
│   ├── fixtures/
│   │   └── saucedemo_mock.html
│   ├── pages/
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── products_page.py
│   │   └── cart_page.py
│   └── specs/
│       ├── test_login.py
│       ├── test_cart.py
│       └── test_ai_self_healing.py
├── reports/
├── requirements.txt
├── pyproject.toml
├── pytest.ini
└── README.md
```

## Sample Test Coverage

The framework automates SauceDemo-like ecommerce flows against a local mock app by default, so tests can run without external internet. Set `BASE_URL=https://www.saucedemo.com` to run against the public SauceDemo site when your network allows it.

1. Valid login
2. Invalid login validation
3. Add product to cart
4. AI self-healing locator fallback for login button

## Setup

```bash
git clone <your-repo-url>
cd playwright-ai-web-framework
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
# .venv\Scripts\activate    # Windows
pip install -r requirements.txt
playwright install chromium
cp .env.example .env
```

## Run Tests

Run all tests:

```bash
pytest
```

If Playwright browser download is blocked but system Chromium is already installed, run:

```bash
CHROMIUM_EXECUTABLE_PATH=/usr/bin/chromium pytest
```

Run smoke tests:

```bash
pytest -m smoke
```

Run regression tests:

```bash
pytest -m regression
```

Run AI-agent tests:

```bash
pytest -m ai
```

Run with browser visible:

```bash
HEADLESS=false pytest
```

Run in parallel:

```bash
pytest -n 2
```

## Report

After execution, open:

```text
reports/report.html
```

## AI Agents Included

### SelfHealingLocatorAgent
Tries the primary selector first. If it fails, it uses fallback selectors. This is useful when UI locators change.

### TestCaseGeneratorAgent
Converts feature acceptance criteria into test scenario titles.

### DefectSummaryAgent
Generates a triage-friendly failure summary using test name, URL, and error message.

## GitHub Actions

The workflow runs on:

- Pull request to `main`
- Push to `main`
- Manual trigger from GitHub Actions

It installs dependencies, installs Chromium, runs Pytest, and uploads the HTML report artifact.
