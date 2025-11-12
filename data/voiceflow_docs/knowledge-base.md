---
category: general
scraped_at: '2025-11-12T14:08:02.955603'
title: Knowledge base tool
url: /docs/knowledge-base
---

# Knowledge base tool

Query data from your agent's knowledge base to answer questions.

The Knowledge base tool lets your agent query data from the Knowledge base from within the [Agent step](/docs/agents). It’s useful when you want the agent to look up information on demand - like answering FAQs, pulling product details, or referencing company docs - then incorporate this information into human-sounding responses.

  

## Querying the knowledge base from inside the Agent step

> ℹ️
>
> This is our recommended approach to querying the knowledge base, as it allows your agent to automatically interpret the information retrieved and turn it into human-readable responses.

  

To enable querying the knowledge base from inside an [Agent step](/docs/agents), open your Agent step then turn on the **Knowledge base** toggle on the sidebar of the Agent popup.

[](https://w17llroiln.ufs.sh/f/JH4JLc5mceYkd0EZs5lpu1oeO8lNrvZq7mJiBcVy0XgAjEbS)

Once enabled, you can also choose to set the tool's LLM description. This tells your agent when to query the knowledge base. If you're using the knowledge base to store a specialized type of data - such as product information - we recommend updating the default instructions to be more specific.

The following advanced query settings are also available:

* **Query** - by default, Voiceflow will use the user's last message as the query used to search the knowledge base. You can override this behaviour by providing a custom query. Please note that the **exact** query entered into this box will be used - this isn't an input where you should enter a prompt!
* **Chunk limit** - this determines the maximum number of chunks that can be returned by the knowledge base. By default, three chunks will be returned.
* **Metadata filtering** - if you set custom metadata when [importing data to your knowledge base](/docs/importing-data-to-the-knowledge-base), you can filter your agent's querying using this option. To do so, press the plus button and select a metadata key that exists in your imported data. Then, either enter a default value (to force a specific value to be used), or set the LLM description (to allow the agent to dynamically set this value).

  

## Using the KB search step

While we don't recommend using it, the legacy [KB search step](/docs/kb-search) is available if you'd like to manually query the knowledge base from outside the Agent step. If you do this, you'll also need to pass queried response into the [Prompt step](/docs/prompt-step) as a variable to generate a useful response.

Updated 14 days ago

---

[Secrets](/docs/secrets-manager)[Importing data](/docs/importing-data-to-the-knowledge-base)

Ask AI

* [Table of Contents](#)
* + [Querying the knowledge base from inside the Agent step](#querying-the-knowledge-base-from-inside-the-agent-step)
  + [Using the KB search step](#using-the-kb-search-step)