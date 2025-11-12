---
category: general
scraped_at: '2025-11-12T14:08:50.776366'
title: Custom web chat styling
url: /docs/advanced-styling
---

# Custom web chat styling

Customize the web chat widget to fully fit your brand.

For most use cases, the built-in widget customization options are more than enough. But if you're an advanced user looking for more visual control, you can customize the widget’s appearance with your own CSS.

  

## Styling methods

There are two primary ways to style the web chat widget:

1. Use the built-in configuration fields (e.g. header image, colors, input placeholder)
2. Override the widget’s CSS using your own stylesheet (either hosted or embedded)

  

## Method 1: Built-in styling options

Voiceflow lets you control the widget’s appearance directly in your `chat.load()` configuration using the assistant object. Here’s an example with optional styling parameters:

JavaScript

```
window.voiceflow.chat.load({
  verify: { projectID: '<your-project-id>' },
  url: 'https://general-runtime.voiceflow.com',
  versionID: 'production',
  assistant: {
    type: 'chat',
    renderMode: 'widget', // also accepts 'embed' or 'popover'

    header: {
      hideImage: false,
      imageUrl: 'https://yourdomain.com/logo.png',
      title: 'Chat with Support'
    },

    banner: {
      hide: false,
      title: 'Welcome!',
      description: 'How can I help you today?',
      imageUrl: 'https://yourdomain.com/banner.jpg'
    },

    avatar: {
      hide: false,
      imageUrl: 'https://yourdomain.com/avatar.png'
    },

    inputPlaceholder: 'Type your message here...',
    
    // Optional external stylesheet
    stylesheet: 'https://yourdomain.com/styles.css'
  }
});
```

  

## Method 2: Custom CSS styling

To go beyond basic styling, you can use your own CSS rules to override the default widget styles.

  

### How to target web chat elements

Voiceflow's web chat elements use class names prefixed with `.vfrc`. To customize these, create CSS rules targeting those classes.

View the full list of supported classes

/\*
PAGE CONTENTS

Customize the page that the chat bubble lives on
\*/

/\* .voiceflow-chat  \*/

/\* .vfrc-launcher  \*/

/\* .vfrc-chat--overlay  \*/

/\* .vfrc-prompt  \*/

/\*
CHAT WIDGET HEADER

Customize the content, controls and styling included in your chat widget header, including the Assistant Information.
Note that changes to the assistant information here will be shared across other elements that consume this styling.
\*/

/\* .vfrc-header  \*/

/\* .vfrc-assistant-info  \*/

/\* .vfrc-assistant-info--title  \*/

/\* .vfrc-assistant-info--description  \*/

/\* .vfrc-avatar  \*/

/\* .vfrc-icon  \*/

/\*
CHAT MESSAGE BODY

Customize the layout and display of the chat body, and the conversation's metadata
\*/

/\* .vfrc-chat  \*/

/\* .vfrc-chat--dialog  \*/

/\* .vfrc-chat--spacer  \*/

/\* .vfrc-chat--session-time  \*/

/\* .vfrc-chat--status  \*/

/\* .vfrc-message  \*/

/\* .vfrc-timestamp  \*/

/\*
ASSISTANT RESPONSES

Customize the style and layout of assistant response messages.
\*/

/\* .vfrc-system-response--indicator  \*/

/\* .vfrc-system-response  \*/

/\* .vfrc-system-response--controls  \*/

/\* .vfrc-system-response--list  \*/

/\* .vfrc-system-response--actions  \*/

/\* .vfrc-button  \*/

/\* .vfrc-image  \*/

/\* .vfrc-image--background  \*/

/\* .vfrc-card--content  \*/

/\* .vfrc-card--header  \*/

/\* .vfrc-card--description  \*/

/\* .vfrc-carousel  \*/

/\* .vfrc-carousel--button  \*/

/\* Targeted styling for just the Assistant messages. */
/* .vfrc-system-response .vfrc-message  \*/

/\* Targeted styling for just the Assistant buttons. */
/* .vfrc-system-response .vfrc-button  \*/

/\*
USER RESPONSES

Customize the style and layout of users response messages.
\*/

/\* .vfrc-user-response  \*/

/\* Targeted styling for just the User messages */
/* .vfrc-user-response .vfrc-message  \*/

/\*
FOOTER

Customize the layout and appearance of the message input field and the VF Branding
\*/

/\* .vf-footer  \*/

/\* .vfrc-input  \*/

/\* .vfrc-chat-input--button  \*/

/\* .vfrc-footer--watermark  \*/

  

For example, you could change the background of agent messages like this:

JavaScript

```
.vfrc-system-response .vfrc-message {
  background-color: #000000;
  color: #FFFFFF;
}
```

Once you've written your CSS, there's two ways to pass it into your widget.

  

### Option A: Link a self-hosted stylesheet

You can host your CSS file and provide the link in the `assistant.stylesheet` property:

JavaScript

```
assistant: {
  stylesheet: 'https://yourdomain.com/custom-styles.css'
}
```

  

### Option B: Embed CSS via data URL

If you don’t want to host a CSS file externally, you can encode your CSS as a base64 data URL and include it inline:

JavaScript

```
<script type="text/javascript">
  (function(d, t) {
    var v = d.createElement(t), s = d.getElementsByTagName(t)[0];
    v.onload = function() {
      window.voiceflow.chat.load({
        verify: { projectID: 'PROJECT_ID' },
        url: 'https://general-runtime.voiceflow.com',
        versionID: 'production',
        assistant: {
          stylesheet: 'data:text/css;base64,LnZmcmMtc3lzdGVtLXJlc3BvbnNlIC52ZnJjLW1lc3NhZ2UgeyBiYWNrZ3JvdW5kLWNvbG9yOiAjMDAwMDAwOyBjb2xvcjogI0ZGRkZGRjsgfQ==' // the base64-encoded data URL containing your stylesheet
        }
      });
    };
    v.src = 'https://cdn.voiceflow.com/widget/bundle.mjs';
    v.type = 'text/javascript';
    s.parentNode.insertBefore(v, s);
  })(document, 'script');
</script>
```

Updated 5 months ago

---

[Custom triggers](/docs/web-chat-api)[Custom forms and extensions](/docs/custom-web-chat-widgets)

Ask AI

* [Table of Contents](#)
* + [Styling methods](#styling-methods)
  + [Method 1: Built-in styling options](#method-1-built-in-styling-options)
  + [Method 2: Custom CSS styling](#method-2-custom-css-styling)
  + - [How to target web chat elements](#how-to-target-web-chat-elements)
    - [Option A: Link a self-hosted stylesheet](#option-a-link-a-self-hosted-stylesheet)
    - [Option B: Embed CSS via data URL](#option-b-embed-css-via-data-url)