---
category: general
scraped_at: '2025-11-12T14:07:47.245236'
title: Using Events
url: /docs/using-the-events-cms
---

# Using Events

**How Events Work in Voiceflow**

Events in Voiceflow are custom triggers that you define and are invoked by the client application sending a request to the Voiceflow runtime. Here’s how the process works:

1. **Event Definition**: You create events in the **Event CMS**, specifying names and descriptions that represent particular triggers.
2. **Association with Workflows**: You assign these events to specific flows in your agent, using the **Event Trigger** in the Trigger step.
3. **Client-Side Triggering**: The client application sends a request to the Voiceflow runtime API or uses the Voiceflow Web Chat widget to trigger the event.
4. **Workflow Initiation**: The runtime processes the event request and initiates the corresponding flow within your agent.

This event-driven approach enhances your agent’s ability to interact based on user actions within the client application, making it more intelligent and adaptable.

**Getting Started with Events**

To start using events in your agent, follow these steps:

**1. Define Events in the Event CMS**

Access the Event CMS within Voiceflow to create events that represent the triggers you need.

* **Create New Event**: Specify a clear and descriptive name that corresponds to the user action.
* **Add Description**: Provide details about what the event represents and when it should be triggered by the client.

**2. Assign Events to Flows**

In your agent’s design:

* **Use the Trigger Step**: Add a **Trigger** step to the flow you want to initiate with the event.
* **Select Event Trigger**: Choose **‘Event’** as the trigger type.
* **Choose the Event**: Select your defined event from the list.

**3. Implement Client-Side Triggering**

Update your client application to send event requests to the Voiceflow runtime when specific user actions occur. This can be done via:

* **REST API Calls**: Use Voiceflow’s runtime REST API to send requests containing the event name and any relevant data.
* **Voiceflow Web Chat Widget**: Utilize the window.voiceflow.chat.interact() method to trigger events directly from the web chat widget.

**4. Test and Refine**

* **Simulate User Actions**: Perform the actions in your application that should trigger events to ensure your agent responds correctly.
* **Monitor Responses**: Verify that the conversation flows as expected when events are triggered.
* **Iterate**: Make adjustments based on testing to optimize the user experience.

**Implementing Client-Side Triggering**

**A. Invoking Events via the API**

To trigger an event from your client application using the Voiceflow Runtime API, send a POST request to the appropriate endpoint with the event payload.

**API Request Payload Example**

JSON

```
{
  "action": {
    "type": "event",
    "payload": {
      "event": {
        "name": "checkout"
      }
    }
  }
}
```

**Explanation**:

* **action.type**: Set to "event" to indicate that you’re triggering an event.
* **action.payload.event.name**: The name of the event you’ve defined in the Event CMS (e.g., "checkout").

**API Request Example Using cURL**

Bash

```
curl -X POST 'https://general-runtime.voiceflow.com/state/userID' \
  -H 'Content-Type: application/json' \
  -d '{
        "action": {
          "type": "event",
          "payload": {
            "event": {
              "name": "checkout"
            }
          }
        }
      }'
```

**Steps to Implement**

1. **Detect User Action**: In your application, detect the specific action (e.g., user clicks the “Checkout” button).
2. **Send API Request**: When the action occurs, send a POST request to the Voiceflow Runtime API with the event payload.
3. **Handle Response**: Process the response from the agent to update the UI or continue the conversation.

**B. Invoking Events via Voiceflow’s Native Web Chat Widget**

If you’re using Voiceflow’s Web Chat widget, you can trigger events directly from your web application using JavaScript. The script should be placed within the `<body>` tags of your HTML page.

**Simplified Example: Triggering an Event on Button Click**

**HTML Code**

Place this code within the `<body>` tags of your HTML page:

HTML

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Your Page Title</title>
  <!-- Other head elements -->
</head>
<body>

  <!-- Your page content -->

  <!-- Example: A button to trigger an event -->
  <button id="myButton">Click Me</button>

  <!-- Voiceflow Web Chat Widget Script -->
  <script type="text/javascript">
    (function(d, t) {
      var v = d.createElement(t), s = d.getElementsByTagName(t)[0];
      v.onload = function() {
        // Initialize the Voiceflow Web Chat widget
        window.voiceflow.chat.load({
          verify: { projectID: 'YOUR_PROJECT_ID' },
          url: 'https://general-runtime.voiceflow.com',
          versionID: 'production'
        }).then(() => {

          // Add event listener to the button
          document.getElementById('myButton').addEventListener('click', () => {
            // Open the chat widget
            window.voiceflow.chat.open();

            // Send the 'button_clicked' event to Voiceflow
            window.voiceflow.chat.interact({
              type: 'event',
              payload: {
                event: {
                  name: 'button_clicked' // The event name defined in your Event CMS
                }
              }
            });
          });

        });
      };
      v.src = "https://cdn.voiceflow.com/widget/bundle.mjs";
      v.type = "text/javascript";
      s.parentNode.insertBefore(v, s);
    })(document, 'script');
  </script>

