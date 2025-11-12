---
category: general
scraped_at: '2025-11-12T14:08:59.296240'
title: Open sourced react-chat
url: /docs/react-chat
---

# Open sourced react-chat

We've open sourced our Web Chat widget so that you can make any modifications you want to it.

# Overview

With Voiceflow’s Chat UI Kit (`react-chat`), you can customize the visual elements of your chat Agent like the font and colors or build a custom component for a [Custom Action](/reference/custom-actions-1) step.

Our `react-chat` library is built in React and [available through npm](https://www.npmjs.com/package/@voiceflow/react-chat). The library provides access to:

* Voiceflow’s React chat UI elements, which you can customize or re-use to display other custom chat components.
* A `useRuntime` hook to interact with your agent's flows and manage conversation turns.

## When to use `@voiceflow/react-chat`

* If you want to launch a chat experience in a `react` application.
* If you want to integrate a custom chat experience with custom message types or components, such as (and not limited to) the following:
  + Calendar widget
  + [Live Chat Handoff](/docs/live-chat-handoff)

> 📘
>
> ### Use [Custom Actions](/docs/custom-actions) in your agent's design to help build custom components like the ones listed above.

# Demo

In this video, we will show you how to get started with our Web Chat UI Kit and what a Custom Action might look like.

# Before you begin

* [Create a Voiceflow project](https://learn.voiceflow.com/hc/en-us/articles/15965489787789-Step-1-Create-a-Project) and
* [Get your Voiceflow agent's Dialog Manager API key](https://learn.voiceflow.com/hc/en-us/articles/13619375958413)

# Instructions & Code Repositories

You can find our open-source code and simple demo project repository with further instructions below:

* [react-chat package on npm](https://www.npmjs.com/package/@voiceflow/react-chat)

## `react-chat`

`react-chat` (<https://github.com/voiceflow/react-chat>) is a repository that contains:

### `packages/react-chat`

`packages/react-chat` is the application code for webchat. It manages the client conversation state and can be customized with various configurations.

This library is bundled and distributed to the Voiceflow CDN. It is intended to be loaded by a simple JavaScript snippet (see [Web Chat (Basic)](/docs/chat-widget)). This is the primary method of consuming this widget in production.

Updated 6 months ago

---

What’s Next

* [Web Chat (Basic)](/docs/chat-widget)
* [Custom Actions](/docs/custom-actions)

Ask AI

* [Table of Contents](#)
* + [Overview](#overview)
  + - [When to use @voiceflow/react-chat](#when-to-use-voiceflowreact-chat)
  + [Demo](#demo)
  + [Before you begin](#before-you-begin)
  + [Instructions & Code Repositories](#instructions--code-repositories)
  + - [react-chat](#react-chat)