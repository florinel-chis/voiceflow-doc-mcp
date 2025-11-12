---
category: general
scraped_at: '2025-11-12T14:07:00.333435'
title: Prompt step
url: /docs/prompt-step
---

# Prompt step

Use AI to generate a single message inside a workflow.

![](https://files.readme.io/3dec4418994820012e8a1be5ba75458022e0ac7a8f4651020b332a83fac576b9-Prompt_1.png)
  

The Prompt step allows your agent to generate responses to a user's message using an LLM. It’s useful for injecting AI into a specific point in your flow, such as generating product suggestions, summarizing information, or rephrasing user input. Each time the prompt step is used, it will generate a single response.

  

## When to use the Prompt step

The prompt step is only recommended for specific situations. If you're looking to build a fully agentic conversational agent, we recommend using the [Agent step](/docs/agents) instead. If you'd like to set a variable to the result of a prompt, use the [Set step](/docs/variables-set).

Here are some situations where the Prompt step might be a good fit:

* Searching the Knowledge Base using the [KB Search step](/docs/kb-search), then summarizing the output using a prompt step. This should only be done if the [Agent step](/docs/agents)'s built in Knowledge Base search doesn't meet your needs.
* Adding LLM-generated responses to a deterministic flow. For example, if you have a calculator that must follow specific steps in order for compliance reasons, you could build these with the [Set step](/docs/variables-set) and [Condition step](/docs/logic), then use the Prompt step to summarize the result.

  

## Basic usage

To use the prompt step, add it to the canvas, connect it to a previous step, then select the prompt you'd like to use with it. If you don't already have a prompt created in your project, you'll be prompted (😉) to create one. We recommend using the templates provided at the bottom of the prompt window as a starting point.

[](https://yz5du1veb1.ufs.sh/f/9fKud4NeF5NSzVYvHMyQXUw9e3lryuWbOH7E5ApCIBaitDYK)

  

## Advanced usage

After you've created a prompt, you can optionally change the model (LLM), temperature, and max tokens settings that should be followed by this step. You can also test the prompt from within the prompt window.

We recommend experimenting with different settings prior to launching your agent into production. Please note that different models cost a varying number of credits - learn more on our [pricing page](/docs/credits-pricing-table).

[](https://yz5du1veb1.ufs.sh/f/9fKud4NeF5NS2JYZY9gQD9nLFZ4JORio7WdbTegAGUcvxfw6)

Updated 4 months ago

---

[Message step](/docs/message)[Image step](/docs/images)

Ask AI

* [Table of Contents](#)
* + [When to use the Prompt step](#when-to-use-the-prompt-step)
  + [Basic usage](#basic-usage)
  + [Advanced usage](#advanced-usage)