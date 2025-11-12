---
category: general
scraped_at: '2025-11-12T14:07:34.447559'
title: Prompts CMS
url: /docs/prompts-cms-and-editor
---

# Prompts CMS

> ❗️
>
> **This feature is part of the old way to build using Voiceflow.**
>
> Although this feature remains available, we recommend using the [Agent step](/docs/agents) and [Tool step](/docs/tool-step) to build modern AI agents. Legacy features, such as the Capture step and Intents often consume more credits and lead to a worse user experience.

  

The **Prompts CMS** is a centralized hub for creating, managing, and testing prompts used by your conversational agents. It offers a structured way to handle complex prompts, ensuring consistency and reusability across your projects. With the Prompts CMS, you can define sophisticated prompts that leverage system prompts, user-agent message pairs, variables, and more.

![](https://files.readme.io/55e9e1adcd558fdbcc116745a45ed1811f7571d59b40d8e36719aaf5f0d0fb13-CleanShot_2024-11-04_at_20.01.082x.png)

## Accessing the Prompts CMS

* **Open “Prompts”**: In the Agent CMS, choose **Prompts** to access the prompts management interface.

## Understanding the Prompts Table

The Prompts CMS displays a table listing all your prompts with the following columns:

* **Name**: The name of the prompt.
* **Description**: A brief description of the prompt’s purpose.
* **Used By**: Indicates where the prompt is used within your agent. This will include links to specific workflows and steps.
* **Last Editor**: The team member who last edited the prompt.
* **Updated**: The date and time when the prompt was last modified.

![](https://files.readme.io/f9bd0069818a2df27b069161ff1690612063dfeb3d41e731b687e2a2e7055c87-CleanShot_2024-11-04_at_19.52.522x.png)

## Creating a New Prompt

**1. Start the Creation Process**

* **Click “New Prompt”**: Located at the top-right corner of the Prompts table.

**2. The Prompt Editor**

* Upon clicking, the **Prompt Editor** appears with two main sections:
  + **Left Side (Prompt Definition)**: Where you define and configure your prompt.
  + **Right Side (Output Preview)**: Displays the generated output when you test the prompt.

**3. Configuring the Prompt**

* **Prompt Name**: Enter a clear and descriptive name for your prompt.
* **Description** (Optional): Provide additional details about the prompt’s purpose.

![](https://files.readme.io/841ea77294ba5727123478863c7d121b2ca665da7e43f7e5a2ca380239462d87-CleanShot_2024-11-04_at_20.09.452x.png)

## Prompt Configuration

### System Prompt

* **Purpose**: Sets the overall behaviour or guidelines for the AI model.
* **Usage**: Click on the **System Prompt** box to enter your instructions.

![](https://files.readme.io/0137cfda5496136e9dd4574a9404d2fbcf569794f039968855d03cfc5e60a3d4-CleanShot_2024-11-04_at_20.26.272x.png)

### User and Agent Messages

* **User Prompt**: The initial message from the user.
* **Adding Message Pairs**:
  + **Click “Add”**: Choose **Add Message Pair**.
  + **New Boxes Appear**: An **Agent** box and a **User** box are added.
    - **Enter Messages**: Fill in the agent’s response and the user’s subsequent input.
* **Deleting Message Pairs**:
  + **Deleted Together**: Message pairs are added and deleted as a unit.

![](https://files.readme.io/3fbe739b7c1945c23ef6973522a7b7558c63c2e7bb00c5644d3c9a446b25a129-CleanShot_2024-11-04_at_20.29.182x.png)

### Conversation History

* **Add Conversation History**:
  + **Click “Add”**: Choose **Add Conversation History**.
  + **Voiceflow Memory Variable**: A special block representing `vf_memory` is inserted.
* **Placement**:
  + **Drag and Drop**: Move the conversation history block to the desired position within your prompt.

![](https://files.readme.io/6f35155ee4baeb77a94043d7c9462af0cf3541ac8106cec50e1c16a29a7fafa4-CleanShot_2024-11-04_at_20.32.562x.png)

## Prompt Variables

* **Access Variables**: Click on the **Variables** button in the header.
* **Manage Variables**:
  + **View Used Variables**: Displays all variables referenced in your prompt (e.g., {agent\_persona}).
  + **Set Test Values**: Enter values for these variables to test how the prompt behaves with different inputs.
* **Usage in Prompt**:
  + **Syntax**: Use curly braces {} to include variables in your prompt.
    - **Example**: “As a helpful assistant named {agent\_persona}, I will…”

![](https://files.readme.io/cdd8a792a6da9d790b2164d163948df9f2e205c4bb5a035063466cd2234b45ca-CleanShot_2024-11-05_at_11.29.212x.png)

## Prompt Settings

* **Access Model Settings**: Click on the **Settings** button in the header.
* **AI Model Selection**: Choose the AI model to use for generating responses.
* **Temperature**: Adjust the creativity level of the AI’s output.
* **Max Tokens**: Set the maximum length of the generated response.

![](https://files.readme.io/5e4dec822524cd57a05745bdcdc6e4096799fed36752ea84bd13ff5072ae2fac-CleanShot_2024-11-04_at_20.34.322x.png)

## Using Structured Outputs

Structured Outputs allow you to define the format of the data you expect the AI to return when using the Prompt step. This gives you more control and predictability over the generated responses.

**Enabling Structured Outputs**

1. **Select a Prompt**: In the Prompt step editor, choose the prompt you want to use.
2. **Open Prompt Settings**: Select the Settings tab
3. **Enable JSON Output**: In the prompt settings, toggle on the "JSON Output" option.
4. **Define Output Structure**: Specify the expected structure of the AI's response using the JSON Schema format. This includes defining the data types, required properties, and any additional constraints.
5. **Test**: Run prompt in the editor to confirm response generated per expected and no errors are present in the output structure.

**Example Output Format Definitions**

Here are a couple of examples showcasing how you can define the output format using JSON Schema:

*Example 1: Sentiment Analysis*

JSON

```
{
  "type": "object",
  "required": [
    "sentiment"
  ],
  "properties": {
    "sentiment": {
      "enum": [
        "happy",
        "neutral",
        "sad"
      ],
      "type": "string"
    }
  },
  "additionalProperties": false
}
```

In this example, the output format specifies that the AI should return an object with a single required property called `sentiment`. The `sentiment` property is a string that must be one of the enumerated values: "happy", "neutral", or "sad".

*Example 2: Problem Solving Steps*

JSON

```
{
  "type": "object",
  "properties": {
    "steps": {
      "type": "string",
      "description": "A single string where each step is separated by a comma. Each step includes 'explanation' and 'output' concatenated with a colon. Never use double quotes in the string."
    },
    "final_answer": {
      "type": "string",
      "description": "The final answer to the problem as a string."
    }
  },
  "required": [
    "steps",
    "final_answer"
  ],
  "additionalProperties": false
}
```

This example defines an output format where the AI should return an object with two required properties: `steps` and `final_answer`. The `steps` property is a string containing problem-solving steps, with each step separated by a comma and including an explanation and output. The `final_answer` property is a string representing the final answer to the problem.

**Working with Structured Outputs**

* **Accessing Response Data**: The AI-generated response will adhere to the defined structure.
* **Dot Notation**: Access specific properties of the structured response using dot notation (e.g., `response.propertyName`).
* **Conditional Logic**: Use the structured data to create conditional paths in your workflow based on the AI's response.

**Supported Data Types**

At launch, Structured Outputs support the following data types:

* String
* Number
* Boolean
* Integer
* Enum
* Arrays
* Objects

**Model Compatibility**

Structured Outputs are currently available with the `gpt-4o-mini`, `gpt-4o` and `o3-mini` models.

## Testing Your Prompt

**Running the Prompt**

* **Click “Run”**: Located within the Prompt Editor.
* **View Output**: The right side displays the AI-generated response based on your prompt and variable values.

**Monitoring Performance**

* **Tokens Consumed**: Displayed at the footer, shows the total tokens used.
  + **Detailed View**: Hover over to see a breakdown of input and output tokens.
* **Latency**: Shows the time taken to generate the response.

![](https://files.readme.io/41ba9d57827cd07fecd05d710a6935a8a828bcfcc465e444964eec8c69bde383-image.png)

**Iterating**

* **Adjust Variables**: Change values in the Variables tab to test different scenarios.
* **Modify Prompt**: Edit the prompt content to refine the output.
* **Re-run Tests**: Click “Run” again to see updated results.

## Best Practices for Creating Prompts

**Use Clear and Descriptive Names**

* **Ease of Selection**: Makes it easier to identify the prompt when using the Prompt Step.
* **Organization**: Helps manage prompts as your collection grows.

**Leverage Message Pairs**

* **Context Building**: Simulate conversation history to provide context to the AI.
* **Improved Responses**: Leads to more accurate and relevant outputs.

**Keep Prompts Modular**

* **Reusability**: Design prompts that can be used in multiple contexts.
* **Maintainability**: Easier to update and manage over time.

---

## Learn more

* [Prompt step](/docs/prompt-step): Learn how to integrate prompts directly into your agent’s flow.
* [Set step](/docs/variables-set): Discover how to dynamically assign prompt outputs to variables for greater control over agent behaviour.

Updated about 1 month ago

---

[Agent content](/docs/agent-content)[Prompt Library](/docs/prompt-library)

Ask AI

* [Table of Contents](#)
* + [Accessing the Prompts CMS](#accessing-the-prompts-cms)
  + [Understanding the Prompts Table](#understanding-the-prompts-table)
  + [Creating a New Prompt](#creating-a-new-prompt)
  + [Prompt Configuration](#prompt-configuration)
  + - [System Prompt](#system-prompt)
    - [User and Agent Messages](#user-and-agent-messages)
    - [Conversation History](#conversation-history)
  + [Prompt Variables](#prompt-variables)
  + [Prompt Settings](#prompt-settings)
  + [Using Structured Outputs](#using-structured-outputs)
  + [Testing Your Prompt](#testing-your-prompt)
  + [Best Practices for Creating Prompts](#best-practices-for-creating-prompts)
  + [Learn more](#learn-more)