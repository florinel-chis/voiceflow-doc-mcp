---
category: general
scraped_at: '2025-11-12T14:09:31.596224'
title: Roles and permissions
url: /docs/roles-permissions
---

# Roles and permissions

Manage the level of access users have to your workspace.

Voiceflow supports different permission levels based on what your team members need to do. Roles are defined at the organization, workspace, and project levels.

## Roles

### Owner

Owners have full control over their workspace. Owners on Enterprise plan have full control over all workspaces owned by an organization. Owners can:

Pro and Team PlansEnterprise Plan

* Modify workspace settings
* Invite or remove members from the workspace
* Manage permissions for users in the workspace
* Change billing and subscription settings
* Edit and publish all projects in the workspace

> ℹ️
>
> The person who creates a workspace is automatically made its Owner. Owners also count as Workspace Editors.

  

### Admin

Admins have full control within a specific workspace. Admins can:

* Modify workspace settings
* Invite or remove members from the workspace
* Manage permissions within the workspace
* Edit and publish all projects in the workspace
* Update billing and subscription details for that workspace

  

### Editor

Editors build and manage assistants inside the workspace. Editors can:

* Edit and publish all projects in the workspace
* Manage project settings
* Import and export projects

> ℹ️
>
> Editors cannot invite new members.

  

### Viewer

Viewers can see the contents of project but cannot make edits. Viewers can:

* View all projects in a workspace
* Leave comments on projects in a workspace

  

### Billing

The Billing role is workspace-specific and focused on account management. Billing users can:

* View all projects in a workspace
* Leave comments on projects in a workspace
* Manage billing and subscription settings
* Invite or remove members

  

## Assistant Level Permissions

You can give **view-only roles** (Viewer or Billing) edit access to specific projects. This is useful when you want limited collaboration without upgrading their entire workspace role.

Some important things to note:

* Project-level permissions only apply to Viewers or Billing roles.
* Owners, Admins, and Editors already have full edit access across all projects. They cannot be restricted to Viewers on single projects.
* If a Viewer is given project-level edit access, they count as an Editor for billing purposes.

Updated 5 months ago

---

[Managing workspaces and team members](/docs/managing-workspaces-teams)[Single Sign-On (SSO) and SAML](/docs/sso)

Ask AI

* [Table of Contents](#)
* + [Roles](#roles)
  + - [Owner](#owner)
    - [Admin](#admin)
    - [Editor](#editor)
    - [Viewer](#viewer)
    - [Billing](#billing)
  + [Assistant Level Permissions](#assistant-level-permissions)