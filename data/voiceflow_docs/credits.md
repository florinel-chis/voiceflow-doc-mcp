---
category: general
scraped_at: '2025-11-12T14:09:38.123188'
title: Credits
url: /docs/credits
---

# Credits

Credits are Voiceflow's currency used to bill for Agent hosting and AI services.

Credits are the currency in Voiceflow to pay for AI usage and project hosting. Voiceflow charges credits for:

* **Agent hosting** - charged by messages sent by the user and minutes the agent spends on phone calls.
* **AI service usage** - this includes LLM tokens, text-to-speech generation, and speech-to-text usage.

Each Voiceflow credit costs $0.005 USD on the *Business monthly* plans and can be used for either Agent hosting or AI services. Voiceflow only makes money on Agent hosting - AI service costs are passed through at cost, with no markup.

## Which actions consume credits?

Credits are charged differently for chat and voice agents because they run in different ways: chat agents are asynchronous and cheaper, while voice agents operate in real time and cost more.

### Chat agents

| **Action** | **Credit Cost** |
| --- | --- |
| **User sends a chat message** (including through the [Dialogue Manager API](/reference/overview#/)) | 1 credit ($0.005 on the Business monthly plan) |
| **LLM usage (e.g. Agent step, Prompt step, or LLM-generated chat messages)** | Based on tokens used, billed at cost (see [pricing table](/docs/credits-pricing-table#/)) |
| **Agent sends a chat message (non LLM-generated)**  E.g. Static messages sent with the Message step, Card step, Carousel step, Buttons, etc | 0 credits (free). |
| **API calls, function calls, logic steps, and other similar actions** | 0 credits (free) |

> ℹ️
>
> While sending a message is free, any message generated using an LLM (e.g. through the [Prompt step](/docs/prompt-step) or [Agent step](/docs/agents)) will incur usage-based charges based on tokens used. This includes auto-start messages or AI-generated responses.

**Here's how this works in practice for a five turn conversation:**

* User sends 5 messages → 5 credits
* Agent sends 15 messages + 3 API calls → 0 credits
* LLM usage - GPT-4o Mini → ~1 credit

Total: 6 credits ($0.03 on the Business monthly)

Example Conversation

**Agent:** Hi! How can I help? *[0.0001 Credits for LLM usage]*

**User:** I need to book a demo *[1 Credit]*

**Agent:** Got it, I can help you with that. One moment please... *[0.0001 Credits for LLM usage]*

**Agent:** <Executes an API call to pull up user info> *[0 Credits]*

**Agent:** <Runs an LLM prompt to format API response> *[0.01 Credits]*

**Agent:** I have pulled up your account information *[0.0002 Credits for LLM usage]*

**User:** Thanks! *[1 Credit]*

  

### Voice agents

Voice agents are billed per minute, plus text-to-speech, speech-to-text, and LLM usage. Telephony rates (such as renting a phone number and connection fees) are charged directly by our supported providers: [Twilio](https://twilio.com) and [Vonage](https://vonage.com).

| Action | Credit Cost |
| --- | --- |
| **Agent call time** | 10 credits per minute ($0.05/min on the Business monthly plan) |
| **Text-to-Speech (TTS)** | Billed per character ([vendor rates](/docs/credits-pricing-table#/)) |
| **Speech-to-Text (STT)** | Billed per minute ([vendor rates](/docs/credits-pricing-table#/)) |
| **LLM usage** | Based on tokens used ([billed at cost](/docs/credits-pricing-table#/)) |
| **Telephony provider charges** | Billed separately by provider (Twilio or Vonage) |

  

**Here's an example of how this works in practice for a five minute conversation:**

* Agent talk time (5 min x 10 credits per minute) → 50 credits
* LLM usage - GPT-4o Mini → ~1 credit
* Text-to-Speech - ElevenLabs Flash (2.5 min, ~2,140 chars, 9 credits per 1,000 characters) → 20 credits
* Speech-to-Text - Deepgram Nova 3 - (5 min x 1 credit per minute) → 5 credits

Total: 76 credits ($0.38, or $0.076 per minute on the Business monthly plan)

  

## Estimating your credit usage

Need help estimating how many credits your LLM or TTS usage will use? Check out our credit usage estimation calculator.

[Tool

## Credit usage estimator

Estimate how many credits your agents will consume per month and have the best value plan recommended to you.

Try tool →](./estimate-your-credit-usage#credits-estimation-calculator)

  

## Why Voiceflow uses credits

We use a credit system to simplify how you pay for Agent hosting and AI services (like LLMs, TTS, and STT), without locking you into specific vendors or surprise bills.

For you, this means that:

* **No separate AI vendor accounts are required**: use models from OpenAI, Anthropic, Google, Meta, and more — all through one Voiceflow account.
* **You can switch AI vendors anytime**: as prices or quality shift, you can change providers without rewriting your agent or renegotiating contracts.
* **Pay-as-you-go with transparent costs**: every action has a clear credit cost, and most non-AI logic (like API calls or logic steps) is free.
* **You have access to volume discounts**: Voiceflow negotiates bulk rates with AI providers and passes those savings directly to you.

> ℹ️
>
> **Example:** if ElevenLabs lowers TTS rates or Anthropic releases a cheaper model, you’ll get those savings automatically — no manual work or vendor management required.

  

## Frequently asked questions

### What happens if I run out of credits?

You’ll get automatic usage alerts at 50%, 75%, 90%, and 100% of your credit limit. Once your credits have run out, your Voiceflow agent will step working. To avoid agent outages, we recommend monitoring your credits usage and upgrading to a credits tier that matches your desired usage level. You can downgrade to a lower credits tier at any time.

  

### Can I turn on auto-upgrade for credit tiers?

* Not today, we are working on this!

  

### How can I optimize my agent to use less credits?

We're on your side - we bill LLM and TTS usage **at cost**, meaning we don't make any profit from you using these features. We also pass along any bulk discounts we get from our providers onto you. This means it's in our best interest to help you optimize your agent to use the least credits possible when building with LLMs and TTS.

We've put together our tips on optimizing agents in the course below, and update whenever we hear new ideas from our community.

[Course

## Optimize your AI agent to use less credits

Save money while building powerful AI agents. We'll show you our tips on how to reduce how many credits you're using.

Go to course →](https://www.voiceflow.com/lessons/what-are-credits)

Updated 3 months ago

---

[Managing your Voiceflow plan](/docs/managing-your-voiceflow-plan)[Estimate your credit usage](/docs/estimate-your-credit-usage)

Ask AI

* [Table of Contents](#)
* + [Which actions consume credits?](#which-actions-consume-credits)
  + - [Chat agents](#chat-agents)
    - [Voice agents](#voice-agents)
  + [Estimating your credit usage](#estimating-your-credit-usage)
  + [Why Voiceflow uses credits](#why-voiceflow-uses-credits)
  + [Frequently asked questions](#frequently-asked-questions)
  + - [What happens if I run out of credits?](#what-happens-if-i-run-out-of-credits)
    - [Can I turn on auto-upgrade for credit tiers?](#can-i-turn-on-auto-upgrade-for-credit-tiers)
    - [How can I optimize my agent to use less credits?](#how-can-i-optimize-my-agent-to-use-less-credits)