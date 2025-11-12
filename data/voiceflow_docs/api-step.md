---
category: general
scraped_at: '2025-11-12T14:07:17.822445'
title: API step
url: /docs/api-step
---

# API step

Send requests to API endpoints and get responses back.

![](https://files.readme.io/abf9aa8877633d39e03198a600fd1f5522b4854ce1f8c4c86b2b19e1c5cbdf8e-Image_6.png)

The API Step allows you to make custom API calls to connect your assistant with external APIs and data.

The API block consists of several parts:

* The request **type** — GET, POST, PUT, DELETE, PATCH
* The **endpoint** — request URL or {variable}
* **Headers**, **parameters**, and **body** — respective parameter keys & values (can input raw body content code)
* **Capture** Response — entering respective keys & saving/capturing to variables
* **Send** Request — a button to test the API Step or call/request directly from Canvas

![](https://files.readme.io/6b71e44ac054a7db0101f55156f5a00e015425ec7c5c7058c0fda1a5f1d9fad9-CleanShot_2024-12-17_at_10.39.24.png)

There are 5 standard request types available through the API block.

* **GET** — Retrieves information from your data source
* **POST** — Creates information in your data source
* **PUT** — Completely updates information in your data source
* **DELETE** — Deletes information in your data source
* **PATCH** — Partially updates information in your data source

![](https://files.readme.io/6e1cc0fcbd1b49b580221b2ea55923146b4ad46ae608a52514e424137a827ae8-CleanShot_2024-12-17_at_10.41.21.png)

Depending on your assistant design, you should consider using an API step for functions that involve retrieving data from an external database or sending data to another source. Some use cases involve making a new Zendesk (or other similar customer support platforms) ticket request, sending and getting data from an Airtable database, or registering a potential client prospect in an internal repository.

> 📘
>
> ### For reusuable use cases that might require more formatting of data in and out, consider using a [function](https://developer.voiceflow.com/v2.0/docs/function-step) instead of an API step.

## Endpoint

The endpoint is the URL that points to your API. Similar to website URL, your endpoint URL is where your requests will be sent to speak with your API. You can also configure endpoints with { variables } by simply putting them into the link string.

An example API endpoint could look like the following:

`https://api.twitter.com/1.1/search/tweets.json`

## Headers, Body, and Parameters

Your API may need additional information in order to give you information. This information can include data like Usernames, Passwords, Authentication tokens, etc. Typically, these fields will be provided by your API provider in their documentation.

If you want to add a Raw Body (often used for JSON) to the request that references **variables** from your agent, you'll need to write them inside quotes and then use the curly braces: `"{variable_name}"`. There isn't any auto-complete for this, so just make sure to exactly match the name and case of your variables.

For example, here's the Raw Body for adding an entry to Airtable. We include `"{caller_name}"`, `"{booking_time}"` and `"{booking_number}"`, that are entities and variables in our agent.

```
{"records": [
  {
    "fields": {
      "Name": "{caller_name}",
      "Time": "{booking_time}",
      "Group Size": "{booking_number}"
    }
  }
]}
```

## Capture Response/Saving to Variables

Once you have successfully made an API call, you will receive back a JSON object. Once you have this, you will likely want to save some of the information you got back onto Voiceflow to speak back to the user, send to another API or compare to something that a user has said.

You can do this using the “Capture Response” section. If you preview the request, you will be able to select the path of the value you want to store in a variables. Simply select the path key and assign it to an agent variable. Once selected, this will be populated in the API editor.

![](https://files.readme.io/593dbf7bae6ca05b3ebe87ec7759dd009c48d67c2c15f9c3ffb82e51ba195345-CleanShot_2025-01-06_at_09.53.262x.png)
  

A path always begins with “**response**” followed with the path you want to map.

As an example, with an API response like this one:

```
{
  "name": "Voiceflow",
  "product": "Creator"
}
```

You can map the **name** to a variable using `response.name`.

## Failure Paths

Should you wish to expose a path if the request returns an error, you can optionally toggle on the *Failure path* and it will render a new port for you to connect into your fallback flow.

![](https://files.readme.io/6432b2068bdbea0319bbe278808b5fd7984dabc0ed45ec99eaa47e18f824570f-CleanShot_2024-12-17_at_10.53.30.png)

## Send and Test Request

Testing the request allows you to make sure that your API call is working before moving on in your assistant. If it succeeds, you will see a message saying "Success".

You can click on the copy icon beside portions of the JSON to copy the object path and save it into a variable.

### Troubleshooting tips

* Double-check the API documentation for what content types are accepted and compare your configuration to any example requests.
* Re-test the API call using a tool like cURL, Postman or Insomnia.
* If the API endpoint accepts JSON body content and the API returns errors regarding missing fields or incorrect body format, try the following steps:
  + Validate the [JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON) format. Use an online JSON formatter or validator to check if the JSON body format is correct. For example, JSON supports straight quotes (i.e., ' or ") and not curly quotes (i.e., “ and “). Some text editors automatically use curly quotes, which is not valid JSON syntax.
  + Check if there are any unexpected, hidden characters. Use an online tool to reveal hidden characters. Sometimes, a copy-paste of Canvas Steps or text between apps may introduce invisible characters, which are still processed by the API call and may cause errors.

Updated 5 months ago

---

[Function step](/docs/function-step)[JavaScript step](/docs/javascript-step)

Ask AI

* [Table of Contents](#)
* + [Endpoint](#endpoint)
  + [Headers, Body, and Parameters](#headers-body-and-parameters)
  + [Capture Response/Saving to Variables](#capture-responsesaving-to-variables)
  + [Failure Paths](#failure-paths)
  + [Send and Test Request](#send-and-test-request)
  + - [Troubleshooting tips](#troubleshooting-tips)