# PySpark — 160 Theoretical Q&A — Part 6

Original interview answers.

<!-- item -->
## 126. **Question:** How would you test **shuffle** in a 10 TB batch?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For shuffle, document the input contract, expected scale, failure behavior, and recovery procedure. In a 10 TB batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 127. **Question:** What production evidence validates **partitioning** in a streaming job?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For partitioning, document the input contract, expected scale, failure behavior, and recovery procedure. In a streaming job, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 128. **Question:** How do you make **AQE** in AWS Glue?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For AQE, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS Glue, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 129. **Question:** How would you explain **broadcast joins** in Amazon EMR?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For broadcast joins, document the input contract, expected scale, failure behavior, and recovery procedure. In Amazon EMR, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 130. **Question:** When would you choose **skew** in a lakehouse?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For skew, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 131. **Question:** How would you troubleshoot **caching** in a 10 TB batch?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For caching, document the input contract, expected scale, failure behavior, and recovery procedure. In a 10 TB batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 132. **Question:** What is the main risk of **checkpointing** in a streaming job?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For checkpointing, document the input contract, expected scale, failure behavior, and recovery procedure. In a streaming job, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 133. **Question:** How would you optimize **Structured Streaming** in AWS Glue?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For Structured Streaming, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS Glue, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 134. **Question:** How would you test **watermarks** in Amazon EMR?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For watermarks, document the input contract, expected scale, failure behavior, and recovery procedure. In Amazon EMR, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 135. **Question:** What production evidence validates **state** in a lakehouse?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For state, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 136. **Question:** How do you make **UDFs** in a 10 TB batch?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For UDFs, document the input contract, expected scale, failure behavior, and recovery procedure. In a 10 TB batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 137. **Question:** How would you explain **Pandas UDFs** in a streaming job?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For Pandas UDFs, document the input contract, expected scale, failure behavior, and recovery procedure. In a streaming job, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 138. **Question:** When would you choose **schema evolution** in AWS Glue?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For schema evolution, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS Glue, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 139. **Question:** How would you troubleshoot **Parquet** in Amazon EMR?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For Parquet, document the input contract, expected scale, failure behavior, and recovery procedure. In Amazon EMR, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 140. **Question:** What is the main risk of **Delta Lake** in a lakehouse?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For Delta Lake, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 141. **Question:** How would you optimize **lazy evaluation** in a 10 TB batch?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For lazy evaluation, document the input contract, expected scale, failure behavior, and recovery procedure. In a 10 TB batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 142. **Question:** How would you test **transformations** in a streaming job?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For transformations, document the input contract, expected scale, failure behavior, and recovery procedure. In a streaming job, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 143. **Question:** What production evidence validates **actions** in AWS Glue?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For actions, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS Glue, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 144. **Question:** How do you make **Catalyst** in Amazon EMR?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For Catalyst, document the input contract, expected scale, failure behavior, and recovery procedure. In Amazon EMR, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 145. **Question:** How would you explain **Tungsten** in a lakehouse?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For Tungsten, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 146. **Question:** When would you choose **shuffle** in a 10 TB batch?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For shuffle, document the input contract, expected scale, failure behavior, and recovery procedure. In a 10 TB batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 147. **Question:** How would you troubleshoot **partitioning** in a streaming job?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For partitioning, document the input contract, expected scale, failure behavior, and recovery procedure. In a streaming job, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 148. **Question:** What is the main risk of **AQE** in AWS Glue?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For AQE, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS Glue, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 149. **Question:** How would you optimize **broadcast joins** in Amazon EMR?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For broadcast joins, document the input contract, expected scale, failure behavior, and recovery procedure. In Amazon EMR, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 150. **Question:** How would you test **skew** in a lakehouse?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For skew, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
