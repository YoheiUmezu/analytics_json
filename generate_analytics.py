import json
import os
import random
import subprocess
import uuid
from datetime import datetime, timedelta, timezone

from faker import Faker

fake = Faker("ja_JP")

OUTPUT_DIR = "analytics_json"
os.makedirs(OUTPUT_DIR, exist_ok=True)
STATE_FILE = os.path.join(OUTPUT_DIR, "run_state.json")

NUM_USERS = 3000
NUM_CONTENTS = 30
PERIOD_DAYS = 7
TARGET_EVENTS = 50000
ALLOWED_DELTA = 4000

DEPARTMENTS = ["営業", "製造", "本社"]
SEARCH_QUERIES = ["勤怠", "申請", "交通費", "福利厚生", "出張", "精算", "社内規程"]
SCENARIOS = [
    {
        "name": "campaign_boost",
        "label": "全社キャンペーン",
        "before_view_prob": {"high": 0.28, "medium": 0.22, "low": 0.16},
        "after_view_prob": {"high": 0.34, "medium": 0.27, "low": 0.21},
        "reaction_bonus": 0.10,
        "search_zero_rate_before": 0.20,
        "search_zero_rate_after": 0.08,
    },
    {
        "name": "policy_change",
        "label": "制度変更周知",
        "before_view_prob": {"high": 0.31, "medium": 0.25, "low": 0.18},
        "after_view_prob": {"high": 0.33, "medium": 0.27, "low": 0.20},
        "reaction_bonus": 0.06,
        "search_zero_rate_before": 0.18,
        "search_zero_rate_after": 0.09,
    },
    {
        "name": "factory_busy",
        "label": "繁忙期",
        "before_view_prob": {"high": 0.26, "medium": 0.20, "low": 0.14},
        "after_view_prob": {"high": 0.30, "medium": 0.24, "low": 0.17},
        "reaction_bonus": 0.04,
        "search_zero_rate_before": 0.24,
        "search_zero_rate_after": 0.11,
    },
    {
        "name": "mobile_push",
        "label": "モバイル強化",
        "before_view_prob": {"high": 0.29, "medium": 0.23, "low": 0.17},
        "after_view_prob": {"high": 0.35, "medium": 0.28, "low": 0.22},
        "reaction_bonus": 0.12,
        "search_zero_rate_before": 0.19,
        "search_zero_rate_after": 0.07,
    },
    {
        "name": "qa_improvement",
        "label": "FAQ改善",
        "before_view_prob": {"high": 0.30, "medium": 0.24, "low": 0.18},
        "after_view_prob": {"high": 0.32, "medium": 0.29, "low": 0.21},
        "reaction_bonus": 0.07,
        "search_zero_rate_before": 0.17,
        "search_zero_rate_after": 0.05,
    },
    {
        "name": "new_joiners",
        "label": "新入社員期",
        "before_view_prob": {"high": 0.27, "medium": 0.21, "low": 0.15},
        "after_view_prob": {"high": 0.31, "medium": 0.25, "low": 0.19},
        "reaction_bonus": 0.05,
        "search_zero_rate_before": 0.23,
        "search_zero_rate_after": 0.10,
    },
]


def build_contents():
    contents = []
    for i in range(1, NUM_CONTENTS + 1):
        if i <= 10:
            importance, content_type = "high", "news"
        elif i <= 20:
            importance, content_type = "medium", "faq"
        else:
            importance, content_type = "low", "video"

        contents.append(
            {
                "content_id": f"c{i}",
                "title": f"社内コンテンツ{i:02d}",
                "type": content_type,
                "importance": importance,
            }
        )
    return contents


def generate_users():
    users = []
    for _ in range(NUM_USERS):
        dept = random.choice(DEPARTMENTS)
        if dept == "営業":
            engagement = random.uniform(0.55, 0.85)
        elif dept == "製造":
            engagement = random.uniform(0.2, 0.5)
        else:
            engagement = random.uniform(0.35, 0.7)

        users.append(
            {
                "user_id": str(uuid.uuid4()),
                "department": dept,
                "role": "employee",
                "device_preference": random.choice(["mobile", "desktop"]),
                "engagement_score": round(engagement, 2),
            }
        )
    return users


def random_timestamp_in_period(base_time):
    delta_seconds = random.randint(0, PERIOD_DAYS * 24 * 60 * 60 - 1)
    return (base_time - timedelta(seconds=delta_seconds)).isoformat()


