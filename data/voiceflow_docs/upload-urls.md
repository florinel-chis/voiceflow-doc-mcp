---
category: general
scraped_at: '2025-11-12T14:10:16.612080'
title: Upload URLs
url: /docs/upload-urls
---

# Upload URLs

## Upload URLs to the Knowledge Base

With the `vocieflow-cli` you can upload content from a URL to your Voiceflow Knowledge Base with customizable processing options. This is useful when you want to perform a automations around your knowledge base. The `voiceflow-cli` has one command that allows you to update your knowledge base from your terminal:

### Command Usage

Bash

```
voiceflow document upload-url [flags]
```

#### Aliases

* `ur`
* `upload-urls`

### Parameters

#### Required Flags

* `--url`: URL to upload content from
* `--name`: Name for the uploaded document

#### Processing Options

* `--max-chunk-size`: Maximum size of content chunks
* `--markdown-conversion`: Convert content to markdown format
* `--overwrite`: Overwrite existing document if present

#### LLM Processing Options

* `--llm-generated-q`: Enable LLM-generated questions
* `--llm-prepend-context`: Prepend context using LLM
* `--llm-based-chunking`: Use LLM for content chunking
* `--llm-content-summarization`: Enable content summarization

#### Metadata

* `--tags`: Array of tags to associate with the document

### Examples

#### Basic Upload

Bash

```
voiceflow document upload-url --url https://docs.example.com/api --name "API Documentation"
```

#### Advanced Upload with LLM Processing

Bash

```
voiceflow document upload-url \
  --url https://docs.example.com/api \
  --name "API Documentation" \
  --max-chunk-size 1000 \
  --markdown-conversion \
  --llm-generated-q \
  --llm-content-summarization \
  --tags api,documentation
```

#### Upload with Overwrite

Bash

```
voiceflow document upload-url \
  --url https://docs.example.com/api \
  --name "API Documentation" \
  --overwrite \
  --tags api,v2
```

Updated 5 months ago

---

[Documents](/docs/documents)[Upload files](/docs/upload-files)

Ask AI

* [Table of Contents](#)
* + [Upload URLs to the Knowledge Base](#upload-urls-to-the-knowledge-base)
  + - [Command Usage](#command-usage)
    - [Parameters](#parameters)
    - [Examples](#examples)