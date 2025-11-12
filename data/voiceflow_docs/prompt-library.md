---
category: general
scraped_at: '2025-11-12T14:07:38.029342'
title: Prompt Library
url: /docs/prompt-library
---

# Prompt Library

This is a growing collection of prompts that you can import into the Prompts CMS

> ❗️
>
> **This feature is part of the old way to build using Voiceflow.**
>
> Although this feature remains available, we recommend using the [Agent step](/docs/agents) and [Tool step](/docs/tool-step) to build modern AI agents. Legacy features, such as the Capture step and Intents often consume more credits and lead to a worse user experience.

# How to import a prompt

To import a prompt into your agent, head to the prompts CMS and click on the 'import' button in the top right.

*Note: This collection of prompts is growing - we'll add more examples each time we create a new template!*

![](https://files.readme.io/5c16bc6786b4673d6fd8392a7a4c66acd8b951333ccbb26e1688a42b122aa4cd-CleanShot_2024-12-12_at_11.27.082x.png)

---

# General Prompts

The prompt step is used to generate a response and show it directly to the customer.

![](https://files.readme.io/6f603cec97036a9cd58b740885210f7ba24ea7fce39ef8eb88a2cc9be058f4e4-CleanShot_2024-12-12_at_16.23.29.gif)
  

## Sales agent

The simplest way to use Voiceflow is the same way you use chatGPT, just a loop with a large prompt. This prompt asks the user specific questions and then sends a final message when its done.

![](https://files.readme.io/d7a3556053c29722f965456ebc7e0c43d9d39e96dcb672c031c7b33e5369d90f-CleanShot_2024-12-12_at_15.31.24.png)

[Download Prompt](https://drive.google.com/uc?export=download&id=1Kf7q-HHGNYCFFaUpFJAMVECj5WtYDVA1)

![](https://files.readme.io/83a3664a19cbe0ce1560da2a5108d185c59d2c690744a20c036f71a50b44fe38-CleanShot_2024-12-12_at_16.16.05.png)
  

## Knowledge Base - Simple answer (ideal for Voice)

To generate an answer using information from the knowledge base, you first need to search the knowledge base with the [KB search step](/docs/kb-search) (item 1 in the image below). The relevant information is saved to a variable. In this case, we have called that variable {chunks}.

The two prompts below show how to use that information to generate a simple answer (for voice) and a detailed answer (for chat)

![](https://files.readme.io/0ec38b44c116268d9f53fe9718e4e6f005cee0719ebb970b19b47e2207801723-CleanShot_2024-12-12_at_15.59.00.png)

[Download Prompt](https://drive.google.com/uc?export=download&id=12Xp-Muayn3I5gLqMhPMZF5-yUQ699xfN)

![](https://files.readme.io/d4f352ffdeec9bd51fa8465f7d6e91e6107451148e9fce44d4ed83859fc401b5-CleanShot_2024-12-12_at_16.16.38.png)
  

## Knowledge Base - detailed answer (ideal for chat)

*Used in the same way as the prompt above*

This prompt uses the information from the Knowledge base (saved in the {chunks} variable) to generate a highly detailed answer for the user that is properly formatted with titles, bullet points, markdown etc. Ideal for a chat experience.

[Download Prompt](https://drive.google.com/uc?export=download&id=1gaELR1CIR9IrRFUocRHaNJ4CsEWtqnbl)

![](https://files.readme.io/f979c903c2c3b200c96358a9abbacee5bdee969d8997fa1779bfe177777de906-CleanShot_2024-12-12_at_16.15.39.png)
  

# Prompts with the Set Step

Prompts can be attached to the Set step to save the output to a variable for later use. Here are some examples.

![](https://files.readme.io/1efd83a6c66ca179446b220c6b7482ac2a1e2110041d1b729988c5748c665d23-CleanShot_2024-12-12_at_16.20.28.gif)
  

## Optimize the customers question with memory

Sometimes customers don't ask questions that have all the necessary context. This prompt combines the conversation memory with the last question the user asked (saved in {last\_utterance}) to generate a question that is better optimized for AI search.

This is especially valuable when you use the Knowledge Base search step since it doesn't use memory by default.

In this example we optimize the customers question and save it to the {optimized\_question} variable. Then we use that in the KB search step for higher quality results.

![](https://files.readme.io/8e33bb1c892be4ce80acd34de92e7d357192bfef99ca7c1073c1b6222130c43b-CleanShot_2024-12-12_at_16.05.42.png)

[Download Prompt](https://drive.google.com/uc?export=download&id=1dhbO_9Ca_6IwX2UtYEAcCCMabKeQthbE)

![](https://files.readme.io/8eacf2ed7a3bf5200c145d988ccd65fb098d500c98797a775ad4da5aa73dbf19-CleanShot_2024-12-12_at_16.15.03.png)
  

## Detect customers language

Another scenario is detecting the customers language. In this case we use a prompt to determine the language and save it to a variable called {language\_JSON}. We then use that variable in a prompt later on to tell the AI to respond in the language indicated in {language\_JSON}.

![](https://files.readme.io/a2c229f9682748a9f3d3e1507e042b27f3ee498e731cb00f56e485818b96bf8f-CleanShot_2024-12-12_at_16.11.52.png)

[Download Prompt](https://drive.google.com/uc?export=download&id=1bHaJxAXJhwnChBPdEIeYEcW9ilFXNqtA)

![](https://files.readme.io/6708c1977c982eac56e9edf4b765cf68d880ab000ae3be2a9b721acdcf535880-CleanShot_2024-12-12_at_16.13.47.png)
  

# Prompts with condition steps

Prompts can be attached to a condition step to have AI process logic for you. Below are a few great examples.

![](https://files.readme.io/0e2a39551710ba588519fcee2f80090cd47e06fc31fccfcf99aca73c63c34b84-CleanShot_2024-12-12_at_16.21.34.gif)
  

## Evaluate Conversation

This prompt is used to evaluate if the conversation should end or keep going. It looks at the last message that the *agent* has sent to the user to see if it contains anything similar to "I have all the information I need". Here is an example of how its used in a conversation. ([Download this template](https://creator.voiceflow.com/dashboard?import=674f6fe099602814797a32ee))

![](https://files.readme.io/b7c600924bf1e0f71b06512064c706c55abc5c14a86604564e4b75dfc5e3d415-CleanShot_2024-12-12_at_13.26.25.png)

[Download Prompt](https://drive.google.com/uc?export=download&id=1kNJOJObZCwDFkmrxQ_n9AsxFsIx0OnNg)

![](https://files.readme.io/01ddcaf5b809ba655059d5384d0b9cb4e410b224066432b2a5eca1c4208693a4-CleanShot_2024-12-12_at_13.21.54.png)
  

## Check is a clarifying question is required

This prompt is intended to be used with the Knowledge Base search step. It evaluates the question that the customer asked in {last\_utterance} and evaluates the information that was found in the knowledge base (saved in the {chunks} variable).

If it determines that a clarifying question is required it will output a #. Here is an example of how it is used in a flow.

![](https://files.readme.io/21e9ecfce2bab554eb39b0ce75a419c3c1a03875dbb6f3a022435fc2eefe1d8f-CleanShot_2024-12-12_at_14.30.47.png)

[Download Prompt](https://drive.google.com/uc?export=download&id=1AsvD6kqWguponHGPc1bavoQlhkvNMiJY)

![](https://files.readme.io/b8121dcfdd48d583e88706928ab7ecde5882b35598810e35c0f95ffa77420678-CleanShot_2024-12-12_at_16.14.25.png)

Updated about 1 month ago

---

What’s Next

* [Prompts CMS](/docs/prompts-cms-and-editor)

Ask AI

* [Table of Contents](#)
* + [How to import a prompt](#how-to-import-a-prompt)
  + [General Prompts](#general-prompts)
  + - [Sales agent](#sales-agent)
    - [Knowledge Base - Simple answer (ideal for Voice)](#knowledge-base---simple-answer-ideal-for-voice)
    - [Knowledge Base - detailed answer (ideal for chat)](#knowledge-base---detailed-answer-ideal-for-chat)
  + [Prompts with the Set Step](#prompts-with-the-set-step)
  + - [Optimize the customers question with memory](#optimize-the-customers-question-with-memory)
    - [Detect customers language](#detect-customers-language)
  + [Prompts with condition steps](#prompts-with-condition-steps)
  + - [Evaluate Conversation](#evaluate-conversation)
    - [Check is a clarifying question is required](#check-is-a-clarifying-question-is-required)