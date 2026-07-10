---
type: cyber-threat-briefing
date: 2026-07-10
tags:
  - briefing/cyber
  - cybersecurity
  - cyberinsurance
  - ransomware
sources_checked: 12
new_items: 26
high_signal_items: 6
status: draft
---

# 2026-07-10 — Cyber Threat Briefing

## Executive Summary

- 26 new item(s) ingested.
- 6 high-signal item(s) flagged for review.
- 18 actively exploited vulnerabilities added to CISA KEV in the last 30 days.
- Top pattern: cyberinsurance

## Fast-Moving Patterns

| Pattern | Signal | Confidence |
|---|---:|---|
| cyberinsurance | 6 | High |
| identity | 5 | High |
| vulnerability_exploitation | 4 | Medium |
| ransomware | 2 | Medium |

## High-Signal Items Today

### 1. Schneider Electric PowerChute Serial Shutdown
- **Source:** CISA Alerts
- **Published:** Thu, 09 Jul 26 12:00:00 +0000
- **URL:** https://www.cisa.gov/news-events/ics-advisories/icsa-26-190-02
- **Score:** 60
- **Mapped pattern:** vulnerability_exploitation, identity
- **Potential mitigations:** identity_hardening: Phishing-resistant MFA, Conditional access, Privileged access management

### 2. OpenPLC v3
- **Source:** CISA Alerts
- **Published:** Thu, 09 Jul 26 12:00:00 +0000
- **URL:** https://www.cisa.gov/news-events/ics-advisories/icsa-26-190-01
- **Score:** 60
- **Mapped pattern:** vulnerability_exploitation, identity
- **Potential mitigations:** identity_hardening: Phishing-resistant MFA, Conditional access, Privileged access management

### 3. Schneider Electric Easergy MiCOM Px40 Series
- **Source:** CISA Alerts
- **Published:** Thu, 09 Jul 26 12:00:00 +0000
- **URL:** https://www.cisa.gov/news-events/ics-advisories/icsa-26-190-03
- **Score:** 60
- **Mapped pattern:** vulnerability_exploitation, identity, cyberinsurance
- **Potential mitigations:** identity_hardening: Phishing-resistant MFA, Conditional access, Privileged access management

### 4. New Helix vishing group emerges in SharePoint data theft attacks
- **Source:** BleepingComputer
- **Published:** Thu, 09 Jul 2026 13:08:29 -0400
- **URL:** https://www.bleepingcomputer.com/news/security/new-helix-vishing-group-emerges-in-sharepoint-data-theft-attacks/
- **Score:** 50
- **Mapped pattern:** ransomware, identity
- **Potential mitigations:** identity_hardening: Phishing-resistant MFA, Conditional access, Privileged access management; ransomware_resilience: Immutable backups, EDR/MDR, Segmentation

### 5. New GigaWiper Windows Backdoor Bundles Disk Wiping, Fake Ransomware, and Spyware
- **Source:** The Hacker News
- **Published:** Thu, 09 Jul 2026 23:38:07 +0530
- **URL:** https://thehackernews.com/2026/07/new-gigawiper-windows-backdoor-bundles.html
- **Score:** 40
- **Mapped pattern:** ransomware
- **Potential mitigations:** ransomware_resilience: Immutable backups, EDR/MDR, Segmentation

### 6. Microsoft Reins in RoguePlanet Zero-Day Threat
- **Source:** Dark Reading
- **Published:** Thu, 09 Jul 2026 20:21:19 GMT
- **URL:** https://www.darkreading.com/vulnerabilities-threats/microsoft-rogueplanet-zero-day-threat
- **Score:** 40
- **Mapped pattern:** vulnerability_exploitation

## Actively Exploited Vulnerabilities Added in Last 30 Days

CISA KEV entries are known actively exploited vulnerabilities. This section is shown every briefing even when no items were newly ingested today.

