---
category: general
scraped_at: '2025-11-12T14:08:33.840341'
title: Memory
url: /docs/memory
---

# Memory

Memory allows your agent to remember past interactions, making conversations feel more natural and context-aware, rather than treating each prompt in isolation. Voiceflow automatically manages this memory, letting agents recall past exchanges and respond accordingly.

# Automatically Managed Memory

Voiceflow automatically keeps track of memory of the conversation in a string variable called `vf_memory`, generated based off an internal representation stored in an object variable called `_memory_`.

By default, it stores the last 25 turns of the conversation (so the agent speaking once is a turn, and then the user answering is another turn), each in their own line, labelled `assistant` and `user`. For example:

Text

```
assistant: Hi there
user: how are you doing
assistant: I'm an AI, so I don't have feelings, but I'm here to help you. How can I assist you today?
user: are mangoes tasty
assistant: Yes, mangoes are often known for their delicious taste.
```

# Prompt conversation history

You can add the memory to any prompt in the prompt CMS through the Add conversation history button. You can also reference the variable anywhere with `{vf_memory}`.

![](https://files.readme.io/002fa9f0006f4f75338fbd3da5d0f5052e6b97bda3d4d20e887f567260e278ab-image.png)

The `vf_memory` variable is also what powers the [agent step’s](/docs/agents) ability to respond based off a conversation’s context naturally!

# Adjusting the number of turns stored in memory

You can set the number of turns you want your agent to remember in`vf_memory` by adjusting the `Max. number of turns saved to memory` setting in Settings > Behavior > General. By default, your agent will remember the last 25 turns, but you can adjust it.

Storing more conversation turns in memory allows the agent to remember more context from previous messages, enabling it to respond more accurately to past discussions. However, this comes with trade-offs: LLM actions may take slightly longer to process due to the additional memory load, and token usage will increase.

![](https://files.readme.io/a17679b892dbb0f8737ff3d8ba5561275fc8279d95b4aa4538509231e25877af-image.png)

## Total Character Length Limit

In addition to turn limits, memory has a total character cap to prevent performance issues. This limit is calculated as `500 characters * turn limit`. For example, with the default setting of 25 turns, the total memory length is 12,500 characters. If the memory exceeds this, older messages are removed until the total falls within the limit. Based on our research, only ~1% of conversations ever reach this limit.

Updated 7 days ago

---

[Zendesk](/docs/zendesk)[No Match handling](/docs/no-match)

Ask AI

* [Table of Contents](#)
* + [Automatically Managed Memory](#automatically-managed-memory)
  + [Prompt conversation history](#prompt-conversation-history)
  + [Adjusting the number of turns stored in memory](#adjusting-the-number-of-turns-stored-in-memory)
  + - [Total Character Length Limit](#total-character-length-limit)