# PySpark — 160 Theoretical Q&A — Part 4

Original interview answers.

<!-- item -->
## 76. **Question:** What is the main risk of **UDFs** in a 10 TB batch?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For UDFs, document the input contract, expected scale, failure behavior, and recovery procedure. In a 10 TB batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 77. **Question:** How would you optimize **Pandas UDFs** in a streaming job?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For Pandas UDFs, document the input contract, expected scale, failure behavior, and recovery procedure. In a streaming job, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 78. **Question:** How would you test **schema evolution** in AWS Glue?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For schema evolution, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS Glue, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 79. **Question:** What production evidence validates **Parquet** in Amazon EMR?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For Parquet, document the input contract, expected scale, failure behavior, and recovery procedure. In Amazon EMR, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 80. **Question:** How do you make **Delta Lake** in a lakehouse?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For Delta Lake, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 81. **Question:** How would you explain **lazy evaluation** in a 10 TB batch?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For lazy evaluation, document the input contract, expected scale, failure behavior, and recovery procedure. In a 10 TB batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 82. **Question:** When would you choose **transformations** in a streaming job?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For transformations, document the input contract, expected scale, failure behavior, and recovery procedure. In a streaming job, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 83. **Question:** How would you troubleshoot **actions** in AWS Glue?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For actions, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS Glue, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 84. **Question:** What is the main risk of **Catalyst** in Amazon EMR?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For Catalyst, document the input contract, expected scale, failure behavior, and recovery procedure. In Amazon EMR, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 85. **Question:** How would you optimize **Tungsten** in a lakehouse?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For Tungsten, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 86. **Question:** How would you test **shuffle** in a 10 TB batch?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For shuffle, document the input contract, expected scale, failure behavior, and recovery procedure. In a 10 TB batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 87. **Question:** What production evidence validates **partitioning** in a streaming job?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For partitioning, document the input contract, expected scale, failure behavior, and recovery procedure. In a streaming job, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 88. **Question:** How do you make **AQE** in AWS Glue?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For AQE, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS Glue, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 89. **Question:** How would you explain **broadcast joins** in Amazon EMR?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For broadcast joins, document the input contract, expected scale, failure behavior, and recovery procedure. In Amazon EMR, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 90. **Question:** When would you choose **skew** in a lakehouse?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For skew, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 91. **Question:** How would you troubleshoot **caching** in a 10 TB batch?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For caching, document the input contract, expected scale, failure behavior, and recovery procedure. In a 10 TB batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 92. **Question:** What is the main risk of **checkpointing** in a streaming job?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For checkpointing, document the input contract, expected scale, failure behavior, and recovery procedure. In a streaming job, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 93. **Question:** How would you optimize **Structured Streaming** in AWS Glue?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For Structured Streaming, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS Glue, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 94. **Question:** How would you test **watermarks** in Amazon EMR?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For watermarks, document the input contract, expected scale, failure behavior, and recovery procedure. In Amazon EMR, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 95. **Question:** What production evidence validates **state** in a lakehouse?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For state, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 96. **Question:** How do you make **UDFs** in a 10 TB batch?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For UDFs, document the input contract, expected scale, failure behavior, and recovery procedure. In a 10 TB batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 97. **Question:** How would you explain **Pandas UDFs** in a streaming job?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For Pandas UDFs, document the input contract, expected scale, failure behavior, and recovery procedure. In a streaming job, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 98. **Question:** When would you choose **schema evolution** in AWS Glue?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For schema evolution, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS Glue, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 99. **Question:** How would you troubleshoot **Parquet** in Amazon EMR?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For Parquet, document the input contract, expected scale, failure behavior, and recovery procedure. In Amazon EMR, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 100. **Question:** What is the main risk of **Delta Lake** in a lakehouse?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For Delta Lake, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
