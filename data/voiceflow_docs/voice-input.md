---
category: general
scraped_at: '2025-11-12T14:09:06.508687'
title: Voice Input
url: /docs/voice-input
---

# Voice Input

Settings for transcribing user-speech

# Concepts

### Providers

![](https://files.readme.io/0d11012a79188c5b36cecb92e5f062dc1bce7b8b526cd5284fe4d9e1f11d2c41-Capture_decran_le_2025-06-18_a_12.57.57.png)

Choosing the right **Speech-to-Text (STT)** model is important for the clarity of your agent and how well it understands the user.  
Certain models may work better for certain languages, certain quality of audio, or for certain industries.

You may want to experiment different providers and their models for your particular use case and see what works best for you. It is also recommended to read the marketing and documentation for each provider for their advantages.

### Chunking

As a user speaks, the STT engine continuously transcribes the audio into words, by breaking the streamed audio into "chunks".

For example, while I say "I want 2 turtles", this is what is happening in the background as I speak:

> I want...
>
> I want to...
>
> I want to turtles...
>
> I want 2 turtles. *(finalized chunk)*

If the user takes a significant pause, it will also create a *chunk*, even if the sentence looks incomplete.  
In the following example, two separate chunks are created.

> Hi...
>
> Hi, my name is... *(pause)*
>
> Hi, my name is *(finalized chunk)*
>
> ...
>
> Joe *(finalized chunk)*

At some point, the chunks will be sent to your agent as a **turn/transcription**, and trigger execution.

### Broken Up Utterances

If your transcription settings lead the STT engine to think that a user is done their utterance, but they're actually not, that might lead to a **broken up utterance**.

For example, if a user says

> User: Hi my name is John (silence) Doe from New York

The agent might think that they were done speaking after John. The agent would then respond, while John keeps speaking.

> User: Hi my name is John
>
> Agent: sorry I don't think...
>
> User: Doe from New York.

In general, you'll want to avoid having broken up utterances in the first place, because they break up the user experience. Consider making your Timeout settings less aggressive and more patient.

# Providers

## Cartesia (Ink-Whisper)

* [Ink-Whisper Annoucement](https://cartesia.ai/blog/introducing-ink-speech-to-text)

### Languages

The model needs to know which language to expect in advance. If you try to speak a different language than what is in settings, it will either miss transcribe what's being said, or not transcribe anything at all. It could look like the agent isn't hearing you at all.

For the known-accuracy in a given language, refer to [OpenAI's Whisper (Large-V3) Word-Error-Rate](https://github.com/openai/whisper?tab=readme-ov-file#available-models-and-languages) ().

## Assembly AI (Universal)

* [Universal Streaming](https://www.assemblyai.com/universal-streaming)
* [Turn detection documentation](https://www.assemblyai.com/docs/speech-to-text/universal-streaming/turn-detection)

Currently only English is supported.

### Confidence threshold

How confident the model needs to be before resolving a chunk. Lower confidence can lead to better latency, but higher word-error-rate and premature turn.

### Minimum turn silence

How long to wait before resolving a turn/transcription. This gives the user more opportunity to say follow-up sentences and prevent broke up utterances.

### Maximum turn silence

Even if the model is not confident, after this amount of time, it will always resolve the turn.

## Deepgram (Nova)

* [Nova-3 Annoucement](https://deepgram.com/learn/introducing-nova-3-speech-to-text-api)
* [Models and Languages Overview](https://developers.deepgram.com/docs/models-languages-overview)

### Languages

The model needs to know which language to expect in advance. Different models support different languages, some only support one.

![](https://files.readme.io/77bc7e5652e01eb316076f1f7d48ed66e2d2996fb3ea1a019da2d8fa756de02b-Capture_decran_le_2025-06-18_a_12.24.47.png)

If you try to speak a different language than what is in settings, it will either miss transcribe what's being said, or not transcribe anything at all. It could look like the agent isn't hearing you at all.

Nova-3 is capable of understanding multiple languages at once (multilingual), however from our testing this comes at a penalty of higher latency.

## Keywords

You may have some specific terms that are not common knowledge. For example, if I have a company called "*RightSea*", sometimes the transcription will come out as "*write see*" or "*ritecy*" "*right c*" etc.

By providing the keyword, it will bias the model into transcribing these words whenever it hears something similar. This is great for hard to pronounce words, homophones and homonyms, and industry specific terms.

### On punctuation/On no punctuation, sec.

**After** a finalized *chunk* is produced, we sometimes want to give the user a chance to continue speaking to form a complete utterance for your agent to process.

Users can often speak in run-on sentences, take long pauses, or try to make corrections.

> 1. Hey my name is
> 2. Joe.
> 3. And I live in
> 4. New York,
> 5. Manhattan actually.

Lines 2, 5 trigger **On punctuation, sec**  
Lines 1, 3, 4 trigger **On no Punctuation, sec**

If the most recent chunk ends in punctuation (!.?¡¿…), it will wait **On punctuation** seconds for the user to say something else before assuming the user is finished speaking, and processing the turn. This is usually when a user says a complete sentence.

If the most recent chunk does not end in punctuation, it will wait for **On no punctuation** seconds. This is often when the user takes a pause during the middle of a sentence (if they're thinking for example, or pulling up some details).

The STT engine is generally pretty good at determining punctuation based on intonation and other cues, so should be taken as the primary cue for if the user is done speaking.

**On no punctuation** should always be significantly higher than **On punctuation** seconds.

### Interruption threshold

How many partially transcribed words are needed before the agent will stop talking, and the chunk will be treated as a valid transcription.

Sometimes the user may say "yes" or "ok" but it is not meant as an interruption. Chunks that do not meet the threshold, while the agent is talking, will be discarded.

### Endpointing

**Endpointing** uses silence to detect when to finalize a *chunk*. A shorter period means faster latency. For example if I say:

> That's awesome!

We will wait the **Endpointing** period before deciding to finalize the chunk. If your **Endpointing** is 1 second, that adds up to 1 second of latency to resolving any response.

In environments with loud background noises, **Endpointing** doesn't work well because there isn’t actually a period of silence. That means we will often fall back on other methods to finalize a transcript (like timeouts), this can cause additional latency. You can learn more [here](https://developers.deepgram.com/docs/endpointing).

### Recommendations

Voiceflow provides default settings under the "Simplified" tab, with three options for "Speed" (optimized for quickly replying to users), "Balanced", and "Accuracy" (optimized for high conversational accuracy, at the cost of agent speed).

If you wish to customize further, you can switch to the "Advanced" tab:

* **On punctuation** and **On no punctuation** are the main levers to prevent broken up utterances.
* Keep **Endpointing** low (~100ms) as long as the transcriptions are accurate - the words produced are what the user actually said. This helps transcribe audio as soon as possible, leading to better interruptions. The latency of your agent to respond to a spoken utterance will be *at least* the endpointing time.
* Start with longer timeout values (3-5 seconds) and gradually reduce them while monitoring the impact on call quality. Timeouts that are too short can lead to the agent interrupting the caller, and generally having to wait a second or two more for the transcription to be finalized is a nicer user experience than being missheard.
* Keep **On punctuation, sec.** low, (less than 300ms) if you expect your users to speak simple *single* sentences. If you’re expecting your users to have more organic and natural conversations with your agent, then it might make sense to increase the punctuation time to 1-2 seconds. This will give the impression of a patient agent listening carefully and really waiting for the user to be done.
* Keep **On no punctuation, sec.** higher than your **On punctuation, sec.**, at *least* 1 second, but often more like 3 seconds, to give users more time to complete their thoughts. *Tip: think about how long you would wait to speak if you're having a conversation with someone on the phone, and they just stop mid-sentence. From our research, it's probably more like 3+ seconds.*

Updated 4 months ago

---

[Configuring voice settings](/docs/configuring-voice-settings)[Advanced - Using custom voice actions](/docs/advanced-using-custom-voice-actions)

Ask AI

* [Table of Contents](#)
* + [Concepts](#concepts)
  + [Providers](#providers-1)
  + - [Cartesia (Ink-Whisper)](#cartesia-ink-whisper)
    - [Assembly AI (Universal)](#assembly-ai-universal)
    - [Deepgram (Nova)](#deepgram-nova)
    - [Keywords](#keywords)