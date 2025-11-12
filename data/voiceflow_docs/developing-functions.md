---
category: general
scraped_at: '2025-11-12T14:07:57.775865'
title: Implementing function code
url: /docs/developing-functions
---

# Implementing function code

A function in Voiceflow is defined by two main components: the [function interface](https://learn.voiceflow.com/hc/en-us/articles/22213934251533) and the function code. The function interface outlines the inputs, outputs, and paths, while the function code dictates the behaviour of the function. In this document, we'll be covering the function code only.

## Starting with the Main Function

Every function is contained within the `main` function that is the default export. This is the entry point for Voiceflow to execute your code when the function step is triggered.

JavaScript

```
export default async function main(args) {  
  // Your function logic goes here  
}
```

## Processing Input Variables

The function accepts a single value, called the **arguments object**, `args`, which contains the data passed into the function when using the function step. In this case, the `args.inputVars` contains a single field called text.:

JavaScript

```
const { text } = args.inputVars;
```

## Performing Transformations

In the function, you may perform operations such as transforming text:

JavaScript

```
const uppercaseText = text.toUpperCase();
```

## Returning Runtime Commands

The function concludes by returning an object containing runtime commands:

JavaScript

```
return {  
  outputVars: {  
    output: uppercaseText  
  },  
  next: {  
    path: 'success'  
  },  
  trace: [  
    {  
      type: 'text',  
      payload: {  
        message: `Converting ${text} to ${uppercaseText}`  
      }  
    }  
  ],  
}
```

The runtime commands include:

* **Output Variables Command**: Assigns values to output variables.
* **Next Command**: Directs the assistant to exit the function step through a specific port.
* **Trace Command**: Generates traces that form part of the agent's response.

> 🚧
>
> ### Environment limitations
>
> Please note that certain JavaScript methods, such as `setTimeout()`, are not supported out-of-the-box due to their dependence on browser or Node.js runtime APIs and not part of the ECMAScript (JavaScript) language specification itself. This JavaScript reference [document](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference) describes all built-in objects supported by functions code.

# Making Network Requests

Voiceflow functions have access to a modified `fetch` API for making network requests. This enables functions to interact with third-party APIs or your own backend services.

Example: GET Request with the Fetch API
Here's how to make a `GET` request to retrieve data from an API:

JavaScript

```
export default async function main(args) {	  
  const response = await fetch(`https://cat-fact.herokuapp.com/facts`);  
  const responseBody = response.json; // Accessing the response body

  // ... (process responseBody)  
}
```

### Mapping Data from Response

To map and process the data from the API response, use JavaScript array methods like `map`:

JavaScript

```
const facts = responseBody.map(fact => fact.text);
```

### Creating Traces from Data

Create traces for each item you want to include in the assistant’s response:

JavaScript

```
return {  
  next: {  
    path: 'success'  
  },  
  trace: facts.map(text => ({  
    type: "text",  
    payload: {  
      message: text  
    }  
  }))  
}
```

The finished function should look like this. Don’t forget to add a path to the function interface with return value `success`.

![](https://files.readme.io/871a754-image.png)

When you run this function within a Voiceflow project, the assistant will recite the fetched cat facts, then move on to the next step through the 'success' port. You can link this to a text step that, for example, could say "Done!" to signal the end of the interaction.

# Specification

> 🚧
>
> ### Node modules imports
>
> Functions code does not fully support module imports, whether it be the CommonJS format or ESModule format.

## Function Code Specification

* Written in JavaScript / ECMAScript.
* The JavaScript engine is V8 and the code executed supports the ES6 standard.
* Contains a default exported main function.
* Accepts a single argument called the **argument object**.
* The argument object contains a field called `inputVars` containing input variable values passed by the step.
* Returns runtime commands to dictate the assistant's actions.
* Functions do not currently support importing modules.

## Runtime Commands

The `RuntimeCommands` is a JSON object, which when returned, specifies the behaviour of a function step. Three types of commands are supported:

* **Next Command:** Dictates the path to follow after the function executes.
* **Output Variables Command:** Sets the output variables with the values to be used later in the conversation.
* **Trace Command:** Produces traces as part of the agent's response.

The schema for the runtime commands is given below as a TypeScript interface:

TypeScript

```
interface RuntimeCommands {
	next?: NextOneCommand | NextManyCommand;
	trace?: Trace[];
	outputVars?: Record<string, string | number | boolean>;
}

