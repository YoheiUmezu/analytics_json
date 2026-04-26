# Manus Analytics Report

## Overview
- Tenant: demo_corp
- Generated At: 2026-04-26T18:13:53.265708
- Scenario: campaign_boost (全社キャンペーン)
- Users: 3000
- Contents: 30
- Period Days: 7

## KPI Comparison (Before / After)
- Views: 19785 / 24409
- Completion Rate: 65.57% / 65.41%
- Engagement Rate: 62.99% / 61.85%
- Zero Result Rate: 20.22% / 7.77%

## Delta
- Views Delta: 4624
- Completion Rate Delta: -0.16%
- Engagement Rate Delta: -1.14%
- Zero Result Rate Delta: -12.46%

## Before JSON (Sample)
```json
{
  "meta": {
    "generated_at": "2026-04-26T18:13:52.780770",
    "tenant_id": "demo_corp",
    "phase": "before",
    "scenario": "campaign_boost",
    "scenario_label": "全社キャンペーン",
    "period_days": 7,
    "num_users": 3000,
    "num_contents": 30,
    "target_events": 50000
  },
  "aggregates": {
    "views": 19785,
    "completion_rate": 0.6556987616881476,
    "engagement_rate": 0.629921657821582,
    "zero_result_rate": 0.20222634508348794
  }
}
```

## After JSON (Sample)
```json
{
  "meta": {
    "generated_at": "2026-04-26T18:13:53.223863",
    "tenant_id": "demo_corp",
    "phase": "after",
    "scenario": "campaign_boost",
    "scenario_label": "全社キャンペーン",
    "period_days": 7,
    "num_users": 3000,
    "num_contents": 30,
    "target_events": 50000
  },
  "aggregates": {
    "views": 24409,
    "completion_rate": 0.6541439632922282,
    "engagement_rate": 0.6185423409398173,
    "zero_result_rate": 0.07766059443911794
  }
}
```
