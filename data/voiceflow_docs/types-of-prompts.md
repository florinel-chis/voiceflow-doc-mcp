---
category: general
scraped_at: '2025-11-12T14:07:39.919088'
title: Types of prompts
url: /docs/types-of-prompts
---

# Types of prompts

Learn the different types of LLM prompts.

## Common types of prompts

### Zero-shot prompting

This involves asking the model to perform a task without any examples. For instance:

**Prompt:**

```
Translate the following English text to French: 'Hello, how are you?'
```

**LLM Response:**

```
Bonjour, comment allez-vous?
```

### Few-shot prompting

In Few-shot prompting, you provide a few examples before asking the model to perform a similar task. For example:

**Prompt**

```
Translate English to French:  
English: Good morning  
French: Bonjour  
English: How are you?  
French: Comment allez-vous?  
English: What's your name?  
French:
```

**LLM Response:**

```
French: Comment vous appelez-vous?
```

### Chain of Thought (COT)

Chain of Thought (COT) prompting gives prompts the model to show its reasoning process. For example:

**Prompt**

```
You have a jar of 50 marbles.
You take out 10 marbles and give them to your friend. 
Then, you decide to add 20 more marbles to the jar.
After that, you take out 15 marbles to play a game.
How many marbles are left in the jar?
Let's go through it step by step.
```

**LLM Response:**

```
To find out how many marbles are left in the jar, let's go through the steps:

You start with 50 marbles.  
You take out 10 marbles, leaving 50 - 10 = 40 marbles.  
You add 20 more marbles, increasing the total to 40 + 20 = 60 marbles.  
You take out 15 marbles, leaving 60 - 15 = 45 marbles.

So, there are 45 marbles left in the jar.
```

### Few-shot Chain of Thought Prompting

Few-shot Chain of Thought Prompting combines few-shot prompting with COT. You provide examples of step-by-step reasoning before asking the model to solve a problem.

**Prompt:**

```
//Example//  
Q: You have a jar of 50 marbles. 
You take out 10 marbles and give them to your friend.
Then, you decide to add 20 more marbles to the jar. 
After that, you take out 15 marbles to play a game. 
How many marbles are left in the jar?  
A: You started with 50 marbles. 
Giving 10 to your friend leaves you with 40. 
Adding 20 more gives you 60. 
Taking out 15 for the game leaves you with 45 marbles.  
//End Example//  
Q: You have a box of 60 chocolates. 
You eat 5 chocolates and then share 10 chocolates with your friends. 
Later, you receive 15 more chocolates as a gift. 
However, you decide to give away 8 chocolates to your siblings. 
How many chocolates do you have left in the box?  
A:
```

**LLM Response:**

```
You began with 60 chocolates. 
Eating 5 leaves you with 55. 
Sharing 10 with your friends brings the total down to 45. 
Receiving 15 more chocolates as a gift brings it back up to 60. 
Giving away 8 chocolates to your siblings leaves you with 52 chocolates remaining in the box.
```

Updated 5 months ago

---

[Prompt Library](/docs/prompt-library)[Crafting great prompts](/docs/crafting-great-prompts)

Ask AI

* [Table of Contents](#)
* + [Common types of prompts](#common-types-of-prompts)
  + - [Zero-shot prompting](#zero-shot-prompting)
    - [Few-shot prompting](#few-shot-prompting)
    - [Chain of Thought (COT)](#chain-of-thought-cot)
    - [Few-shot Chain of Thought Prompting](#few-shot-chain-of-thought-prompting)