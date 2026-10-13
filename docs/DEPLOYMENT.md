# Deployment notes

This is a Salesforce DX metadata project containing the implemented Starter adaptation. The source is a snapshot, not a universal one-click installer. Target edition, field limits, Flow entitlements, and existing layouts must be checked in the target org.

## Prepare and validate

Install the Salesforce CLI from its official distribution and authenticate interactively:

```powershell
sf org login web --alias TransferHubTarget
python scripts/prepare_deployment.py --username YOUR_SALESFORCE_USERNAME
sf project deploy validate --source-dir .deploy/force-app --target-org TransferHubTarget --test-level NoTestRun
```

The preparation script substitutes only the dashboard owner, running user, and folder-sharing username in a generated copy. `.deploy` is ignored by Git. Use an existing user in the target org; do not enter a password or access token.

After reviewing validation and backing up the target layouts:

```powershell
sf project deploy start --source-dir .deploy/force-app --target-org TransferHubTarget --test-level NoTestRun
sf org assign permset --name TransferHub_Starter --target-org TransferHubTarget
```

If the target does not support validate, use `sf project deploy start --dry-run` for a validation-only operation supported by that org. Review errors before any actual deployment.

## After metadata deployment

1. In Setup, verify TH_Recalculate_Club_Budget is active, then activate the three record-triggered Flows. Salesforce may save deployed Flows as drafts.
2. Import clubs, then players, then deals, then scout Tasks. `data/fixtures.json` contains mapped values; resolve external club/player keys to target record IDs before loading dependent records. The original CSVs retain the kit's custom-object column names and need mapping.
3. Use Account Club External ID, Contact Player External ID, and Opportunity Deal External ID for matching. Scout Task Report External ID is a text field and is not unique; check existing values to avoid duplicate assessments.
4. Assign current clubs through Contact.AccountId, buyers through Opportunity.AccountId, sellers through Selling_Club__c, players through Player__c, and scout subjects through Task.WhoId.
5. Standard Opportunity Name, StageName, and CloseDate remain required. Use valid target stage values; TransferHub Deal Status and Negotiation Stage are independent custom fields. Do not populate standard Amount with GBP while the org uses INR.
6. Select Fictional Demo Record for project records and populate Report External ID for scout Tasks. Store complete scout narratives in Task.Description.
7. Run TH_Recalculate_Club_Budget with each affected ClubId after initial import. Refresh and verify all reports and dashboard widgets.

The existing implementation passed fifteen checks. The files in evidence are results from that implementation; they are not executable Apex unit tests and do not certify a different target org.

