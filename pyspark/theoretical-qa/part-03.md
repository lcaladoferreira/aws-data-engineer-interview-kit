# PySpark — 160 Theoretical Q&A — Part 3

Original interview answers.

<!-- item -->
## 51. **Question:** How would you troubleshoot **caching** in a 10 TB batch?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For caching, document the input contract, expected scale, failure behavior, and recovery procedure. In a 10 TB batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 52. **Question:** What is the main risk of **checkpointing** in a streaming job?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For checkpointing, document the input contract, expected scale, failure behavior, and recovery procedure. In a streaming job, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 53. **Question:** How would you optimize **Structured Streaming** in AWS Glue?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For Structured Streaming, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS Glue, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 54. **Question:** How would you test **watermarks** in Amazon EMR?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For watermarks, document the input contract, expected scale, failure behavior, and recovery procedure. In Amazon EMR, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 55. **Question:** What production evidence validates **state** in a lakehouse?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For state, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 56. **Question:** How do you make **UDFs** in a 10 TB batch?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For UDFs, document the input contract, expected scale, failure behavior, and recovery procedure. In a 10 TB batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 57. **Question:** How would you explain **Pandas UDFs** in a streaming job?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For Pandas UDFs, document the input contract, expected scale, failure behavior, and recovery procedure. In a streaming job, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 58. **Question:** When would you choose **schema evolution** in AWS Glue?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For schema evolution, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS Glue, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 59. **Question:** How would you troubleshoot **Parquet** in Amazon EMR?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For Parquet, document the input contract, expected scale, failure behavior, and recovery procedure. In Amazon EMR, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 60. **Question:** What is the main risk of **Delta Lake** in a lakehouse?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For Delta Lake, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 61. **Question:** How would you optimize **lazy evaluation** in a 10 TB batch?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For lazy evaluation, document the input contract, expected scale, failure behavior, and recovery procedure. In a 10 TB batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 62. **Question:** How would you test **transformations** in a streaming job?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For transformations, document the input contract, expected scale, failure behavior, and recovery procedure. In a streaming job, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 63. **Question:** What production evidence validates **actions** in AWS Glue?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For actions, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS Glue, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 64. **Question:** How do you make **Catalyst** in Amazon EMR?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For Catalyst, document the input contract, expected scale, failure behavior, and recovery procedure. In Amazon EMR, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 65. **Question:** How would you explain **Tungsten** in a lakehouse?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For Tungsten, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 66. **Question:** When would you choose **shuffle** in a 10 TB batch?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For shuffle, document the input contract, expected scale, failure behavior, and recovery procedure. In a 10 TB batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 67. **Question:** How would you troubleshoot **partitioning** in a streaming job?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For partitioning, document the input contract, expected scale, failure behavior, and recovery procedure. In a streaming job, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 68. **Question:** What is the main risk of **AQE** in AWS Glue?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For AQE, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS Glue, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 69. **Question:** How would you optimize **broadcast joins** in Amazon EMR?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For broadcast joins, document the input contract, expected scale, failure behavior, and recovery procedure. In Amazon EMR, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 70. **Question:** How would you test **skew** in a lakehouse?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For skew, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 71. **Question:** What production evidence validates **caching** in a 10 TB batch?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For caching, document the input contract, expected scale, failure behavior, and recovery procedure. In a 10 TB batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 72. **Question:** How do you make **checkpointing** in a streaming job?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For checkpointing, document the input contract, expected scale, failure behavior, and recovery procedure. In a streaming job, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 73. **Question:** How would you explain **Structured Streaming** in AWS Glue?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For Structured Streaming, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS Glue, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 74. **Question:** When would you choose **watermarks** in Amazon EMR?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For watermarks, document the input contract, expected scale, failure behavior, and recovery procedure. In Amazon EMR, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 75. **Question:** How would you troubleshoot **state** in a lakehouse?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For state, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
