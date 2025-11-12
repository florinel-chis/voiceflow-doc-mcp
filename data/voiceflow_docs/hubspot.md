---
category: general
scraped_at: '2025-11-12T14:08:21.241052'
title: Hubspot
url: /docs/hubspot
---

# Hubspot

Use the HubSpot actions in both Agent and Tool steps to create powerful sales, support, and marketing workflows.

# HubSpot

Use HubSpot actions in both Agent and Tool steps for dynamic, real-time CRM interactions with your data.  
Easily connect your Voiceflow agent with HubSpot to create and manage contacts, leads, and tickets directly from your conversations. Use the HubSpot actions in both Agent and Tool steps to create powerful sales and support workflows.

## Basic usage

[](https://w17llroiln.ufs.sh/f/JH4JLc5mceYkK9h0DiEqUQ3veuBLjYnM1XTJ2ZzHV8fWlK9G)

  
> 🔐
>
> To use the HubSpot integration, you'll need to **OAuth into HubSpot** from the Voiceflow Creator. This ensures your agent can securely create and manage CRM records from your connected account.

## What you can do with HubSpot

The HubSpot integration supports the following actions:

| Action | Description |
| --- | --- |
| Create contact | Add a new contact to your HubSpot CRM. |
| Create lead | Create a new lead (prospect) in your HubSpot CRM. |
| Create ticket | Log a new support or service ticket within HubSpot. |

## Use cases

Here are some common ways to use HubSpot in your Voiceflow agent's workflow:

* Capture and store lead information from live conversations.
* Automatically create support tickets when a customer reports an issue.
* Add new contacts to your CRM when users provide their details.

Example:

> For `Create lead`, you might provide an LLM description such as `Add a new lead to HubSpot when the user expresses interest in our services but has not yet purchased.`

> 👀
>
> ### Be wary of each action's required arguments.
>
> Each action may require unique parameters such as `firstname`, `lastname`, `email`, or `ticketDescription`. Decide whether these should be *defaulted, hardcoded, or collected by the agent*. Always provide LLM descriptions for each input variable so the agent knows exactly how to use them.
>
> ![](https://files.readme.io/0b08008a4bf110a9dc56b8d313ae38f44b777cbd82cb499abcb2f209d7e43242-CleanShot_2025-08-10_at_12.12.222x.png)
>
> ![](https://files.readme.io/example-hubspot-action-args.png)

## Frequently asked questions

### Can I create both a lead and a contact at the same time?

> Not directly in a single action. You can chain actions in your flow so that creating a lead also triggers creating a contact.

### Can I assign a ticket to a specific team member?

> Yes, if you provide the correct `ownerId` or `assignee` parameter when creating the ticket.

### Can I prevent duplicate contacts?

> Yes. Include logic in your flow to check for an existing contact by email before creating a new one.

### Do I need to set up custom fields in HubSpot first?

> If you want to capture information beyond the standard fields, yes — create the custom properties in HubSpot before mapping them in Voiceflow.

[Doc

## Integrations

Learn more about what integrations are available to supercharge your agent's workflow and capabilities.

Read doc →](https://docs.voiceflow.com/update/docs/integrations#/)

Updated 3 months ago

---

[Google Sheets](/docs/google-sheets)[Make](/docs/make)

Ask AI

* [Table of Contents](#)
* + [HubSpot](#hubspot)
  + - [Basic usage](#basic-usage)
    - [What you can do with HubSpot](#what-you-can-do-with-hubspot)
    - [Use cases](#use-cases)
    - [Frequently asked questions](#frequently-asked-questions)