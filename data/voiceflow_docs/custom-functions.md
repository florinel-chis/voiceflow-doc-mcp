---
category: general
scraped_at: '2025-11-12T14:07:55.639204'
title: Introduction to developing functions
url: /docs/custom-functions
---

# Introduction to developing functions

In Voiceflow, functions allow you to create reusable, user-defined steps that can perform tasks ranging from simple text manipulation to making complex API calls. Functions are written in JavaScript (ES6 on V8).

## Example functions

**Extract Chunks from a Knowledge Base Response:**[Click to Download](https://drive.google.com/uc?export=download&id=15t2e-Rei3Pj-xbqezjo6qNYe9N04pEwA)

**Send a Query to Mistral 7xB and Parse Answer (via. together.ai):** [Click to Download](https://drive.google.com/uc?export=download&id=1d2nRcmVXYVzdmyYhBwKjTQLHbo9HH9VM)

**The function** [marketplace](https://www.voiceflow.com/resources-template?products=Function) :You can find a large collection of Voiceflow and community-made functions on our marketplace that you can study for inspiration and code formatting.

# Overview

The Functions page in Voiceflow serves as a central hub for managing custom functions that enhance the capabilities of your AI agent. Here, you can create, edit, and organize functions that execute specific logic or calculations based on user inputs or other data.

![](https://files.readme.io/85f5e0f-image.png)

## To create a function

1. In the Function page, **click on the "New function"** button in the upper right area of the screen.
2. A modal will appear prompting you to enter details for the new function.
3. **Enter a name** for the function in the "Name" field—choose a name that clearly represents the function's purpose, such as "Create Ticket".
4. **Provide a description** in the "Description" text box, which explains the function's purpose, like "This function will create a Zendesk ticket." The function description will be displayed on the function step editor when used on canvas for designer visibility.
5. Once all information is entered, **click "Create function"** to save the new function.

## Configure a function

![](https://files.readme.io/30ea6cb-image.png)

1. Once created, you can define the function's logic within the editor. You can learn more about how to write function code in the sections below.
2. On the right editor, you should see the **input variables**, **output variables**, and **paths** sections. Input variables, output variables, and paths define the function interface that a designer would interact with to use your function as a step.
3. **Input Variables**:
   1. Adding Variables: You can define input variables that the function will accept. These are the data points you provide to the function for processing.
   2. Instructions: For each input variable, you can add instructions that describe the variable's purpose or provide guidance on the type of data expected, available as a Builder note on-canvas.
4. **Output Variables**:
   1. Defining Outputs: Output variables are where you specify what data the function will return after processing. These variables can be used in subsequent steps of your conversation flow.
   2. Instructions: Just like with input variables, you can provide instructions or a description for each output variable, ensuring users understand what data will be provided.
5. **Paths**:
   1. Creating Execution Paths: Paths allow you to define different execution flows based on the function's output. You can specify multiple paths for different scenarios or outcomes of the function.
   2. On-Canvas Labels: Each path can be given an on-canvas label, which serves as a visual cue on the design canvas, helping users understand where each path leads.
6. **Description**: The description section is where you provide a high-level overview of what the function does. This should be a clear and concise explanation to ensure that anyone using the function can understand its intended purpose and the context in which it should be used.
7. **Image**: You can upload or select an image to represent your function visually. This image will appear as an icon on the design canvas, making it easier to identify the function at a glance and aiding in creating a more intuitive design experience.

# Best Practices

## Add designer-friendly documentation

Functions are intended to be build by code-literate developers and typically used by non-technical designers.

When building your function, **take advantage of the built-in documentation features**.

1. **Function description** - Use the Description field of a function definition to describe the purpose of a function, give some example use-cases, etc.
2. **Variable documentation** - Use the variable-level documentation fields to describe the purpose of a variable, the acceptable range of argument values, etc.
3. **Image** - Use the Image field of a function definition to provide a visual cue on the function’s purpose. Adding a unique icon to a function also helps with its readability as a step on the Voiceflow canvas.

Additionally, your documentation should be **aimed towards a non-technical audience**. It should use simple language that does not require an understanding of coding. This allows your function to be usable by a wider audience, as not everyone using Voiceflow is code literate.

---

### Learn more

* [Implementing Function Code](/docs/developing-functions-copy-1): Learn how to write function code, process inputs and outputs, and make network requests within Voiceflow.
* [Function Step](/docs/functions): Learn how to use the function step within your Voiceflow projects by visiting the Function Step documentation.
* [Voiceflow Marketplace](https://www.voiceflow.com/resources-template?products=Function): Discover pre-made functions and get inspiration from the Voiceflow Function Marketplace.

Updated 5 months ago

---

[Previewing Intent Classification and Improvements](/docs/previewing-intent-classification-and-improvements)[Implementing function code](/docs/developing-functions)

Ask AI

* [Table of Contents](#)
* + - [Example functions](#example-functions)
  + [Overview](#overview)
  + - [To create a function](#to-create-a-function)
    - [Configure a function](#configure-a-function)
  + [Best Practices](#best-practices)
  + - [Add designer-friendly documentation](#add-designer-friendly-documentation)