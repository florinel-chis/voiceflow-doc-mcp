---
category: general
scraped_at: '2025-11-12T14:08:30.146316'
title: Zapier
url: /docs/zapier
---

# Zapier

Connect your Voiceflow agent to all the tools your business uses.

## Connecting to Zapier from inside Voiceflow

Voiceflow does not yet have a native Zapier integration available in the [Agent step](/docs/agents) or [Tool step](/changelog/tools-step). For now, we recommend using using a [Zapier webhook trigger](https://help.zapier.com/hc/en-us/articles/8496288690317-Trigger-Zaps-from-webhooks) with an API on the [Agent step](/docs/agents) or [Tool step](/changelog/tools-step) to trigger zaps from inside your agent.

  

## Trigger Voiceflow events from your Zapier zaps

Voiceflow is available as a [native integration on Zapier](https://zapier.com/apps/voiceflow/integrations). This allows you to trigger outbound calls when an action happens in another tool, as well as routing conversations from a wide range of platforms into your Voiceflow agent.

The following actions are available inside Zapier:

| Action Name | Description |
| --- | --- |
| Start agent conversation | [Sends a launch request to your agent](/reference/stateinteract-1#/). When starting a new conversation, always start with a launch request. |
| Send message to agent | [Sends a text request to your agent](/reference/stateinteract-1#/). This allows you to send text messages to your agent. |
| Send event to agent | [Sends an event request to your agent](/reference/stateinteract-1#/). This lets you jump to a specific part of your agent's workflow. |
| Make outbound call | [Sends a call using the outbound calling API](/docs/outbound-calls). |

Please note that Voiceflow doesn't currently have any triggers available on Zapier.

  

### Using Voiceflow actions in Zapier

Voiceflow's actions can be added to your zaps in the same way as any other integration. Simply click on an empty action, search for Voiceflow, then choose the action you'd like to trigger.

[](https://yz5du1veb1.ufs.sh/f/9fKud4NeF5NSVB2D8jhwmvNPCJSYUL25jhGKozr09iZnAIe1)

> ℹ️
>
> **Protip:** if you're beginning a new conversation, make sure you use the **Start agent conversation** action before sending a message or an event to your agent!

  

Once you've chosen the action you'd like to trigger, you'll then need to link your Voiceflow project to Zapier. To do this, click on the **Account** dropdown and select **Connect a new account**.

For each Voiceflow project, you'll need to provide two values:

* Your **Voiceflow Project API Key**, which can be found by opening your project from the dashboard, clicking the ⚙️ icon on the sidebar, then selecting **API keys**. To get your API key, click the **copy** button.
* Your **Voiceflow Project ID**, which is found in the **General** tab of your project's settings.

After entering these values, click the continue button to link your Voiceflow project to Zapier.

[](https://yz5du1veb1.ufs.sh/f/9fKud4NeF5NSiyWVrS5Va6w0sMdTR4hluogEBjIFvbXzpqf7)

### Handling outbound calls

While most of Voiceflow's Zapier actions only require the project's ID and API key, the **Make outbound call** action requires an **Agent Phone Number ID**. This can be found by opening clicking the **Interfaces** button on your project's sidebar, selecting **Telephony**, then clicking the **View** button next to the phone number that you'd like to call from.

The `Agent Phone Number ID` is the set of characters shown in the cURL request.

[](https://yz5du1veb1.ufs.sh/f/9fKud4NeF5NSv5eRI08xoDVQXmAUr9uGNzwaYSd78tfRT6F1)

---

Updated 3 months ago

---

[Twilio](/docs/twilio)[Zendesk](/docs/zendesk)

Ask AI

* [Table of Contents](#)
* + [Connecting to Zapier from inside Voiceflow](#connecting-to-zapier-from-inside-voiceflow)
  + [Trigger Voiceflow events from your Zapier zaps](#trigger-voiceflow-events-from-your-zapier-zaps)
  + [Using Voiceflow actions in Zapier](#using-voiceflow-actions-in-zapier)
  + [Handling outbound calls](#handling-outbound-calls)