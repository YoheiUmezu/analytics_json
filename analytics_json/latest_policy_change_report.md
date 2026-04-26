# Manus Analytics Report

## Overview
- Tenant: demo_corp
- Generated At: 2026-04-26T18:14:01.102510
- Scenario: policy_change (制度変更周知)
- Users: 3000
- Contents: 30
- Period Days: 7

## KPI Comparison (Before / After)
- Views: 21988 / 23871
- Completion Rate: 66.19% / 65.63%
- Engagement Rate: 58.63% / 58.28%
- Zero Result Rate: 19.73% / 9.54%

## Delta
- Views Delta: 1883
- Completion Rate Delta: -0.56%
- Engagement Rate Delta: -0.35%
- Zero Result Rate Delta: -10.19%

## Before JSON (Sample)
```json
{
  "meta": {
    "generated_at": "2026-04-26T18:14:00.636206",
    "tenant_id": "demo_corp",
    "phase": "before",
    "scenario": "policy_change",
    "scenario_label": "制度変更周知",
    "period_days": 7,
    "num_users": 3000,
    "num_contents": 30,
    "target_events": 50000
  },
  "aggregates": {
    "views": 21988,
    "completion_rate": 0.661861015099145,
    "engagement_rate": 0.5863198108058941,
    "zero_result_rate": 0.19731800766283525
  }
}
```

## After JSON (Sample)
```json
{
  "meta": {
    "generated_at": "2026-04-26T18:14:01.062616",
    "tenant_id": "demo_corp",
    "phase": "after",
    "scenario": "policy_change",
    "scenario_label": "制度変更周知",
    "period_days": 7,
    "num_users": 3000,
    "num_contents": 30,
    "target_events": 50000
  },
  "aggregates": {
    "views": 23871,
    "completion_rate": 0.6562774915169034,
    "engagement_rate": 0.5827992124334967,
    "zero_result_rate": 0.0953757225433526
  }
}
```
