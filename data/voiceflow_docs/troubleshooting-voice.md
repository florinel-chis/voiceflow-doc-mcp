---
category: general
scraped_at: '2025-11-12T14:09:12.249648'
title: Troubleshooting voice
url: /docs/troubleshooting-voice
---

# Troubleshooting voice

Sometimes your agent does strange things. Let's fix them.

## Limits

Certain voice features have limits. These are:

* **Number of concurrent calls**: this is limited by your [workspace's plan](https://voiceflow.com) .
* **Maximum duration of call:** all calls automatically end after 30 minutes.
* **Maximum user silence:** if the user does not speak or interact for three minutes, all calls will automatically end.

  

## "Sorry, no agents are available to take your call at this time" when calling your agent

* If you hear this message from the agent it means you've hit the limit for concurrent sessions for your workspace's plan. [Upgrade your plan to increase this limit](https://voiceflow.com/pricing).

  

## Integration authorization error

If you receive an `integration authorization error` when connecting your phone number to your agent, double check that you've entered your Twilio credentials (account SID, auth token, and phone number) correctly. If you have and the.issue persists, check if your Twilio account is suspended due to lack of funds.

  

## Calls not routing to your Voiceflow agent

* Ensure that the **Routing** region is US. If it is not, please select US and then press 're-route' to save, you should see a URL that starts with <https://runtime-api.voiceflow.com/>... in the 'A call comes in' section.

  ![](https://files.readme.io/34f88dfaa18ee1fe4e231a8f9786aedcd9a50741ffa05d5d57d42fd1c2f1c4ce-image.png)
* On Twilio, if you are porting a number from another service, check your number's *Configure With* isn't on an existing **TwiML App** or **SIP Trunk**. If so, select the **Webhook, TwiML Bin, Function, Studio Flow, Proxy Service** option and save the configuration. Then reassign the agent on Voiceflow.

  ![](https://files.readme.io/6ae647cb3b51dc082c29be22df4e7c088faa948cb4ceae3decb7da6e8513982d-Screenshot_2024-12-13_at_8.54.00_AM.png)
  + **If the "A call comes in" - "URL" starts with`https://runtime-api.voiceflow.com/...` then it's correct.**
* Confirm that the phone number has been properly assigned to the correct agent and environment in Voiceflow.
* Check that the agent's Interaction Endpoint URL has been correctly configured in the Twilio phone number's webhook settings.
* Verify that the agent is reachable and not throwing errors by testing it in the Voiceflow prototype tool.

Updated 6 months ago

---

[SIP Functionality](/docs/sip-functionality)[Custom interfaces (API)](/docs/custom-interfaces)

Ask AI

* [Table of Contents](#)
* + [Limits](#limits)
  + ["Sorry, no agents are available to take your call at this time" when calling your agent](#sorry-no-agents-are-available-to-take-your-call-at-this-time-when-calling-your-agent)
  + [Integration authorization error](#integration-authorization-error)
  + [Calls not routing to your Voiceflow agent](#calls-not-routing-to-your-voiceflow-agent)