---
category: setup
source: claude-code
title: Advanced Setup
url: https://code.claude.com/docs/en/setup
---

##### Administration

- [Advanced installation](/docs/en/setup)
- [Identity and Access Management](/docs/en/iam)
- [Security](/docs/en/security)
- [Data usage](/docs/en/data-usage)
- [Monitoring](/docs/en/monitoring-usage)
- [Costs](/docs/en/costs)
- [Analytics](/docs/en/analytics)
- [Plugin marketplaces](/docs/en/plugin-marketplaces)

On this page

- [System requirements](#system-requirements)
- [Additional dependencies](#additional-dependencies)
- [Standard installation](#standard-installation)
- [Windows setup](#windows-setup)
- [Alternative installation methods](#alternative-installation-methods)
- [Native installation options](#native-installation-options)
- [NPM installation](#npm-installation)
- [Local installation](#local-installation)
- [Running on AWS or GCP](#running-on-aws-or-gcp)
- [Update Claude Code](#update-claude-code)
- [Auto updates](#auto-updates)
- [Update manually](#update-manually)

## [​](#system-requirements) System requirements

- **Operating Systems**: macOS 10.15+, Ubuntu 20.04+/Debian 10+, or Windows 10+ (with WSL 1, WSL 2, or Git for Windows)
- **Hardware**: 4GB+ RAM
- **Software**: [Node.js 18+](https://nodejs.org/en/download) (only required for NPM installation)
- **Network**: Internet connection required for authentication and AI processing
- **Shell**: Works best in Bash, Zsh or Fish
- **Location**: [Anthropic supported countries](https://www.anthropic.com/supported-countries)

### [​](#additional-dependencies) Additional dependencies

- **ripgrep**: Usually included with Claude Code. If search functionality fails, see [search troubleshooting](/docs/en/troubleshooting#search-and-discovery-issues).

## [​](#standard-installation) Standard installation

To install Claude Code, use one of the following methods:

- Native Install (Recommended)
- NPM

**Homebrew (macOS, Linux):**

Copy

Ask AI

```shiki
brew install --cask claude-code
```

**macOS, Linux, WSL:**

Copy

Ask AI

```shiki
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell:**

Copy

Ask AI

```shiki
irm https://claude.ai/install.ps1 | iex
```

**Windows CMD:**

Copy

Ask AI

```shiki
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

Some users may be automatically migrated to an improved installation method.

After the installation process completes, navigate to your project and start Claude Code:

Copy

Ask AI

```shiki
cd your-awesome-project
claude
```

Claude Code offers the following authentication options:

1. **Claude Console**: The default option. Connect through the Claude Console and complete the OAuth process. Requires active billing at [console.anthropic.com](https://console.anthropic.com). A “Claude Code” workspace will be automatically created for usage tracking and cost management. Note that you cannot create API keys for the Claude Code workspace - it is dedicated exclusively for Claude Code usage.
2. **Claude App (with Pro or Max plan)**: Subscribe to Claude’s [Pro or Max plan](https://claude.com/pricing) for a unified subscription that includes both Claude Code and the web interface. Get more value at the same price point while managing your account in one place. Log in with your Claude.ai account. During launch, choose the option that matches your subscription type.
3. **Enterprise platforms**: Configure Claude Code to use [Amazon Bedrock or Google Vertex AI](/docs/en/third-party-integrations) for enterprise deployments with your existing cloud infrastructure.

Claude Code securely stores your credentials. See [Credential Management](/docs/en/iam#credential-management) for details.

## [​](#windows-setup) Windows setup

**Option 1: Claude Code within WSL**

- Both WSL 1 and WSL 2 are supported

**Option 2: Claude Code on native Windows with Git Bash**

- Requires [Git for Windows](https://git-scm.com/downloads/win)
- For portable Git installations, specify the path to your `bash.exe`:

  Copy

  Ask AI

  ```shiki
  $env:CLAUDE_CODE_GIT_BASH_PATH="C:\Program Files\Git\bin\bash.exe"
  ```

## [​](#alternative-installation-methods) Alternative installation methods

Claude Code offers multiple installation methods to suit different environments.
If you encounter any issues during installation, consult the [troubleshooting guide](/docs/en/troubleshooting#linux-permission-issues).

Run `claude doctor` after installation to check your installation type and version.

### [​](#native-installation-options) Native installation options

The native installation is the recommended method and offers several benefits:

- One self-contained executable
- No Node.js dependency
- Improved auto-updater stability

If you have an existing installation of Claude Code, use `claude install` to migrate to the native binary installation.
For advanced installation options with the native installer:
**macOS, Linux, WSL:**

Copy

Ask AI

```shiki
# Install stable version (default)
curl -fsSL https://claude.ai/install.sh | bash

# Install latest version
curl -fsSL https://claude.ai/install.sh | bash -s latest

# Install specific version number
curl -fsSL https://claude.ai/install.sh | bash -s 1.0.58
```

**Alpine Linux and other musl/uClibc-based distributions**: The native build requires you to install `libgcc`, `libstdc++`, and `ripgrep`. Install (Alpine: `apk add libgcc libstdc++ ripgrep`) and set `USE_BUILTIN_RIPGREP=0`.

Claude Code installed via Homebrew will auto-update outside of the brew directory unless explicitly disabled with the `DISABLE_AUTOUPDATER` environment variable (see [Auto updates](#auto-updates) section).

**Windows PowerShell:**

Copy

Ask AI

```shiki
# Install stable version (default)
irm https://claude.ai/install.ps1 | iex

# Install latest version
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) latest

# Install specific version number
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) 1.0.58
```

**Windows CMD:**

Copy

Ask AI

```shiki
REM Install stable version (default)
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd

REM Install latest version
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd latest && del install.cmd

REM Install specific version number
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd 1.0.58 && del install.cmd
```

Make sure that you remove any outdated aliases or symlinks before installing.

### [​](#npm-installation) NPM installation

For environments where NPM is preferred or required:

Copy

Ask AI

```shiki
npm install -g @anthropic-ai/claude-code
```

Do NOT use `sudo npm install -g` as this can lead to permission issues and security risks.
If you encounter permission errors, see [configure Claude Code](/docs/en/troubleshooting#linux-permission-issues) for recommended solutions.

### [​](#local-installation) Local installation

- After global install via npm, use `claude migrate-installer` to move to local
- Avoids autoupdater npm permission issues
- Some users may be automatically migrated to this method

## [​](#running-on-aws-or-gcp) Running on AWS or GCP

By default, Claude Code uses the Claude API.
For details on running Claude Code on AWS or GCP, see [third-party integrations](/docs/en/third-party-integrations).

## [​](#update-claude-code) Update Claude Code

### [​](#auto-updates) Auto updates

Claude Code automatically keeps itself up to date to ensure you have the latest features and security fixes.

- **Update checks**: Performed on startup and periodically while running
- **Update process**: Downloads and installs automatically in the background
- **Notifications**: You’ll see a notification when updates are installed
- **Applying updates**: Updates take effect the next time you start Claude Code

**Disable auto-updates:**
Set the `DISABLE_AUTOUPDATER` environment variable in your shell or [settings.json file](/docs/en/settings):

Copy

Ask AI

```shiki
export DISABLE_AUTOUPDATER=1
```

### [​](#update-manually) Update manually

Copy

Ask AI

```shiki
claude update
```

[Identity and Access Management](/docs/en/iam)

⌘I