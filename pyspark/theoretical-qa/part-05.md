# PySpark — 160 Theoretical Q&A — Part 5

Original interview answers.

<!-- item -->
## 101. **Question:** How would you optimize **lazy evaluation** in a 10 TB batch?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For lazy evaluation, document the input contract, expected scale, failure behavior, and recovery procedure. In a 10 TB batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 102. **Question:** How would you test **transformations** in a streaming job?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For transformations, document the input contract, expected scale, failure behavior, and recovery procedure. In a streaming job, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 103. **Question:** What production evidence validates **actions** in AWS Glue?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For actions, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS Glue, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 104. **Question:** How do you make **Catalyst** in Amazon EMR?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For Catalyst, document the input contract, expected scale, failure behavior, and recovery procedure. In Amazon EMR, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 105. **Question:** How would you explain **Tungsten** in a lakehouse?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For Tungsten, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 106. **Question:** When would you choose **shuffle** in a 10 TB batch?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For shuffle, document the input contract, expected scale, failure behavior, and recovery procedure. In a 10 TB batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 107. **Question:** How would you troubleshoot **partitioning** in a streaming job?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For partitioning, document the input contract, expected scale, failure behavior, and recovery procedure. In a streaming job, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 108. **Question:** What is the main risk of **AQE** in AWS Glue?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For AQE, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS Glue, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 109. **Question:** How would you optimize **broadcast joins** in Amazon EMR?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For broadcast joins, document the input contract, expected scale, failure behavior, and recovery procedure. In Amazon EMR, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 110. **Question:** How would you test **skew** in a lakehouse?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For skew, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 111. **Question:** What production evidence validates **caching** in a 10 TB batch?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For caching, document the input contract, expected scale, failure behavior, and recovery procedure. In a 10 TB batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 112. **Question:** How do you make **checkpointing** in a streaming job?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For checkpointing, document the input contract, expected scale, failure behavior, and recovery procedure. In a streaming job, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 113. **Question:** How would you explain **Structured Streaming** in AWS Glue?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For Structured Streaming, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS Glue, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 114. **Question:** When would you choose **watermarks** in Amazon EMR?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For watermarks, document the input contract, expected scale, failure behavior, and recovery procedure. In Amazon EMR, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 115. **Question:** How would you troubleshoot **state** in a lakehouse?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For state, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 116. **Question:** What is the main risk of **UDFs** in a 10 TB batch?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For UDFs, document the input contract, expected scale, failure behavior, and recovery procedure. In a 10 TB batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 117. **Question:** How would you optimize **Pandas UDFs** in a streaming job?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For Pandas UDFs, document the input contract, expected scale, failure behavior, and recovery procedure. In a streaming job, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 118. **Question:** How would you test **schema evolution** in AWS Glue?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For schema evolution, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS Glue, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 119. **Question:** What production evidence validates **Parquet** in Amazon EMR?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For Parquet, document the input contract, expected scale, failure behavior, and recovery procedure. In Amazon EMR, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 120. **Question:** How do you make **Delta Lake** in a lakehouse?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For Delta Lake, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 121. **Question:** How would you explain **lazy evaluation** in a 10 TB batch?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For lazy evaluation, document the input contract, expected scale, failure behavior, and recovery procedure. In a 10 TB batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 122. **Question:** When would you choose **transformations** in a streaming job?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For transformations, document the input contract, expected scale, failure behavior, and recovery procedure. In a streaming job, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 123. **Question:** How would you troubleshoot **actions** in AWS Glue?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For actions, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS Glue, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 124. **Question:** What is the main risk of **Catalyst** in Amazon EMR?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For Catalyst, document the input contract, expected scale, failure behavior, and recovery procedure. In Amazon EMR, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 125. **Question:** How would you optimize **Tungsten** in a lakehouse?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For Tungsten, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
