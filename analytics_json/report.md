# Manus Analytics Report

## Overview
- Tenant: demo_corp
- Generated At: 2026-04-26T17:43:46.103107
- Users: 3000
- Contents: 30
- Period Days: 7

## KPI Comparison (Before / After)
- Views: 22478 / 21529
- Completion Rate: 65.57% / 65.82%
- Engagement Rate: 57.62% / 57.73%
- Zero Result Rate: 20.97% / 10.05%

## Delta
- Views Delta: -949
- Completion Rate Delta: 0.25%
- Engagement Rate Delta: 0.11%
- Zero Result Rate Delta: -10.92%

## Before JSON (Sample)
```json
{
  "meta": {
    "generated_at": "2026-04-26T17:43:44.971322",
    "tenant_id": "demo_corp",
    "scenario": "before",
    "period_days": 7,
    "num_users": 3000,
    "num_contents": 30,
    "target_events": 50000
  },
  "aggregates": {
    "views": 22478,
    "completion_rate": 0.6557078031853367,
    "engagement_rate": 0.5761633597295133,
    "zero_result_rate": 0.20970873786407768
  }
}
```

## After JSON (Sample)
```json
{
  "meta": {
    "generated_at": "2026-04-26T17:43:45.325150",
    "tenant_id": "demo_corp",
    "scenario": "after",
    "period_days": 7,
    "num_users": 3000,
    "num_contents": 30,
    "target_events": 50000
  },
  "aggregates": {
    "views": 21529,
    "completion_rate": 0.6582284360629848,
    "engagement_rate": 0.577267871243439,
    "zero_result_rate": 0.10049751243781095
  }
}
```
