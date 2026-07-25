# System Design — Batch Processing — Part 2

End-to-end batch design questions.

<!-- item -->
## 26. **Question:** When would you choose **incremental loads** in hourly micro-batch?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For incremental loads, document the input contract, expected scale, failure behavior, and recovery procedure. In hourly micro-batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 27. **Question:** How would you troubleshoot **idempotency** in 10 TB backfill?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For idempotency, document the input contract, expected scale, failure behavior, and recovery procedure. In 10 TB backfill, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 28. **Question:** What is the main risk of **backfills** in daily batch?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For backfills, document the input contract, expected scale, failure behavior, and recovery procedure. In daily batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 29. **Question:** How would you optimize **compaction** in hourly micro-batch?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For compaction, document the input contract, expected scale, failure behavior, and recovery procedure. In hourly micro-batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 30. **Question:** How would you test **quality** in 10 TB backfill?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For quality, document the input contract, expected scale, failure behavior, and recovery procedure. In 10 TB backfill, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 31. **Question:** What production evidence validates **lineage** in daily batch?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For lineage, document the input contract, expected scale, failure behavior, and recovery procedure. In daily batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 32. **Question:** How do you make **recovery** in hourly micro-batch?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For recovery, document the input contract, expected scale, failure behavior, and recovery procedure. In hourly micro-batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 33. **Question:** How would you explain **cost** in 10 TB backfill?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For cost, document the input contract, expected scale, failure behavior, and recovery procedure. In 10 TB backfill, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 34. **Question:** When would you choose **ingestion** in daily batch?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For ingestion, document the input contract, expected scale, failure behavior, and recovery procedure. In daily batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 35. **Question:** How would you troubleshoot **object storage** in hourly micro-batch?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For object storage, document the input contract, expected scale, failure behavior, and recovery procedure. In hourly micro-batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
