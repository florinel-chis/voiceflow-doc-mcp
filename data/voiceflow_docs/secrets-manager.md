---
category: general
scraped_at: '2025-11-12T14:08:01.586190'
title: Secrets
url: /docs/secrets-manager
---

# Secrets

The Secrets Manager enables you to securely store and manage a variety of sensitive information within your conversational AI agents. Think of secrets like passwords for your code and infrastructure—anything used to access essential services and functions within your software. This includes API keys, database credentials, encryption keys, and more. This guide provides step-by-step instructions on how to access, create, manage, and utilize secrets, as well as how to handle environment-specific overrides.

![](https://files.readme.io/c936b02bab930747aa0dfa8e76f6c5003627695cc26215c5fd90ab94b6ca18a3-CleanShot_2024-10-02_at_21.30.542x.png)
  

---

## 1. Accessing the Secrets Manager

To begin managing your secrets:

1. **Navigate to Agent Settings**:

   * In the left sidebar, click on **Agent Settings**.
2. **Open the Secrets Tab**:

   * Select the **Secrets** tab to access the Secrets Manager interface.

---

## 2. Creating a New Secret

To add a new secret:

1. **Click "New Secret"**:

   * In the top-right corner of the Secrets Manager, click **New Secret**.

     ![](https://files.readme.io/991cae7cdb4b8bbab9caea01ac5ba24b7d1827cde581555e24cbeee9a35c69cf-CleanShot_2024-10-02_at_21.34.392x.png)
2. **Enter Secret Details**:

   * A modal window will appear prompting you to enter:
     + **Name**: A descriptive label for your secret (e.g., `Database_Password`).
     + **Value**: The sensitive data you wish to store.
     + **Visibility**:
       - **Masked**: The value is hidden but can be temporarily revealed.
       - **Restricted**: The value remains hidden and cannot be revealed after creation.
3. **Save the Secret**:

   * Click **Create Secret** to add the secret to your Secrets Manager.

---

## 3. Managing Secrets

### Viewing and Revealing Secrets

* **Masked Secrets**:

  + Hover over the value in the **Value** column.
  + Click to temporarily reveal the secret value.
* **Restricted Secrets**:

  + The value is permanently hidden and displayed as a series of dots or dashes.
  + The value cannot be revealed after creation.

### Editing and Deleting Secrets

* **Access Secret Options**:

  + Click the **three dots** (**⋮**) next to the secret you wish to manage.
* **Available Actions**:

  + **Edit**: Update the secret's value or visibility settings.
  + **Copy**: Copy the secret's value to your clipboard (only available for **Masked** secrets).
  + **Delete**: Permanently remove the secret from the Secrets Manager.

---

## 4. Environment Overrides

Environment overrides allow you to specify different secret values for different deployment stages.

![](https://files.readme.io/1897820d66e97c93e4dca0e137813858f21f4b55ca33ad3abf7c74ba4d4bd402-CleanShot_2024-10-02_at_21.36.392x.png)
  

### Accessing Environment Settings

1. **Navigate to Environments Tab**:

   * Within **Agent Settings**, select the **Environments** tab.
2. **Available Environments**:

   * **Development**:
     + Used when building and testing your agent on the canvas.
   * **Production**:
     + Used when your agent is published and live.

### Overriding Secrets for Environments

1. **Override Secrets**:

   * Click **Override Secrets** next to the environment you wish to configure.
2. **Set Environment-Specific Values**:

   * A modal will display all existing secrets.
   * Enter the new value for each secret you wish to override in this environment.
3. **Save Overrides**:

   * Click **Save** to apply the overrides.

### Notes

* **Default Values**:

  + If a secret does not have an environment-specific override, it will use the default value from the Secrets Manager.
* **Isolation**:

  + Overrides ensure that sensitive data appropriate for each environment is used, enhancing security and operational integrity.

---

## 5. Using Secrets in Function and API Steps

Secrets can be utilized within your agent's logic to keep sensitive data out of your code.

![](https://files.readme.io/cc76477a393df6c5df278c83d80e723b5f5e4ca5e2ce86546a2a3b30f4a86eec-CleanShot_2024-10-02_at_21.37.292x.png)
  

### Inserting Secrets into Steps

1. **Open Variable Selector**:

   * In any input field within a **Function** or **API** step, type an opening curly brace `{`.
2. **Select Secrets**:

   * A dropdown menu will appear.
   * Toggle to the **Secrets** tab at the top of the dropdown.
3. **Choose a Secret**:

   * Select the desired secret from the list to insert it into your code.

### Creating Secrets from the Canvas

* **Quick Creation**:
  + If you need to create a new secret while working on the canvas, click **Create Secret** at the bottom of the dropdown.
  + Fill in the secret details as described in [Creating a New Secret](#2-creating-a-new-secret).

---

## 6. Duplicating or Exporting Projects with Secrets

### Security Measures

* **Exclusion of Secret Values**:
  + When duplicating or exporting a project, only the secret names are retained.
  + Secret **values are not included** to protect sensitive information.

### Post-Duplication Actions

* **Re-Adding Secret Values**:
  + After importing or duplicating a project, navigate to the Secrets Manager.
  + Re-enter the secret values as needed for the new project instance.

---

## 7. Security and Encryption Details

Voiceflow prioritizes the security of your sensitive data.

### Encryption Standards

* **Algorithm Used**:
  + Secrets are encrypted using **AES-256 GCM (Galois/Counter Mode)**.

### Benefits of AES-256 GCM

* **Confidentiality**:

  + Ensures that secret values are obscured and cannot be read without proper decryption.
* **Integrity**:

  + Includes a **Message Authentication Code (MAC)** to detect any tampering with the encrypted data.

### Security Best Practices

* **Key Protection**:

  + Encryption keys are securely managed to prevent unauthorized access.
* **Data Handling**:

  + Secrets are stored and transmitted according to industry best practices to maintain confidentiality and integrity.

---

## 8. Best Practices

* **Use Restricted Visibility for Highly Sensitive Data**:

  + For secrets that should never be exposed, choose **Restricted** visibility.
* **Regularly Update Secrets**:

  + Periodically change secret values to enhance security.
* **Leverage Environment Overrides**:

  + Use overrides to separate development and production credentials.
* **Avoid Hardcoding Sensitive Data**:

  + Always use the Secrets Manager instead of hardcoding sensitive information in your agent logic.
* **Secure Sharing and Collaboration**:

  + Be mindful when sharing projects; recipients will need to provide their own secret values.

Updated 5 months ago

---

[Supporting listen in functions](/docs/functions-listen)[Native tools](/docs/tools-1)

Ask AI

* [Table of Contents](#)
* + [1. Accessing the Secrets Manager](#1-accessing-the-secrets-manager)
  + [2. Creating a New Secret](#2-creating-a-new-secret)
  + [3. Managing Secrets](#3-managing-secrets)
  + - [Viewing and Revealing Secrets](#viewing-and-revealing-secrets)
    - [Editing and Deleting Secrets](#editing-and-deleting-secrets)
  + [4. Environment Overrides](#4-environment-overrides)
  + - [Accessing Environment Settings](#accessing-environment-settings)
    - [Overriding Secrets for Environments](#overriding-secrets-for-environments)
    - [Notes](#notes)
  + [5. Using Secrets in Function and API Steps](#5-using-secrets-in-function-and-api-steps)
  + - [Inserting Secrets into Steps](#inserting-secrets-into-steps)
    - [Creating Secrets from the Canvas](#creating-secrets-from-the-canvas)
  + [6. Duplicating or Exporting Projects with Secrets](#6-duplicating-or-exporting-projects-with-secrets)
  + - [Security Measures](#security-measures)
    - [Post-Duplication Actions](#post-duplication-actions)
  + [7. Security and Encryption Details](#7-security-and-encryption-details)
  + - [Encryption Standards](#encryption-standards)
    - [Benefits of AES-256 GCM](#benefits-of-aes-256-gcm)
    - [Security Best Practices](#security-best-practices)
  + [8. Best Practices](#8-best-practices)