# Data Storage Policy

**Policy ID:** DSP-001
**Effective Date:** 1 January 2025
**Review Date:** 1 January 2026
**Owner:** Chief Information Security Officer

## Purpose

This policy defines the requirements for storing company and customer data across all systems, whether on-premises or cloud-hosted.

## Scope

Applies to all employees, contractors, and third-party vendors who handle company data.

## Policy

### 1. Encryption

All data must be encrypted at rest using AES-256 or equivalent. Encryption keys must be stored separately from the data they protect, using a dedicated key management service. Keys must be rotated every 90 days.

### 2. Access Control

Access to stored data requires multi-factor authentication (MFA). Access is granted on a least-privilege basis and must be approved by the data owner. All access must be logged and logs retained for 12 months.

### 3. Backups

Full backups must be performed weekly. Incremental backups must be performed daily. Backups must be stored in a geographically separate location from the primary data. Backup restoration must be tested quarterly.

### 4. Data Retention

Customer data must be retained for 7 years from the date of last activity. After the retention period, data must be securely deleted using NIST 800-88 compliant methods. Deletion must be logged and certified by the data owner.

### 5. Cloud Storage

Only approved cloud providers may be used (currently: AWS, Azure, GCP). Data classified as "Restricted" must not be stored in public cloud without explicit CISO approval. All cloud storage must have versioning enabled.

## Violations

Violations of this policy may result in disciplinary action up to and including termination. Violations must be reported to the Information Security team within 24 hours of discovery.
