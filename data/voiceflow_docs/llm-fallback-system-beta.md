---
category: general
scraped_at: '2025-11-12T14:08:40.493825'
title: LLM fallback
url: /docs/llm-fallback-system-beta
---

# LLM fallback

Maximize agent availability by configuring secondary LLMs to take over when primary LLMs suffer an outage.

> 📘
>
> ### Teams and Enterprise Feature
>
> This feature is exclusive to Voiceflow workspaces with the Teams or Enterprise plan.

# Overview

The **LLM Fallback** is a realtime monitoring system that detects potential outages from 3rd-party LLM providers (such as OpenAI) and substitutes calls to unavailable LLMs for calls to alternative LLMs.

The purpose of this system is to maximize the availability of Voiceflow agents. It allows users to configure redundant, secondary models that will take over the handling of LLM-related functionality in case the main models are suffering an outage.

# Usage

## Navigating to fallback configuration

To use the LLM fallback, we must first create a **fallback configuration** to specify what fallback models to use. The fallback configuration can be set by navigating to the **AI models page** by following these steps:

1. Open the **Content Management System (CMS) view** of your agent and navigate to **Settings** (red box)

   ![](https://files.readme.io/b02a12c87e455751f960418778adca81f91b59892909081ff859d0afed4dd6d0-1-cms.png)
2. In Settings, navigate to **AI models**

   ![](https://files.readme.io/8983e14b111c0f32255dc268bfeecb5013a46820bd6c653575c0e3cced8ee3df-2-settings.png)
3. You should arrive at the **AI models**page shown below.

   ![](https://files.readme.io/8b351033b9c93c8ad9f5ab0433eed525f00b00cb9989b83f17fb9eb39cfe6290-3-fallback.png)

## Configuring a fallback configuration

Configuring a fallback configuration is straightforward. For each 3rd-party LLM provider (OpenAI, Anthropic, and Gemini), you can set a fallback model by opening the dropdown on an input in the right column and selecting a model from the list.

![](https://files.readme.io/4d5b82049373d6f0a3fcb44366da0cc8f194227e78facd86a7d183c1dca0f7df-4-configuration.png)

As an example, in the image below, we have configured Claude 3.5 Haiku as the fallback for any OpenAI model, Gemini 1.5 Pro as the fallback for any Anthropic model, and GPT-3.5 Turbo as the fallback for any Google model.

![](https://files.readme.io/b9d622e1b2ed14fd03257cd4359dd16c6e3633db0026d7654ddb8d59d5f93d6f-Screenshot_2025-02-18_at_12.20.27_PM.png)
  

## Fallback in action

Once a fallback configuration is set, then LLM fallback is automatically enabled.

While LLM fallback is enabled and no outages occur, your Voiceflow agent will behave exactly as before. For example, consider a project with a single Prompt step with the following prompt which is configured to use **Claude 3.5 - Haiku** as its LLM.

![](https://files.readme.io/bd0be941566ee1b828572321b388afd5b433a0bcf7120cfdf7e0221f2b249d25-Screenshot_2025-02-18_at_12.38.05_PM.png)

When we interact with the agent, it will behave as expected. Here our agent lists out three Canadian companies.

![](https://files.readme.io/39bd72012f6b4282d70f39a9d035a5de57eab7f237f024b5d13ed75092eaba47-Screenshot_2025-02-18_at_12.36.17_PM.png)

Imagine now that Anthropic is suffering an outage and so Claude 3.5 - Haiku is unavailable. In the previous section, we set the fallback model of Claude 3.5 - Haiku to be Gemini 1.5 Pro. When we execute the Prompt step during this outage, the agent will continue to work properly because after detecting that Claude 3.5 - Haiku is unavailable, it sends a request to Gemini 1.5 Pro to handle our request instead.

This behaviour is logged as a debug trace with the text *"'Anthropic, claude-3.5-haiku' on the fallback chain suffered an outage, falling back to 'google, gemini-pro-1.5'"* on the Prototype Tool:

![](https://files.readme.io/17cc99d50a7fd6c7ab7d7e08858b4de6fd81fc28ea52dd8bcb035409329b88d1-Screenshot_2025-02-18_at_12.44.26_PM.png)

Thus, as we can see, LLM fallback increases the availability of Voiceflow agents through fallback configurations providing redundant models to fallback on.

> ❗️
>
> ### Fallback and non-outage errors
>
> LLM fallback only triggers if an LLM fails for an **outage-related reason**, that is, the 3rd-party LLM provider responded with an error which Voiceflow's outage detection system classifies as an outage.
>
> In practice, this includes nearly all errors from LLMs, but on the rare occasion that an error is classified as a non-outage, it is treated as user error that you as the Voiceflow user need to correct.
>
> **For non-outages, Voiceflow agents do not perform LLM fallback at all**, as the cause of the issue is not the unavailability of 3rd-party LLM providers, but instead a problem with the Voiceflow agent's design, and thus, user action is required to fix the agent as this is not an error scenario the fallback is meant to handle.

## Interpreting a fallback configuration

In this section, we will describe the complete behaviour of the LLM fallback system. Recall that in previous sections, we set the following fallback configuration:

![](https://files.readme.io/b9d622e1b2ed14fd03257cd4359dd16c6e3633db0026d7654ddb8d59d5f93d6f-Screenshot_2025-02-18_at_12.20.27_PM.png)

This fallback configuration can be interpreted as meaning the following:

1. If any OpenAI model (GPT-3.5-Turbo, GPT-4o, etc) suffers an outage, then fall back to Claude 3.5 - Haiku
2. If any Anthropic model (Claude 3.5 - Haiku, Claude 3.5 - Sonnet, etc) suffers an outage, then fall back to Gemini 1.5 - Pro
3. If any Google model (Gemini 1.5 Pro) suffers an outage, fall back to GPT-3.5 Turbo

Note that fallbacks **cascade**, meaning that if a fallback model is itself suffering an outage, then we fallback *again* onto another model determined by the fallback configuration. This repeats until an available model is found or all fallback models are exhausted.

For example, imagine if a Prompt step called GPT-4o (an OpenAI model), but OpenAI's *and* Anthropic services are suffering an outage. Therefore, GPT-4o has configured Claude 3.5 - Haiku to be its fallback model, but Claude 3.5 - Haiku is itself unavailable and act in place of GPT-4o. In this situation, the LLM fallback system will behave as follows:

1. Detected that GPT-4o (OpenAI) is suffering an outage, try to fallback to Claude 3.5 - Haiku
2. Detected that Claude 3.5 - Haiku (Anthropic) is suffering an outage, try to fallback to Gemini 1.5 Pro
3. Gemini 1.5 Pro is available and will be used to generate the LLM output.

In the Voiceflow Prototype Tool, you will see a debug trace reflecting this behaviour:

![](https://files.readme.io/490fb44d822f7c17f5b53189be8d10fafed18e5d7b98ec8ededfcf14b0692ca2-Screenshot_2025-02-18_at_1.20.51_PM.png)

In the highly unlikely event that *all* supported 3rd-party LLM providers are suffering simultaneous outages, cascading behaviour has the risk of putting the LLM fallback system in an infinite loop by following the fallback configuration indefinitely.

Fortunately, the LLM fallback system explicitly checks for this possibility and the fallback process will terminate if it detects that it is revisiting previously visited fallback models, preventing an infinite loop. Concretely, if we again consider a Prompt step contacting GPT-4o and assume that all LLM providers are down, the fallback system behaves as follows:

1. Detected that GPT-4o (OpenAI) is suffering an outage, try to fallback to Claude 3.5 - Haiku
2. Detected that Claude 3.5 - Haiku (Anthropic) is suffering an outage, try to fallback to Gemini 1.5 Pro
3. Detected that Gemini 1.5 Pro (Google) is suffering an outage, try to fallback to GPT-3.5 Turbo
4. Detected that GPT-3.5 Turbo (OpenAI) is suffering an outage, try to fallback to Claude 3.5 - Haiku
5. Claude 3.5 - Haiku was already visited before. An infinite loop has been detected and so we abort the fallback process.

In this worst-case scenario, fallback cannot help since there is nothing left to fallback to. The fallback system terminates and emits a debug trace indicating that an across-the-board outage has taken down the Voiceflow agent.

![](https://files.readme.io/d56fb5932a6cc7a9d9e7f9c86535cbc02105a8ad65c5c32671a3ab4e6a87d682-Screenshot_2025-02-18_at_1.16.23_PM.png)
  

## LLM fallback debug trace

For technical users of Voiceflow, if you are directly calling the [Voiceflow Dialog Manager API](/reference/stateinteract-1), then the LLM fallback system will emit a debug trace that indicates when each fallback that occurs. For example, when the LLM falls back from GPT-4o to Claude 3.5 - Haiku, the following debug trace is emitted:

JSON

```
{
  "time": 1739902968927,
  "type": "debug",
  "payload": {
    "message": "'open-ai, gpt-4o' on the fallback chain suffered an outage, falling back to 'anthropic, claude-3.5-haiku'"
  }
}
```

A full example response body from the DM API, which includes LLM fallback debug traces, is shown below:

JSON

```
[
    {
        "time": 1739902965684,
        "type": "debug",
        "payload": {
            "type": "start",
            "message": "beginning flow"
        }
    },
    {
        "time": 1739902968927,
        "type": "debug",
        "payload": {
            "message": "'open-ai, gpt-4o' on the fallback chain suffered an outage, falling back to 'anthropic, claude-3.5-haiku'"
        }
    },
    {
        "time": 1739902968927,
        "type": "debug",
        "payload": {
            "message": "'anthropic, claude-3.5-haiku' on the fallback chain suffered an outage, falling back to 'google, gemini-pro-1.5'"
        }
    },
    {
        "time": 1739902968927,
        "type": "debug",
        "payload": {
            "message": "__AI Response__<br />\nModel: `gemini-pro-1.5`<br />\nToken Multiplier: `3.5x`<br />\nToken Consumption: `{total: 82, query: 42, answer: 40}`<br />\nPost-Multiplier Token Consumption: `{total: 284, query: 144, answer: 140}`<br />"
        }
    },
    {
        "time": 1739902968928,
        "type": "debug",
        "payload": {
            "type": "ai-response-parameters-model",
            "message": "AI Response Parameters (Model): `user input (if any): undefined, LLM prompt: , output: 1. Lululemon Athletica Inc. - Vancouver, British Columbia\n2. Canada Goose Holdings Inc. - Toronto, Ontario\n3. Aritzia LP - Vancouver, British Columbia \n `"
        },
        "paths": [
            {
                "event": {
                    "type": "ai-response-parameters-model",
                    "payload": {
                        "system": "",
                        "assistant": "",
                        "output": "1. Lululemon Athletica Inc. - Vancouver, British Columbia\n2. Canada Goose Holdings Inc. - Toronto, Ontario\n3. Aritzia LP - Vancouver, British Columbia \n",
                        "model": "gemini-pro-1.5",
                        "temperature": 0.3,
                        "maxTokens": 256,
                        "queryTokens": 144,
                        "answerTokens": 140,
                        "tokens": 284,
                        "multiplier": 3.5
                    }
                }
            }
        ]
    },
    {
        "time": 1739902968927,
        "type": "text",
        "payload": {
            "slate": {
                "id": "xr60oeg",
                "content": [
                    {
                        "children": [
                            {
                                "text": "1. Lululemon Athletica Inc. - Vancouver, British Columbia"
                            }
                        ]
                    },
                    {
                        "children": [
                            {
                                "text": "2. Canada Goose Holdings Inc. - Toronto, Ontario"
                            }
                        ]
                    },
                    {
                        "children": [
                            {
                                "text": "3. Aritzia LP - Vancouver, British Columbia"
                            }
                        ]
                    }
                ],
                "messageDelayMilliseconds": 500
            },
            "delay": 500,
            "message": "1. Lululemon Athletica Inc. - Vancouver, British Columbia\n2. Canada Goose Holdings Inc. - Toronto, Ontario\n3. Aritzia LP - Vancouver, British Columbia",
            "ai": true,
            "voice": "elevenlabs:eleven_flash_v2_5:FGY2WhTYpPnrIDTdsKH5"
        }
    },
    {
        "time": 1739902968929,
        "type": "end"
    }
]
```

# Fallback Coverage

Currently, LLM fallback covers the Prompt step and Generative No Match feature.

Future improvements will extend the coverage of fallback to internal Voiceflow LLM calls, such as entity extraction.

# Definition of outage

The LLM fallback system includes an **outage detection system (ODS)** which checks LLM responses for possible outage-related failure. The responses to LLM requests sent by *all* Voiceflow agents are inspected this way (regardless if they have a paid plan with access to LLM fallback) and this data is aggregated to flag potential outages on an LLM.

The ODS defines an **outage** as an issue that disrupts the availability of a Voiceflow agent, which is caused by Voiceflow or 3rd-party LLM providers (OpenAI, Anthropic, Google, etc). An outage excludes anything that would be considered a **user error**, that is, a mistake caused by a Voiceflow user that causes their agent to behave incorrectly. Additionally, this definition excludes issues which are caused by non-LLM 3rd-party providers (e.g. AWS downtime).

Updated 7 days ago

---

[No Reply handling](/docs/no-reply-response)[Keypad input (DTMF)](/docs/dtmf)

Ask AI

* [Table of Contents](#)
* + [Overview](#overview)
  + [Usage](#usage)
  + - [Navigating to fallback configuration](#navigating-to-fallback-configuration)
    - [Configuring a fallback configuration](#configuring-a-fallback-configuration)
    - [Fallback in action](#fallback-in-action)
    - [Interpreting a fallback configuration](#interpreting-a-fallback-configuration)
    - [LLM fallback debug trace](#llm-fallback-debug-trace)
  + [Fallback Coverage](#fallback-coverage)
  + [Definition of outage](#definition-of-outage)