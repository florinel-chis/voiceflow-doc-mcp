---
category: general
scraped_at: '2025-11-12T14:09:52.548029'
title: Authentication
url: /docs/authentication
---

# Authentication

## Voiceflow API Key

`voiceflow-cli` uses Voiceflow APIs. To interact with your Voiceflow projects you will need a [Voiceflow API Key](/reference/authentication). You can get your API Key in your Voiceflow project > Settings page. You can pass the API Key to the CLI using the `--voiceflow-api-key` flag or by setting the `VF_API_KEY` environment variable. `voiceflow-cli` also works with `.env` files. You can create a `.env` file in the root of your project and add the `VF_API_KEY` variable to it.

The `voiceflow-cli` source code is open source, you can check it out [here](https://github.com/xavidop/voiceflow-cli) to learn more about the actions the tool performs.

## Base URL

The base URL for the Voiceflow API is `https://<api>.<subdomain>.voiceflow.com`. The default value is without subdomain: `https://<api>.voiceflow.com`. If you are using a different Voiceflow environment, you can pass the subdomain using the `--voiceflow-subdomain` flag.

## Open AI API Key

`voiceflow-cli` uses Open AI APIs. To interact with Open AI you will need an API Key. You can get your API Key in your Open AI account. You can pass the API Key to the CLI using the `--openai-api-key` flag or by setting the `OPENAI_API_KEY` environment variable. `voiceflow-cli` also works with `.env` files. You can create a `.env` file in the root of your project and add the `OPENAI_API_KEY` variable to it.

Updated 8 days ago

---

[Install](/docs/cli-install)[Roadmap](/docs/roadmap)

Ask AI

* [Table of Contents](#)
* + [Voiceflow API Key](#voiceflow-api-key)
  + [Base URL](#base-url)
  + [Open AI API Key](#open-ai-api-key)