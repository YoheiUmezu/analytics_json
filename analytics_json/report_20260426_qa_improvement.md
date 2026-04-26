# Manus Analytics Report

## Overview
- Tenant: demo_corp
- Generated At: 2026-04-26T17:48:53.280177
- Scenario: qa_improvement (FAQ改善)
- Users: 3000
- Contents: 30
- Period Days: 7

## KPI Comparison (Before / After)
- Views: 21633 / 24731
- Completion Rate: 65.46% / 65.34%
- Engagement Rate: 59.09% / 59.10%
- Zero Result Rate: 15.70% / 4.98%

## Delta
- Views Delta: 3098
- Completion Rate Delta: -0.12%
- Engagement Rate Delta: 0.01%
- Zero Result Rate Delta: -10.72%

## Before JSON (Sample)
```json
{
  "meta": {
    "generated_at": "2026-04-26T17:48:52.039532",
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
    "views": 21633,
    "completion_rate": 0.6546017658207368,
    "engagement_rate": 0.5909027874081265,
    "zero_result_rate": 0.1569713758079409
  }
}
```

## After JSON (Sample)
```json
{
  "meta": {
    "generated_at": "2026-04-26T17:48:52.476379",
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
    "views": 24731,
    "completion_rate": 0.6534309166632971,
    "engagement_rate": 0.5909587157818122,
    "zero_result_rate": 0.04975609756097561
  }
}
```
