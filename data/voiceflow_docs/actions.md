---
category: general
scraped_at: '2025-11-12T14:07:31.514140'
title: Actions
url: /docs/actions
---

# Actions

Actions let you easily do things other than going down a path on the exit of step. This can include setting variables, going to a trigger or even jumping back to other blocks without having to add an arrow. They can only be added from a pre-existing step.

**Note:** Actions execute small behaviors *in* your agent, and are different from [Custom Actions](https://developer.voiceflow.com/v2.0/docs/custom-actions) that send a customizable trace to your agent for displaying. Actions are useful for cleaning up your agent's logic, and custom actions are mainly for special deployments and for developers.

Most of their behavior can be replicated with either path arrows or just adding steps, but action chips can make it easier to understand simple actions rather than tracing through blocks.

On canvas, actions are shown as chips linked to a step's path exit.

![](https://files.readme.io/32b5dbf-CleanShot_2024-06-24_at_14.26.202x.png)

Some actions have exits coming out of them that let you move on after the action is executed, like in the set action.

# Adding Actions

Actions can be added by dragging out a new arrow from the end of a step, and then picking actions from the dropdown.

![](https://files.readme.io/f01f39c-CleanShot_2024-06-24_at_14.34.172x.png)

Actions can also be directly attached to objects in certain steps, like in buttons.

![](https://files.readme.io/e7fa99a-CleanShot_2024-06-24_at_14.37.282x.png)

# Actions Available

## Navigation Actions

**Go to Block** — Goes to a specific block referenced within the assistant

**Go to Intent** — Goes to an existing intent contained in the assistant

**End** — Ends the conversation at its current state

## Backend Actions

**Set Variable** — Allows you to set and change the value of variables

**Open URL** — Supported on Button Steps only. Lets you add or connect a Go-to URL & link-out from your selected Step.

**API** — Allows you to set up, configure and execute API calls & functions

**Custom Code** — Allows you to set up and code custom JavaScript functions & commands

Updated 5 months ago

---

[Library](/docs/template-library)[Agent content](/docs/agent-content)

Ask AI

* [Table of Contents](#)
* + [Adding Actions](#adding-actions)
  + [Actions Available](#actions-available)
  + - [Navigation Actions](#navigation-actions)
    - [Backend Actions](#backend-actions)