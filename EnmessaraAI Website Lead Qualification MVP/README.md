# Enmessara Website Lead Qualification Automation

Public sample workflow showing how a website form can trigger lead qualification, call follow-up, CRM-style logging, and internal notification routing.

## What It Demonstrates

- Website form submission into an n8n webhook
- Form normalization and phone-number validation
- Conditional routing for invalid leads versus callable leads
- Outbound call handoff to a voice AI provider
- Callback webhook processing for call analysis
- Google Sheets-style lead logging
- Gmail-style internal follow-up notification

## Files

- `workflows/enmessara-request-time.sample.json` - sanitized primary workflow sample
- `workflows/form-response-book-a-meeting.sample.json` - sanitized alternate/imported version
- `docs/IMPLEMENTATION_SUMMARY.md` - implementation overview
- `docs/QUICK_START.md` - setup and testing notes
- `docs/TEST_CHECKLIST.md` - QA checklist
- `docs/FIX_REPORT_EXEC_938.md` - example production debugging note

## Public Safety Notes

This sample intentionally uses placeholders for webhook hosts, API keys, credential IDs, phone numbers, account emails, and Google resource IDs. Replace values like `{{N8N_BASE_URL}}`, `{{RETELL_API_KEY}}`, and `{{GOOGLE_SHEET_ID}}` with your own environment-specific values before importing or running.
