---
category: general
scraped_at: '2025-11-12T14:10:31.533521'
title: API Endpoints
url: /docs/api-endpoints
---

# API Endpoints

## Health Check

HTTP

```
GET /health
```

Returns the health status of the server.

## Execute Test Suite

HTTP

```
POST /api/v1/tests/execute
Content-Type: application/json

{
  "api_key": "your_api_key (optional)",
  "voiceflow_subdomain": "your_custom_subdomain (optional)",
  "suite": {
    "name": "Example Suite",
    "description": "Suite used as an example",
    "environment_name": "production",
    "tests": [
      {
        "id": "test_1",
        "test": {
          "name": "Example test",
          "description": "These are some tests",
          "interactions": [
            {
              "id": "test_1_1",
              "user": {
                "type": "text",
                "text": "hi"
              },
              "agent": {
                "validate": [
                  {
                    "type": "contains",
                    "value": "hello"
                  }
                ]
              }
            }
          ]
        }
      }
    ]
  }
}
```

**Response:**

JSON

```
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "status": "running",
  "started_at": "2023-01-01T00:00:00Z",
  "logs": ["Test execution started"]
}
```

Executes a test suite asynchronously and returns an execution ID for tracking. The suite configuration and tests are now embedded directly in the request body, making the API more HTTP-friendly and eliminating the need for file system access.

### Request Parameters

* `api_key` (optional): Override the global Voiceflow API key for this specific test execution
* `voiceflow_subdomain` (optional): Override the global Voiceflow subdomain for this specific test execution. This allows you to test against different Voiceflow environments or custom subdomains without affecting the global configuration
* `suite`: The test suite configuration containing the test definitions

### Using Custom Subdomains

When you specify a `voiceflow_subdomain`, the API will use that subdomain for all interactions in the test suite. For example:

* If you set `"voiceflow_subdomain": "my-custom-env"`, requests will be sent to `https://general-runtime.my-custom-env.voiceflow.com`
* If you omit this field, the global subdomain configuration will be used
* This is particularly useful for testing against staging environments or customer-specific deployments

## Get Test Status

HTTP

```
GET /api/v1/tests/status/{execution_id}
```

**Response:**

JSON

```
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "status": "completed",
  "started_at": "2023-01-01T00:00:00Z",
  "completed_at": "2023-01-01T00:05:00Z",
  "logs": [
    "Starting test suite execution...",
    "Running Test ID: example_test",
    "Test suite execution completed successfully"
  ]
}
```

Retrieves the current status and logs of a test execution.

## System Information

HTTP

```
GET /api/v1/system/info
```

**Response:**

JSON

```
{
  "version": "1.0.0",
  "go_version": "go1.20.0",
  "os": "linux",
  "arch": "amd64"
}
```

Returns system information about the running server instance.

## OpenAPI/Swagger Documentation

Once the server is running, you can access the interactive API documentation at:

```
http://localhost:8080/swagger/index.html
```

  

```
http://localhost:8080/swagger/index.html
```

Updated 4 months ago

---

[API Server](/docs/api-serve)[Security & Troubleshooting](/docs/security-troubleshooting)

Ask AI

* [Table of Contents](#)
* + [Health Check](#health-check)
  + [Execute Test Suite](#execute-test-suite)
  + - [Request Parameters](#request-parameters)
    - [Using Custom Subdomains](#using-custom-subdomains)
  + [Get Test Status](#get-test-status)
  + [System Information](#system-information)
  + [OpenAPI/Swagger Documentation](#openapiswagger-documentation)