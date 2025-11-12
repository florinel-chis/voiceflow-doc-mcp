---
category: general
scraped_at: '2025-11-12T14:08:44.389681'
title: Setting the version and runtime URL
url: /docs/custom-configurations
---

# Setting the version and runtime URL

Customize the version of your agent that the web chat widget uses, and set the runtime environment.

To embed a Voiceflow agent in your website, you'll use the `chat.load()` function. This function initializes the web chat widget by specifying essential configuration values like your project ID, runtime URL, and version ID.

Here’s an example of the default script snippet you’ll find in your [web chat integration settings](/docs/chat-widget#how-to-add-your-agents-widget-to-your-website):

JavaScript

```
<script type="text/javascript">
  (function(d, t) {
    var v = d.createElement(t), s = d.getElementsByTagName(t)[0];
    v.onload = function() {
      window.voiceflow.chat.load({
        verify: { projectID: 'YOUR_PROJECT_ID' },
        url: 'https://general-runtime.voiceflow.com',
        versionID: 'production'
      });
    }
    v.src = 'https://cdn.voiceflow.com/widget/bundle.mjs';
    v.type = 'text/javascript';
    s.parentNode.insertBefore(v, s);
  })(document, 'script');
</script>
```

  

## Set a version ID (optional)

The `versionID` specifies which version of your agent to load. If not set, this will default to `development`. The code snippet provided in your agent's integration settings automatically sets this to `production`.

Use `development` to test and iterate on your agent without affecting your production setup. This is helpful while actively building in Voiceflow's creator tool. Note that if `versionID` is set to `production` before publishing your agent, the web chat widget will not render any messages.

JavaScript

```
// Optional versionID configuration
versionID: 'development' | 'production' | '<specific-version-id>'
```

To see your latest changes when testing a development version, click the **Run** button or press `R` from your agent's canvas to push updates.

  

## Set a runtime URL (optional)

> 🏢
>
> ### This feature is only available to Enterprise customers.

  

The `url` property defines the runtime endpoint the widget communicates with. This is especially important for Enterprise users running on Private Cloud environments. If you're not on Private Cloud, you can safely use the default:

JavaScript

```
// Optional URL override
url: 'https://general-runtime.voiceflow.com'
```

Private Cloud customers should replace this with their dedicated runtime endpoint provided by Voiceflow.

Updated 5 months ago

---

[Web chat widget](/docs/chat-widget)[Chat persistence](/docs/chat-persistence)

Ask AI

* [Table of Contents](#)
* + [Set a version ID (optional)](#set-a-version-id-optional)
  + [Set a runtime URL (optional)](#set-a-runtime-url-optional)