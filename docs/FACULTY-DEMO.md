# Faculty demonstration guide

## Project introduction

“TransferHub is a football recruitment and transfer management demonstration built on Salesforce. Clubs, players, transfer deals, and scouting assessments are connected through standard Salesforce objects with custom fields. Native Flows automate budget calculations and negotiation follow-ups. Reports and a dashboard support recruitment and spending analysis. The implementation is adapted to Salesforce Starter Edition.”

## Demonstration sequence

1. Open TransferHub Dashboard from the TransferHub Dashboards folder. Explain 20 players, 8 active deals, 4 completed transfers, and GBP 21.8 million in completed spending.
2. Open Contacts and a player. Show the TransferHub — Fictional Demo section: position, nationality, status, valuation, and contract details.
3. Open Accounts and a club. Explain estimated budget, completed spending, and remaining budget.
4. Open Opportunities and a transfer deal. Show player, buyer, seller, fee, negotiation stage, status, and deadline.
5. Open a linked scouting assessment Task. Explain ratings, recommendations, and the complete narrative in Description.
6. Open a report from TransferHub Reports and explain how its fictional-record filters isolate the project data.
7. Explain the Flow lifecycle checks using evidence/lifecycle-test-results.json.

## Questions and answers

**Why standard objects?** The available Starter org did not permit custom objects or an additional custom application. The model was adapted using Accounts, Contacts, Opportunities, and Tasks.

**How does budget automation work?** A reusable Flow queries completed fictional deals for a club and sums their final fees. Save and delete flows call it; buyer changes also repair the old club's budget.

**What was tested?** Completion, fee corrections, buyer changes, repeated saves, reopening, deletion, follow-up timing and deduplication, validation rejection, and preservation of the original demo totals. Fifteen checks passed.

**What are its limits?** There is no deployed custom LWC marketplace or Apex trigger. Flows do not guarantee parent locking for concurrent updates; restored deals require reconciliation. No real payments or outgoing recruitment messages occur.

**Was AI used?** Yes. The supplied kit was adapted and implemented with AI assistance. Be transparent about that assistance and explain the actual data model and automation demonstrated in the org.

