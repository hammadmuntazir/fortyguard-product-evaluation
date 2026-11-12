# FortyGuard Product Evaluation

A hands-on technical evaluation of the FortyGuard Temperature Dashboard, Temperature API, and Temperature MCP as part of the Data Engineering Internship application process.

## Products Evaluated

- Temperature Dashboard
- Temperature API
- FortyGuard Temperature MCP

## 1. Dashboard Evaluation

Explored the interactive temperature heatmap, visualization modes, time-series simulation, statistical summaries, layer controls, and environmental parameters.

## 2. API Testing

Used Python and the Requests library to:

- Configure API authentication using environment variables.
- Submit a heatmap request for a geographical polygon.
- Handle asynchronous processing through status polling.
- Retrieve and save the completed GeoJSON response.
- Inspect the returned data.

## 3. Data Validation

Developed a Python script to validate the API response.

| Validation Check | Result |
|---|---|
| Total features | 66 |
| Required properties | Passed |
| Missing average temperatures | 0 |
| Invalid temperature ranges | 0 |
| Independent mean validation | Passed |
| Overall validation | Passed |

These checks verified the internal consistency of the returned data, not its real-world temperature accuracy.

## 4. MCP Evaluation

Used MCP Inspector CLI to connect to the remote FortyGuard MCP server.

Testing included:

- Remote connection using HTTP transport.
- Bearer authentication.
- Discovery of 11 available tools.
- Execution of the read-only `credit_balance` tool.
- Strict input-schema validation.

Schema validation reported zero errors and one warning concerning the `tiles` parameter of the `satellite` tool.

No credit-consuming MCP operations were executed.

## 5. Project Structure

```text
fortyguard_api_evaluation/
├── api_test.py
├── inspect_result.py
├── requirements.txt
├── .gitignore
├── README.md
├── screenshots/
│   ├── api-validation.png
│   ├── mcp-tools-list.png
│   └── mcp-schema-validation.png
└── results/
    └── sample-response.json
```

## 6. Requirements

- Python
- requests
- python-dotenv

Install dependencies:

```bash
pip install -r requirements.txt
```

## 7. Security

API credentials are stored locally in an environment file and are not included in this repository.

## 8. Purpose

This evaluation demonstrates practical exploration of API integration, asynchronous data processing, GeoJSON inspection, Python-based data validation, dashboard usability, and MCP tool discovery.
