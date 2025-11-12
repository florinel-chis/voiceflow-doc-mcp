---
category: general
scraped_at: '2025-11-12T14:09:01.935667'
title: Managing interuptions
url: /docs/interruption-behavior
---

# Managing interuptions

Humans might talk over your agent. Here's how to handle that.

Voiceflow voice agents operate on a turn-by-turn model. At any given moment, the user is at a specific state in the conversation, which is tied to a step in the workflow (e.g. a [message step](/docs/message), [capture step](/docs/capture-v2), or [API step](/docs/api-step)).

During voice interactions, users may interrupt the agent while it's speaking. Handling these interruptions correctly is important for maintaining a natural and functional experience.

## Controlling interruption behaviour

Voiceflow's interruption behaviour settings can be found by visiting **Agent Settings > Behaviour > Voice**. Most users will find that the simple controls that allow you to set the balance of speed vs accuracy are good enough for their use-case. We recommend experimenting with this slider and seeing which option works best for your agent.

[](https://yz5du1veb1.ufs.sh/f/9fKud4NeF5NSw351PLqEGMDpIXu5W2NnhOr30QY4UBJcmZFA)

### Advanced options

If you'd like full control over how your agent handles interruptions, you can toggle the interruption behaviour settings to advanced mode.

![](https://files.readme.io/5c446f5ceea626f43d679a90bdd880d9ef3d785aa525974e799cf0f267e13c63-CleanShot_2025-05-29_at_16.16.532x_1.png)
  

* **On punctuation** and **on no punctuation** allow you to control how many seconds to wait if the transcription of the user's message ends with or without punctuation.
* **Interruption threshold** is the number of spoken words needed to stop the agent’s audio mid-sentence. The agent will stop talking once the threshold is met. However, it continues executing the current step in the background until a full interruption is triggered.
* **Endpointing** refers to the number is milliseconds that your agent will wait before transcribing a portion of speech.

  

## Interruption State

Message steps are professed effectively instantaneously, but other steps (including the [API step](/docs/api-stept), [Function step](/docs/function-step), and [Prompt step](/docs/prompt-step)) are blocking and take time to process. Take a look at our example agent below: after the user says something, there are a series of simple message steps broken up by long running API and Prompt steps.

![](https://files.readme.io/e11c3fae9ec0ccc46daa6855306f8821c80060d93a8d857491385fa27dd8f280-Capture_decran_le_2024-12-20_a_11.46.34.png)

When an interruption happens, as the previous turn hasn't made it to the "next state" block, we will always start at the capture step in the "starting point" block. The previous turn will also stop executing.

For example if the interruption happened during the `GET - long API call` API step, it will no longer call `long LLM prompt` and use up tokens in the background. If the previous turn has made it to `next state`, we are no longer interrupting, but rather just starting the next turn normally.

  

### Audio does not represent current state

There’s a slight delay between the agent's current state and what the user hears. This is due to TTS buffering and background execution. Here's an example of this in action:

* As soon as Message 1 is triggered, the API call begins immediately in the background.
* The text-to-speech audio for Message 1 is generated and starts playing after a delay.
* By the time the user hears Message 3, the system has likely already moved to the next step.

Here's what this looks like visually:

![](https://files.readme.io/99650ed596f1d51395a7c48cdeba7b1e3247d59dbe7b5e6acb1ed3685c824daf-Frame_48095753_1.png)

This design reduces latency and awkward silences but may make debugging difficult since audio does not always reflect real-time state.

Updated 6 months ago

---

[Outbound calls](/docs/outbound-calls)[Call recording](/docs/twilio-call-recording)

Ask AI

* [Table of Contents](#)
* + [Controlling interruption behaviour](#controlling-interruption-behaviour)
  + - [Advanced options](#advanced-options)
  + [Interruption State](#interruption-state)
  + - [Audio does not represent current state](#audio-does-not-represent-current-state)