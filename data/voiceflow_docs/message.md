---
category: general
scraped_at: '2025-11-12T14:06:58.531138'
title: Message step
url: /docs/message
---

# Message step

Send pre-written responses with rich formatting, variants, and conditions.

![](https://files.readme.io/322d0fc7059fbd27fcc8a1f3f232d936e072703f37a7afe23b55e9d0f28316a4-Message.png)

The Message step outputs a pre-written message to the user. This is commonly used to provide information, confirm an action, display errors, or give feedback. Messages can be static (single response), dynamic (conditional variants), or reused across your agent for consistency.

Each Message step is connected to a message stored in your agent’s CMS. These messages support basic formatting, multiple variants, and condition logic to determine which version is shown.

  

## Basic usage

To use the Message step, simply drag it onto the canvas, click on the step, then set the message you'd like the agent to send using the input on the sidebar. Don't forget to then connect your step to the rest of your workflow!

[](https://yz5du1veb1.ufs.sh/f/9fKud4NeF5NSwKf3RWqEGMDpIXu5W2NnhOr30QY4UBJcmZFA)

  

## Variants

Variants are alternate versions of a message within a single Message step. Each variant can contain different content and is shown based on logic conditions you define. This allows you to adapt a message to different users, states, or inputs without creating multiple steps.

You can add variants manually or use AI to generate them. Each variant can include its own formatting and conditions. When your agent is run, Voiceflow checks your variants in order and uses the first one that matches its condition. If none match, the default message is used.

Below is an example of variants in action. If the user is chatting with our agent via Voiceflow's [web chat widget](/docs/chat-widget), they'll be sent "Greetings, I'm a chatbot!". If they're talking to our agent using any other platform - such as [over the phone](/docs/telephony) - they'll see one of the other messages at random.

[](https://yz5du1veb1.ufs.sh/f/9fKud4NeF5NSPEMFy3lF9by0OHwa4UL5XrKMoYGdeckgTqN3)

  

## Formatting

![](https://files.readme.io/729eb38edd0c337081f63b6dd6c6d79faf957aaa9b67ccf92ec95ae24fc776ed-Frame_48095756.png)

The Message step supports rich text formatting, such as bold, underlined, and italic. You can also include external links and emojis in messages.

  

## Message delay

![](https://files.readme.io/4e6a4e0f352bca1d70f8c1f2a3ef7a86bb9477df401818f2129942f2b01b2c7e-Frame_48095759.png)

The message delay option allows you to add a delay between the step in the agent's flow being reached and the message being sent. The message delay is set in milliseconds - for example, if the message delay is set to 500 would add a 0.5 second delay before the message is sent.

One example use-case of message delay is if you're sending multiple pieces of information to the user at once. For example, you could send three short messages with a 1000ms delay each rather than one huge message. This is less overwhelming to the user and creates a better experience.

  

## Reusing messages

![](https://files.readme.io/9f5516d556408f026ab9dec7efcfb545dccf4ef2bcad309238934a07f6378615-Frame_48095758.png)

Sometimes you’ll want to use the same message in multiple places - like a legal disclaimer or a standard confirmation message. To reuse a message, type `/` in the message input and start typing part of the message. Then, select the message you'd like to use from the list that appears.

If you edit a reused message, that change will apply across all steps that it’s used in. This helps keep things consistent across your agent. Messages can also be managed from the [CMS](/docs/cms)

Updated 5 months ago

---

[Agent step](/docs/agents)[Prompt step](/docs/prompt-step)

Ask AI

* [Table of Contents](#)
* + [Basic usage](#basic-usage)
  + [Variants](#variants)
  + [Formatting](#formatting)
  + [Message delay](#message-delay)
  + [Reusing messages](#reusing-messages)