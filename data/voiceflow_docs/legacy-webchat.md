---
category: general
scraped_at: '2025-11-12T14:11:42.975920'
title: Migrating to the new web chat
url: /docs/legacy-webchat
---

# Migrating to the new web chat

Welcome to our migration guide for Voiceflow's new webchat experience. This guide will walk you through the necessary steps to upgrade from the legacy webchat to our latest version, ensuring a smooth transition while maintaining your existing customizations where possible.

## Key Changes and Timeline

**The legacy webchat will be deprecated on June 15th, 2025.** To ensure uninterrupted service and access to new features, you should migrate to the new version before this date. The legacy version will continue to function normally during the migration period, giving you time to test and validate the new implementation.

## Updating Your Webchat Implementation

### 1. Replacing the Snippet

The most important step in migrating to the new webchat is updating your implementation snippet. The new version uses a different initialization approach that provides enhanced functionality and better performance.

To get started:

1. Navigate to the Webchat Settings page in your VoiceFlow dashboard
2. Select the "New" tab
3. Copy the new snippet provided

![](https://files.readme.io/70b30868837b43d8f2933bb0c741697ee6c3aa0eaedb39b5942ae72606147558-CleanShot_2025-01-22_at_12.54.51.png)
  

*Example Old Snippet (Legacy Version):*

JavaScript

```
<script type="text/javascript">
  (function(d, t) {
      var v = d.createElement(t), s = d.getElementsByTagName(t)[0];
      v.onload = function() {
        window.voiceflow.chat.load({
          verify: { projectID: 'XXX' },
          url: 'https://general-runtime.voiceflow.com',
          versionID: 'production'
        });
      }
      v.src = "https://cdn.voiceflow.com/widget/bundle.mjs"; v.type = "text/javascript"; s.parentNode.insertBefore(v, s);
  })(document, 'script');
</script>
```

*New Snippet:*

JavaScript

```
<script type="text/javascript">
  (function(d, t) {
      var v = d.createElement(t), s = d.getElementsByTagName(t)[0];
      v.onload = function() {
        window.voiceflow.chat.load({
          verify: { projectID: 'XXX' },
          url: 'https://general-runtime.voiceflow.com',
          versionID: 'production'
        });
      }
      v.src = "https://cdn.voiceflow.com/widget-next/bundle.mjs"; v.type = "text/javascript"; s.parentNode.insertBefore(v, s);
  })(document, 'script');
</script>
```

### 2. Chat Persistence Configuration

In the new webchat, chat persistence is configured directly in the snippet rather than through the UI. This gives you more control and flexibility over conversation persistence across sessions and browser tabs.

To configure persistence, add the `persistence` property to your assistant configuration:

JavaScript

```
window.voiceflow.chat.load({
  verify: { projectID: 'your-project-id' },
  url: 'your-runtime-url',
  versionID: 'production',
  assistant: {
    persistence: 'localStorage' // Configure persistence here
  }
});
```

Available persistence options:

* `'localStorage'` (default): Conversations persist across page refreshes and browser sessions
* `'sessionStorage'`: Conversations persist across page refreshes but reset when all tabs are closed
* `'memory'`: Conversations reset on each page refresh or new tab

### 3. Custom CSS and Styling

If you're using custom CSS to style your webchat, most of your existing styles should continue to work. We've maintained compatibility with legacy class names where possible. However, there are some important considerations:

Important notes about CSS compatibility:

* Most existing class names are preserved and still target the correct elements
* Some components may have different internal structure or additional wrapper elements
* Certain elements (like timestamps) have been removed or restructured
* New features and components may use new class names
* Some elements might require updated CSS selectors due to structural changes

We strongly recommend:

1. Testing your custom CSS thoroughly with the new webchat
2. Reviewing and updating selectors that may no longer work as expected
3. Reaching out to our support team if you need specific elements to be made targetable with class names

Remember that targeting specific DOM elements with CSS or JavaScript is inherently fragile. While we strive to maintain compatibility, structural changes may be necessary for improvements and new features.

### 4. Extensions

If you're using custom UI extensions with the current webchat, you'll be pleased to know that extension support continues in the new version. However, you will need to port your extensions to work with the new implementation. The core functionality remains the same, but you'll need to:

1. Update your extension code to use the new webchat's initialization pattern
2. Test your extensions thoroughly in a development environment
3. Deploy updated extensions alongside the new webchat snippet

### 5) Proactive Messages

Please note that proactive messages are temporarily unavailable in the new webchat version. We are actively working on implementing this feature, and it will be available soon. In the meantime, you have two options:

1. Continue using the legacy webchat if proactive messages are critical to your implementation
2. Migrate to the new webchat without proactive messages and add them back when the feature becomes available

We will notify all users when proactive message support is released for the new webchat.

## Testing Your Migration

Before deploying to production, we recommend:

1. Implementing the new webchat in a development environment
2. Testing all existing customizations and features
3. Validating chat persistence behavior
4. (If applicable) Testing custom CSS and styling across different devices and browsers
5. (If applicable) Verifying the functionality of any extensions you've implemented

## Need Help?

If you encounter any issues during migration or have questions about specific features:

* Join our community forum at <https://link.voiceflow.com/community>

We're here to ensure your migration is successful and to help you take advantage of all the new features and improvements in our latest webchat version.

Updated 6 months ago

---

[Allowing dangerous HTML elements](/docs/web-chat-developer-information)[Embed and customize styling](/docs/embed-customize-styling)

Ask AI

* [Table of Contents](#)
* + [Key Changes and Timeline](#key-changes-and-timeline)
  + [Updating Your Webchat Implementation](#updating-your-webchat-implementation)
  + - [1. Replacing the Snippet](#1-replacing-the-snippet)
    - [2. Chat Persistence Configuration](#2-chat-persistence-configuration)
    - [3. Custom CSS and Styling](#3-custom-css-and-styling)
    - [4. Extensions](#4-extensions)
    - [5) Proactive Messages](#5-proactive-messages)
  + [Testing Your Migration](#testing-your-migration)
  + [Need Help?](#need-help)