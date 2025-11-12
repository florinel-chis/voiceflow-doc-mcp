---
category: general
scraped_at: '2025-11-12T14:08:05.841821'
title: Call forwarding tool
url: /docs/call-forwarding
---

# Call forwarding tool

Automatically forward calls to a human.

> ℹ️
>
> This feature is only available when calling an agent via [phone](/docs/telephony).

  

After interacting with your AI agent, some callers may still need to speak with a person for certain requests or follow-ups. Call forwarding lets you send the call to another phone number, SIP address, or extension. It’s useful when the agent collects initial details, then directs the caller to the right teammate, department, or specialist to finish the conversation.

  

## Forwarding calls from inside the Agent step

[](https://yz5du1veb1.ufs.sh/f/9fKud4NeF5NS9TAp2deF5NSgc7ztGr8nO1qDJyewRlHWPUv2)

Inside an [Agent step](/docs/agents), enable the **Call forward** option on the sidebar. Then, set the following three options:

* **LLM description** - this allows you to to describe the tool to your agent and tell it when it should be triggered.
* **Phone number** - the phone number that the caller should be forwarded to, including country code. For example, `+16471112222`.
* **Extension (optional)** - if you'd like to automatically connect the caller to a specific extension, enter the extension here. Otherwise, leave this input blank.

Some advanced users may wish to forward the call via SIP instead. This can be done by selecting the SIP option and entering a SIP address when prompted.

  

## Manually forwarding calls

You can also manually forward a call using the [Call forwarding step](/docs/call-forwarding-step).

[Doc

## Call forwarding step

Forward calls from outside the Agent step.

Read doc →](./call-forwarding-step)

  

## Billing

Once your call has been forwarded, you'll no longer be charged Voiceflow credits for any future time spent on the call. For example, if a caller spends 2 minutes speaking with your AI agent, then the call is forwarded to a human who they spend 3 minutes talking to, you'll be billed 20 credits in per-minute fees (plus LLM, STT, and TTS usage), rather than 50 credits. [Learn more about credits pricing here](/docs/credits-pricing-table).

Updated about 2 months ago

---

[Importing data](/docs/importing-data-to-the-knowledge-base)[Buttons tool](/docs/buttons-tool)

Ask AI

* [Table of Contents](#)
* + [Forwarding calls from inside the Agent step](#forwarding-calls-from-inside-the-agent-step)
  + [Manually forwarding calls](#manually-forwarding-calls)
  + [Billing](#billing)