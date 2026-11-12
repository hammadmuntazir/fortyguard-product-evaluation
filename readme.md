# FortyGuard Product Evaluation

A hands-on technical evaluation of the FortyGuard Temperature Dashboard, Temperature API, and Temperature MCP as part of the Data Engineering Internship application process.

## Products Evaluated

- Temperature Dashboard
- Temperature API
- FortyGuard Temperature MCP

## 1. API Testing

I used Python and the Requests library to interact with the FortyGuard Temperature API.

The testing workflow included:

- Configuring API authentication using environment variables.
- Submitting a heatmap request for a selected geographical polygon.
- Handling asynchronous processing through status polling.
- Retrieving and saving the completed JSON response.
- Inspecting the returned GeoJSON FeatureCollection.

## 2. Data Validation

I developed a separate Python script to inspect and validate the API response.

The validation covered:

- Total number of returned features.
- Presence of required properties.
- Missing average-temperature values.
- Minimum, average, and maximum temperature consistency.
- Independent calculation of the mean and comparison with the API result.

### Validation Results

| Check | Result |
|---|---|
| Total features | 66 |
| Required properties | Passed |
| Missing average temperatures | 0 |
| Invalid temperature ranges | 0 |
| Mean validation | Passed |
| Overall validation | Passed |

These checks verified the internal consistency of the returned data, not its real-world temperature accuracy.

## 3. MCP Evaluation

I used MCP Inspector CLI to connect to the remote FortyGuard MCP server.

The evaluation included:

- Remote connection using HTTP transport.
- Bearer authentication.
- Discovery of available MCP tools.
- Execution of the read-only `credit_balance` tool.
- Strict input-schema validation.

The live server exposed 11 tools. Strict schema validation reported zero errors and one warning concerning the `tiles` parameter of the `satellite` tool.

No credit-consuming MCP operations were executed.

## 4. Project Structure

```text
fortyguard_api_evaluation/
├── api_test.py
├── inspect_result.py
├── requirements.txt
├── .gitignore
├── README.md
└── screenshots/
```

## 5. Requirements

- Python
- requests
- python-dotenv

Install dependencies:

```bash
pip install -r requirements.txt
```

## 6. Security

The API key is stored locally in an environment file and is not included in this repository.

## 7. Purpose

This project documents my practical exploration of API integration, asynchronous data processing, GeoJSON inspection, Python-based data validation, and MCP tool discovery.
