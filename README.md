# analytics_json automation

毎朝 9:00 に analytics データを自動生成し、GitHub に push するプロジェクトです。

## What this does

- 6つのシナリオを日替わりローテーションで選択
- `before` / `after` の JSON を生成
- KPI 比較を含む Markdown レポートを生成
- 生成物を `git add` / `commit` / `push` して GitHub に反映

## Scenarios

- `campaign_boost` (全社キャンペーン)
- `policy_change` (制度変更周知)
- `factory_busy` (繁忙期)
- `mobile_push` (モバイル強化)
- `qa_improvement` (FAQ改善)
- `new_joiners` (新入社員期)

## Output files

出力先は `analytics_json/` です。

- `analytics_YYYYMMDD_<scenario>_before.json`
- `analytics_YYYYMMDD_<scenario>_after.json`
- `report_YYYYMMDD_<scenario>.md`

日付入りファイル名のため、毎日 Raw URL が変わります。

## Raw URL format

- `https://raw.githubusercontent.com/YoheiUmezu/analytics_json/main/analytics_json/report_YYYYMMDD_<scenario>.md`
- `https://raw.githubusercontent.com/YoheiUmezu/analytics_json/main/analytics_json/analytics_YYYYMMDD_<scenario>_before.json`
- `https://raw.githubusercontent.com/YoheiUmezu/analytics_json/main/analytics_json/analytics_YYYYMMDD_<scenario>_after.json`

## Manual run

```bash
cd /Users/umedzuyouhei/Desktop/analytics
source venv/bin/activate
python generate_analytics.py
```

## Cron schedule

以下の cron を登録済みです。

```cron
0 9 * * * /Users/umedzuyouhei/Desktop/analytics/run_daily_analytics.sh >> /Users/umedzuyouhei/Desktop/analytics/cron.log 2>&1
```

`run_daily_analytics.sh` は venv 有効化後に `generate_analytics.py` を実行します。
