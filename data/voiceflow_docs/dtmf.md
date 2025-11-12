---
category: general
scraped_at: '2025-11-12T14:08:41.315717'
title: Keypad input (DTMF)
url: /docs/dtmf
---

# Keypad input (DTMF)

Detect the number keys the user presses during a call.

> ℹ️
>
> This feature is only available for Voiceflow’s [phone integration](/docs/telephony) and isn’t supported by the [Web chat widget](/docs/chat-widget).

  

Voiceflow’s DTMF capability allows your agent to automatically detect and respond to keypad inputs during phone calls. For example, if a caller types `676767` on their phone, the agent can interpret that input and use it to drive the conversation flow - like entering an account number, selecting a menu option, or confirming a passcode - all without leaving the call. DTMF is great for handling fiddly numeric inputs during conversations.

  

## Setting up keypad input

To use keypad input, it must first be enabled on your project. To enable it, open your project's settings, click **Behaviour**, then open the **Voice** tab. Then, scroll down and set **Keypad input** to **On**.

[](https://yz5du1veb1.ufs.sh/f/9fKud4NeF5NSGsOY3S4nRy3vf7nmBxZFkjKPItoDAUizpGWc)

From here, you can also set the following settings:

* **Timeout** - the number of seconds to wait between the user stopping typing and the input to be sent to your agent. Voiceflow will automatically send multiple numbers entered in quick succession as single message to your agent, allowing things like order numbers and PIN codes to be handled easily.
* **Delimiter** - you can optionally set the pound (`#`) and star (`*`) keys as send buttons. If enabled, when a delimiter key is pressed, the user's keypad input will be immediately sent to the agent.

  

## Receiving keypad input

Once keypad input is setup, any [Agent step](/docs/agents) with **Listen for other triggers** enabled will be able to receive keypad input. You do not need include anything special in your agent's instructions to handle DTMF input beyond what you'd include to handle any verbal numeric input.

  
![](https://files.readme.io/41893a91f2407cb89d8b2a04402d16eb27b9b01c20eb7a00120a527407d29ff0-Frame_48095788.png)
  

While you can differentiate between the type of input a conversation's debug logs, your agent cannot tell the difference between a user saying numbers and entering them using a keypad. Therefore, we recommend designing agents to say things like "say or enter your six digit passcode" rather than "enter your six digit passcode then press the star key".

Updated 2 days ago

---

[LLM fallback](/docs/llm-fallback-system-beta)[Publishing agents to production](/docs/publishing-agents)

Ask AI

* [Table of Contents](#)
* + [Setting up keypad input](#setting-up-keypad-input)
  + [Receiving keypad input](#receiving-keypad-input)