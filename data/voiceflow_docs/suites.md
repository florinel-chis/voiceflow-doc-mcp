---
category: general
scraped_at: '2025-11-12T14:09:59.672320'
title: Suite Reference
url: /docs/suites
---

# Suite Reference

## Reference

A suite is a yaml file with the following structure:

YAML

```
# suite.yaml

# Name of the suite.
name: Example Suite
# Brief description of the suite.
description: Suite used as an example
# Environment name of your Voiceflow agent. It could be development, or production.
environmentName: development
# You can have multiple tests defined in separated files
tests:
  # ID of the test.
  - id: test_id
    # File where the test specification is located
    file: ./test.yaml
```

It has the same structure as the NLU Profiler suite.

## JSON Schema

`voiceflow-cli` also has a [jsonschema](http://json-schema.org/draft/2020-12/json-schema-validation.html) file, which you can use to have better  
editor support:

Shell

```
https://voiceflow.xavidop.me/static/conversationsuite.json
```

You can also specify it in your `yml` config files by adding a  
comment like the following:

YAML

```
# yaml-language-server: $schema=https://voiceflow.xavidop.me/static/conversationsuite.json
```

Updated 4 months ago

---

[Automated testing](/docs/automated-testing)[Interaction-Based Tests Reference](/docs/tests)

Ask AI

* [Table of Contents](#)
* + [Reference](#reference)
  + [JSON Schema](#json-schema)