# SQL — 180 Solved Coding Problems — Part 6

Engine-neutral solutions; validate dialect-specific date and qualification syntax.

<!-- item -->
## 126. Given `inventory_snapshots`, create monthly cohorts.

```sql
WITH prepared AS (
  SELECT *, DATE_TRUNC('month', MIN(event_ts) OVER (PARTITION BY user_id)) AS result_value
  FROM inventory_snapshots
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 127. Given `support_tickets`, create monthly cohorts.

```sql
WITH prepared AS (
  SELECT *, DATE_TRUNC('month', MIN(event_ts) OVER (PARTITION BY user_id)) AS result_value
  FROM support_tickets
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 128. Given `CDC_records`, create monthly cohorts.

```sql
WITH prepared AS (
  SELECT *, DATE_TRUNC('month', MIN(event_ts) OVER (PARTITION BY user_id)) AS result_value
  FROM CDC_records
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 129. Given `subscriptions`, create monthly cohorts.

```sql
WITH prepared AS (
  SELECT *, DATE_TRUNC('month', MIN(event_ts) OVER (PARTITION BY user_id)) AS result_value
  FROM subscriptions
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 130. Given `job_runs`, create monthly cohorts.

```sql
WITH prepared AS (
  SELECT *, DATE_TRUNC('month', MIN(event_ts) OVER (PARTITION BY user_id)) AS result_value
  FROM job_runs
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 131. Given `page_views`, create monthly cohorts.

```sql
WITH prepared AS (
  SELECT *, DATE_TRUNC('month', MIN(event_ts) OVER (PARTITION BY user_id)) AS result_value
  FROM page_views
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 132. Given `device_telemetry`, create monthly cohorts.

```sql
WITH prepared AS (
  SELECT *, DATE_TRUNC('month', MIN(event_ts) OVER (PARTITION BY user_id)) AS result_value
  FROM device_telemetry
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 133. Given `orders`, calculate percentiles.

```sql
WITH prepared AS (
  SELECT *, PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY duration_ms) AS result_value
  FROM orders
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 134. Given `clickstream_events`, calculate percentiles.

```sql
WITH prepared AS (
  SELECT *, PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY duration_ms) AS result_value
  FROM clickstream_events
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 135. Given `IoT_readings`, calculate percentiles.

```sql
WITH prepared AS (
  SELECT *, PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY duration_ms) AS result_value
  FROM IoT_readings
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 136. Given `payments`, calculate percentiles.

```sql
WITH prepared AS (
  SELECT *, PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY duration_ms) AS result_value
  FROM payments
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 137. Given `shipments`, calculate percentiles.

```sql
WITH prepared AS (
  SELECT *, PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY duration_ms) AS result_value
  FROM shipments
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 138. Given `inventory_snapshots`, calculate percentiles.

```sql
WITH prepared AS (
  SELECT *, PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY duration_ms) AS result_value
  FROM inventory_snapshots
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 139. Given `support_tickets`, calculate percentiles.

```sql
WITH prepared AS (
  SELECT *, PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY duration_ms) AS result_value
  FROM support_tickets
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 140. Given `CDC_records`, calculate percentiles.

```sql
WITH prepared AS (
  SELECT *, PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY duration_ms) AS result_value
  FROM CDC_records
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 141. Given `subscriptions`, calculate percentiles.

```sql
WITH prepared AS (
  SELECT *, PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY duration_ms) AS result_value
  FROM subscriptions
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 142. Given `job_runs`, calculate percentiles.

```sql
WITH prepared AS (
  SELECT *, PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY duration_ms) AS result_value
  FROM job_runs
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 143. Given `page_views`, calculate percentiles.

```sql
WITH prepared AS (
  SELECT *, PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY duration_ms) AS result_value
  FROM page_views
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 144. Given `device_telemetry`, calculate percentiles.

```sql
WITH prepared AS (
  SELECT *, PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY duration_ms) AS result_value
  FROM device_telemetry
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 145. Given `orders`, identify gaps and islands.

```sql
WITH prepared AS (
  SELECT *, event_date-ROW_NUMBER() OVER (PARTITION BY entity_id ORDER BY event_date) * INTERVAL '1 day' AS result_value
  FROM orders
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 146. Given `clickstream_events`, identify gaps and islands.

```sql
WITH prepared AS (
  SELECT *, event_date-ROW_NUMBER() OVER (PARTITION BY entity_id ORDER BY event_date) * INTERVAL '1 day' AS result_value
  FROM clickstream_events
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 147. Given `IoT_readings`, identify gaps and islands.

```sql
WITH prepared AS (
  SELECT *, event_date-ROW_NUMBER() OVER (PARTITION BY entity_id ORDER BY event_date) * INTERVAL '1 day' AS result_value
  FROM IoT_readings
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 148. Given `payments`, identify gaps and islands.

```sql
WITH prepared AS (
  SELECT *, event_date-ROW_NUMBER() OVER (PARTITION BY entity_id ORDER BY event_date) * INTERVAL '1 day' AS result_value
  FROM payments
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 149. Given `shipments`, identify gaps and islands.

```sql
WITH prepared AS (
  SELECT *, event_date-ROW_NUMBER() OVER (PARTITION BY entity_id ORDER BY event_date) * INTERVAL '1 day' AS result_value
  FROM shipments
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.

<!-- item -->
## 150. Given `inventory_snapshots`, identify gaps and islands.

```sql
WITH prepared AS (
  SELECT *, event_date-ROW_NUMBER() OVER (PARTITION BY entity_id ORDER BY event_date) * INTERVAL '1 day' AS result_value
  FROM inventory_snapshots
)
SELECT * FROM prepared;
```

**Why:** The CTE exposes the target grain and makes the analytical step testable. Adapt date syntax and `QUALIFY` to the target engine.
