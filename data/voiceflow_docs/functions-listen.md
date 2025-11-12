---
category: general
scraped_at: '2025-11-12T14:07:59.714520'
title: Supporting listen in functions
url: /docs/functions-listen
---

# Supporting listen in functions

### Following a Specific Path Based on User Input

Function steps can be coded to exit through specific paths based on user input, using **listen functionality**. This behaviour allows your agent to respond dynamically when users interact with elements like buttons in carousels or choice traces. The code below demonstrates how this is implemented:

JavaScript

```
export default async function main(args) {
  return {
    // Choice trace
    trace: [
      {
        type: 'choice',
        payload: {
          buttons: [
            {
              name: "Button A",
              request: { type: 'event_A', payload: { label: 'example' } }
            },
            {
              name: "Button B",
              request: { type: 'event_B', payload: { label: 'another-example' } }
            }
          ]
        }
      }
    ],

    // Next many command
    next: {
      listen: true,
      to: [
        {
          on: { 'event.type': 'event_A' },
          dest: 'path-A'
        },
        {
          on: { 'event.type': 'event_B' },
          dest: 'path-B'
        }
      ],
      defaultTo: 'path-C'
    }
  }
}
```

  

### Understanding the next Command Properties

The next command defines how your function handles user input and controls the conversation flow.

* `listen` **(Boolean)**:
  + `true`: Agent waits for immediate user input at this function step.
  + `false`: Agent continues execution without waiting, but events persist.
* `to` **(Array)**:
  + An array of conditional transfers.
  + Each transfer includes
  + `on`: A MongoDB-style query to match incoming events.
  + `dest`: The path to exit through if the condition is met.
* `defaultTo` **(String)**:
  + The path to exit through if none of the conditions in to are met.

JavaScript

```
{
  // ...
  next: {
    listen: true,
    to: [
      {
        on: { 'event.type': 'event_A' },
        dest: 'path-A'
      },
      {
        on: { 'event.type': 'event_B' },
        dest: 'path-B'
      }
    ],
    defaultTo: 'path-C'
  }
}
```

When listen functionality causes execution to pause at the function step, the function step is said to be **listening** for user input. The next time you interact with your assistant by contacting the Dialog Manager API, the incoming request object is checked against the `on` objects specified in the next many command.

When we find the first `on` query matching the incoming request object, the function step will leave from the path specified in `dest`. Essentially, the behaviour of the `to` and `defaultTo` properties are similar to `if` and `else` statements.

As an example, suppose that the function step received the following user input:

JavaScript

```
// request object from button B
{
  type: 'event_B',
  payload: { label: 'another-example' }
}
```

The first conditional transfer in the `to` array is shown below. This conditional transfer expects that the `type` property of the request object has value `'event_A'`. The request object actually has the value `event_B` for `type`. Therefore, we do **not** follow `'path-B'`

JavaScript

```
{
  on: { 'event.type': 'event_A' }, // Does not match - 'event_A' != 'event-B'
  dest: 'path-A'
}
```

The second conditional transfer in the `to` is shown below. Here, the conditional transfer expects that the `type` property has value `event_B`, which it does. Therefore, the request object causes the function step to leave from `'path-B'`

JavaScript

```
{
  on: { 'event.type': 'event_B' }, // Matches! - 'event_B' == 'event-B'
  dest: 'path-B'                   // Therefore, follow 'path-B'
}
```

If the second conditional transfer did not match the request object, then we will have exhausted every conditional transfer in `to`. Thus, the function step would leave from the path specified in `defaultTo`, that is, `path-C`.

#### Understanding the choice trace

The **choice trace** allows the function code to render buttons which transmit a pre-defined request object to the listening function step.

