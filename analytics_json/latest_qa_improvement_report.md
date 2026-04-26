# Manus Analytics Report

## Overview
- Tenant: demo_corp
- Generated At: 2026-04-26T18:10:59.877420
- Scenario: qa_improvement (FAQ改善)
- Users: 3000
- Contents: 30
- Period Days: 7

## KPI Comparison (Before / After)
- Views: 21768 / 24354
- Completion Rate: 65.57% / 65.42%
- Engagement Rate: 59.53% / 60.23%
- Zero Result Rate: 16.47% / 4.67%

## Delta
- Views Delta: 2586
- Completion Rate Delta: -0.15%
- Engagement Rate Delta: 0.70%
- Zero Result Rate Delta: -11.80%

## Before JSON (Sample)
```json
{
  "meta": {
    "generated_at": "2026-04-26T18:10:58.634958",
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
    "views": 21768,
    "completion_rate": 0.6557331863285557,
    "engagement_rate": 0.5953234105108416,
    "zero_result_rate": 0.16470588235294117
  }
}
```

## After JSON (Sample)
```json
{
  "meta": {
    "generated_at": "2026-04-26T18:10:59.072732",
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
    "views": 24354,
    "completion_rate": 0.6541841175987517,
    "engagement_rate": 0.6023240535435658,
    "zero_result_rate": 0.04672057502246182
  }
}
```
