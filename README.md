# Text Dataset Fetcher & Cleaner

A lightweight, dependency-minimal Python script to ingest a text dataset, pass it through a data preprocessing pipeline, and export the output into a clean CSV format.

## Features
- **Lowercasing**: Standardizes all text to avoid case-sensitive duplicate tokens.
- **Punctuation Removal**: Filters out special characters and punctuation marks using regex boundaries.
- **Tokenization**: Isolates individual words dynamically.
- **Stopword Removal**: Strips out high-frequency words (e.g., "the", "and", "is") that do not carry semantic weight.

## Prerequisites
You only need **Pandas** installed. Everything else utilizes Python's built-in libraries.

```bash
pip install pandas

# nlp-text-cleaner
A lightweight Python pipeline to ingest, clean, and tokenize text datasets into CSV format using Pandas and Regex.