If an official Voiceflow UI client (such as our [Prototype Tool](https://learn.voiceflow.com/hc/en-us/articles/9203698793357-Test-Tool) or `[react-chat](https://github.com/voiceflow/react-chat)` library) receives a choice trace, then it is rendered as clickable buttons.

For example, in the example above, we defined the following choice trace:

JavaScript

```
{
  type: 'choice',
  payload: {
    buttons: [
      {
        name: "Button A",
        request: { type: 'event_A', payload: { label: 'example' } }
      },
      {
        name: "Button B",
        request: { type: 'event_B', payload: { label: 'another-example' } }
      }
    ]
  }
}
```

Clicking on “Button A” sends the following request payload to the `general-runtime`

JavaScript

```
{ type: 'event_A', payload: { label: 'example' } }
```

Recall that our next many command was defined like so:

JavaScript

```
{
  // ...
  next: {
    listen: true,
    to: [
      {
        on: { 'event.type': 'event_A' },
        dest: 'path-A'
      },
      {
        on: { 'event.type': 'event_B' },
        dest: 'path-B'
        }
      ], 
      defaultTo: 'path-C'
  }
}
```

Therefore, clicking “ButtonA” will cause the function step to leave from `'path-A'`

#### Listen functionality with carousel and card

Carousels and cards may define buttons which can trigger listen functionality.

##### Card with listen functionality

JavaScript

```
export default async function main(args) {
  return {
    // Next many command
    next: {
      listen: true,
      to: [
        {
          on: { 'event.type': 'event_A' },
          dest: 'path-A'
        },
        {
          on: { 'event.type': 'event_B' },
          dest: 'path-B'
        },
      ],
      defaultTo: 'default'
    },
    trace: [
      {
        type: "cardV2",
        payload: {
          title: "Card title",
          description: { text: "Card description" },
          imageUrl: "https://image-url.com",
          buttons: [
            {
              name: "Button A",
              request: { type: "event_A" }
            },
            {
              name: "Button B",
              request: { type: "event_B" }
            },
          ]
        }
      }
    ]
  };
}
```

##### Carousel with listen functionality:

JavaScript

```
export default async function main(args) {
  return {
    // Next many command
    next: {
      listen: true,
      to: [
        {
          on: { 'event.type': 'event_A' },
          dest: 'path-A'
        },
        {
          on: { 'event.type': 'event_B' },
          dest: 'path-B'
        },
        {
          on: { 'event.type': 'event_C' },
          dest: 'path-C'
        },
        {
          on: { 'event.type': 'event_D' },
          dest: 'path-D'
        },
      ],
      defaultTo: 'default'
    },
    trace: [
      {
        type: "carousel",
        payload: {
          cards: [
            {
              title: "First card",
              description: { text: "Description of first card" },
              imageUrl: "https://first-image.com",
              buttons: [
                {
                  name: "Button A",
                  request: { type: "event_A" }
                },
                {
                  name: "Button B",
                  request: { type: "event_B" }
                },
              ]
            },
            {
              title: "Second card",
              description: { text: "Description of second card" },
              imageUrl: "https://second-image.com",
              buttons: [
                {
                  name: "Button C",
                  request: { type: "event_C" }
                },
                {
                  name: "Button D",
                  request: { type: "event_D" }
                },
              ]
            },
          ]
        }
      }
    ]
  };
}
```

  

### Persistent Listen Functionality

Listen events defined in your function **persist for the duration of the conversation session**. This means:

* **Event Availability:** If you generate a component (e.g., a carousel with buttons), the events associated with those buttons remain available throughout the conversation.
* **Delayed Interaction:** Users can interact with those buttons at any point during the session, and the agent will respond accordingly, even if the conversation has moved on from the point where the function was executed.
* **Function Paths:** When an event is triggered, the agent will refer back to the original function and proceed down the relevant path defined in your function code.

#### Using Listen Functionality

To utilize this feature, you define the events and paths within your function's `next` command. There are two ways to control how the agent handles user input:

1. **`listen: true`** (Agent Pauses Execution)
2. **`listen: false`** (Agent Continues Execution, Events Persist)

---

#### **Option 1:`listen: true` (Agent Pauses Execution)**

When you set `listen: true` in the `next` command:

* **Agent Behavior:**
  + The agent **pauses execution** at the function step.
  + It **waits for user input** before proceeding.
* **Use Case:**
  + Ideal when you want the user to make an immediate choice or selection.
  + Common in scenarios where the next action depends on the user's immediate response.

**Example:**

JavaScript

```
export default async function main(args) {
  return {
    // Choice trace
    trace: [
      {
        type: 'choice',
        payload: {
          buttons: [
            {
              name: 'Button A',
              request: { type: 'event_A', payload: { label: 'example' } },
            },
            {
              name: 'Button B',
              request: { type: 'event_B', payload: { label: 'another-example' } },
            },
          ],
        },
      },
    ],

    // Next command with listen: true
    next: {
      listen: true,
      to: [
        {
          on: { 'event.type': 'event_A' },
          dest: 'path-A',
        },
        {
          on: { 'event.type': 'event_B' },
          dest: 'path-B',
        },
      ],
      defaultTo: 'path-C',
    },
  };
}
```

* **Implications:**
  + The agent will wait at this function step until the user interacts.
  + The conversation flow is paused, ensuring the user’s immediate input is handled before proceeding.

#### Option 2: listen: false (Agent Continues Execution, Events Persist)

When you set `listen: false` in the next command:

* **Agent Behavior:**
  + The agent **does not pause execution** at the function step.
  + It **continues down the default path immediately.**
* **Event Persistence:**
  + The events defined in your function’s next command **persist throughout the session.**
  + Users can trigger these events at any point later in the conversation.
* **Use Case:**
* Ideal when you want to present options or actions that the user might engage with later.
* Useful for non-blocking interactions where the agent should continue without waiting.

**Example:**

JavaScript

```
export default async function main(args) {
  return {
    // Carousel trace
    trace: [
      {
        type: 'carousel',
        payload: {
          cards: [
            {
              title: 'Item 1',
              description: { text: 'Description for item 1' },
              imageUrl: 'https://example.com/image1.png',
              buttons: [
                {
                  name: 'Select Item 1',
                  request: { type: 'item_selected', payload: { label: 'Item 1' } },
                },
              ],
            },
            {
              title: 'Item 2',
              description: { text: 'Description for item 2' },
              imageUrl: 'https://example.com/image2.png',
              buttons: [
                {
                  name: 'Select Item 2',
                  request: { type: 'item_selected', payload: { label: 'Item 2' } },
                },
              ],
            },
          ],
        },
      },
    ],

    // Next command with listen: false
    next: {
      listen: false, // Must be explicitly set to false
      to: [
        {
          on: { 'event.type': 'item_selected', 'event.payload.label': 'Item 1' },
          dest: 'item_1_selected',
        },
        {
          on: { 'event.type': 'item_selected', 'event.payload.label': 'Item 2' },
          dest: 'item_2_selected',
        },
      ],
      defaultTo: 'default_path',
    },
  };
}
```

* **Implications:**
  + The agent proceeds immediately to `default_path` without waiting.
  + The events (`item_selected`) remain available to be triggered later in the session.  
    • When the user selects an item, the agent will refer back to this function and proceed down the relevant path (`item_1_selected` or `item_2_selected`).

**Important Note:** You must explicitly set `listen: false` in the next command to enable this behaviour. Omitting listen or setting it to true will cause the function to fail.

Updated 5 months ago

---

[Implementing function code](/docs/developing-functions)[Secrets](/docs/secrets-manager)

Ask AI

* [Table of Contents](#)
* + [Following a Specific Path Based on User Input](#following-a-specific-path-based-on-user-input)
  + [Understanding the next Command Properties](#understanding-the-next-command-properties)
  + - [Understanding the choice trace](#understanding-the-choice-trace)
    - [Listen functionality with carousel and card](#listen-functionality-with-carousel-and-card)
  + [Persistent Listen Functionality](#persistent-listen-functionality)
  + - [Using Listen Functionality](#using-listen-functionality)
    - [Option 1: listen: true (Agent Pauses Execution)](#option-1listen-true-agent-pauses-execution)
    - [Option 2: listen: false (Agent Continues Execution, Events Persist)](#option-2-listen-false-agent-continues-execution-events-persist)