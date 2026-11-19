name: Archive public pages

on:
  workflow_dispatch:
    inputs:
      start_url:
        description: Public category or thread URL to start from
        required: true
        type: string
      max_pages:
        description: Maximum pages to fetch in this run
        required: true
        default: "100"
        type: string

permissions:
  contents: write

jobs:
  archive:
    runs-on: ubuntu-latest
    timeout-minutes: 360

    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: python -m pip install requests beautifulsoup4

      - name: Run crawler
        run: |
          python archive.py "${{ inputs.start_url }}" \
            --repo "$GITHUB_WORKSPACE" \
            --max-pages "${{ inputs.max_pages }}" \
            --chunk-size 10 \
            --delay 3

