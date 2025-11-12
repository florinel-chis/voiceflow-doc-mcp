---
category: general
scraped_at: '2025-11-12T14:09:33.713913'
title: Single Sign-On (SSO) and SAML
url: /docs/sso
---

# Single Sign-On (SSO) and SAML

> 🏢
>
> ### This feature is only available to Enterprise customers.

This document serves as a comprehensive overview on how to configure your Single Sign-On (SSO) and SAML authentication on Voiceflow, and manage your member access.

With Voiceflow's SAML authentication support, **Enterprise** customers are able to manage access to their organization's workspace. All access will be provisioned using your chosen identity management provider, and that will be used to dictate who can Sign Up and Sign In to Voiceflow.

![](https://files.readme.io/d3aeab1-image.png)

All features, configurations, and SAML/SSO and other non-Google custom sign-in options found on this document are unavailable on **non-Enterprise plans**.

## Getting Started

Voiceflow supports SAML 2.0 authentication through either an SP or IdP initiated flow.

* SP is Service Provider (i.e., Voiceflow)
* IdP is Identity Provider (i.e., Okta or a custom SAML implementation)

Here are the overall steps required to configure your SAML instance:

1. Once SAML has been enabled for your organization (see next section, if not done), you will find the configuration menu (see above screenshot) under Workspace Settings on your workspace.
2. On your identity provider, you will need to input the Audience URI and ACS/Callback URL links listed in the Authentications settings.
3. From your identify provider setup, copy and paste the Entity ID URL and IdP SSO Target URL.
4. From your identity provider, copy and paste the X.509 certificate content into the field provided.
5. Once your configuration is saved and validated, SAML SSO is now enabled. Through your Identity provider dashboard, you can now log in to Voiceflow.

## Enabling SAML on Voiceflow:

Ensure you are on a [Voiceflow Enterprise plan](https://www.voiceflow.com/enterprise). Contact your **Voiceflow Customer Success Manager** to flag all relevant workspaces as part of an organization, and ensure anyone configuring SAML/SSO settings is an [admin of the workspace](https://developer.voiceflow.com/v2.0/docs/managing-workspaces-teams).

![](https://files.readme.io/8d31288-image.png)

Once everything is filled out and saved, an IdP-initiated login flow should be possible for the admin.

* To **retroactively add existing Voiceflow accounts** to SAML, contact your Voiceflow Customer Success manager.
* **For an SP-initiated login flow**, contact your Voiceflow Customer Success manager to flag a specific email domain name. This is done for verification and security purposes.

Whenever a login is detected with the email domain, the user will be prompted to Log In via SSO.

![](https://files.readme.io/41b1174-image.png)

**Implementation Details**

*Voiceflow provides:*

* Audience URI (SP Entity ID)
* Assertion Consumer Service URL / Callback URL — The endpoint where the IdP will redirect with its authentication response + Email Identifier

*Voiceflow requires:*

* Entity ID URL
* IdP SSO Target URL — The URL users of your organization will be directed to on login via an SP initiated flow (optional)
* X.509 certificate

\**On the IdP side, you will need to send the Email identifier* (`urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`) to uniquely identify SSO users.

## Domain Whitelisting

Once the initial setup is complete, domains can be whitelisted. This will ensure that users with email addresses containing these domains will be directed to your SAML authentication.

1. Provide your Voiceflow Customer Success Rep with a list of domains that will be whitelisted for your SAML auth. *Note: You may configure more than one domain if your organization requires it — ex. voiceflow.com and getvoiceflow.com*
2. We can enable SAML authentication, and once enabled, all users on your domains will only be able to access Voiceflow using your SSO

## Microsoft Azure mappings

Attribute and Claims → leave default

| Voiceflow | Azure | Data Direction | Example |
| --- | --- | --- | --- |
| Audience URI (SP Entity ID) | Identifier (EntityID) | VF → Azure | <https://voiceflow.com> |
| ACS/Callback URL | Reply URL (Assertion Customer Service URL) | VF → Azure | <https://api.>`<something>`.voiceflow.com/ |
| Entity ID URL | Azure ID Identifier | Azure → VF | [https://sts.windows.net/……](https://sts.windows.net/%E2%80%A6%E2%80%A6) |
| IdP SSO Target URL | Login URL | Azure → VF | [https://login.microsoftonline.com/……](https://login.microsoftonline.com/%E2%80%A6%E2%80%A6) |
| X.509 Certificate | Certificate (Base64) | Azure → VF | —Begin Certificate —— …… |

## Common SAML/SSO Questions

1. *Is this an SP or IdP initiated flow? If SP initiated, what is the SP login URL?*
   1. Voiceflow supports SAML 2.0 authentication through either an SP or IdP initiated flow. SP is Service Provider, i.e., Voiceflow, and IdP is Identity Provider, i.e., Okta or a custom SAML implementation.
2. *What is the application username format (e.g., email address or user ID)?*
   1. It is the customers' (your) email address domain.
3. *What additional attributes need to be included in the SAML assertion*?
   1. Entity ID URL
   2. IdP SSO Target URL — The URL users of your organization will be directed to on login via an SP initiated flow (optional)
   3. X.509 certificate
4. *How are group/role membership mapped? Is it 1 user –to –1 group, or 1 user –to –many groups?*
   1. Voiceflow SSO only uses SSO for authentication purposes — not authorization. Therefore, no mapping is done.
5. *Can the application reference IdP metadata URL? If not, can it reference an XML file?*
   1. Yes. Voiceflow provides:
      1. Audience URI (SP Entity ID)
      2. Assertion Consumer Service URL / Callback URL — The endpoint where the IdP will redirect with its authentication response + Email Identifier urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress
      3. **Please note**: Voiceflow expects:  
         `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`
      4. SAML name identifier from your identity provider as a part of the SAML authentication response in order to uniquely identify SSO users on our platform. Authorization is handled internally within the Voiceflow platform based on assigned user roles.
6. *Can the application store multiple IdP SAML certificates at once?*
   1. Yes, with multiple domains.
7. *How are users created, updated, and removed in the application?*
   1. The Voiceflow Workspace Owners are the able to perform user management on the organization's users
8. *Is Basic Auth currently available? Once SSO is in enabled, will Basic Auth be disabled?*
   1. It is recommended Basic Auth be disabled once SSO is enabled. Basic Auth is disabled when SSO is enabled.
9. *Is there an admin back door, in case SSO is down?*
   1. Voiceflow administrators can access without SSO
10. *Is there SSO integration documentation for the application?*
    1. Yes, found [here](https://www.notion.so/voiceflow/Voiceflow-SAML-SSO-Flow-ae64d6fd0f4944b692935c1c386f1880).

Updated 5 months ago

---

[Roles and permissions](/docs/roles-permissions)[Billing](/docs/billing-plans)

Ask AI

* [Table of Contents](#)
* + [Getting Started](#getting-started)
  + [Enabling SAML on Voiceflow:](#enabling-saml-on-voiceflow)
  + [Domain Whitelisting](#domain-whitelisting)
  + [Microsoft Azure mappings](#microsoft-azure-mappings)
  + [Common SAML/SSO Questions](#common-samlsso-questions)