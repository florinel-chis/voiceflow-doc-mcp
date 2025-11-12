---
category: general
scraped_at: '2025-11-12T14:07:45.279214'
title: Introduction to Events
url: /docs/introduction-to-events
---

# Introduction to Events

**Events** are custom triggers that allow your agent to respond to specific actions or occurrences within the client application or platform. Think of events as signals from the user’s interactions—the clicks, commands, or actions that indicate what the user is doing beyond just their conversational input. Whether it’s a user clicking a “Checkout” button, navigating to a new page, or performing an in-app action, events enable your agent to initiate specific workflows dynamically.

In Voiceflow, events act as **instructions** sent by the client to the agent, telling it to trigger a particular flow. They make your agent more **responsive** and **context-aware**, allowing it to handle a wide range of user interactions and ensuring that the conversation remains relevant and engaging.

![](https://files.readme.io/41e599ea17516962616cc46ddaad9675465ec9820f6da1f94cb0fef7257b44d6-image.png)

## How Events Work in Voiceflow

Events in Voiceflow are custom triggers that you define and are initiated by the client application sending a request to the Voiceflow dialog manager. Here’s how the process works:

1. **Event Definition**: You create events in the **Event CMS**, specifying request name and descriptions that represent particular triggers.
2. **Association with Workflows**: You assign these events to specific flows in your agent, using the **Event** trigger in the Trigger step.
3. **Client-Side Triggering**: The client application sends a request to the Voiceflow Dialog Manager API, including the event name and any necessary data.
4. **Workflow Initiation**: The runtime processes the event request and initiates the corresponding flow within your agent.

This event-driven approach enhances your agent’s ability to interact based on user actions within the client application, making it more intelligent and adaptable.

---

## Why Use Events?

**Expanding Interaction Footprint**

Events allow your agent to respond to specific actions taken by the user within your application or platform. For example, when a user clicks a “Help” button, the client can trigger an event to initiate a support conversation with the agent.

**Creating Contextual Experiences**

By responding to events, your agent can provide contextually relevant interactions based on what the user is doing in your application.

**Streamlining User Flows**

Events enable your agent to assist users at critical points in their journey, providing guidance, confirmations, or additional information exactly when needed.

### Examples of How Events Can Be Used

**Scenario 1: User Clicks a Checkout Button**

* **Event**: `InitiateCheckout`
  + **Trigger**: The user clicks the “Checkout” button in your e-commerce app or website.
  + **Action**: The application sends an event request to the Voiceflow dialog manager with the event name `InitiateCheckout`.
  + **Agent Action**: The agent initiates a workflow to assist the user with the checkout process, such as confirming the items, offering shipping options, or applying discounts.
* **Workflow Message Example**:
  + **Agent**: “You’re ready to check out! Would you like to review your order or proceed to payment?”

  

**Scenario 2: In-App Feature Usage**

* **Event**: `FeatureTutorialStart`
  + **Trigger**: The user accesses a new feature for the first time.
  + **Action**: The application detects this and sends an event request named `FeatureTutorialStart`.
  + **Agent Action**: The agent begins a flow to guide the user through a tutorial of the new feature.
* **Workflow Message Example**:
  + **Agent**: “I see you’re exploring our new dashboard. Would you like a quick tour to get familiar with its capabilities?”

  

**Scenario 3: User Sends a Command in a Messaging App**

* **Event**: `ShowRecentTransactions`
  + **Trigger**: In a messaging platform like Slack or Telegram, the user types a specific command, such as /recent\_transactions.
  + **Action**: The messaging platform sends an event request to the agent with the event name `ShowRecentTransactions`.
  + **Agent Action**: The agent retrieves and presents the user’s recent transactions.
* **Workflow Message Example**:
  + **Agent**: “Here are your most recent transactions: [list of transactions]. Do you need help with anything else?”

  

**Scenario 4: User Navigates to a Specific Page**

* **Event**: `PageVisitPricing`
  + **Trigger**: The user navigates to the pricing page on your website.
  + **Action** : The website detects the page change and sends an event request named `PageVisitPricing`.
  + **Agent Action**: The agent offers assistance related to pricing, such as explaining different plans or answering FAQs.
* **Workflow Message Example**:
  + **Agent**: “Looking at our pricing options? I’m here to help if you have any questions about our plans.”

---

## Learn more

* **[Using Events](/docs/using-the-events-cms)**: Learn how to use the events via API or Web chat.

Updated 5 months ago

---

[Components](/docs/components)[Using Events](/docs/using-the-events-cms)

Ask AI

* [Table of Contents](#)
* + [How Events Work in Voiceflow](#how-events-work-in-voiceflow)
  + [Why Use Events?](#why-use-events)
  + - [Examples of How Events Can Be Used](#examples-of-how-events-can-be-used)
  + [Learn more](#learn-more)