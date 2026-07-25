# SQL — 180 Solved Coding Problems — Part 8

Engine-neutral solutions; validate dialect-specific date and qualification syntax.

<!-- item -->
## 176. Given `CDC_records`, avoid double counting after joins.

```sql
WITH prepared AS (
  SELECT *, SUM(amount) OVER (PARTITION BY business_key) AS result_value
  FROM CDC_records
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 177. Given `subscriptions`, avoid double counting after joins.

```sql
WITH prepared AS (
  SELECT *, SUM(amount) OVER (PARTITION BY business_key) AS result_value
  FROM subscriptions
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 178. Given `job_runs`, avoid double counting after joins.

```sql
WITH prepared AS (
  SELECT *, SUM(amount) OVER (PARTITION BY business_key) AS result_value
  FROM job_runs
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 179. Given `page_views`, avoid double counting after joins.

```sql
WITH prepared AS (
  SELECT *, SUM(amount) OVER (PARTITION BY business_key) AS result_value
  FROM page_views
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 180. Given `device_telemetry`, avoid double counting after joins.

```sql
WITH prepared AS (
  SELECT *, SUM(amount) OVER (PARTITION BY business_key) AS result_value
  FROM device_telemetry
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.
