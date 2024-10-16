Installing Playwright (Python)

https://playwright.dev/python/docs/intro

pip install pytest-playwright
Install the required browsers:playwright install

Update playwright command: pip install pytest-playwright playwright -U

extra parameters:
--headed: Run tests in headed mode (default: headless).
--browser: Run tests in a different browser chromium, firefox, or webkit. It can be specified multiple times (default: chromium).
--browser-channel Browser channel to be used.
--slowmo Slows down Playwright operations by the specified amount of milliseconds. Useful so that you can see what is going on (default: 0).
--device Device to be emulated.
--output Directory for artifacts produced by tests (default: test-results).
--tracing Whether to record a trace for each test. on, off, or retain-on-failure (default: off).
--video Whether to record video for each test. on, off, or retain-on-failure (default: off).
--screenshot Whether to automatically capture a screenshot after each test. on, off, or only-on-failure (default: off).
--full-page-screenshot Whether to take a full page screenshot on failure. By default, only the viewport is captured. Requires --screenshot to be enabled (default: off).

Install reports
https://www.way2automation.com/generate-html-report-using-playwright-python/

pip install pytest-html​​

run it with report:
pytest -s -v --headed --html=pwreport1.htm



Playwright inspector
Use the codegen command to run the test generator followed by the URL of the website you want to generate tests for. The URL is optional and you can always run the command without it and then add the URL directly into the browser window instead.

playwright codegen demo.playwright.dev/todomvc
