# Manus Analytics Report

## Overview
- Tenant: demo_corp
- Generated At: 2026-04-26T18:14:23.250843
- Scenario: qa_improvement (FAQ改善)
- Users: 3000
- Contents: 30
- Period Days: 7

## KPI Comparison (Before / After)
- Views: 21287 / 24619
- Completion Rate: 65.41% / 65.32%
- Engagement Rate: 59.54% / 58.70%
- Zero Result Rate: 18.30% / 5.74%

## Delta
- Views Delta: 3332
- Completion Rate Delta: -0.09%
- Engagement Rate Delta: -0.84%
- Zero Result Rate Delta: -12.56%

## Before JSON (Sample)
```json
{
  "meta": {
    "generated_at": "2026-04-26T18:14:22.771873",
    "tenant_id": "demo_corp",
    "phase": "before",
    "scenario": "qa_improvement",
    "scenario_label": "FAQ改善",
    "period_days": 7,
    "num_users": 3000,
    "num_contents": 30,
    "target_events": 50000
  },
  "aggregates": {
    "views": 21287,
    "completion_rate": 0.6541081411189928,
    "engagement_rate": 0.5953868558275004,
    "zero_result_rate": 0.18303145853193517
  }
}
```

## After JSON (Sample)
```json
{
  "meta": {
    "generated_at": "2026-04-26T18:14:23.209216",
    "tenant_id": "demo_corp",
    "phase": "after",
    "scenario": "qa_improvement",
    "scenario_label": "FAQ改善",
    "period_days": 7,
    "num_users": 3000,
    "num_contents": 30,
    "target_events": 50000
  },
  "aggregates": {
    "views": 24619,
    "completion_rate": 0.6532353060644218,
    "engagement_rate": 0.58698566148097,
    "zero_result_rate": 0.05742935278030994
  }
}
```
