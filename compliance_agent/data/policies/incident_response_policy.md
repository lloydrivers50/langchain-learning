# Incident Response Policy

**Policy ID:** IRP-001
**Effective Date:** 1 January 2025
**Review Date:** 1 January 2026
**Owner:** Head of Information Security

## Purpose

This policy defines the process for identifying, responding to, and recovering from information security incidents.

## Scope

Applies to all security incidents affecting company systems, data, or personnel, whether caused by internal or external actors.

## Definitions

- **Security Incident:** Any event that compromises the confidentiality, integrity, or availability of company information or systems.
- **Severity 1 (Critical):** Active data breach, ransomware, or complete system outage affecting customers.
- **Severity 2 (High):** Unauthorised access detected, malware infection contained to single system, partial service degradation.
- **Severity 3 (Medium):** Phishing attempt reported, policy violation detected, vulnerability identified in production.
- **Severity 4 (Low):** Failed login attempts, minor policy deviation, informational security alerts.

## Policy

### 1. Detection and Reporting

All employees must report suspected security incidents to the Security Operations team immediately. Reports can be made via email to security@company.com, the #security-incidents Slack channel, or by phone to the 24/7 security hotline. Automated monitoring systems must alert the on-call security engineer within 5 minutes of detection.

### 2. Triage and Classification

The on-call security engineer must classify the incident severity within 15 minutes of receiving the report. Severity 1 and 2 incidents must trigger the Incident Response Team callout. The Incident Commander must be assigned within 30 minutes for Severity 1 incidents.

### 3. Containment

Immediate containment actions must be taken to prevent further damage. For Severity 1: affected systems may be isolated from the network without prior management approval. For Severity 2-4: containment actions must be proportionate and documented. All containment actions must be logged with timestamps in the incident ticket.

### 4. Investigation

A root cause analysis must be conducted for all Severity 1 and 2 incidents. Evidence must be preserved in accordance with forensic best practices. External forensic investigators must be engaged for Severity 1 incidents involving customer data.

### 5. Recovery

Recovery procedures must be documented and tested before implementation. Systems must be verified as clean before being returned to production. Recovery must be signed off by the Incident Commander and the system owner.

### 6. Post-Incident Review

A post-incident review must be held within 5 business days of incident closure. The review must produce a written report including timeline, root cause, impact assessment, and remediation actions. Lessons learned must be shared with relevant teams and incorporated into security training.

### 7. Communication

Severity 1 incidents require notification to the CEO and Board within 2 hours. Customer-facing communications must be approved by Legal and Communications before release. Regulatory notifications must be made in accordance with the Data Protection Policy.

## Testing

The incident response plan must be tested through tabletop exercises at least twice per year. A full simulation exercise must be conducted annually. Test results must be documented and used to improve the response plan.
