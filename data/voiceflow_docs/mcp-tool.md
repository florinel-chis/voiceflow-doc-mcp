---
category: general
scraped_at: '2025-11-12T14:08:25.426628'
title: MCP
url: /docs/mcp-tool
---

# MCP

Send requests to any MCP (Model Context Protocol) server.

> ℹ️
>
> MCP, or Model Context Protocol, is a standardized way for your agent to connect to external services. Think of it as a layer on top of an API that gives the agent context on how to use the API. [You can learn more about MCP here](https://modelcontextprotocol.io/docs/getting-started/intro).

  

With the MCP tool, your agent can connect to any MCP server directly from within the Agent step or Tool step. This allows you to bring in data, trigger external actions, or use custom logic that lives outside of Voiceflow. It’s helpful when you want your AI agent to be able to access external services that don't have built-in [Integration tools](/docs/integrations).

  

## Basic usage

To connect to a MCP server from inside your Voiceflow agent, the server must be hosted and accessible from the internet. Local MCP servers are not supported by Voiceflow. You can find a [list of self-hosted, officially supported MCP servers here](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#%EF%B8%8F-official-integrations), or can use a tool such as [Zapier MCP](https://docs.zapier.com/mcp/home) to build a hosted MCP server.

  

### Using the MCP tool inside the Agent step

[](https://yz5du1veb1.ufs.sh/f/9fKud4NeF5NSstyhA68zzvNuIPLsxO2KUc05GVE9RlySWktC)

Once your MCP server is hosted, open your [Agent step](/docs/agents) and click the **MCP** option in the tools section of the sidebar. Then, click **Create MCP tool**. You'll then be asked to provide the following information:

* **Server name** - this can be set to anything, and is a user-friendly name for your MCP server that'll be shown inside Voiceflow.
* **Server URL** - enter the root URL of your server. This shouldn't be the URL of any specific endpoint, just the root URL used to access your MCP server.
* **Headers** - this is most often used for authentication, and allows you to pass in API keys, auth tokens, and other similar values to your MCP server. Headers are provided as a key-value pair.

You can also optionally add an image to your server, which will be displayed inside Voiceflow.

Once you've inputted the required values, click **Add MCP server**. You should then see the tools available on your server - click one to add it to your agent. Finally, set the tool's LLM description to describe what the tool is and when it should be called, as well as providing any required input variables.

  

### Using the MCP tool inside the Tool step

The MCP tool can also be used with the [Tool step](/docs/tool-step). To do so, add the Tool step to your canvas, select **New tool**, then **MCP**. Then, follow the same process as with the Agent step to connect your MCP server to Voiceflow.

  

## Managing MCP servers

You can manage your agent's MCP servers from **Settings** > **MCP Servers**. From here, you can add new MCP servers to your agent and modify data related to an existing MCP server (such as the server's name, image, URL, or headers). You can also re-sync a server's information to your agent, updating the endpoints available to your agent.

![](https://files.readme.io/a4f8bee122fa788529b462ad18d3ca362bfcdaf757e331b21672c0cbf3f6645c-CleanShot_2025-09-25_at_20.46.272x.png)

Updated about 2 months ago

---

[Make](/docs/make)[Salesforce](/docs/salesforce)

Ask AI

* [Table of Contents](#)
* + [Basic usage](#basic-usage)
  + - [Using the MCP tool inside the Agent step](#using-the-mcp-tool-inside-the-agent-step)
    - [Using the MCP tool inside the Tool step](#using-the-mcp-tool-inside-the-tool-step)
  + [Managing MCP servers](#managing-mcp-servers)