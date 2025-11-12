---
category: general
scraped_at: '2025-11-12T14:08:17.221410'
title: Gmail
url: /docs/gmail
---

# Gmail

Use Gmail actions in both Agent and Tool steps to enable your agent to send emails to users.

Easily connect your Voiceflow agent with Gmail to send emails dynamically based on user input or agent logic. Use the Gmail action in both Agent and Tool steps for maximum flexibility in your email workflows.

## Basic usage

[](https://w17llroiln.ufs.sh/f/JH4JLc5mceYkxy8f4ehHB63EAecr4ldMRpWtKsU5fLaQgvGk)

> 🔐
>
> To use the Gmail integration, you'll need to **OAuth into Gmail** from the Voiceflow Creator. This ensures your agent can send authenticated emails securely from your connected account.

## What you can do with Gmail

The Gmail integration currently supports one powerful action:

| Action | Description |
| --- | --- |
| Send email | Send an email to one or more recipients with custom subject, body, and optional attachments. |

## Use cases

Here are some common ways to use Gmail in your Voiceflow agent's workflow:

* Send a confirmation or follow-up email after a conversation.
* Deliver automated receipts or summaries of support tickets.
* Email a team member or user with data collected during the interaction.

> 👀
>
> ### Be wary of each action's required arguments.
>
> The **Send email** action requires several key arguments like `To`, `Subject`, and `Body`. Ensure you decide whether each field should be *defaulted, hardcoded, or collected by the agent*. Include LLM descriptions to help the agent understand how to populate these values properly.
>
> ![](https://files.readme.io/004b710e44755d7fe74ef3949dd5ecb9fc5052272ce1d56ed643610115aa35a7-CleanShot_2025-08-10_at_11.35.412x.png)

## Frequently asked questions

### Can I send emails to multiple people?

> Yes, the `To` field can accept multiple comma-separated email addresses. Make sure the agent formats this field correctly using commas before sending by instructing it in its `Instructions`.

### Can I personalize the email content?

> Absolutely. Use agent-collected variables (like name, order info, etc.) in the subject or body to generate fully personalized messages. Ensure you instruct the agent to personalize the email in its `Instructions`.

### What happens if the email fails to send?

> If the Gmail action fails (e.g., due to invalid addresses or missing fields), the agent will surface an error and inform the user of the unsuccessful action. You can handle this with conditional prompts or fallbacks in your flow.

### Can I include attachments?

> Not currently. The Gmail integration supports plain text and HTML bodies but does not yet support file attachments.

[Doc

## Integrations

Learn more about what integrations are available to supercharge your agent's workflow and capabilities.

Read doc →](https://docs.voiceflow.com/update/docs/integrations#/)

Updated 3 months ago

---

[Airtable](/docs/airtable)[Google Sheets](/docs/google-sheets)

Ask AI

* [Table of Contents](#)
* + [Basic usage](#basic-usage)
  + [What you can do with Gmail](#what-you-can-do-with-gmail)
  + [Use cases](#use-cases)
  + [Frequently asked questions](#frequently-asked-questions)
  + - [Can I send emails to multiple people?](#can-i-send-emails-to-multiple-people)
    - [Can I personalize the email content?](#can-i-personalize-the-email-content)
    - [What happens if the email fails to send?](#what-happens-if-the-email-fails-to-send)
    - [Can I include attachments?](#can-i-include-attachments)