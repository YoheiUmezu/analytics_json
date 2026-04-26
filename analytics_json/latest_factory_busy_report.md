# Manus Analytics Report

## Overview
- Tenant: demo_corp
- Generated At: 2026-04-26T18:14:07.612754
- Scenario: factory_busy (繁忙期)
- Users: 3000
- Contents: 30
- Period Days: 7

## KPI Comparison (Before / After)
- Views: 18060 / 21137
- Completion Rate: 65.69% / 65.01%
- Engagement Rate: 57.29% / 55.80%
- Zero Result Rate: 26.06% / 12.56%

## Delta
- Views Delta: 3077
- Completion Rate Delta: -0.68%
- Engagement Rate Delta: -1.49%
- Zero Result Rate Delta: -13.50%

## Before JSON (Sample)
```json
{
  "meta": {
    "generated_at": "2026-04-26T18:14:07.156378",
    "tenant_id": "demo_corp",
    "phase": "before",
    "scenario": "factory_busy",
    "scenario_label": "繁忙期",
    "period_days": 7,
    "num_users": 3000,
    "num_contents": 30,
    "target_events": 50000
  },
  "aggregates": {
    "views": 18060,
    "completion_rate": 0.656921373200443,
    "engagement_rate": 0.5729235880398671,
    "zero_result_rate": 0.26062322946175637
  }
}
```

## After JSON (Sample)
```json
{
  "meta": {
    "generated_at": "2026-04-26T18:14:07.578075",
    "tenant_id": "demo_corp",
    "phase": "after",
    "scenario": "factory_busy",
    "scenario_label": "繁忙期",
    "period_days": 7,
    "num_users": 3000,
    "num_contents": 30,
    "target_events": 50000
  },
  "aggregates": {
    "views": 21137,
    "completion_rate": 0.6500922552869376,
    "engagement_rate": 0.558026209963571,
    "zero_result_rate": 0.12560386473429952
  }
}
```
