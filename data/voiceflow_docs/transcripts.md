---
category: general
scraped_at: '2025-11-12T14:09:25.003966'
title: Transcripts
url: /docs/transcripts
---

# Transcripts

Record and analyze conversations between agents and users.

## What are transcripts?

Transcripts are automatically generated logs of conversations between users and your agent. They capture both user input and agent responses across voice and chat interactions.

Transcripts are valuable for:

* Debugging issues in conversation flows.
* Identifying points of confusion or user drop-off from conversations.
* Improving assistant performance using real interaction data.
* Maintaining a history of conversations for review or auditing

[](https://w17llroiln.ufs.sh/f/JH4JLc5mceYk3UGza4xvHiSLdUJE7T2askXuFCm1RcjpZWMz)

> ⚠️
>
> ### Ensure audio recordings are toggled on!
>
> Call recordings need to be enabled in **transcript settings** to retrieve audio files for a conversation's transcript. Click on the ⚙️ icon to view settings.
>
> ![](https://files.readme.io/3661fb308989555f5dd9d73bff0b3c98dee98dc1498f709b56fa408daf414e92-CleanShot_2025-07-30_at_11.06.542x.png)

## Analyzing transcripts

Transcripts are tied to **individual** agents, not the overall workspace. Each transcript provides information including:

| Data attribute | Description |
| --- | --- |
| Date | Timestamp of when the conversation started. |
| Platform | Source of the interaction (Chat widget or Telephony). |
| User ID | Unique identifier for the user interacting with the agent. |
| Credits | The number of credits consumed by the agent during the conversation. |
| From | The user's phone number that was used during the conversation. |
| Evaluations | Displays evaluation results such as test pass/fail status or validation values. By default, no evaluations are applied to transcripts, unless created and enabled through the [Evaluations](/docs/evaluations) editor. |
| Duration | Total length of the conversation (in minutes and seconds). |

![](https://files.readme.io/295f22ce08418ad79a352ae61889087b722c50c822084c948f438a8748ef9c71-image.png)
  

## Debugging using transcripts

Agent and user conversations can be analyzed in depth for debugging through the Logs tab on each transcript. Logs display the behind-the-scenes of the Agent's interactions and what exact steps were executed within its designated workflow. They also provide additional information such as the agent's Input, Output and how many credits were consumed per action.

![](https://files.readme.io/51697c4dbba0aed9a616883b7b61f4b28ca4a9b76827a0e7e23ba45f410de301-image.png)

## Evaluations

Evaluations are a set of custom criteria you can define to determine whether specific events occurred during a conversation—based on the transcript data.

> For example, you might want to evaluate whether:
>
> * The user expressed satisfaction or frustration
> * The agent confirmed an action(e.g. upload to database)
> * The conversation included a proper sign-off, such as the agent saying “Let me know if you need anything else”

Evaluations allow you to automate conversation review and score interactions against key success metrics, quality standards, or compliance requirements.

Updated 20 days ago

---

[Analytics](/docs/analytics)[Evaluations](/docs/evaluations)

Ask AI

* [Table of Contents](#)
* + [What are transcripts?](#what-are-transcripts)
  + [Analyzing transcripts](#analyzing-transcripts)
  + [Debugging using transcripts](#debugging-using-transcripts)
  + [Evaluations](#evaluations)