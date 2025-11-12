---
category: general
scraped_at: '2025-11-12T14:11:09.232081'
title: Test Suites
url: /docs/test-suites
---

# Test Suites

![](https://files.readme.io/bb062b2db3db9553b36a632643f176f7b8f92fe350e528f17500e13b23467ba6-test-suites.png)
  

## Overview

Test Suites are the core building blocks of your Voiceflow testing workflow. They define collections of tests that validate your agents against expected behaviors and responses.

## What is a Test Suite?

A Test Suite is a JSON-formatted definition that contains:

* **Test Configuration**: API keys, environment settings, and Voiceflow project details
* **Test Cases**: Individual test scenarios with user inputs and expected agent responses
* **Validation Rules**: Criteria for determining test success or failure

## Creating Test Suites

  

### Method 1: From a template

![](https://files.readme.io/42575e6d8ac4dade3b548d09e12e2d5df985c2f01ba0e1a118e28168fda07960-image.png)
  

### Method 2: Visual Builder

![](https://files.readme.io/1c7bee790cb903dc667f7db8bd1e054a07e0d279c9c68ac10fe18b73069e9e8d-image.png)
  
  

### Method 3: Import YAML Files

![](https://files.readme.io/3de26c424fa50521bf997fff37205b8819a90fdc705ce8e25d12dcb2f682b40a-yaml-import.png)
  

1. Navigate to **Test Suites** → **"Create New Suite"**
2. Choose the **"Import YAML Files"** tab
3. Upload your files:
   * **Suite File**: Your main `suite.yaml` file
   * **Test Files**: All referenced test YAML files
4. The system automatically converts YAML to JSON format
5. Review the imported data before saving

#### Supported File Structure

##### Required Files

The YAML import feature expects the standard Voiceflow CLI file structure:

###### Suite File (suite.yaml or suite.yml)

Individual test case files referenced in the suite. You can find more details on the [Suite Reference](/docs/automated-testing#/) page.

###### Test Files (individual .yaml/.yml files)

Individual test case files referenced in the suite. You can find more details on the [Test Reference](/docs/automated-testing#/) page.

  

### Method 4: Manual Entry

![](https://files.readme.io/c5d478abfb76f6674ce76fea01927f91b7e885252f3e260adaf798a2d28716ce-test-suite-detail.png)

1. Navigate to **Test Suites** in the sidebar
2. Click **"Create New Suite"**
3. Choose the **"Manual Entry"** tab
4. Fill in the required information:
   * **Suite Name**: A descriptive name for your test suite
   * **Voiceflow API Key**: Your Voiceflow project API key (format: VF.*****.*****)
   * **Voiceflow Subdomain** (Optional): For private cloud customers
   * **JSON Definition**: The complete test definition in JSON format

## Managing Test Suites

### Viewing Your Test Suites

* **Suite List**: All your test suites are displayed as cards with key information
* **Last Updated**: See when each suite was last modified
* **Quick Actions**: Run, edit, duplicate, or delete suites directly from the list

### Suite Actions

* **Run Test**: Execute the test suite immediately
* **Edit**: Modify the suite configuration and test definitions
* **Duplicate**: Create a copy of an existing suite for modification
* **Delete**: Permanently remove a test suite (requires confirmation)

### Test Suite Structure

Your JSON definition should include:

JSON

```
{
  "api_key": "VF.xxxxx.xxxxx",
  "suite": {
    "name": "Main Conversation Flow Tests",
    "description": "Tests for primary user interactions",
    "environment_name": "production",
    "tests": [
      {
        "id": "greeting_test",
        "test": {
          "name": "Greeting Test",
          "description": "Test the bot's greeting response",
          "interactions": [
            {
              "id": "greeting_interaction",
              "user": {
                "type": "text",
                "text": "Hello"
              },
              "agent": {
                "validate": [
                  {
                    "id": "greeting_validation",
                    "type": "exact_match",
                    "value": "Hello! How can I help you today?"
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

For more details on the JSON structure, refer to the [Test Suite JSON Schema](/reference/post_api-v1-tests-execute#/).

## API Integration

Test suites integrate with the Voiceflow API for execution:

* **Execution Endpoint**: Tests are submitted to the Voiceflow Dialog Manager API
* **Status Monitoring**: Real-time status updates during test execution
* **Results Retrieval**: Detailed logs and results are fetched after completion

## Validation Types

Your tests can use various validation methods:

* **Exact Match**: Response must exactly match expected text
* **Contains**: Response must contain specific text
* **Regex**: Response must match a regular expression pattern
* **Similarity**: Response must be semantically similar (AI-powered)
* **Variable Check**: Validate specific variables are set correctly

Updated 4 months ago

---

[Voiceflow Test Platform](/docs/voiceflow-test-platform)[Scheduled Tests](/docs/scheduled-tests)

Ask AI

* [Table of Contents](#)
* + [Overview](#overview)
  + [What is a Test Suite?](#what-is-a-test-suite)
  + [Creating Test Suites](#creating-test-suites)
  + - [Method 1: From a template](#method-1-from-a-template)
    - [Method 2: Visual Builder](#method-2-visual-builder)
    - [Method 3: Import YAML Files](#method-3-import-yaml-files)
    - [Method 4: Manual Entry](#method-4-manual-entry)
  + [Managing Test Suites](#managing-test-suites)
  + - [Viewing Your Test Suites](#viewing-your-test-suites)
    - [Suite Actions](#suite-actions)
    - [Test Suite Structure](#test-suite-structure)
  + [API Integration](#api-integration)
  + [Validation Types](#validation-types)