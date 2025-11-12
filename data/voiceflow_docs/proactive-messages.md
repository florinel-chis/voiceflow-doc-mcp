---
category: general
scraped_at: '2025-11-12T14:08:49.450332'
title: Proactive messages
url: /docs/proactive-messages
---

# Proactive messages

Send messages to the user before they start chatting.

Proactive messages allow you to send messages to the user before they open the chat widget. These messages do not appear in transcripts, and do not consume credits. You can add and remove proactive messages to your web chat widget using the `window.voiceflow.chat.proactive` method.

[](https://yz5du1veb1.ufs.sh/f/9fKud4NeF5NSnzvO3ayLLDzbg1qhkwJW5SmtN92ciaEe8MjI)

  

## Sending proactive messages

To send a proactive message to the user, use the `window.voiceflow.chat.proactive.push()` method. You can send one or more messages to the user at the same time.

JavaScript

```
// one message  
window.voiceflow.chat.proactive  
  .push({ type: 'text', payload: { message: 'hello world' } })

// multiple messages  
window.voiceflow.chat.proactive  
  .push(  
    { type: 'text', payload: { message: '1!' } },  
    { type: 'text', payload: { message: '2!' } }  
  )
```

🦉

Send multiple proactive messages

Open Recipe

  

## Clearing messages

You can use the `window.voiceflow.chat.proactive.clear()` method to hide all the proactive messages that have been sent to a user.

  

## Triggering proactive messages when certain things happen

One great use-case for proactive messages is to trigger them when the user does a specific action. For example, you could offer a promo code if the user navigates away from the checkout page, or suggest product recommendations if the user is clicking on lots of similar products.

Here's an example of clearing existing messages and showing a new one if the user visits a certain page.

🦉

Send a proactive message when the user visits a certain page

Open Recipe

Updated 6 months ago

---

[Passing custom variables into web chat](/docs/customization-configuration)[Custom triggers](/docs/web-chat-api)

Ask AI

* [Table of Contents](#)
* + [Sending proactive messages](#sending-proactive-messages)
  + [Clearing messages](#clearing-messages)
  + [Triggering proactive messages when certain things happen](#triggering-proactive-messages-when-certain-things-happen)