def get_today_scenario(today=None):
    if today is None:
        today = datetime.now(timezone.utc).date()
    return SCENARIOS[today.toordinal() % len(SCENARIOS)]


def load_state():
    if not os.path.exists(STATE_FILE):
        return {"completed_scenarios": []}
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def update_scenario_progress(scenario_name):
    state = load_state()
    completed = set(state.get("completed_scenarios", []))
    completed.add(scenario_name)
    state["completed_scenarios"] = sorted(completed)
    state["updated_at"] = datetime.utcnow().isoformat()
    save_state(state)
    return len(completed) >= len(SCENARIOS), state


def stop_cron_job():
    cron_entry = (
        "0 9 * * * /Users/umedzuyouhei/Desktop/analytics/run_daily_analytics.sh "
        ">> /Users/umedzuyouhei/Desktop/analytics/cron.log 2>&1"
    )
    result = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
    if result.returncode != 0:
        return
    lines = [line for line in result.stdout.splitlines() if line.strip() and line.strip() != cron_entry]
    new_cron = "\n".join(lines) + ("\n" if lines else "")
    subprocess.run(["crontab", "-"], input=new_cron, text=True, check=True)


def generate_events(users, contents, phase, scenario):
    events = []
    now = datetime.utcnow()

    view_prob = scenario["before_view_prob"] if phase == "before" else scenario["after_view_prob"]

    for user in users:
        for content in contents:
            if random.random() >= view_prob[content["importance"]]:
                continue

            dwell_time = random.randint(5, 120)
            events.append(
                {
                    "event_id": str(uuid.uuid4()),
                    "user_id": user["user_id"],
                    "content_id": content["content_id"],
                    "event_type": "view",
                    "timestamp": random_timestamp_in_period(now),
                    "properties": {"dwell_time": dwell_time},
                }
            )

            completion_threshold = 45
            if dwell_time >= completion_threshold:
                events.append(
                    {
                        "event_id": str(uuid.uuid4()),
                        "user_id": user["user_id"],
                        "content_id": content["content_id"],
                        "event_type": "completion",
                        "timestamp": random_timestamp_in_period(now),
                        "properties": {},
                    }
                )

            reaction_prob = min(user["engagement_score"] + scenario["reaction_bonus"], 0.95)
            if random.random() < reaction_prob:
                events.append(
                    {
                        "event_id": str(uuid.uuid4()),
                        "user_id": user["user_id"],
                        "content_id": content["content_id"],
                        "event_type": "reaction",
                        "timestamp": random_timestamp_in_period(now),
                        "properties": {"reaction_type": random.choice(["like", "bookmark"])},
                    }
                )

                if random.random() < 0.15:
                    events.append(
                        {
                            "event_id": str(uuid.uuid4()),
                            "user_id": user["user_id"],
                            "content_id": content["content_id"],
                            "event_type": "comment",
                            "timestamp": random_timestamp_in_period(now),
                            "properties": {"text": fake.sentence()},
                        }
                    )

        if random.random() < 0.35:
            zero_rate = (
                scenario["search_zero_rate_before"]
                if phase == "before"
                else scenario["search_zero_rate_after"]
            )
            results = 0 if random.random() < zero_rate else random.randint(1, 8)
            events.append(
                {
                    "event_id": str(uuid.uuid4()),
                    "user_id": user["user_id"],
                    "content_id": None,
                    "event_type": "search",
                    "timestamp": random_timestamp_in_period(now),
                    "properties": {"query": random.choice(SEARCH_QUERIES), "results_count": results},
                }
            )

    random.shuffle(events)
    return events


def calculate_kpis(events):
    views = [e for e in events if e["event_type"] == "view"]
    completions = [e for e in events if e["event_type"] == "completion"]
    reactions = [e for e in events if e["event_type"] == "reaction"]
    searches = [e for e in events if e["event_type"] == "search"]
    zero_results = [s for s in searches if s["properties"]["results_count"] == 0]

    return {
        "views": len(views),
        "completion_rate": len(completions) / len(views) if views else 0,
        "engagement_rate": len(reactions) / len(views) if views else 0,
        "zero_result_rate": len(zero_results) / len(searches) if searches else 0,
    }