</body>
</html>
```

**Explanation of the Code**

1. **HTML Button**:

* A button with the ID myButton is added to the HTML. This is the button the user will click to trigger the event.

2. **Include the Voiceflow Web Chat Widget Script**:

* The widget script is included within the `<body>` tags.
* The script loads the Voiceflow Web Chat widget on your page.

3. **Widget Initialization**:

* The `window.voiceflow.chat.load()` function is called within the v.onload callback to ensure it runs after the widget script is loaded.
* The .then() method is used to run code after the widget is fully initialized.

4. **Setting Up the Event Listener**:

* Within the `.then()` block, an event listener is added to the button with `id="myButton"`.
* When the button is clicked:
  + The chat widget is opened using `window.voiceflow.chat.open()`.
  + An event named 'button\_clicked' is sent to the agent using `window.voiceflow.chat.interact()`.

**Steps to Implement**

1. **Define the Event in Voiceflow**:

* Go to the **Event CMS** in your Voiceflow project.
* Create a new event named button\_clicked.
* Add a description if desired.

2. **Associate the Event with a Flow**:

* In your agent’s canvas, add a **Trigger** step where you want the flow to start.
* Set the trigger type to **Event** and select button\_clicked from the list.

3. **Add the Button to Your Web Page**:

* Place the HTML code for the button in your web page where appropriate.

4. **Include the Web Chat Widget Script**:

* Ensure the widget script is included within the `<body>` tags of your HTML.

5. **Test the Implementation**:

* Open your web page in a browser.
* Click the button labeled “Click Me”.
* The chat widget should open, and the agent should respond according to the flow you’ve designed for the button\_clicked event.

**Additional Notes**

* **Consistency in Event Names**: Ensure that the event name used in `window.voiceflow.chat.interact()` matches exactly with the event name defined in your Event CMS and associated with a Trigger step.

**Example: Triggering an Event on “Subscribe” Button Click**

If you have a “Subscribe” button in your HTML:

HTML

```
<button id="subscribeButton">Subscribe</button>
```

You can set up an event listener for it:

HTML

```
<!-- Voiceflow Web Chat Widget Script -->
<script type="text/javascript">
  (function(d, t) {
    var v = d.createElement(t), s = d.getElementsByTagName(t)[0];
    v.onload = function() {
      // Initialize the Voiceflow Web Chat widget
      window.voiceflow.chat.load({
        verify: { projectID: 'YOUR_PROJECT_ID' },
        url: 'https://general-runtime.voiceflow.com',
        versionID: 'production'
      }).then(() => {

        // Add event listener to the "Subscribe" button
        document.getElementById('subscribeButton').addEventListener('click', () => {
          // Open the chat widget
          window.voiceflow.chat.open();

          // Send the 'newsletter_signup' event to Voiceflow
          window.voiceflow.chat.interact({
            type: 'event',
            payload: {
              event: {
                name: 'newsletter_signup' // The event name defined in your Event CMS
              }
            }
          });
        });

      });
    };
    v.src = "https://cdn.voiceflow.com/widget/bundle.mjs";
    v.type = "text/javascript";
    s.parentNode.insertBefore(v, s);
  })(document, 'script');
</script>
```

### Best Practices for Using Events

* **Be Specific with Request Names**
  + Use clear, descriptive request names for your events to ensure they are easily identifiable and manageable.
    - **Good Example**: `userClickedCheckout`
    - **Poor Example**: `Event1`
* **Consider the User Experience**
  + Ensure that the agent’s responses to events are contextually appropriate and enhance the user’s interaction.
    - **Relevance**: Only trigger events that provide value to the user in that context.
  + **Timing**: Trigger events at appropriate moments in the user journey to avoid overwhelming the user.
  + **Personalization**: Tailor messages to the user’s actions and preferences.

### Learn More

* [**Using the Event CMS**](/docs/using-the-events-cms): Learn how to define and manage events in the Event CMS.
* [**Voiceflow Dialog Manager API**](/reference/stateinteract-1): Get detailed information on how to interact with the Voiceflow Dialog Manager API.
* [**Voiceflow Web Chat**](/docs/web-chat-overview): Understand how to integrate and use the Voiceflow Web Chat widget in your application.

Updated 5 months ago

---

[Introduction to Events](/docs/introduction-to-events)[Variables](/docs/variables)

Ask AI

* [Table of Contents](#)
* + [Best Practices for Using Events](#best-practices-for-using-events)
  + [Learn More](#learn-more)