---
category: general
scraped_at: '2025-11-12T14:10:23.884526'
title: Transform transcripts into tests
url: /docs/transcripts-to-test
---

# Transform transcripts into tests

## Overview

Convert a Voiceflow transcript into a reusable [test case](/tests/tests).

## Command

Bash

```
voiceflow transcript to-test [flags]
```

## Parameters

### Required flags

* `--agent-id`: Voiceflow Agent ID
* `--transcript-id`: ID of the transcript to convert

### Optional flags

* `--output-file`: Path to save the generated test (default: test.yaml)
* `--test-name`: Name for the generated test
* `--test-description`: Description for the generated test

## Examples

### Basic usage

Bash

```
voiceflow transcript to-test \
  --agent-id your-agent-id \
  --transcript-id transcript-123
```

### Full example with options

Bash

```
voiceflow transcript to-test \
  --agent-id your-agent-id \
  --transcript-id transcript-123 \
  --output-file my-test.yaml \
  --test-name "Payment Flow Test" \
  --test-description "Validates the payment processing dialogue"
```

## Output

The command generates a YAML file containing:

* Test metadata (name, description)
* User interactions
* Expected agent responses
* Validation rules

Updated 5 months ago

---

[Fetching transcripts](/docs/fetching)[Agent](/docs/agent)

Ask AI

* [Table of Contents](#)
* + [Overview](#overview)
  + [Command](#command)
  + [Parameters](#parameters)
  + - [Required flags](#required-flags)
    - [Optional flags](#optional-flags)
  + [Examples](#examples)
  + - [Basic usage](#basic-usage)
    - [Full example with options](#full-example-with-options)
  + [Output](#output)