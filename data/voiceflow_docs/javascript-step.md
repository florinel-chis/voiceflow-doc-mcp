---
category: general
scraped_at: '2025-11-12T14:07:19.568031'
title: JavaScript step
url: /docs/javascript-step
---

# JavaScript step

Run custom JavaScript to manipulate variables or control logic.

![](https://files.readme.io/066734229cab35b1378481902918e55d24605558c46b433d08a7f2cb018a587c-Image_7.png)

The JavaScript step lets you write and execute short JavaScript snippets (ES6 on V8) directly in your agent. It’s useful for logic that doesn’t require an external API call or reusable function like parsing JSON, modifying variables, or adding conditional paths.

This step runs once when reached and evaluates immediately. If your use case involves longer or reusable code, we recommend using a [Function](/docs/functions) instead.

  

## Basic usage

To use the JavaScript step, drag it onto the canvas and click into the step to open the code editor.

All of the agent's variables are automatically available for use—no need to reference them with curly braces. You can update variable values by reassigning them directly.

Here's an example of a JavaScript step that increments the `score` variable by 1:

[](https://yz5du1veb1.ufs.sh/f/9fKud4NeF5NSEnaxIH9641VSkrpQRJIKob2De5U3aXGdyMh8)

  

## Paths

The JavaScript step supports paths, which allow you to route your agent based on the value that is returned by the JavaScript step. There are two ways to use paths: with the standard paths, or using custom paths.

### Standard paths

The code step has two standard paths: `Default` and `Fail`. The Default path will be followed if your code is successfully run, and the Fail path will be followed if your code fails to run or has an error during its execution.

![](https://files.readme.io/66838cf9b87ac246bbd270fb86109d4f4827e4e6fca36279de58063274f957e2-CleanShot_2025-06-04_at_10.34.232x.png)
  

### Custom paths

You can add up to 10 custom paths to route users based on your logic. Each path must be named. Use a `return [path_name]` statement in your code to route the agent to that path. If no path is returned, the flow continues through the `Default` path.

Here's example with two custom paths: `victory`, `defeat`. If the `score` variable is above `100`, `victory` is returned. If `score` is less than `0`, then `defeat` is returned. Otherwise, the `Default` path is followed.

[](https://yz5du1veb1.ufs.sh/f/9fKud4NeF5NS7skiv4KUJ2mGoWcAYZ4TIKVbRjQtdHvh1CLu)

JavaScript

```
if (score > 100) { 
  return "victory" 
} else if (score < 0) { 
  return "defeat" 
} 
// otherwise it will go down the Default path here
```

  

## Limitations

Some constraints to consider when using the JavaScript step include:

* JavaScript steps **cannot be used to make requests to external servers**, so cannot be used to call external APIs. Alternatively, you can use the API Step to pull or push data between your Voiceflow agent and a third-party system, or [functions](https://developer.voiceflow.com/v2.0/docs/custom-functions).
* JavaScript steps do not currently support importing modules.
* JavaScript steps cannot be used to create new variables. Any variables that you want to use after the JavaScript step is executed must already exist before being referenced in the JavaScript step.

  

## Debugging

### Common error: TypeError when testing the JavaScript step

In the Creator tool, if a variable hasn’t been set before the step runs, it defaults to `0`. This can lead to a `TypeError` if your code expects a string or other type.

For example, this will fail if username hasn’t been set:

JavaScript

```
username.toLowerCase();
```

To avoid this, always check for the variable first:

JavaScript

```
if (username) {
  username = username.toLowerCase();
}
```

Updated 5 months ago

---

[API step](/docs/api-step)[KB search step](/docs/kb-search)

Ask AI

* [Table of Contents](#)
* + [Basic usage](#basic-usage)
  + [Paths](#paths)
  + - [Standard paths](#standard-paths)
    - [Custom paths](#custom-paths)
  + [Limitations](#limitations)
  + [Debugging](#debugging)
  + - [Common error: TypeError when testing the JavaScript step](#common-error-typeerror-when-testing-the-javascript-step)