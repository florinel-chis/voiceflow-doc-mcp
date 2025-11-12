---
category: general
scraped_at: '2025-11-12T14:08:19.253918'
title: Google Sheets
url: /docs/google-sheets
---

# Google Sheets

Use Google Sheets actions in both Agent and Tool steps for dynamic, real-time data interactions with your data.

Easily connect your Voiceflow agent with Google Sheets to store, retrieve, and update spreadsheet data directly from your conversations. Use the Google Sheets actions in both Agent and Tool steps to create powerful data-driven workflows.

  
> 🔐
>
> To use the Google Sheets integration, you'll need to **OAuth into Google Sheets** from the Voiceflow Creator. This ensures your agent can read and write spreadsheet data securely from your connected account.

## What you can do with Google Sheets

The Google Sheets integration supports the following actions:

| Action | Description |
| --- | --- |
| Add to sheet | Append a new row of data to an existing sheet. |
| Create new spreadsheet | Create a completely new spreadsheet in your Google account. |
| Get rows | Retrieve one or more rows from a specific sheet. |
| Get sheet | Retrieve details and structure of a specific sheet. |
| Update sheet | Update data in existing cells or rows within a sheet. |

## Use cases

Here are some common ways to use Google Sheets in your Voiceflow agent's workflow:

* Log user responses or form submissions into a spreadsheet.
* Pull dynamic data (like product lists or prices) into a conversation.
* Maintain an up-to-date database of customer information.
* Track support cases or internal operations directly in Sheets.

Ensure you provide an `LLM description` for each tool to provide the agent with context for when to use them.

> E.g. for `Get rows`, you might provide an LLM description such as `Fetch rows from spreadsheet when user asks about all expenses from budget spreadsheet`.

> 👀
>
> ### Be wary of each action's required arguments.
>
> Each action may require unique parameters such as `spreadsheetURL`, `sheetName`, or `rowNumber`. Decide whether these should be *defaulted, hardcoded, or collected by the agent*. Always provide LLM descriptions for each input variable so the agent knows exactly how to use them.
>
> ![](https://files.readme.io/f5dbb47c269102684ad642b6925440b8fa6a0b822f113a904522e2bb0175db24-CleanShot_2025-08-10_at_11.44.542x.png)

## Frequently asked questions

### Can I write to multiple sheets in the same spreadsheet?

> Yes. As long as you provide the correct `Sheet Name` and `Spreadsheet ID`, the agent can target different sheets within the same document.

### Can I overwrite existing data?

> Yes. The **Update sheet** action allows you to replace existing cell values or rows with new data.

### Can I create a spreadsheet with multiple sheets?

> By default, the **Create new spreadsheet** action creates a single sheet. You can later add more sheets manually in Google Sheets or via the API.

### How can I avoid data duplication?

> When adding rows, ensure you include logic in your flow to check for existing entries before writing to the sheet.

[Doc

## Integrations

Learn more about what integrations are available to supercharge your agent's workflow and capabilities.

Read doc →](https://docs.voiceflow.com/update/docs/integrations#/)

Updated 15 days ago

---

[Gmail](/docs/gmail)[Hubspot](/docs/hubspot)

Ask AI

* [Table of Contents](#)
* + [What you can do with Google Sheets](#what-you-can-do-with-google-sheets)
  + [Use cases](#use-cases)
  + [Frequently asked questions](#frequently-asked-questions)
  + - [Can I write to multiple sheets in the same spreadsheet?](#can-i-write-to-multiple-sheets-in-the-same-spreadsheet)
    - [Can I overwrite existing data?](#can-i-overwrite-existing-data)
    - [Can I create a spreadsheet with multiple sheets?](#can-i-create-a-spreadsheet-with-multiple-sheets)
    - [How can I avoid data duplication?](#how-can-i-avoid-data-duplication)