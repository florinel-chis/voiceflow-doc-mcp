---
category: general
scraped_at: '2025-11-12T14:10:27.070929'
title: Export agent information
url: /docs/export
---

# Export agent information

With the `voiceflow-cli` you can export your agent information. This is useful when you want to get the `.vf` file of your project. The `voiceflow-cli` has one command that allows you to export an agent from your terminal:

To export an agent, you need to know the `agent-id` and the `version-id` of the agent you want to export from. You can find that information in the Voiceflow Agent section under your Agent Settings on [voiceflow.com](https://voiceflow.com).

Shell

```
voiceflow agent export --agent-id <your-agent-id> --version-id <your-version-id> --output-file <path-to-save>
```

Updated 5 months ago

---

[Agent](/docs/agent)[API Server](/docs/api-serve)

Ask AI