interface NextOneCommand {
	path: string;
}

interface NextManyCommand {
	listen: boolean;
	defaultTo: string;
	to: Array<{
		on: MongoQueryObject;
		dest: string;
	}>
}
```

> 📘
>
> ### Next command with a default port
>
> If the function has no paths defined, then a default port is automatically generated. You do not need to send a next command to leave through the default port.

### `on` query

The `NextManyCommand` supports an object of type `QueryObject` for the `on` property. This `QueryObject` is exactly the type of a Mongo query object, used for read operations in MongoDB.

Under the hood, the [sift.js](https://www.npmjs.com/package/sift) library to validate that the incoming request object matches an `on` query using the following logic:

JavaScript

```
[requestObject].filter(sift(on)).length > 0
```

**Example 1 - Exact match**

Suppose we have the following `on` query

JavaScript

```
on: {
  'event.type': 'event_A'
}
```

Suppose we are given the following request objects:

JavaScript

```
{ type: 'event_A', payload: { label: 'example' } } // matches
{ type: 'event_B', payload: { label: 'example' } } // does not match
{ payload: { label: 'example' } }                  // does not match
{ Type: 'event_A', payload: { label: 'example' } } // does not match
```

**Example 2 - $in operator**

Suppose we have the following `on` query

JavaScript

```
on: {
  'event.type': { $in: ['california', 'new york'] }
}
```

Suppose we are given the following request objects:

JavaScript

```
{ type: 'california', payload: { label: 'example' } }.      // matches
{ type: 'new york', payload: { label: 'another example' } } // matches
{ type: 'washington', payload: { label: 'example' } }.      // does not match
{ payload: { label: 'example' } }.                          // does not match
```

**Example 3 - Matching multiple properties**

Suppose we have the following `on` query

JavaScript

```
on: {
  'event.type': 'event_A',
  'event.payload.label': 'example'
}
```

Suppose we are given the following request objects:

JavaScript

```
{ type: 'event_A', payload: { label: 'example' } }.        // matches
{ type: 'event_A', payload: { label: 'another example' } } // does not match
```

## Supported Traces

Traces are response segments from an interaction with the assistant. Voiceflow supports various trace types, including text, visual content, cards, and more. Below are the TypeScript schemas for the supported trace types:

### Available on all project types

TypeScript

```
interface VisualTrace {
  type: "visual",
  payload: {
    image: string;
  }
}

interface DebugTrace {
  type: "debug",
  payload: {
    message: string;
  }
}

interface GeneralButton {
  name: string;      // button label
  request: {         // request object sent to `general-runtime` when button is clicked
    type: string;    // user-defined type value
    payload?: Record<string, any>; // optional payload with any data
  }
}

interface ChoiceTrace {
  type: 'choice',
  payload: {
    buttons: Array<GeneralButton>
  }
}
```

### Available on chat projects

TypeScript

```
interface TextTrace {
  type: "text";
  payload: {
    message: string;
  }
}

interface URLButton {
  name: string;
  payload: {
    actions: Array<{
      type: "open_url",
      url: string;
    }>;
  }
}

interface Card {
  imageUrl: string;
  title: string;
  description: {
    text: string;
  };
  buttons?: Array<URLButton | GeneralButton>;
}

interface CardTrace {
  type: "cardV2",
  payload: Card;
}

