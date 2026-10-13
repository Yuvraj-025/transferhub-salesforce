# TransferHub — Salesforce Football Transfer Management

TransferHub is an educational football recruitment and transfer management project implemented in Salesforce Starter Edition. It connects clubs, player profiles, scouting assessments, transfer negotiations, and club budgets through native Salesforce records, Flow automation, reports, and a dashboard.

The project adapts a supplied TransferHub build kit to the capabilities of the available Starter org. All records are fictional and all TransferHub monetary values are in GBP.

## Implemented features

- 64 custom fields and dedicated TransferHub sections on 4 standard record layouts.
- 6 saved list views for clubs, players, available players, and transfer deal status.
- 4 active Flows for budget recalculation and negotiation follow-ups.
- Scoped validation rules and a TransferHub Starter permission set.
- 4 custom report types, 12 reports, and a dashboard with 13 widgets.
- 65 fictional records: 10 clubs, 20 players, 15 deals, and 20 scout assessments.

## Data model

| Salesforce object | TransferHub role | Relationships |
|---|---|---|
| Account | Club | Owns player Contacts; buying or selling club on a deal |
| Contact | Player | Current club through AccountId |
| Opportunity | Transfer deal | Buyer through AccountId; custom lookups to seller and player |
| Task / Activity | Scout assessment | Player through WhoId; negotiation follow-ups through WhatId |

## Automation

| Flow | Purpose |
|---|---|
| TH_Recalculate_Club_Budget | Sums final fees from fictional completed deals for a club |
| TH_Budget_On_Save | Recalculates budgets after deal creation or changes; repairs the former buyer after a buyer change |
| TH_Budget_On_Delete | Recalculates before deletion while excluding the deleted deal |
| TH_Starter_Negotiation_Followup | Creates one follow-up task due in two days when an active deal enters negotiation |

Completed spending uses final transfer fees and excludes agent fees. Reopening a completed deal removes its fee from spending. Follow-up tasks are deduplicated by deal and subject.

## Verified results

Verified in the implemented org on 13 October 2026:

| Metric | Result |
|---|---:|
| Players | 20 |
| Transfer-listed players | 4 |
| Active deals | 8 |
| Completed transfers | 4 |
| Active proposed fees | GBP 21,000,000 |
| Completed transfer spending | GBP 21,800,000 |
| Recommended scout assessments | 10 |
| Lifecycle checks passed | 15 |

All 13 dashboard components returned DATA without errors. See [verification evidence](evidence/) and the [faculty demonstration guide](docs/FACULTY-DEMO.md).

## Repository contents

```text
force-app/main/default/   Salesforce source metadata
data/                    Original fictional CSVs and mapped import fixtures
docs/                    Deployment notes and faculty demo guide
evidence/                Verification results without account identifiers
scripts/                 Target-specific deployment preparation
sfdx-project.json        Salesforce DX project configuration
field-mapping.json       Original kit to Starter field mapping
```

## Setup

Install the official Salesforce CLI, authenticate to your own org, then follow [deployment notes](docs/DEPLOYMENT.md). This repository has no login credentials. Dashboard and folder metadata use `REPLACE_WITH_SALESFORCE_USERNAME`; the preparation script writes a deployment copy for your target username.

Metadata deployment alone does not load data, assign the permission set, or guarantee Flow activation. Review existing standard layouts before deploying them into another org.

## Starter Edition adaptations

The implemented Starter org rejected custom object and custom app creation. Standard objects and native Flows replace the kit's custom objects, standalone app, Apex budget trigger, and LWC marketplace. This repository contains the implemented Starter adaptation; it does not claim those original components were deployed.

The existing org uses INR. TransferHub fees and budgets use explicit GBP number fields, while standard Opportunity Amount is unused for the imported deals. Full scout narratives are stored in Task Description because the supported custom scout note fields are limited to 255 characters. Administrator corrections are allowed on closed deals.

Budget Flows do not provide Apex parent locking guarantees for simultaneous updates. Undeleting a deal requires budget reconciliation with TH_Recalculate_Club_Budget. Validation and automation are scoped to Fictional Demo Record; scout validation also requires Report External ID.

## Attribution

Adapted from the supplied TransferHub Complete Build Kit. The Starter implementation and verification were prepared with AI assistance. No additional open-source license is asserted for third-party material from the supplied kit.

