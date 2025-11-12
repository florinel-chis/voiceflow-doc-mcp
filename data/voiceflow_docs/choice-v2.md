---
category: general
scraped_at: '2025-11-12T14:07:06.814027'
title: Choice step
url: /docs/choice-v2
---

# Choice step

## Introduction

The Choice Step in Voiceflow is a versatile step that allows you to direct the flow of your conversation based on user inputs. It enables your AI agent to recognize user intents and route the conversation accordingly, or simply use buttons to trigger actions. With the Choice step, you can:

* Add multiple triggers that the agent should listen for.
* Define required entities for each trigger.
* Configure automatic reprompts to guide the user when necessary information is missing.
* Attach buttons to triggers for quick user selection.
* Use both intents and buttons simultaneously within the same Choice Step.
* Set up rules and exit scenarios to manage conversation flow.

This guide will walk you through:

* Adding a Choice step to your project.
* Configuring triggers within the Choice step.
* Setting up required entities, automatic reprompts, buttons, rules, and exit scenarios.
* Managing multiple triggers with independent paths.

![](https://files.readme.io/1238d82cb5dc3a0f076b4a8389b96c8821bfe58167e4763643bcec876b127a26-CleanShot_2024-10-28_at_12.43.12.png)

---

## Adding the Choice Step to Your Canvas

1. **Open the Step Toolbar**: On the left side of your Voiceflow workspace, you'll find the step toolbar containing various steps you can use in your project.
2. **Drag the Choice Step onto the Canvas**: Hover over Listen and locate the **Choice step** and drag it onto your canvas where you want to introduce decision-making based on user input.

---

## Configuring the Choice Step

### 1. Adding Triggers

Triggers represent the possible actions or responses that the user might provide at this point in the conversation. Each trigger can be configured to include an intent or be used with a button, providing flexibility in how users interact with your agent.

#### Adding a Trigger

![](https://files.readme.io/2e562a4be03c0afe7b6c3270e4c5be7c1f04d9b597bd2f9772ebef13a97c329d-CleanShot_2024-10-28_at_12.39.18.png)
  
  

1. **Access the Triggers Section**: In the Choice Step editor, find the **Triggers** label.
2. **Click the “+” Button**: Beside the **Triggers** label, click the “+” button to add a new trigger. This will create an empty trigger.
3. **Configure the Trigger**: Select the newly created trigger from the list to open the configuration modal. From here, you can configure it as an intent-based trigger or attach a button directly to the trigger.

### Intent Selection

#### Intent Configuration

Once you select a trigger, a modal will appear, allowing you to configure an intent for that trigger if needed.

#### Configuring an Intent (Optional)

* **Change Intent**: Use the dropdown at the top of the modal to select an existing intent or create a new one.

#### Required Entities

* **Overview**:

  + **Required Entities** are specific pieces of information needed to fulfill the intent.
  + Adding required entities ensures that the agent collects all necessary data before proceeding.
* **Adding Required Entities**:

  1. **Click the "+" Button** in the **Required Entities** section.
  2. **Select Entities**:
     + Choose from existing entities or create a new one.
  3. **Configure Each Entity** (if applicable):
     + Provide prompts or validation rules specific to the entity.
* **Effects of Adding Required Entities**:

  + **Automatic Reprompt Toggle Appears**: This feature helps the agent prompt the user for missing information.
  + **New Sections Displayed**:
    - **Rules**
    - **Exit Scenarios**

#### Automatic Reprompt

* **Purpose**:

  + Automatically generates prompts to ask the user for any missing or invalid entities required for the intent.
* **Default Setting**:

  + The **Automatic Reprompt** toggle is **ON** by default when required entities are added.
* **Configuring Automatic Reprompt**:

  1. **Toggle Automatic Reprompt**: Ensure it is turned **ON**.
  2. **Access Settings**:
     + Click on the settings icon or label next to the toggle.
  3. **Configure Model Settings**:
     + **AI Model**: Select the AI model to use for generating reprompts.
     + **Temperature**: Adjust the creativity of the AI's responses. Lower values make the output more deterministic.
     + **Max Tokens**: Set the maximum length of the AI's response.
     + **System Prompt**: Optionally provide instructions to guide the AI in generating reprompts.

#### Buttons

* **Purpose**:

  + Attach a button to the trigger, allowing users to trigger the path by clicking rather than typing.
* **Adding a Button**:

  1. **Navigate to the Buttons Section** within the trigger modal.
  2. **Click the "+" Button** to add a new button.
  3. **Set Button Label**:

     + Enter the text for the button.
     + You can use variables to personalize the button label (e.g., "Order {ProductName}").![](https://files.readme.io/fc1a4d74124a4d73bbfcfe9e8660725b1288d511b29c108f0d6e79fb48a194a3-CleanShot_2024-10-28_at_12.40.04.png)
* **Behavior**:

  + Users can either select the button or use natural language input (if trigger includes intent) to active the trigger.

##### Rules and Exit Scenarios

* **Rules**

  + **Purpose**:
    - Define conditions or validations that the user's input must meet for the entities.
  + **Adding Rules**:
    1. **Click the "+" Button** in the **Rules** section.
    2. **Write Natural Language Rules**:
       - Specify criteria for entity validation (e.g., "The date must be within the next 30 days").

![](https://files.readme.io/003af25e5ad83c64ffb8f791658d2f631068c980b8df3501e33a545b7f4a07df-CleanShot_2024-10-28_at_12.41.41.png)
  

* **Exit Scenarios**

  + **Purpose**:

    - Define conditions under which the agent should stop trying to capture required entities and proceed differently.
  + **Adding Exit Scenarios**:

    1. **Click the "+" Button** in the **Exit Scenarios** section.
    2. **Define Exit Conditions**:
       - Specify phrases or situations indicating the user cannot provide the required entities (e.g., "I don't know", "Skip this").
  + **Exit Scenario Path Toggle**:

    - **Toggle ON**: Creates a separate exit path for this exit scenario.
    - **Toggle OFF**: The conversation continues through the main intent path even if an exit scenario is triggered.![](https://files.readme.io/88688782b5d2eb0b980cef683c2e332d59204a4c6230c92500d740861af0ebcf-CleanShot_2024-10-28_at_12.47.05.png)

---

### 2. Managing Multiple Intents

You can add multiple intents to a single Choice Step, each with its own configuration.

#### Adding Multiple Intents

* Repeat the process of adding intents for each new intent you want to include.

#### Independent Configurations

* Each intent can have:

  + **Its Own Required Entities**
  + **Separate Automatic Reprompt Settings**
  + **Individual Buttons**
  + **Specific Rules**
  + **Unique Exit Scenarios and Paths**

#### Exit Scenario Paths

* **Main Port**: The default path the conversation follows when the intent is successfully fulfilled.
* **Exit Scenario Port**: An optional secondary path that is followed if an exit scenario is triggered for that intent.

---

## Connecting Paths Based on Intents

Each intent you add to the Choice Step creates a port on the step, allowing you to define different conversation paths.

### How to Connect Paths

1. **Locate the Ports**: On the bottom of the Choice Step, you'll see ports labeled with your intent names.
2. **Connect to Other Steps**:

   * **Intent Port**:
     + Connect this port to the next step in the conversation when the intent is successfully triggered and required entities are captured.
   * **Exit Scenario Port** (if enabled):
     + Connect this port to an alternative path for handling situations where the user cannot provide required entities.
3. **No Match and No Reply Ports**:

   * **No Match**:
     + Handles inputs that do not match any of the intents.
     + Enable **No Match** in the Choice Step settings to create this port.
   * **No Reply**:
     + Handles situations where the user doesn't respond.
     + Enable **No Reply** to create this port.

---

## Additional Options in the Choice Step

### 1. No Match

#### Purpose

* Handles situations where the user's input doesn't match any of the added intents.

#### How to Enable

* Toggle **No Match** to **ON** in the Choice Step editor.

#### Configuration

* **No Match Reprompt**:

  + Provide a message to prompt the user when their input doesn't match any intents (e.g., "I'm sorry, I didn't understand that. Could you please rephrase?").
* **Follow Path After Reprompts**:

  + **Toggle ON**: After reprompts are exhausted, the conversation will follow the **No Match** path.
  + **Toggle OFF**: The agent will continue to reprompt indefinitely.

#### No Match Path

* Enabling **No Match** creates a **No Match** port on the Choice Step.
* Connect this port to a step that handles unmatched inputs, such as offering help or ending the conversation.

### 2. No Reply

#### Purpose

* Manages situations where the user doesn't respond within a specified time frame.

#### How to Enable

* Toggle **No Reply** to **ON** in the Choice Step editor.

#### Configuration

* **Inactivity Time**:

  + Set how long the agent should wait for a response before considering it a no-reply.
* **No Reply Reprompt**:

  + Provide a message to prompt the user when they haven't responded (e.g., "Are you still there?").
* **Follow Path After Reprompts**:

  + **Toggle ON**: After reprompts are exhausted, the conversation will follow the **No Reply** path.
  + **Toggle OFF**: The agent will continue to reprompt indefinitely.

#### No Reply Path

* Enabling **No Reply** creates a **No Reply** port on the Choice Step.
* Connect this port to a step that handles no-response situations.

### 3. Listen for Other Triggers

#### Purpose

* Allows the agent to recognize and respond to other intents or events while the Choice Step is active.

#### How to Enable

* Toggle **Listen for Other Triggers** to **ON** in the Choice Step editor.

#### Behavior

* **ON**:
  + The agent listens for other intents outside of the ones added to the Choice Step.
  + If the user says something matching another intent, the agent will trigger that intent.
* **OFF**:
  + The agent focuses solely on the intents within the Choice Step.
  + Other intents will not be recognized until after the Choice Step is resolved.

---

## Summary of Choice Step Configuration

1. **Add Intents**:

   * Use the "+" button to add one or more intents.
   * Configure each intent individually.
2. **Configure Required Entities**:

   * Add required entities to each intent as needed.
   * Enable **Automatic Reprompt** to assist users in providing necessary information.
3. **Set Up Buttons**:

   * Optionally attach buttons to intents for user selection.
4. **Define Rules and Exit Scenarios**:

   * Add rules to validate entity inputs.
   * Set up exit scenarios to handle situations where users cannot provide required information.
   * Decide whether to use an exit scenario path for each intent.
5. **Configure Additional Options**:

   * **No Match**: Handle unrecognized inputs.
   * **No Reply**: Manage user inactivity.
   * **Listen for Other Triggers**: Allow or prevent recognition of other intents during this step.
6. **Connect Paths**:

   * Use the ports created for intents, exit scenarios, No Match, and No Reply to define your conversation flow.

---

## Practical Example: Booking an Appointment

Let's illustrate how to use the Choice Step with multiple intents, required entities, and exit scenarios.

### Scenario

You want your agent to handle different appointment-related intents:

* **Schedule Appointment**
* **Reschedule Appointment**
* **Cancel Appointment**

### Steps

1. **Add a Choice Step to Your Canvas**.
2. **Add Triggers**:

   * **Intent 1**: **ScheduleAppointment**

     + **Required Entities**:
       - `AppointmentDate`
       - `AppointmentTime`
     + **Automatic Reprompt**: Enabled.
     + **Rules**:
       - "The appointment date must be at least 24 hours from now."
     + **Exit Scenarios**:
       - "If the user says 'I don't know when', 'I'm not sure yet'."
       - **Exit Scenario Path**: Enabled.
     + **Button**: "Schedule Appointment"
   * **Intent 2**: **RescheduleAppointment**

     + **Required Entities**:
       - `ExistingAppointmentID`
       - `NewAppointmentDate`
       - `NewAppointmentTime`
     + **Automatic Reprompt**: Enabled.
     + **Rules**:
       - "New appointment date must be different from the existing one."
     + **Exit Scenarios**:
       - "If the user says 'I changed my mind', 'Forget it'."
       - **Exit Scenario Path**: Enabled.
     + **Button**: "Reschedule Appointment"
   * **Intent 3**: **CancelAppointment**

     + **Required Entities**:
       - `AppointmentID`
     + **Automatic Reprompt**: Enabled.
     + **Button**: "Cancel Appointment"
3. **Configure No Match**:

   * **Enable No Match**: Toggle **ON**.
   * **No Match Reprompt**: "I'm sorry, I didn't understand that. Please choose an option or tell me what you'd like to do."
   * **Follow Path After Reprompts**: Toggle **ON**.
   * **Connect No Match Port**: Direct to a help message or transfer to a human agent.
4. **Configure No Reply**:

   * **Enable No Reply**: Toggle **ON**.
   * **Inactivity Time**: Set to 30 seconds.
   * **No Reply Reprompt**: "Are you still there? Please let me know how I can assist you."
   * **Follow Path After Reprompts**: Toggle **ON**.
   * **Connect No Reply Port**: End the conversation politely.
5. **Listen for Other Triggers**:

   * **Enable**: Toggle **ON**.
6. **Connect Paths**:

   * **Schedule Appointment Port**: Connect to steps that process scheduling.
   * **Reschedule Appointment Port**: Connect to steps for rescheduling.
   * **Cancel Appointment Port**: Connect to cancellation steps.
   * **Exit Scenario Ports**: For each intent with exit scenarios, connect the exit scenario port to appropriate handling steps.

### Conversation Flow Example

1. **Agent**: "Welcome! How can I assist you today?"  
   **[Displays Buttons: Schedule Appointment | Reschedule Appointment | Cancel Appointment]**
2. **User**: "I need to schedule an appointment."
3. **Agent**: "Sure, when would you like to schedule your appointment?"  
   **[Collects`AppointmentDate` and`AppointmentTime`][Collects `AppointmentDate` and `AppointmentTime`]**
4. **User**: "I'm not sure yet."
5. **Agent**: "No problem. Feel free to let me know when you're ready."  
   **[Follows the Exit Scenario Path for`ScheduleAppointment`][Follows the Exit Scenario Path for `ScheduleAppointment`]**
6. **User**: "Actually, can I reschedule my existing appointment?"
7. **Agent**: "Certainly! May I have your appointment ID?"  
   **[Switches to`RescheduleAppointment` intent][Switches to `RescheduleAppointment` intent]**
8. **User**: **[Provides information]**

---

## Best Practices

* **Clear Intent Definitions**: Ensure each intent has a clear purpose and is not overlapping significantly with others.
* **Effective Prompts**: Write prompts that guide the user effectively toward providing the necessary information.
* **Thoughtful Use of Exit Scenarios**: Use exit scenarios to enhance user experience, allowing them to gracefully opt-out or skip steps.
* **Consistent Configuration**: Keep settings like **Automatic Reprompt** and **Listen for Other Triggers** consistent where appropriate to avoid confusing the user.
* **Testing**: Simulate various conversation paths to ensure that all intents, entities, and scenarios work as intended.
* **User-Friendly Buttons**: If using buttons, make sure labels are clear and actions are immediately understandable.

Updated 5 months ago

---

[Button step](/docs/buttons-v2)[Capture step](/docs/capture-v2)

Ask AI

* [Table of Contents](#)
* + [Introduction](#introduction)
  + [Adding the Choice Step to Your Canvas](#adding-the-choice-step-to-your-canvas)
  + [Configuring the Choice Step](#configuring-the-choice-step)
  + - [1. Adding Triggers](#1-adding-triggers)
    - [Intent Selection](#intent-selection)
    - [2. Managing Multiple Intents](#2-managing-multiple-intents)
  + [Connecting Paths Based on Intents](#connecting-paths-based-on-intents)
  + - [How to Connect Paths](#how-to-connect-paths)
  + [Additional Options in the Choice Step](#additional-options-in-the-choice-step)
  + - [1. No Match](#1-no-match)
    - [2. No Reply](#2-no-reply)
    - [3. Listen for Other Triggers](#3-listen-for-other-triggers)
  + [Summary of Choice Step Configuration](#summary-of-choice-step-configuration)
  + [Practical Example: Booking an Appointment](#practical-example-booking-an-appointment)
  + - [Scenario](#scenario)
    - [Steps](#steps)
    - [Conversation Flow Example](#conversation-flow-example)
  + [Best Practices](#best-practices)