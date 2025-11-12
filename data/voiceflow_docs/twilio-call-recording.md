---
category: general
scraped_at: '2025-11-12T14:09:04.315125'
title: Call recording
url: /docs/twilio-call-recording
---

# Call recording

Monitor your agent's calls and measure quality.

Voiceflow supports call recording for Twilio-powered voice experiences, including both inbound and outbound calls. This feature allows you to automatically record conversations handled through your Voiceflow agent when connected via Twilio, enabling quality assurance and compliance check workflows.

## Enabling and disabling call recording

> ⚠️
>
> You are solely responsible for complying with applicable laws related to call recording and consent in your region. Voiceflow does not access, store, or manage any call recordings. All recordings are handled directly by your Twilio account. Voiceflow is not liable for any misuse of the recording feature.

  

Call recording can be enabled by opening the settings tab of your agent, opening **Behaviour** settings, then selecting **Voice**. The **save call recordings** toggle can be found bottom of this page.

[](https://yz5du1veb1.ufs.sh/f/9fKud4NeF5NSq73XJyBe98Elmq4kxJ1Vv0CSoXDObGzif7WU)

  

## Listening to call recordings

Calls can be listened to from your [Twilio console](https://console.twilio.com/). Login to your Twilio account, then navigate to **Monitor > Logs > Call recordings** to listen to recordings.

[](https://yz5du1veb1.ufs.sh/f/9fKud4NeF5NSKowMrczNIhSvxwGVX58OPtY0fWsCKNQblBjr)

  

## Limitations

Please note that only calls routed through a phone number are able to be recorded. Voice calls over the web (for example, through the [web chat widget](/docs/chat-widget) cannot be recorded at this time.

Updated 6 months ago

---

[Managing interuptions](/docs/interruption-behavior)[Configuring voice settings](/docs/configuring-voice-settings)

Ask AI

* [Table of Contents](#)
* + [Enabling and disabling call recording](#enabling-and-disabling-call-recording)
  + [Listening to call recordings](#listening-to-call-recordings)
  + [Limitations](#limitations)