interface CarouselTrace {
  type: "carousel",
  payload: {
    cards: Array<Card>;
  }
}
```

### Available on voice projects

TypeScript

```
interface SpeakTrace {
  type: "speak";
  payload: {
    message: string;
  }
}

interface AudioTrace {
  type: "audio";
  payload: {
    src: string; // `src` must be base64 audio data encoded as a string
  }
}
```

## Voiceflow Fetch API

Functions code has access to a modified fetch API, called the Voiceflow Fetch APl. This is mostly identical to the standard [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API), but **there are some important differences**.

For example, to perform a POST request:

1. The first argument of `fetch` is the URL of the server
2. The second argument is an options object supporting the standard fetch options such as `method`, `headers`, and `body`

TypeScript

```
await fetch(
  `<YOUR-NGROK-URL-HERE>`,
  {
    method: 'POST',
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name,
      age
    })
  }
);
```

The **main difference** with the standard Fetch API is how to access the response body of a fetch request. In the standard Fetch API, you would use the `.json()` method. However, in the Voiceflow Fetch API, the response body is available through the `` field.

TypeScript

```
// Standard Fetch API
const response = await fetch("https://someurl.com");
const responseBody = await response.json();

// Voiceflow Fetch API
const responseBody = (await fetch("https://someurl.com")).json;
```

### Extended Fetch Options

To change how the response body is parsed, you may pass in a third argument to `fetch` called the **extended fetch options**. For example, to parse the response instead as plain text, we would do the following:

TypeScript

```
const responseBody = await fetch(
	"https://someurl.com", 
	requestInit, 
	{ parseType: 'text' }
);
const responseContent = responseBody.text;
```

The type definition for the extended fetch options is given below:

TypeScript

```
export interface ExtendedFetchOptions {
    parseType?: 'arrayBuffer' | 'blob' | 'json' | 'text';
}
```

To access the parsed result, access the corresponding property of the return value like so:

TypeScript

```
const data = (await fetch(url, requestInit, { parseType: 'arrayBuffer' })).arrayBuffer;

const data = (await fetch(url, requestInit, { parseType: 'blob' })).blob;

const data = (await fetch(url, requestInit, { parseType: 'json' })).json;

const data = (await fetch(url, requestInit, { parseType: 'text' })).text;
```

## Debugging functions

A trace command can issue a **debug trace**, a type of trace that should include debugging information.

Debug traces are not visible in production, and therefore, are not seen by your users. However, they are visible on the Voiceflow prototype tool and provide diagnostic information that helps the designer resolve bugs.

For example, in the functions code below we return a debug trace:

JavaScript

```
export default async function main(args) {
  return {
    trace: [
      {
        type: "text",
        payload: {
          message: `Attempting to retrieve information on "Tony Rossi"...`,
        },
      },
      {
        type: "debug",
        payload: {
          message: `Failed to retrieve information for user "Tony Rossi"`,
        },
      },
    ],
  };
}
```

This debug trace would appear on the Prototype Tool and the Functions test modal:

![](https://files.readme.io/2e2f52d-Screen_Shot_2023-12-18_at_1.47.26_AM.png)

Use debug traces to provide helpful error messages, so that designers can troubleshoot an issue and resolve bugs when using your function step.

Updated about 2 months ago

---

[Introduction to developing functions](/docs/custom-functions)[Supporting listen in functions](/docs/functions-listen)

Ask AI

* [Table of Contents](#)
* + - [Starting with the Main Function](#starting-with-the-main-function)
    - [Processing Input Variables](#processing-input-variables)
    - [Performing Transformations](#performing-transformations)
    - [Returning Runtime Commands](#returning-runtime-commands)
  + [Making Network Requests](#making-network-requests)
  + [Specification](#specification)
  + - [Function Code Specification](#function-code-specification)
    - [Runtime Commands](#runtime-commands)
    - [Supported Traces](#supported-traces)
    - [Voiceflow Fetch API](#voiceflow-fetch-api)
    - [Debugging functions](#debugging-functions)