# Manus Analytics Report

## Overview
- Tenant: demo_corp
- Generated At: 2026-04-26T18:14:30.254037
- Scenario: new_joiners (新入社員期)
- Users: 3000
- Contents: 30
- Period Days: 7

## KPI Comparison (Before / After)
- Views: 19013 / 22554
- Completion Rate: 65.22% / 65.23%
- Engagement Rate: 57.10% / 56.93%
- Zero Result Rate: 24.17% / 9.50%

## Delta
- Views Delta: 3541
- Completion Rate Delta: 0.01%
- Engagement Rate Delta: -0.17%
- Zero Result Rate Delta: -14.67%

## Before JSON (Sample)
```json
{
  "meta": {
    "generated_at": "2026-04-26T18:14:29.815609",
    "tenant_id": "demo_corp",
    "phase": "before",
    "scenario": "new_joiners",
    "scenario_label": "新入社員期",
    "period_days": 7,
    "num_users": 3000,
    "num_contents": 30,
    "target_events": 50000
  },
  "aggregates": {
    "views": 19013,
    "completion_rate": 0.6521853468679325,
    "engagement_rate": 0.570977752064377,
    "zero_result_rate": 0.24168297455968688
  }
}
```

## After JSON (Sample)
```json
{
  "meta": {
    "generated_at": "2026-04-26T18:14:30.215835",
    "tenant_id": "demo_corp",
    "phase": "after",
    "scenario": "new_joiners",
    "scenario_label": "新入社員期",
    "period_days": 7,
    "num_users": 3000,
    "num_contents": 30,
    "target_events": 50000
  },
  "aggregates": {
    "views": 22554,
    "completion_rate": 0.6522568058880908,
    "engagement_rate": 0.5692560078034938,
    "zero_result_rate": 0.09500959692898273
  }
}
```
