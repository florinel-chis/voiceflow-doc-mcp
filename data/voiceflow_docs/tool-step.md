---
category: general
scraped_at: '2025-11-12T14:07:26.690351'
title: Tool step
url: /docs/tool-step
---

# Tool step

Add Integrations, Functions and API requests to your agent's workflow.

The tool step allows you to run any tool — [functions](https://docs.voiceflow.com/update/docs/function-step#/), [API requests](https://docs.voiceflow.com/update/docs/api-step#/) or [integrations](https://docs.voiceflow.com/update/docs/integrations#/) — anywhere in your workflow, not just within an agent step. This gives you more control and flexibility over when and how you trigger third-party integrations. You can integrate the tool step into your workflow, just like any other step. You’ll find the Tool Step in the ‘**Dev**’ section of the tool bar.

## Basic Usage

![](https://files.readme.io/23665b7f9c7ed9126a038c2c7ed071dccc29a3ece10ba03fd607d3b49f58efff-image.png)

## Use cases

You can use Tool Steps to:

* Send confirmation emails after an appointment is booked
* Trigger external workflows using Make.com
* Log conversation outcomes in Hubspot
* Create or update tickets in Zendesk
* Fetch product data from Google Sheets
* Send SMS via Twilio
* Update customer records in Airtable or your CRM

And much more...

> 📘
>
> All the functions, integrations and APIs available in the **Tool step** can also be toggled and selected for use in the **Agent step**.
>
> ![](https://files.readme.io/1ba143caec56c024d2dc331bedc2e4aee95dca847705d6213b80d9943fddefb2-CleanShot_2025-07-29_at_14.44.212x.png)

## Example use case: *Gmail*

In the example shown, the *Basic Template*'s customer support specialist agent needs to handle email functionality at the end of the conversation with the user. The tool step is used to send a confirmation email using Gmail. The following variables were configured as variables, to be captured in the *agent step* and passed as arguments to the *tool step*:

> * To
> * Body
> * Bcc

Optional fields such as cc and bcc can also be added.

[](https://w17llroiln.ufs.sh/f/JH4JLc5mceYkxy8f4ehHB63EAecr4ldMRpWtKsU5fLaQgvGk)

[Doc

## Integrations

Supercharge your agent's workflow with third party integrations with tools such as Google Sheets, Zendesk and Airtable!

Read doc →](https://docs.voiceflow.com/update/docs/integrations#/)

Updated 3 months ago

---

[Call forwarding step](/docs/call-forwarding-step)[Triggers](/docs/trigger)

Ask AI

* [Table of Contents](#)
* + [Basic Usage](#basic-usage)
  + [Use cases](#use-cases)
  + [Example use case: Gmail](#example-use-case-gmail)