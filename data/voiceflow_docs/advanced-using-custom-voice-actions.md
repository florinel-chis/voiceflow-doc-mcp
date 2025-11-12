---
category: general
scraped_at: '2025-11-12T14:09:08.529030'
title: Advanced - Using custom voice actions
url: /docs/advanced-using-custom-voice-actions
---

# Advanced - Using custom voice actions

> 🚧
>
> ### Experimental Beta
>
> Advanced custom actions are in experimental beta and subject to change or removal.

## Overview

Custom actions allow you to extend the functionality of your voice agents and implement advanced telephony workflows. By leveraging custom actions, you can:

* Create interactive voice response (IVR) menus with DTMF (touch-tone) input
* Capture and validate caller input, such as account numbers or PINs
* Transfer calls to external phone numbers based on caller responses
* Dynamically update the agent's STT settings during the conversation

This guide will show you how to set up and use custom actions to build sophisticated voice experiences.

> 📘
>
> ### Forward calls from your agent to other phone numbers
>
> The Call forwarding step is designed for seamless handoffs to humans or external systems from your agent. You can forward to phone numbers, SIP addresses, or menu-based systems using DTMF tones - allowing your Agent to transfer callers without requiring manual input from the user.
>
> Check out [Call forwarding step](https://docs.voiceflow.com/update/docs/call-forwarding-step#/)

## Getting Started

To add a custom action to your canvas:

1. Drag the "Custom action" step from the Dev section in the steps toolbar.
2. Enter a name for your action in the block's settings panel
3. Select "Stop on action" if you want the action to interrupt the agent's speech
4. Define the expected inputs and outputs for your action in the "Body" section using JSON notation

## Key Concepts

* **DTMF (Dual-Tone Multi-Frequency):** The touch tones generated when a caller presses keys on their phone keypad. Each number key corresponds to a unique frequency pair.
* **DTMF Input**: Collecting caller input by having them press number keys on their phone in response to your agent's prompts. Useful for navigating menus, entering data, or making selections.
* **Call Transfer**: Programmatically forwarding an in-progress call to a different phone number, such as to route the caller to a live agent or another department.
* **STT Settings:** The configuration options that control the agent's speech to text (STT) behavior, such as the language model, recognition timeout, and confidence threshold.

## How To

### Retrieve Call Metadata

As part of the initial launch request (at the start step), we will include:

* `userNumber` - phone number of the user
* `agentNumber` - phone number of the agent (you may have multiple numbers attached to the same agent)
* `callType` - if this is an inbound or outbound call

TypeScript

```
{
  type: "launch",
  payload: {
    callType: "inbound" | "outbound",
    userNumber: string,
    agentNumber: string
  }
}
```

You can access this information through the `last_event` variable in a Javascript step. For example:

![](https://files.readme.io/a4da522d2ed4b32d2057a97bb82317bb6f85d78f02ff59db6fb8074ddf1c082f-Screenshot_2024-12-13_at_9.10.20_AM.png)

### Set Up a DTMF Menu

1. Add a Message step to your flow and have your agent prompt the caller to select from a numbered list of options ("Press 1 for Sales, 2 for Support...).
2. Drag a Custom action step onto the canvas and name it "DTMF" (use that exact name).
3. Enable the "Stop on action" option.
4. Under Paths you can add `DTMF 1`, `DTMF 2`, etc. The `default` path will be followed if the user presses or says something that is not setup as its own discrete path in the step configuration.
5. Add connections from the custom action step to other steps representing each menu option.
6. In each connected block, check for the DTMF input using the `last_event.data` variable (e.g., `last_event.data == "1"` for the first option).
7. Route the caller to the appropriate flow based on their DTMF selection.

![](https://files.readme.io/a497442567e0dd09cc8d0eed9039caaa78c2d8959956ab914fa34affcb1914d5-image.png)

### Capture a PIN Code

Following the same steps above to capture the keys a user presses, we will now set up a design to use this method for capturing user input.

1. Drag a Custom action step onto canvas and name it "DTMF" (use that exact name).
2. Enable the "Stop on action " option.
3. Setup `default` path only as this will allow for any keys during capture to be registered as part of the loop.
4. Use a Javascript step to validate the captured digit and to continue once input length has been met.
   1. We can make use of the `last_event` built-in variable inside the Javascript step
   2. The name of a DTMF event is always called `DTMF {DIGIT}`, so we can just look for events that start with DTMF and pluck out the digit at the end. When you turn this into a loop, you are now collecting numbers from the user (see image below for example).
5. Design appropriate flows for valid and invalid PIN scenarios.

![](https://files.readme.io/0b77151c821687409c437c6db962d97caa7b2ae1770c38b46f2d7a7c318987e2-image.png)

### Transfer Call to Agent

1. At the point in your flow where you want to transfer the call, add a Custom action step.
2. Name the block "forward-call" (use that exact name).
3. In the Body field, enter:

   JSON

   ```
   {
     "number": "+1415XXXXXXX"
   }
   ```
4. Add a Message step before the Transfer explaining to the caller that they will be transferred.

  

### Prevent Interruptions

By default, the call is always interruptable - the agent will stop talking when a user speaks over it.  
Upon the next utterance, the previous flow will be cancelled (the steps that haven't run won't be run).

For more info on this, reference: [https://docs.voiceflow.com/docs/interruption-behavior](/docs/interruption-behavior)

However there is a special use case - for critical long running actions, we don't want any interruptions until the action is completed. Even with a human, sometimes you might be put on hold while something is happening.

For example, if it takes up to 15 seconds to book an airline ticket, we should not let the user interrupt until the booking is complete and we confirm it back with them.

To achieve this, create a custom action step labelled "**interruption**" (use that exact name), in the body you can set `"allowInterrupts"` to `true` or `false`.

* `true`: the user can now interrupt the bot for the rest of the call
* `false`: the user can no longer interrupt the bot for the rest of the call, anything they say while the bot is not listening *is ignored*.

![](https://files.readme.io/e7165978948f8210f75fdadeecbdf85c8b28a554c1445be7fe6ff0423147a1a0-Capture_decran_le_2025-02-19_a_16.08.01.png)

Once this action is hit, the setting applies for the rest of the call. So ideally after your uninterruptable action is performed, you can turn it off again with `allowInterrupts: true`.

### Change Speech-to-Text Settings

It is possible to dynamically change STT settings and switch vendors during a conversation. This may be useful for switching the language or end-of-speech tolerance.

Add a custom action that has **Stop on Action** enabled, is titled `asr`, and has a JSON body with a `settings` property defined below.

![](https://files.readme.io/69fb750849960d658c63180f6657a0c89d06bbca553e6e07a97d9aa861f1ba93-Capture_decran_le_2025-06-28_a_17.40.19.png)

Follow the following formats for `setting` (these properties may be subject to change):

TypeScript

```
{ // deepgram
  "provider": "deepgram"
  "model": "nova-3" | "nova-3-medical" | "nova-2",
  "locale": string, // e.g. en-US
  "keywords": string[],
  "punctuationWaitMS": number, // punc wait
  "partialWaitMS": number, // no punc wait
  "silenceWaitMS": number, // endpointing
  "interruptionWaitWords": number,
};

{ // cartesia
  "provider": "cartesia",
  "model": "ink-whisper",
	"language": string, // e.g. en
}

{	// assemblyAI
  "provider": "assemblyai",
  "confidenceThreshold": number, // e.g. 0.7
	"maxTurnSilence": number
	"minTurnSilence": number
}
```

From your default `provider` (defined in project settings), you can just provide a partial update of a single property. For example, if Deepgram is already the default provider, I can just write:

```
{ "settings": { "locale": "es" } }
```

## Best Practices & Tips

* Use DTMF menus judiciously to avoid overloading callers with too many options. Limit menus to 3-5 clearly differentiated choices.
* When capturing data like PINs, use a Message step to confirm the caller's input before proceeding.
* Be mindful of the caller's experience when transferring calls - provide estimated wait times or option to continue talking to AI agent.
* Test your STT settings changes with a diverse set of voices and accents to ensure they improve recognition accuracy for your target audience.

## Troubleshooting

### Caller Hears Silence After Entering PIN

* Check that your PIN validation code is executing quickly and not hanging the conversation
* Use a Message step to confirm the caller's PIN was received before processing it
* Investigate transcript logs and test your PIN flow to debug any issues.

Updated 3 months ago

---

[Voice Input](/docs/voice-input)[SIP Functionality](/docs/sip-functionality)

Ask AI

* [Table of Contents](#)
* + [Overview](#overview)
  + [Getting Started](#getting-started)
  + [Key Concepts](#key-concepts)
  + [How To](#how-to)
  + - [Retrieve Call Metadata](#retrieve-call-metadata)
    - [Set Up a DTMF Menu](#set-up-a-dtmf-menu)
    - [Capture a PIN Code](#capture-a-pin-code)
    - [Transfer Call to Agent](#transfer-call-to-agent)
    - [Prevent Interruptions](#prevent-interruptions)
    - [Change Speech-to-Text Settings](#change-speech-to-text-settings)
  + [Best Practices & Tips](#best-practices--tips)
  + [Troubleshooting](#troubleshooting)
  + - [Caller Hears Silence After Entering PIN](#caller-hears-silence-after-entering-pin)