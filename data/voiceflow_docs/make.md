---
category: general
scraped_at: '2025-11-12T14:08:23.115102'
title: Make
url: /docs/make
---

# Make

Use Make actions in both Agent and Tool steps to trigger automated workflows (scenarios) from your agent.

## Make (formerly Integromat)

Use Make actions in both Agent and Tool steps to trigger complex, automated workflows (called *scenarios*) directly from your Voiceflow agent. With the Make integration, you can connect to hundreds of apps and services, allowing your agent to orchestrate advanced automations with a single step.

  
> 🔐
>
> To use the Make integration, you'll need to **OAuth into Make** from the Voiceflow Creator. This ensures your agent can securely trigger scenarios from your connected Make account.

## What you can do with Make

The Make integration currently supports the following action:

| Action | Description |
| --- | --- |
| Run scenario | Trigger a specific scenario in your Make account to execute automation. |

## Use cases

Here are some common ways to use Make in your Voiceflow agent's workflow:

* Trigger a workflow to send a follow-up email when a conversation ends.
* Send user form data from Voiceflow to multiple services at once.
* Automate updates in CRMs, databases, or messaging apps based on agent interactions.

Example:

> If a user asks to "sign up for the newsletter and send me a welcome package," you might use the **Run scenario** action to trigger a Make scenario that adds them to your email list, updates your CRM, and sends a Slack notification to your team.

Ensure you provide an `LLM description` for each tool so the agent understands when to use it.

> E.g. for `Run scenario`, you might write: `Trigger the automation scenario in Make when a user requests an action that involves multiple connected services or workflows.`

> 👀
>
> ### Be wary of each action's required arguments.
>
> The **Run scenario** action typically requires a `scenarioURL` or a unique name. Decide whether this should be *defaulted, hardcoded, or collected by the agent*. Always provide LLM descriptions for each input so the agent knows exactly how to use them.
>
> [img ]

## Frequently asked questions

### Can I pass variables from Voiceflow into my Make scenario?

> Yes. You can pass data such as user inputs, IDs, or conversation context to your Make scenario by mapping information in the Tool or Agent step configuration's `data` input variable.

### Can I trigger multiple Make scenarios from one conversation?

> Asked mike, answer pending.

### Do I need to configure my scenario before using it in Voiceflow?

> Yes. You must first create and test your scenario in Make, then connect it in Voiceflow by providing the correct `scenarioURL` and `data` configuration.

[Doc

## Integrations

Learn more about what integrations are available to supercharge your agent's workflow and capabilities.

Read doc →](https://docs.voiceflow.com/update/docs/integrations#/)

Updated 15 days ago

---

[Hubspot](/docs/hubspot)[MCP](/docs/mcp-tool)

Ask AI

* [Table of Contents](#)
* + [Make (formerly Integromat)](#make-formerly-integromat)
  + [What you can do with Make](#what-you-can-do-with-make)
  + [Use cases](#use-cases)
  + [Frequently asked questions](#frequently-asked-questions)
  + - [Can I pass variables from Voiceflow into my Make scenario?](#can-i-pass-variables-from-voiceflow-into-my-make-scenario)
    - [Can I trigger multiple Make scenarios from one conversation?](#can-i-trigger-multiple-make-scenarios-from-one-conversation)
    - [Do I need to configure my scenario before using it in Voiceflow?](#do-i-need-to-configure-my-scenario-before-using-it-in-voiceflow)