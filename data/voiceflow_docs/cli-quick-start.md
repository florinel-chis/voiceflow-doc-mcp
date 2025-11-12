---
category: general
scraped_at: '2025-11-12T14:09:48.455356'
title: Quick start
url: /docs/cli-quick-start
---

# Quick start

`voiceflow-cli` is a command-line tool that allows Voiceflow users to [upload files to their knowledge base](/docs/upload-files), [download transcripts](/docs/fetching), [run automated tests](/docs/automated-testing), and more.

In a few minutes, this guide will walk you through installing the CLI, authenticating your agent, and uploading a document to your [knowledge base](/docs/knowledge-base).

  

## 1. Install the CLI

Open your terminal, then input the command below that corresponds to your operating system. If you're on MacOS or Linux, [install brew before running this command](https://brew.sh/).

Mac or LinuxWindows

```
brew install xavidop/tap/voiceflow
```

```
curl -sfL https://voiceflow.xavidop.me/static/run | bash
```

Alternatively, you can install the Voiceflow CLI via Chocolatey (Windows) or APT (Linux). [Click here to learn more.](/docs/cli-install)

  

To check if the Voiceflow CLI was successfully installed, run:

Bash

```
voiceflow --help
```

You should see a list of commands, as shown below. If you do, the installation was successful - you're all set!!

[](https://yz5du1veb1.ufs.sh/f/9fKud4NeF5NSxkKo0EIimEag8BWSoQbTdFYpDN5wRPeli0j2)

  

## 2. Grab your agent's API key

* Open the [Voiceflow Creator](https://creator.voiceflow.com/), and click the agent you want to use with the CLI.
* In the sidebar, click **Settings** → **API keys**
* Click the **copy** button to grab your API key

[](https://yz5du1veb1.ufs.sh/f/9fKud4NeF5NSgC3lEmcdtVY8pvMo6K2ksaDj0z4g5XZ7nI3h)

  
  

## 3. Add the agent's API key to your environment

Run the following command, making sure you replace `YOUR_KEY` with the copied API key from the previous step. This will add your API key to the environment.

bash

```
export VF_API_KEY=YOUR_KEY
```

Alternatively, you can authenticate using a flag, or a `.env` file. [Click here to learn more.](/docs/authentication)

[](https://yz5du1veb1.ufs.sh/f/9fKud4NeF5NSsKfjoUzzvNuIPLsxO2KUc05GVE9RlySWktCi)

  

## 4. Upload data to your agent's knowledge base

You're almost there! Finally, paste the following command into your terminal to upload data to your agent's knowledge base. In this example, we'll upload the contents of this page!

Bash

```
voiceflow document upload-url --url https://docs.voiceflow.com/docs/cli-quick-start.md --name "Quick Start"
```

While the upload processes, you'll see a pending status in your terminal.

To check if your data was successfully updated to the agent's knowledge base, go back to your Voiceflow project, and click **knowledge base** button in your sidebar. You should see your newly updated file as shown below.

[](https://yz5du1veb1.ufs.sh/f/9fKud4NeF5NSP20Noz7lF9by0OHwa4UL5XrKMoYGdeckgTqN)

  

## Congratulations!

You just successfully installed the CLI, authenticated your agent, and uploaded your first document to the knowledge base. From here, you can explore the full range of CLI commands to test your agent, fetch transcripts, and automate your workflows. Happy building!

Updated about 1 month ago

---

[Voiceflow CLI](/docs/voiceflow-cli)[Overview](/docs/overview-1)

Ask AI

* [Table of Contents](#)
* + [1. Install the CLI](#1-install-the-cli)
  + [2. Grab your agent's API key](#2-grab-your-agents-api-key)
  + [3. Add the agent's API key to your environment](#3-add-the-agents-api-key-to-your-environment)
  + [4. Upload data to your agent's knowledge base](#4-upload-data-to-your-agents-knowledge-base)
  + [Congratulations!](#congratulations)