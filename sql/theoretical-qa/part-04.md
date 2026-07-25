# SQL — 175 Theoretical Q&A — Part 4

Original interview answers.

<!-- item -->
## 76. **Question:** What is the main risk of **data types** in OLTP?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For data types, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 77. **Question:** How would you optimize **cardinality** in a warehouse?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For cardinality, document the input contract, expected scale, failure behavior, and recovery procedure. In a warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 78. **Question:** How would you test **aggregation** in a lakehouse?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For aggregation, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 79. **Question:** What production evidence validates **recursive SQL** in an incremental pipeline?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For recursive SQL, document the input contract, expected scale, failure behavior, and recovery procedure. In an incremental pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 80. **Question:** How do you make **MERGE** in a high-concurrency dashboard?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For MERGE, document the input contract, expected scale, failure behavior, and recovery procedure. In a high-concurrency dashboard, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 81. **Question:** How would you explain **joins** in OLTP?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For joins, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 82. **Question:** When would you choose **window functions** in a warehouse?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For window functions, document the input contract, expected scale, failure behavior, and recovery procedure. In a warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 83. **Question:** How would you troubleshoot **CTEs** in a lakehouse?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For CTEs, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 84. **Question:** What is the main risk of **subqueries** in an incremental pipeline?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For subqueries, document the input contract, expected scale, failure behavior, and recovery procedure. In an incremental pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 85. **Question:** How would you optimize **indexes** in a high-concurrency dashboard?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For indexes, document the input contract, expected scale, failure behavior, and recovery procedure. In a high-concurrency dashboard, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 86. **Question:** How would you test **query plans** in OLTP?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For query plans, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 87. **Question:** What production evidence validates **transactions** in a warehouse?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For transactions, document the input contract, expected scale, failure behavior, and recovery procedure. In a warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 88. **Question:** How do you make **isolation** in a lakehouse?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For isolation, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 89. **Question:** How would you explain **normalization** in an incremental pipeline?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For normalization, document the input contract, expected scale, failure behavior, and recovery procedure. In an incremental pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 90. **Question:** When would you choose **constraints** in a high-concurrency dashboard?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For constraints, document the input contract, expected scale, failure behavior, and recovery procedure. In a high-concurrency dashboard, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 91. **Question:** How would you troubleshoot **partitioning** in OLTP?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For partitioning, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 92. **Question:** What is the main risk of **materialized views** in a warehouse?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For materialized views, document the input contract, expected scale, failure behavior, and recovery procedure. In a warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 93. **Question:** How would you optimize **SCD** in a lakehouse?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For SCD, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 94. **Question:** How would you test **NULL semantics** in an incremental pipeline?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For NULL semantics, document the input contract, expected scale, failure behavior, and recovery procedure. In an incremental pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 95. **Question:** What production evidence validates **set operations** in a high-concurrency dashboard?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For set operations, document the input contract, expected scale, failure behavior, and recovery procedure. In a high-concurrency dashboard, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 96. **Question:** How do you make **data types** in OLTP?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For data types, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 97. **Question:** How would you explain **cardinality** in a warehouse?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For cardinality, document the input contract, expected scale, failure behavior, and recovery procedure. In a warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 98. **Question:** When would you choose **aggregation** in a lakehouse?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For aggregation, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 99. **Question:** How would you troubleshoot **recursive SQL** in an incremental pipeline?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For recursive SQL, document the input contract, expected scale, failure behavior, and recovery procedure. In an incremental pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 100. **Question:** What is the main risk of **MERGE** in a high-concurrency dashboard?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For MERGE, document the input contract, expected scale, failure behavior, and recovery procedure. In a high-concurrency dashboard, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