def generate_dataset(phase, scenario):
    users = generate_users()
    contents = build_contents()
    events = generate_events(users, contents, phase, scenario)

    return {
        "meta": {
            "generated_at": datetime.utcnow().isoformat(),
            "tenant_id": "demo_corp",
            "phase": phase,
            "scenario": scenario["name"],
            "scenario_label": scenario["label"],
            "period_days": PERIOD_DAYS,
            "num_users": NUM_USERS,
            "num_contents": len(contents),
            "target_events": TARGET_EVENTS,
        },
        "users": users,
        "contents": contents,
        "events": events,
        "aggregates": calculate_kpis(events),
    }


def save_json(data, filename):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def generate_md_report(before, after, scenario):
    before_kpi = before["aggregates"]
    after_kpi = after["aggregates"]

    def fmt_pct(value):
        return f"{value * 100:.2f}%"

    report = f"""# Manus Analytics Report

## Overview
- Tenant: {before["meta"]["tenant_id"]}
- Generated At: {datetime.utcnow().isoformat()}
- Scenario: {scenario["name"]} ({scenario["label"]})
- Users: {before["meta"]["num_users"]}
- Contents: {before["meta"]["num_contents"]}
- Period Days: {before["meta"]["period_days"]}

## KPI Comparison (Before / After)
- Views: {before_kpi["views"]} / {after_kpi["views"]}
- Completion Rate: {fmt_pct(before_kpi["completion_rate"])} / {fmt_pct(after_kpi["completion_rate"])}
- Engagement Rate: {fmt_pct(before_kpi["engagement_rate"])} / {fmt_pct(after_kpi["engagement_rate"])}
- Zero Result Rate: {fmt_pct(before_kpi["zero_result_rate"])} / {fmt_pct(after_kpi["zero_result_rate"])}

## Delta
- Views Delta: {after_kpi["views"] - before_kpi["views"]}
- Completion Rate Delta: {fmt_pct(after_kpi["completion_rate"] - before_kpi["completion_rate"])}
- Engagement Rate Delta: {fmt_pct(after_kpi["engagement_rate"] - before_kpi["engagement_rate"])}
- Zero Result Rate Delta: {fmt_pct(after_kpi["zero_result_rate"] - before_kpi["zero_result_rate"])}

## Before JSON (Sample)
```json
{json.dumps({"meta": before["meta"], "aggregates": before["aggregates"]}, ensure_ascii=False, indent=2)}
```

## After JSON (Sample)
```json
{json.dumps({"meta": after["meta"], "aggregates": after["aggregates"]}, ensure_ascii=False, indent=2)}
```
"""
    return report


def save_md(md, filename):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(md)


def git_push():
    subprocess.run(["git", "add", "analytics_json"], check=True)
    status = subprocess.run(["git", "status", "--porcelain"], check=True, capture_output=True, text=True)
    if not status.stdout.strip():
        print("No changes to commit.")
        return
    message = f"Daily analytics update {datetime.utcnow().strftime('%Y-%m-%d')}"
    subprocess.run(["git", "commit", "-m", message], check=True)
    subprocess.run(["git", "push", "origin", "HEAD"], check=True)
    print("Git push completed.")


def is_close_to_target(event_count):
    return abs(event_count - TARGET_EVENTS) <= ALLOWED_DELTA


if __name__ == "__main__":
    scenario = get_today_scenario()
    today_key = datetime.utcnow().strftime("%Y%m%d")
    max_attempts = 8
    selected_before = None
    selected_after = None

    for _ in range(max_attempts):
        before = generate_dataset("before", scenario)
        after = generate_dataset("after", scenario)
        if is_close_to_target(len(before["events"])) and is_close_to_target(len(after["events"])):
            selected_before = before
            selected_after = after
            break

    if selected_before is None:
        selected_before = before
        selected_after = after

    save_json(selected_before, f"analytics_{today_key}_{scenario['name']}_before.json")
    save_json(selected_after, f"analytics_{today_key}_{scenario['name']}_after.json")
    md = generate_md_report(selected_before, selected_after, scenario)
    save_md(md, f"report_{today_key}_{scenario['name']}.md")
    finished_all, state = update_scenario_progress(scenario["name"])
    if finished_all:
        stop_cron_job()
    git_push()

    print("JSON generated: analytics_json/")
    print(f"scenario: {scenario['name']}")
    print(f"completed scenarios: {len(state.get('completed_scenarios', []))}/{len(SCENARIOS)}")
    if finished_all:
        print("All scenarios completed once. Cron job removed.")
    print(f"before events: {len(selected_before['events'])}")
    print(f"after events: {len(selected_after['events'])}")
