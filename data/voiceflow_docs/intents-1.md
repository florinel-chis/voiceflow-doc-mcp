---
category: general
scraped_at: '2025-11-12T14:11:35.618170'
title: Introduction to Intents
url: /docs/intents-1
---

# Introduction to Intents

> ❗️
>
> **This feature is part of the old way to build using Voiceflow.**
>
> Although this feature remains available, we recommend using the [Agent step](/docs/agents) and [Tool step](/docs/tool-step) to build modern AI agents. Legacy features, such as the Capture step and Intents often consume more credits and lead to a worse user experience.

## What Are Intents?

In the realm of conversational AI, **intents** represent the underlying goals or purposes behind a user's input. They are the actions the user wants to perform or the information they seek through their queries. By identifying intents, your Voiceflow agent can understand what the user is trying to achieve and respond appropriately.

  

## The Role of Intents in Agent Design

Intents are foundational elements in designing conversational agents because they:

* **Guide Conversation Flow**: Help determine the next steps in the conversation based on user input.
* **Enhance Understanding**: Enable the agent to interpret user messages accurately, even if phrased differently.
* **Improve User Experience**: Allow for more natural and efficient interactions by anticipating user needs.

## How Intents Work in Voiceflow

In Voiceflow, intents are defined within the **Intent CMS**. Each intent includes:

* **Name**: A clear identifier for the intent (e.g., `BookAppointment`).
* **Description**: A brief explanation of when the intent should be triggered.
* **Utterances**: Example phrases users might say to invoke the intent.
* **Required Entities** (optional): Specific pieces of information needed to fulfill the intent.

Intents are utilized in various steps within Voiceflow, such as:

* **Choice Step**: To branch the conversation based on different user intents.
* **Button Step**: To provide clickable options that trigger intents.
* **Trigger Step**: To jump to different parts of the conversation when certain intents are recognized.

## Intents vs. Entities

While **intents** capture the user's goal, **entities** represent specific pieces of information within the user's input that are necessary to fulfill that intent. For example:

* **Intent**: `showWeather`
* **Entities**: `Date`, `City`

![](https://files.readme.io/0c8fa062c4cc691148161ddccbb1b2e34ae3790a545ae1b0bae031a4e3d7cf01-image.png)

Understanding the distinction between intents and entities is crucial for designing effective conversational agents. Intents determine **what** the user wants to do, and entities provide the details needed to complete that action.

## Benefits of Using Intents

* **Simplifies Design**: Organizing user goals into intents streamlines the conversation design process.
* **Enhances Scalability**: New functionalities can be added by introducing new intents without overhauling existing structures.
* **Facilitates Maintenance**: Clear intent definitions make it easier to update and manage the agent over time.

Updated about 1 month ago

---

[Variables](/docs/variables)[Using the Intent CMS](/docs/using-the-intent-cms)

Ask AI

* [Table of Contents](#)
* + [What Are Intents?](#what-are-intents)
  + [The Role of Intents in Agent Design](#the-role-of-intents-in-agent-design)
  + [How Intents Work in Voiceflow](#how-intents-work-in-voiceflow)
  + [Intents vs. Entities](#intents-vs-entities)
  + [Benefits of Using Intents](#benefits-of-using-intents)