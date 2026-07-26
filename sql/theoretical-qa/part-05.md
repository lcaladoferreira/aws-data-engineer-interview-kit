# SQL — 175 Theoretical Q&A — Part 5

Original interview answers.

<!-- item -->
## 101. **Question:** How would you optimize **joins** in OLTP?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For joins, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 102. **Question:** How would you test **window functions** in a warehouse?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For window functions, document the input contract, expected scale, failure behavior, and recovery procedure. In a warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 103. **Question:** What production evidence validates **CTEs** in a lakehouse?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For CTEs, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 104. **Question:** How do you make **subqueries** in an incremental pipeline?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For subqueries, document the input contract, expected scale, failure behavior, and recovery procedure. In an incremental pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 105. **Question:** How would you explain **indexes** in a high-concurrency dashboard?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For indexes, document the input contract, expected scale, failure behavior, and recovery procedure. In a high-concurrency dashboard, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 106. **Question:** When would you choose **query plans** in OLTP?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For query plans, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 107. **Question:** How would you troubleshoot **transactions** in a warehouse?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For transactions, document the input contract, expected scale, failure behavior, and recovery procedure. In a warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 108. **Question:** What is the main risk of **isolation** in a lakehouse?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For isolation, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 109. **Question:** How would you optimize **normalization** in an incremental pipeline?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For normalization, document the input contract, expected scale, failure behavior, and recovery procedure. In an incremental pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 110. **Question:** How would you test **constraints** in a high-concurrency dashboard?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For constraints, document the input contract, expected scale, failure behavior, and recovery procedure. In a high-concurrency dashboard, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 111. **Question:** What production evidence validates **partitioning** in OLTP?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For partitioning, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 112. **Question:** How do you make **materialized views** in a warehouse?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For materialized views, document the input contract, expected scale, failure behavior, and recovery procedure. In a warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 113. **Question:** How would you explain **SCD** in a lakehouse?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For SCD, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 114. **Question:** When would you choose **NULL semantics** in an incremental pipeline?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For NULL semantics, document the input contract, expected scale, failure behavior, and recovery procedure. In an incremental pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 115. **Question:** How would you troubleshoot **set operations** in a high-concurrency dashboard?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For set operations, document the input contract, expected scale, failure behavior, and recovery procedure. In a high-concurrency dashboard, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 116. **Question:** What is the main risk of **data types** in OLTP?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For data types, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 117. **Question:** How would you optimize **cardinality** in a warehouse?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For cardinality, document the input contract, expected scale, failure behavior, and recovery procedure. In a warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 118. **Question:** How would you test **aggregation** in a lakehouse?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For aggregation, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 119. **Question:** What production evidence validates **recursive SQL** in an incremental pipeline?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For recursive SQL, document the input contract, expected scale, failure behavior, and recovery procedure. In an incremental pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 120. **Question:** How do you make **MERGE** in a high-concurrency dashboard?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For MERGE, document the input contract, expected scale, failure behavior, and recovery procedure. In a high-concurrency dashboard, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 121. **Question:** How would you explain **joins** in OLTP?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For joins, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 122. **Question:** When would you choose **window functions** in a warehouse?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For window functions, document the input contract, expected scale, failure behavior, and recovery procedure. In a warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 123. **Question:** How would you troubleshoot **CTEs** in a lakehouse?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For CTEs, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 124. **Question:** What is the main risk of **subqueries** in an incremental pipeline?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For subqueries, document the input contract, expected scale, failure behavior, and recovery procedure. In an incremental pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 125. **Question:** How would you optimize **indexes** in a high-concurrency dashboard?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For indexes, document the input contract, expected scale, failure behavior, and recovery procedure. In a high-concurrency dashboard, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
