---
category: general
scraped_at: '2025-11-12T14:06:57.215140'
title: Agent step
url: /docs/agents
---

# Agent step

Handle user input, search the knowledge base, call tools, and follow exit conditions — all in one step

![](https://files.readme.io/96eec3b6b1ff9caa0bd5f670d8bfe0fa144af6b3fab6328228fd0851346ed182-Image_11.png)

The Agent step is a flexible all-in-one tool that lets your assistant interpret user input using AI, access your knowledge base, route the conversation based on intent, and run external functions — all within a single step.

Use it when you want the agent to handle an open-ended request without needing to manually define each path ahead of time.

## Introduction to the Agent step

The Agent step provides a comprehensive solution for creating AI agents that can:

* Intelligently respond to user queries
* Search knowledge base for relevant information
* Follow specific conversation paths based on user intent
* Execute functions to interact with external services

**To add an Agent step to your canvas:**

1. Look for the "Agent" option in the top left corner of the Voiceflow canvas
2. Drag this step onto your canvas
3. Choose an existing agent, create a new agent or search for community-created agents

## Prompting Your Agent

Effective prompting is the foundation of a successful agent. The instructions you provide serve as the agent's "brain" and determine how it will interact with users:

* **Clear Directives**: Be specific about your agent's role and how it should respond in different scenarios
* **Personality Design**: Define your agent's tone, level of formality, and communication style
* **Knowledge Parameters**: Indicate what domain knowledge your agent should rely on and when it should search external resources
* **Context Awareness**: Include instructions for handling sensitive topics or escalating to human support when necessary

> 👍
>
> ### Create an effective prompt.
>
> Learn more about crafting great prompts [here](/docs/crafting-great-prompts)

Good prompting helps your agent understand what information to prioritize, when to use the knowledge base, and how to respond to user queries in a consistent manner. Taking time to craft detailed, thoughtful instructions will dramatically improve your agent's performance and reduce the need for additional steps in your flow.

For example, instead of simply saying "This is a support agent," you might specify: "You are a friendly e-commerce support agent that helps customers with order tracking, returns, and account issues. Maintain a positive tone, offer proactive suggestions, and provide specific details when available."

## [Integrations](/docs/integrations#/)

Integrations are native connections to popular third-party platforms. These require minimal setup and expose helpful, opinionated actions specific to each tool.

### Supported Integrations & Common Use Cases:

| Integration | Use case |
| --- | --- |
| Zendesk | Look up or create support tickets, fetch user info. |
| Shopify | Get contact, lead, or opportunity data, update CRM records. |
| Google Sheets | Check orders, fetch product details, initiate returns. |
| Gmail | Send transactional or templated emails. |
| Airtable | Query tables, update or add records, track interactions. |
| Make.com | Trigger custom workflows, connect to 1000+ apps. |
| Twilio | Send SMS or make calls with custom logic. |
| Hubspot | Create or update CRM contacts, log conversation outcomes. |

![](https://files.readme.io/1ba143caec56c024d2dc331bedc2e4aee95dca847705d6213b80d9943fddefb2-CleanShot_2025-07-29_at_14.44.212x.png)

## Functions

Functions allow your agent to connect with external services and retrieve or update data. Based on the UI screenshot, configuring a function in an Agent Step involves several important components:

### Function Configuration:

1. **Select Function**: Choose from available functions in the dropdown menu
2. **LLM Description**: This is critical - you need to tell the LLM when and how to use this function

![](https://files.readme.io/24eac212512d887b57d7475185ec621172dad9ffc4ab27ddac69d91c71397a73-CleanShot_2025-07-29_at_15.12.312x.png)

### LLM Description:

The `LLM Description` field is where you provide detailed instructions that help the LLM understand:

* When to call this function
* What the function does
* What information is needed to use it

For example, for an order lookup function:

> **LLM Description**: "Use this function to retrieve a customer's order details from Shopify when they ask about their order status, delivery date, shipping address, or tracking information. This function requires a valid order ID to proceed. Only call this function when the customer explicitly mentions needing information about a specific order they've placed."

### Input Variable Configuration:

For each input variable your function requires:

1. **Variable Name**: Set a clear, descriptive name (shown as "orderID" in the UI example)
2. **Variable Description**: Explain what this variable represents and how to collect it
3. **Default Value**: Optionally provide a default value

### Variable Description:

The description for each input variable helps the LLM understand:

* What information to collect
* How to validate it
* When to request it from the user

For example, for an Order ID variable:

**LLM Variable Description**: "This variable should contain the customer's order ID. Valid order IDs are 10-digit numbers that start with 'ORD-'. If the customer doesn't provide their order ID initially, ask them for it. If they don't know their order ID, ask if they have a confirmation email where they can find it."

**Default Value**: You can optionally set a default value, but for user-specific information like order IDs, this field is typically left empty.

> #### Order Lookup Function (Example)
>
> **Function Name**: Get Order by ID
> **LLM Description**: "Use this function to retrieve a customer's order details from Shopify when they ask about their order status, delivery date, shipping address, or tracking information. The function requires a valid order ID to proceed."
>
> **Input Variable Name**: orderID
> **LLM Variable Description**: "The customer's order ID. This should be a 10-digit number that starts with 'ORD-'. Ask the customer to provide this number if they haven't already."

## Exit conditions

Exit conditions allow your agent to handle specific conversation flows and take appropriate actions:

* **Automatic Routing**: The agent detects user intent and automatically routes to the appropriate path
* **Variable Collection**: You can require specific data to be collected before entering a path
* **Seamless Integration**: Paths work within natural conversation, without requiring specific commands

When an exit condition is triggered, the Agent step will still retain the full conversation context. This means you can route the user through another part of your flow- such as a component or custom action- and then **return to the Agent step** *without losing memory* of the conversation.

[](https://w17llroiln.ufs.sh/f/JH4JLc5mceYks8l3KfGlT9yobAZqe36tMHzS78D0muRx2fLJ)

### Exit condition examples:

> **Exit condition name**: Process Order Return
> **Description**: "Trigger this path when the user wants to return an item they purchased, expresses dissatisfaction with their order, mentions that an item is defective, or asks about the return policy. The user might use phrases like 'I want to return', 'how do I send this back', 'my product is broken', or 'does this have a warranty'."
>
> **Required Variable**: orderID
> **LLM Variable Description**: "This variable should contain the order ID that the customer wants to return. Valid order IDs are 10-digit numbers. If the user doesn't provide their order ID initially, ask them for it. Make sure to verify that the provided ID matches the expected format before proceeding with the return pr

> 👍
>
> ### Tip: create looping workflows and return the Agent step.
>
> You can create looping workflows that exit the Agent step and later return to it while preserving context.
>
> For example:
>
> > Agent step → Exit condition → Menu carousel component → Agent step
>
> [](https://w17llroiln.ufs.sh/f/JH4JLc5mceYkyY4Nk23hfmDYQGEyVntJoqO8RAc1Idsg7ezb)
>
> This is useful for triggering custom workflows or components (e.g., static card/carousel components, feedback forms, navigation menu, etc) before returning and resuming the original conversation flow. Memory limits still apply, so older messages will eventually be dropped.

## Knowledge Base

When you enable knowledge base integration, your agent can automatically search for information it doesn't know:

* **Automatic Queries**: Your agent will search the knowledge base without requiring a separate search step
* **Contextual Responses**: The agent intelligently combines its built-in knowledge with information from your knowledge base
* **Knowledge Weighting**: You can adjust how much the agent relies on its built-in knowledge versus your knowledge base through the instructions

For example, if a user asks about a password reset but that information isn't in your knowledge base, the agent can provide general guidance. But when asked about email confirmation—which is in your knowledge base—it can provide specific, accurate information from your documentation.

![](https://files.readme.io/690a1fde9e1a9df1786ef65aa0fd4862b4d6ecbe6793df7d2d3646d323bb0749-CleanShot_2025-07-29_at_15.26.252x.png)
> 📘
>
> ### Ensure knowledge base is toggled on!
>
> Your agent can only have access to your knowledge base if the tool is toggled on the agent step.

## Agent-generated components

The Agent step in Voiceflow allows agents to **dynamically** generate components in real time during a conversation. These components- **Buttons, Cards, and Carousel**- can be toggled on to let the agent include them in its replies. Once enabled, the agent will reference your prompt to determine how and when to use them.

> 🚧
>
> For best results, we suggest you use the available **Anthropic models**(Claude 4, Claude 3.7 Sonnet, Claude 4 Opus, etc). OpenAI and other lower end LLM models reportedly face issues rendering and executing agent-generated components.

> 👀
>
> **Important**: These components will only be generated if you explicitly instruct the agent to use them in the prompt. The more specific you are, the better. **Only chat interface agents** using the Agent step can dynamically generate these components.

ButtonsCardsCarousel

### Button step

Buttons allow your agent to offer **clickable response options** to the user. When a user clicks a button, it's treated as if they typed the button label as a message—triggering the next appropriate step in the flow.

**Use case**: Great for quick selections, confirming decisions, or giving a few directions without overloading the user with text.

**Example prompt:**

```
Offer the user three clear options after they describe their issue. Display buttons labeled "Speak to support", "Check order status", and "Return a product". When the user clicks one, treat it as if they typed it, and respond accordingly with follow-up questions or solutions based on their selection.
```

![](https://files.readme.io/cea9cb4921ad883e8ec018bdf0bed2ec92ef988d99c3f759106d95efbace173c-CleanShot_2025-08-05_at_14.24.382x.png)

  

## Advanced Usage

For even more powerful implementations:

* **Multiple Agent steps**: Chain several Agent steps together for complex workflows
* **Custom Functions**: Develop your own functions to connect with any service your business uses
* **Prompt Refinement**: Continuously refine your agent's instructions based on conversation logs and user feedback

Updated about 1 month ago

---

[Steps](/docs/steps-1)[Message step](/docs/message)

Ask AI

* [Table of Contents](#)
* + [Introduction to the Agent step](#introduction-to-the-agent-step)
  + [Prompting Your Agent](#prompting-your-agent)
  + [Integrations](#integrations)
  + - [Supported Integrations & Common Use Cases:](#supported-integrations--common-use-cases)
  + [Functions](#functions)
  + - [Function Configuration:](#function-configuration)
    - [LLM Description:](#llm-description)
    - [Input Variable Configuration:](#input-variable-configuration)
    - [Variable Description:](#variable-description)
  + [Exit conditions](#exit-conditions)
  + - [Exit condition examples:](#exit-condition-examples)
  + [Knowledge Base](#knowledge-base)
  + [Agent-generated components](#agent-generated-components)
  + [Advanced Usage](#advanced-usage)