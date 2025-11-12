---
category: general
scraped_at: '2025-11-12T14:11:11.277682'
title: Scheduled Tests
url: /docs/scheduled-tests
---

# Scheduled Tests

![](https://files.readme.io/8443f5a743553dd78efb4e12d580293836d3d74e679e7f481875790b90db9ffc-scheduled-tests.png)
  

## Overview

Scheduled Tests enable automated, recurring execution of your Test Suites at predefined times. This feature ensures continuous monitoring of your Voiceflow agents without manual intervention.

## What are Scheduled Tests?

Scheduled Tests are automated test executions that:

* **Run Automatically**: Execute without user interaction at specified times
* **Follow Schedules**: Run once or repeatedly based on your configuration
* **Monitor Continuously**: Provide ongoing validation of your agents
* **Send Notifications**: Alert you of results via email (when configured)

## Creating Scheduled Tests

![](https://files.readme.io/50c0f410ce10b220b1f35957b4e52aeed5ad338be8b2d57e844d593397f39fae-scheduled-test-detail.png)
  

### Basic Setup

1. Navigate to **Scheduled Tests** in the sidebar
2. Click **"Create New Scheduled Test"**
3. Configure the following:
   * **Test Suite**: Select which test suite to run
   * **Schedule Date & Time**: Choose when to execute
   * **Enable/Disable**: Toggle to activate or deactivate the schedule

### Schedule Configuration

#### One-time Execution

* Select a specific date and time
* Test runs once at the scheduled time
* Automatically disabled after execution

#### Recurring Execution

* **Daily**: Repeat every day at the specified time
* **Custom**: Use cron expressions for complex schedules
* Examples:
  + `0 9 * * 1-5`: Every weekday at 9:00 AM
  + `0 */6 * * *`: Every 6 hours
  + `0 0 1 * *`: First day of every month at midnight

### Advanced Options

* **Description**: Add notes about the scheduled test purpose
* **Enable/Disable**: Control whether the schedule is active
* **Email Notifications**: Receive results via email (requires configuration in Settings)

### Email Notifications

Configure in Settings to receive **Failure Alerts** which are immediate notifications of test failures

Updated 4 months ago

---

[Test Suites](/docs/test-suites)[Test Execution](/docs/test-execution)

Ask AI

* [Table of Contents](#)
* + [Overview](#overview)
  + [What are Scheduled Tests?](#what-are-scheduled-tests)
  + [Creating Scheduled Tests](#creating-scheduled-tests)
  + - [Basic Setup](#basic-setup)
    - [Schedule Configuration](#schedule-configuration)
    - [Advanced Options](#advanced-options)
    - [Email Notifications](#email-notifications)