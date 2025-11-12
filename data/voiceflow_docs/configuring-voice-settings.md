---
category: general
scraped_at: '2025-11-12T14:09:05.164522'
title: Configuring voice settings
url: /docs/configuring-voice-settings
---

# Configuring voice settings

## Overview

The Voice settings allow you to fine-tune the behaviour of your voice agents during voice calls. By adjusting parameters like silence timeouts, audio cues, and STT/TTS settings, you can make conversations more organic and enhance the caller experience. This guide will walk you through the available options and how to configure them for your voice agent.

![](https://files.readme.io/47c70a1be0d3c9139622f708681f8ad91a62e665c23271cb133b18115f2493c1-Capture_decran_le_2025-06-18_a_11.59.52.png)

## Getting Started

To access the Voice behavior settings for your agent:

1. Navigate to your project.
2. Navigate to the *Settings* > *Behaviour* tab.
3. Select the *Voice* tab.

You'll see several settings that control different aspects of the voice interaction.

## Key Concepts

* **Voice Output**: Also referred to as Text-to-Speech (TTS). Determines the voice and speech patterns of the agent speaking back to the user.
* **Voice Input**: Also referred to as Speech-to-Text (STT). Determines how we capture user speech for the agent to understand. See [Voice Input](/docs/voice-input).
* **Audio Cue**: A short sound effect played to the caller to signal that the agent has received their input and is processing it.
* **Background Audio:**: Simulated background audio that helps give more realism to the call

## How To

### Set an Audio Cue

1. Navigate to the Audio Cue setting.
2. Click the drop-down menu and select one of the preset sound effects. Hear a preview of the cue by selecting the play button in the dropdown.
3. Test the audio cue by calling your agent and hearing it play after you finish speaking.

![](https://files.readme.io/8b0f4b568d0cbf60ec08f02f49fd8466d02c438b586eb5ce35fb94d4e6409e89-CleanShot_2024-12-02_at_11.51.42.png)

### Select TTS Voice

1. Navigate to Settings > Behavior > Voice
2. Choose your TTS provider (ElevenLabs, Rime, Google, Amazon, Microsoft) from the top tab selector. Different providers are more or less expensive.
3. For each provider, you can hear what a voice sounds like by pressing the play button, and then select it by clicking on the voice name.
4. Test the voice by calling your agent and listening to its responses.

Explore the variety of TTS voices to find one that callers find natural and engaging to interact with. Don't be afraid to experiment with different options.

![](https://files.readme.io/b9ee5842b4f918981c1fc77d826c99d26efb3601d0e8539973d0518a6ef157fe-image_3.png)

## Troubleshooting

### Agent is Interrupting Caller

* Modify various Voice Input settings to give callers more time to start and complete their statements.
* Make sure your agent prompts are worded clearly to elicit succinct responses from callers. Open-ended or ambiguous prompts may encourage rambling.

Updated 5 months ago

---

[Call recording](/docs/twilio-call-recording)[Voice Input](/docs/voice-input)

Ask AI

* [Table of Contents](#)
* + [Overview](#overview)
  + [Getting Started](#getting-started)
  + [Key Concepts](#key-concepts)
  + [How To](#how-to)
  + - [Set an Audio Cue](#set-an-audio-cue)
    - [Select TTS Voice](#select-tts-voice)
  + [Troubleshooting](#troubleshooting)
  + - [Agent is Interrupting Caller](#agent-is-interrupting-caller)