# Analytics Scenario Generator

このフォルダは、6シナリオの analytics データと Manus 向けレポートを生成し、GitHub に保存するための作業ディレクトリです。

## Folder Structure

- `generate_analytics.py`: メイン生成スクリプト
- `run_daily_analytics.sh`: 日次実行用ランナー（必要時のみ使用）
- `analytics_json/`: 生成物出力先
- `requirements.txt`: Python依存関係

## Scenarios

- `campaign_boost`（全社キャンペーン）
- `policy_change`（制度変更周知）
- `factory_busy`（繁忙期）
- `mobile_push`（モバイル強化）
- `qa_improvement`（FAQ改善）
- `new_joiners`（新入社員期）

## Generated Artifacts

`analytics_json/` 配下に以下を出力します。

- 日付付き成果物
  - `analytics_YYYYMMDD_<scenario>_before.json`
  - `analytics_YYYYMMDD_<scenario>_after.json`
  - `report_YYYYMMDD_<scenario>.md`
- シナリオ最新成果物（上書き）
  - `latest_<scenario>_before.json`
  - `latest_<scenario>_after.json`
  - `latest_<scenario>_report.md`
- 一覧インデックス
  - `scenario_index.md`
  - `scenario_index.json`

## Raw URLs

- シナリオ一覧  
  `https://raw.githubusercontent.com/YoheiUmezu/analytics_json/main/analytics_json/scenario_index.md`
- 例: latest レポート  
  `https://raw.githubusercontent.com/YoheiUmezu/analytics_json/main/analytics_json/latest_campaign_boost_report.md`
- 例: latest JSON  
  `https://raw.githubusercontent.com/YoheiUmezu/analytics_json/main/analytics_json/latest_campaign_boost_before.json`

## Local Run

```bash
cd /Users/umedzuyouhei/Desktop/analytics
source venv/bin/activate
python generate_analytics.py
```

## Cron Status

- 9:00 の analytics 自動実行 cron は停止済みです。
- 再開する場合は下記を登録してください。

```cron
0 9 * * * /Users/umedzuyouhei/Desktop/analytics/run_daily_analytics.sh >> /Users/umedzuyouhei/Desktop/analytics/cron.log 2>&1
```
