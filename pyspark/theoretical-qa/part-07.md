# PySpark — 160 Theoretical Q&A — Part 7

Original interview answers.

<!-- item -->
## 151. **Question:** What production evidence validates **caching** in a 10 TB batch?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For caching, document the input contract, expected scale, failure behavior, and recovery procedure. In a 10 TB batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 152. **Question:** How do you make **checkpointing** in a streaming job?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For checkpointing, document the input contract, expected scale, failure behavior, and recovery procedure. In a streaming job, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 153. **Question:** How would you explain **Structured Streaming** in AWS Glue?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For Structured Streaming, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS Glue, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 154. **Question:** When would you choose **watermarks** in Amazon EMR?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For watermarks, document the input contract, expected scale, failure behavior, and recovery procedure. In Amazon EMR, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 155. **Question:** How would you troubleshoot **state** in a lakehouse?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For state, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 156. **Question:** What is the main risk of **UDFs** in a 10 TB batch?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For UDFs, document the input contract, expected scale, failure behavior, and recovery procedure. In a 10 TB batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 157. **Question:** How would you optimize **Pandas UDFs** in a streaming job?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For Pandas UDFs, document the input contract, expected scale, failure behavior, and recovery procedure. In a streaming job, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 158. **Question:** How would you test **schema evolution** in AWS Glue?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For schema evolution, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS Glue, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 159. **Question:** What production evidence validates **Parquet** in Amazon EMR?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For Parquet, document the input contract, expected scale, failure behavior, and recovery procedure. In Amazon EMR, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 160. **Question:** How do you make **Delta Lake** in a lakehouse?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For Delta Lake, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
