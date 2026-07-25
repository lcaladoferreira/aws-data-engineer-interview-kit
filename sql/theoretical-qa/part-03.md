# SQL — 175 Theoretical Q&A — Part 3

Original interview answers.

<!-- item -->
## 51. **Question:** How would you troubleshoot **partitioning** in OLTP?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For partitioning, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 52. **Question:** What is the main risk of **materialized views** in a warehouse?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For materialized views, document the input contract, expected scale, failure behavior, and recovery procedure. In a warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 53. **Question:** How would you optimize **SCD** in a lakehouse?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For SCD, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 54. **Question:** How would you test **NULL semantics** in an incremental pipeline?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For NULL semantics, document the input contract, expected scale, failure behavior, and recovery procedure. In an incremental pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 55. **Question:** What production evidence validates **set operations** in a high-concurrency dashboard?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For set operations, document the input contract, expected scale, failure behavior, and recovery procedure. In a high-concurrency dashboard, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 56. **Question:** How do you make **data types** in OLTP?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For data types, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 57. **Question:** How would you explain **cardinality** in a warehouse?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For cardinality, document the input contract, expected scale, failure behavior, and recovery procedure. In a warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 58. **Question:** When would you choose **aggregation** in a lakehouse?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For aggregation, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 59. **Question:** How would you troubleshoot **recursive SQL** in an incremental pipeline?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For recursive SQL, document the input contract, expected scale, failure behavior, and recovery procedure. In an incremental pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 60. **Question:** What is the main risk of **MERGE** in a high-concurrency dashboard?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For MERGE, document the input contract, expected scale, failure behavior, and recovery procedure. In a high-concurrency dashboard, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 61. **Question:** How would you optimize **joins** in OLTP?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For joins, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 62. **Question:** How would you test **window functions** in a warehouse?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For window functions, document the input contract, expected scale, failure behavior, and recovery procedure. In a warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 63. **Question:** What production evidence validates **CTEs** in a lakehouse?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For CTEs, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 64. **Question:** How do you make **subqueries** in an incremental pipeline?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For subqueries, document the input contract, expected scale, failure behavior, and recovery procedure. In an incremental pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 65. **Question:** How would you explain **indexes** in a high-concurrency dashboard?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For indexes, document the input contract, expected scale, failure behavior, and recovery procedure. In a high-concurrency dashboard, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 66. **Question:** When would you choose **query plans** in OLTP?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For query plans, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 67. **Question:** How would you troubleshoot **transactions** in a warehouse?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For transactions, document the input contract, expected scale, failure behavior, and recovery procedure. In a warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 68. **Question:** What is the main risk of **isolation** in a lakehouse?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For isolation, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 69. **Question:** How would you optimize **normalization** in an incremental pipeline?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For normalization, document the input contract, expected scale, failure behavior, and recovery procedure. In an incremental pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 70. **Question:** How would you test **constraints** in a high-concurrency dashboard?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For constraints, document the input contract, expected scale, failure behavior, and recovery procedure. In a high-concurrency dashboard, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 71. **Question:** What production evidence validates **partitioning** in OLTP?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For partitioning, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 72. **Question:** How do you make **materialized views** in a warehouse?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For materialized views, document the input contract, expected scale, failure behavior, and recovery procedure. In a warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 73. **Question:** How would you explain **SCD** in a lakehouse?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For SCD, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 74. **Question:** When would you choose **NULL semantics** in an incremental pipeline?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For NULL semantics, document the input contract, expected scale, failure behavior, and recovery procedure. In an incremental pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 75. **Question:** How would you troubleshoot **set operations** in a high-concurrency dashboard?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For set operations, document the input contract, expected scale, failure behavior, and recovery procedure. In a high-concurrency dashboard, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
