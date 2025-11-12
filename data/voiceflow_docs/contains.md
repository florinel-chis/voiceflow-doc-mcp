---
category: general
scraped_at: '2025-11-12T14:10:03.324519'
title: Interaction-Based Examples
url: /docs/contains
---

# Interaction-Based Examples

# Example using `contains` validation

## Suite file

YAML

```
# suite.yaml

name: Example Suite
description: Suite used as an example
environmentName: production
tests:
  - id: test_id
    file: ./test.yaml
```

## Test file

YAML

```
# test.yaml

name: Example test
description: These are some tests
interactions:
  - id: test_1
    user: 
      type: text
      text: hi
    agent:
      validate:
        - type: contains
          value: hello
```

  

YAML

```
# test.yaml

name: Example test
description: These are some tests
interactions:
  - id: test_1
    user: 
      type: text
      text: hi
    agent:
      validate:
        - type: contains
          value: hello
```

Updated 4 months ago

---

[Interaction-Based Tests Reference](/docs/tests)[Agent-to-Agent Tests Reference](/docs/agent-to-agent-tests)

Ask AI

* [Table of Contents](#)
* + [Example using contains validation](#example-using-contains-validation)
  + - [Suite file](#suite-file)
    - [Test file](#test-file)