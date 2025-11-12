---
category: general
scraped_at: '2025-11-12T14:09:01.020322'
title: Outbound calls
url: /docs/outbound-calls
---

# Outbound calls

Make your agent call phone numbers - programatically.

Voiceflow supports outbound calling using Twilio, allowing your agent to initiate a call to any number via API. This is useful for automating voice actions - such as welcome calls, reminders, or follow-ups - triggered from tools like Zapier or your own scripts.

> ⚠️
>
> ### Comply with your local regulations regarding automated calls
>
> In many regions, it is a violation of law to create automated outbound calls without consent. This may lead to your Twilio number or account being suspended and potentially incur fines. You are solely responsible for ensuring compliance with all relevant regulations.
>
> * [Twilio Phone Number Regulations](https://www.twilio.com/en-us/guidelines/regulatory)
> * [Twilio Voice Guidelines](https://www.twilio.com/en-us/guidelines/voice)

## How it works

To trigger an outbound call, your app must make a `POST` request to a Voiceflow API endpoint associated with your agent. You can find this endpoint by navigating to **Interfaces > Telephony > View Outbound API**. Each agent has a unique API URL based on its internal ID.

[](https://yz5du1veb1.ufs.sh/f/9fKud4NeF5NS6cFRoyG9t5VYWaO0GfNrPI1S4ncjDlbBKXs7)

  

The API is shown in a `curl` format. It must include an `Authorization` header with the [associated API Key](/reference/how-to-get-your-voiceflow-project-api-key#/) of the agent. This can be found under **Interfaces > API keys**.

  

## API reference

### Endpoint

`POST https://runtime-api.voiceflow.com/v1alpha1/phone-number/<AGENT_ID>/outbound`

  

### Headers

| Header | Value |
| --- | --- |
| `Authorization` | `Bearer <your Voiceflow API Key>` ([How to get it](/reference/how-to-get-your-voiceflow-project-api-key#/)) |
| `Content-Type` | `application/json` |

  

### Body

JSON

```
{
  "to": "+15551234567",
  "variables": {
    "user_name": "Jane",
    "account_type": "Premium"
  },
  "amd": true
}
```

* `to`: The phone number to call (E.164 format).
* `variables` (Optional): A JSON object with any Voiceflow variables to inject at launch.
* `amd` (Optional): whether to use built-in answering machine detection or not.
  + [Twilio](https://www.twilio.com/docs/voice/answering-machine-detection) - `asyncAmd: true` `machineDetection: 'DetectMessageEnd'`.

  

## Concurrency limits

Outbound calls share the same concurrency pool as inbound calls. The number of simultaneous calls you can make is [determined by your plan limits](https://voiceflow.com/pricing).

  

## Troubleshooting

### 500 Internal Server Error

If you're seeing a 500 error, your Twilio number may not have outbound permissions for the region you're calling. Make sure the region is enabled in your [Twilio geo-permissions dashboard](https://www.twilio.com/console/voice/calls/geo-permissions/low-risk).

Updated 4 months ago

---

[Phone](/docs/telephony)[Managing interuptions](/docs/interruption-behavior)

Ask AI

* [Table of Contents](#)
* + [How it works](#how-it-works)
  + [API reference](#api-reference)
  + - [Endpoint](#endpoint)
    - [Headers](#headers)
    - [Body](#body)
  + [Concurrency limits](#concurrency-limits)
  + [Troubleshooting](#troubleshooting)
  + - [500 Internal Server Error](#500-internal-server-error)