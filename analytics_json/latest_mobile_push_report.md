# Manus Analytics Report

## Overview
- Tenant: demo_corp
- Generated At: 2026-04-26T18:14:15.468724
- Scenario: mobile_push (モバイル強化)
- Users: 3000
- Contents: 30
- Period Days: 7

## KPI Comparison (Before / After)
- Views: 20803 / 25400
- Completion Rate: 65.14% / 65.58%
- Engagement Rate: 64.50% / 64.02%
- Zero Result Rate: 18.47% / 6.74%

## Delta
- Views Delta: 4597
- Completion Rate Delta: 0.44%
- Engagement Rate Delta: -0.48%
- Zero Result Rate Delta: -11.73%

## Before JSON (Sample)
```json
{
  "meta": {
    "generated_at": "2026-04-26T18:14:14.962981",
    "tenant_id": "demo_corp",
    "phase": "before",
    "scenario": "mobile_push",
    "scenario_label": "モバイル強化",
    "period_days": 7,
    "num_users": 3000,
    "num_contents": 30,
    "target_events": 50000
  },
  "aggregates": {
    "views": 20803,
    "completion_rate": 0.651396433206749,
    "engagement_rate": 0.6449550545594386,
    "zero_result_rate": 0.18470149253731344
  }
}
```

## After JSON (Sample)
```json
{
  "meta": {
    "generated_at": "2026-04-26T18:14:15.424630",
    "tenant_id": "demo_corp",
    "phase": "after",
    "scenario": "mobile_push",
    "scenario_label": "モバイル強化",
    "period_days": 7,
    "num_users": 3000,
    "num_contents": 30,
    "target_events": 50000
  },
  "aggregates": {
    "views": 25400,
    "completion_rate": 0.6558267716535433,
    "engagement_rate": 0.6401574803149607,
    "zero_result_rate": 0.06742640075973409
  }
}
```
