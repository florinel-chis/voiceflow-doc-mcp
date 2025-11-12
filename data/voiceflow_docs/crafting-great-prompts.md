---
category: general
scraped_at: '2025-11-12T14:07:41.767898'
title: Crafting great prompts
url: /docs/crafting-great-prompts
---

# Crafting great prompts

Learn how to build great prompts in Voiceflow.

## Crafting great prompts

A great resource for learning how to prompt is [Learn Prompting](https://learnprompting.org/).

They put forward the following framework for what makes a good prompt. It’s worth noting, that for a prompt to be ‘good’ it doesn’t require all of these elements. Indeed, if the prompt is simple it may only require one, or two of these elements. However, as your prompts get more and more complex, you will start to see the need to include more of these elements:

* **Instruction:** Clear directions on what to do
* **Context:** Relevant background information
* **Role:** Assigning a specific role to the AI (e.g., "Act as a French teacher")-
* **Examples:** Demonstrations of desired output
* **Formatting:** Specifying how the output should be structured
* **Tone:** Indicating the desired style or mood of the response

### Example of a great prompt

The following prompt is designed to generate a single, clear clarifying question based on a user's initial query, a previous check that has determined a clarifying question is required, and a knowledge base retrieval stored in ‘chunks’.

```
Given the guidelines provided in 'clarifying question check' as`{clarifyingQuestionCheck}`,
the user's question stated in `{userQuestion}`, and the information in 'chunks' as `{chunks}`, 
your task is to construct a single, clear clarifying question.

This question should smoothly integrate the details provided and guide the user towards providing a 
precise response. 

Your clarifying question is crucial for offering a helpful and direct answer,
focusing on a single aspect that needs clarification. 

Instructions:  
Output one clear clarifying question that integrates the user's query and provided details.  
Focus on a single aspect that requires clarification to ensure the response is helpful and direct.

Avoid multiple or double-barreled questions.  

Ensure your question is concise, without any additional text or explanation. 

Examples:  
User: What phone plans do you have with 100 GBs of data?  
Bot: Are you interested in pre-paid or post-paid plans with 100 GBs of data?  
User: How do I check my email?  
Bot: Which device are you using to check your email, an Apple or an Android device?  
You must maintain a professional and friendly tone throughout your interaction.

Now, output the question and nothing else.
```

Let’s break down how it is using each of the elements.

#### Instruction:

The prompt begins with clear directives, setting the stage for what the AI needs to accomplish:

* Construct a single, clear clarifying question
* Integrate details from the user's query and provided information
* Focus on a single aspect that needs clarification
* Avoid multiple or double-barreled questions
* Ensure the question is concise, without additional text or explanation
* Output only the question, with nothing else

#### Context:

To ground the AI's understanding, the prompt provides essential background information:

* The prompt provides guidelines for clarifying questions ({clarifyingQuestionCheck})
* It references a user's initial question ({userQuestion})
* Additional information is provided in 'chunks' ({chunks})
* The purpose is to guide the user towards providing a more precise response

#### Role:

While not explicitly stated, the LLM is implicitly asked to act as a customer service or information retrieval assistant

Examples:

To illustrate the desired output, the prompt includes concrete examples.

```
User: "What phone plans do you have with 100 GBs of data?"  
Bot: "Are you interested in pre-paid or post-paid plans with 100 GBs of data?"  
User: "How do I check my email?"  
Bot: "Which device are you using to check your email, an Apple or an Android device?"
```

#### Formatting:

The prompt outlines specific structural requirements for the AI's response:

* The output should be a single question
* No additional text or explanation should be included

#### Tone:

To ensure the right communication style, the prompt specifies the desired tone:

* The prompt specifies to "maintain a professional and friendly tone throughout your interaction"

## The prompting process

Interacting with Large Language Models (LLMs) is an art that goes beyond simple question-asking. It involves crafting prompts that effectively guide the model to produce desired outputs. The process is iterative, combining creativity with systematic refinement. It’s because of this, that we prefer to call it prompting or prompt design (rather than, prompt engineering).

The process typically involves four main stages: Design, Test, Refine, and Repeat.

### Design

This stage is about setting the foundation. Here, you'll translate your goals into a structured prompt. Consider these key elements in the design phase:

* **Define your objective clearly:** What specific outcome are you seeking?
* **Incorporate key elements:** Include instructions, context, role, examples, formatting, and tone as appropriate.
* **Consider the LLM's capabilities:** Tailor your prompt to what you know the model can do.
* **Start broad:** Begin with a more general prompt that you can refine later.
* **Choosing the right model for the job:** Is your task complex, and therefore requires a more expensive model? Or, could you potentially break up your prompt into bite sized chunks, and use a faster, and less expensive model?

### Test

It's time to put your prompt to work. Feed it to the LLM and carefully observe the results. Keep these factors in mind during the testing phase:

* **Generate multiple responses:** LLMs can produce different outputs for the same prompt, so test a few times.
* **Vary input slightly:** Try minor variations of your prompt to see how it affects the output.  
  Test edge cases: Consider extreme or unusual scenarios related to your prompt.

### Refine

With test results in hand, it's time to analyze the output and make necessary adjustments. Focus on these aspects during the refinement process:

* Evaluation of responses: Do they meet your objectives? Are they accurate, relevant, and appropriate?
* Look for patterns: Look for consistent strengths or weaknesses in the outputs.
* Pinpoint areas for improvement: Is the LLM misunderstanding certain aspects? Is it providing irrelevant information?
* Adjust your prompt: Based on your analysis, modify elements of your prompt. This might involve:
  + Clarifying instructions
  + Providing more context
  + Adjusting the role or tone
  + Adding or modifying examples
  + Changing the formatting requirements

### Repeat

Prompt engineering thrives on iteration. Continue the cycle of testing and refining to achieve the best possible outcomes. Consider these points as you repeat the process:

* **Iterate through the process:** Design -> Test -> Refine -> Repeat
* **Track changes:** Keep a record of your prompt variations and their results.
* **A/B testing:** Compare different versions of your prompt to see which performs better.
* **Gradual refinement:** Make incremental changes rather than wholesale revisions.
* **Set a threshold:** Determine what level of performance is "good enough" for your needs.
* **Consider diminishing returns:** At some point, further refinement may yield minimal improvements.

Updated 5 months ago

---

[Types of prompts](/docs/types-of-prompts)[Prompting](/docs/prompting)

Ask AI

* [Table of Contents](#)
* + [Crafting great prompts](#crafting-great-prompts)
  + - [Example of a great prompt](#example-of-a-great-prompt)
  + [The prompting process](#the-prompting-process)
  + - [Design](#design)
    - [Test](#test)
    - [Refine](#refine)
    - [Repeat](#repeat)