| CVE | Vulnerability | Vendor/Product | Date Added | Due Date | Ransomware Use |
|---|---|---|---|---|---|
| [CVE-2026-48282](https://nvd.nist.gov/vuln/detail/CVE-2026-48282) | Adobe ColdFusion Path Traversal Vulnerability | Adobe / ColdFusion | 2026-07-07 | 2026-07-10 | Unknown |
| [CVE-2026-48908](https://nvd.nist.gov/vuln/detail/CVE-2026-48908) | JoomShaper SP Page Builder Unrestricted Upload of File with Dangerous Type Vulnerability | JoomShaper / SP Page Builder | 2026-07-07 | 2026-07-10 | Unknown |
| [CVE-2026-56290](https://nvd.nist.gov/vuln/detail/CVE-2026-56290) | Joomlack Page Builder Improper Access Control Vulnerability | Joomlack / Page Builder | 2026-07-07 | 2026-07-10 | Unknown |
| [CVE-2026-55255](https://nvd.nist.gov/vuln/detail/CVE-2026-55255) | Langflow Authorization Bypass Through User-Controlled Key Vulnerability | Langflow / Langflow | 2026-07-07 | 2026-07-10 | Unknown |
| [CVE-2026-45659](https://nvd.nist.gov/vuln/detail/CVE-2026-45659) | Microsoft SharePoint Server Deserialization of Untrusted Data Vulnerability | Microsoft / SharePoint Server | 2026-07-01 | 2026-07-04 | Unknown |
| [CVE-2026-48558](https://nvd.nist.gov/vuln/detail/CVE-2026-48558) | SimpleHelp Authentication Bypass Vulnerability | SimpleHelp  / SimpleHelp | 2026-06-29 | 2026-07-02 | Unknown |
| [CVE-2026-20230](https://nvd.nist.gov/vuln/detail/CVE-2026-20230) | Cisco Unified Communications Manager Server-Side Request Forgery (SSRF) Vulnerability | Cisco / Unified Communications Manager | 2026-06-25 | 2026-06-28 | Unknown |
| [CVE-2026-12569](https://nvd.nist.gov/vuln/detail/CVE-2026-12569) | PTC Windchill and FlexPLM Improper Input Validation Vulnerability | PTC / Windchill and FlexPLM | 2026-06-25 | 2026-06-28 | Unknown |
| [CVE-2025-67038](https://nvd.nist.gov/vuln/detail/CVE-2025-67038) | Lantronix EDS5000 Code Injection Vulnerability | Lantronix / EDS5000 | 2026-06-23 | 2026-06-26 | Unknown |
| [CVE-2026-34908](https://nvd.nist.gov/vuln/detail/CVE-2026-34908) | Ubiquiti UniFi OS Improper Access Control Vulnerability | Ubiquiti / UniFi OS | 2026-06-23 | 2026-06-26 | Unknown |
| [CVE-2026-34910](https://nvd.nist.gov/vuln/detail/CVE-2026-34910) | Ubiquiti UniFi OS Improper Input Validation Vulnerability | Ubiquiti / UniFi OS | 2026-06-23 | 2026-06-26 | Unknown |
| [CVE-2026-34909](https://nvd.nist.gov/vuln/detail/CVE-2026-34909) | Ubiquiti UniFi OS Path Traversal Vulnerability | Ubiquiti / UniFi OS | 2026-06-23 | 2026-06-26 | Unknown |
| [CVE-2026-20253](https://nvd.nist.gov/vuln/detail/CVE-2026-20253) | Splunk Enterprise Missing Authentication for Critical Function Vulnerability | Splunk / Enterprise | 2026-06-18 | 2026-06-21 | Unknown |
| [CVE-2026-48907](https://nvd.nist.gov/vuln/detail/CVE-2026-48907) | Widget Factory Joomla Content Editor Improper Access Control Vulnerability | Widget Factory / Joomla Content Editor  | 2026-06-16 | 2026-06-19 | Unknown |
| [CVE-2026-20262](https://nvd.nist.gov/vuln/detail/CVE-2026-20262) | Cisco Catalyst SD-WAN Manager Directory or Path Traversal Vulnerability | Cisco / Catalyst SD-WAN Manager | 2026-06-15 | 2026-06-29 | Unknown |
| [CVE-2026-54420](https://nvd.nist.gov/vuln/detail/CVE-2026-54420) | LiteSpeed cPanel Plugin UNIX Symbolic Link (Symlink) Following Vulnerability | LiteSpeed / cPanel Plugin | 2026-06-15 | 2026-06-18 | Unknown |
| [CVE-2026-35273](https://nvd.nist.gov/vuln/detail/CVE-2026-35273) | Oracle PeopleSoft Enterprise PeopleTools Missing Authentication for Critical Function Vulnerability | Oracle /  PeopleSoft Enterprise PeopleTools | 2026-06-12 | 2026-06-15 | Known |
| [CVE-2026-10520](https://nvd.nist.gov/vuln/detail/CVE-2026-10520) | Ivanti Sentry OS Command Injection Vulnerability | Ivanti / Sentry | 2026-06-11 | 2026-06-14 | Unknown |

## Solution Alignment

| Threat Pattern | Control Category | Candidate Solution Type | Why Now? |
|---|---|---|---|
| vulnerability_exploitation, identity | identity_hardening | Phishing-resistant MFA | Schneider Electric PowerChute Serial Shutdown |
| vulnerability_exploitation, identity | identity_hardening | Conditional access | Schneider Electric PowerChute Serial Shutdown |
| vulnerability_exploitation, identity | identity_hardening | Privileged access management | Schneider Electric PowerChute Serial Shutdown |
| vulnerability_exploitation, identity | identity_hardening | Phishing-resistant MFA | OpenPLC v3 |
| vulnerability_exploitation, identity | identity_hardening | Conditional access | OpenPLC v3 |
| vulnerability_exploitation, identity | identity_hardening | Privileged access management | OpenPLC v3 |
| vulnerability_exploitation, identity, cyberinsurance | identity_hardening | Phishing-resistant MFA | Schneider Electric Easergy MiCOM Px40 Series |
| vulnerability_exploitation, identity, cyberinsurance | identity_hardening | Conditional access | Schneider Electric Easergy MiCOM Px40 Series |
| vulnerability_exploitation, identity, cyberinsurance | identity_hardening | Privileged access management | Schneider Electric Easergy MiCOM Px40 Series |
| ransomware, identity | identity_hardening | Phishing-resistant MFA | New Helix vishing group emerges in SharePoint data theft attacks |
| ransomware, identity | identity_hardening | Conditional access | New Helix vishing group emerges in SharePoint data theft attacks |
| ransomware, identity | identity_hardening | Privileged access management | New Helix vishing group emerges in SharePoint data theft attacks |
| ransomware, identity | ransomware_resilience | Immutable backups | New Helix vishing group emerges in SharePoint data theft attacks |
| ransomware, identity | ransomware_resilience | EDR/MDR | New Helix vishing group emerges in SharePoint data theft attacks |
| ransomware, identity | ransomware_resilience | Segmentation | New Helix vishing group emerges in SharePoint data theft attacks |
| identity | identity_hardening | Phishing-resistant MFA | New Forg365 phishing platform uses AI to target Microsoft 365 accounts |
| identity | identity_hardening | Conditional access | New Forg365 phishing platform uses AI to target Microsoft 365 accounts |
| identity | identity_hardening | Privileged access management | New Forg365 phishing platform uses AI to target Microsoft 365 accounts |
| ransomware | ransomware_resilience | Immutable backups | New GigaWiper Windows Backdoor Bundles Disk Wiping, Fake Ransomware, and Spyware |
| ransomware | ransomware_resilience | EDR/MDR | New GigaWiper Windows Backdoor Bundles Disk Wiping, Fake Ransomware, and Spyware |

## Source Health

| Source | Status | New Items | Last Error |
|---|---|---:|---|
| CISA Alerts | ok | 3 |  |
| CISA Known Exploited Vulnerabilities | ok | 0 |  |
| SANS Internet Storm Center | ok | 1 |  |
| Tenable News | ok | 0 |  |
| BleepingComputer | ok | 6 |  |
| The Hacker News | ok | 4 |  |
| Dark Reading | ok | 4 |  |
| Cybersecurity Hub News | ok | 0 |  |
| Insurance Day All | ok | 4 |  |
| DTCC Important Notices | ok | 4 |  |
| The Actuary Magazine | ok | 0 |  |
| SEC 8-K Cybersecurity Filings | ok | 0 |  |
