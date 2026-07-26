# System Design — Batch Processing — Part 1

End-to-end batch design questions.

<!-- item -->
## 1. **Question:** How would you explain **ingestion** in daily batch?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For ingestion, document the input contract, expected scale, failure behavior, and recovery procedure. In daily batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 2. **Question:** When would you choose **object storage** in hourly micro-batch?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For object storage, document the input contract, expected scale, failure behavior, and recovery procedure. In hourly micro-batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 3. **Question:** How would you troubleshoot **orchestration** in 10 TB backfill?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For orchestration, document the input contract, expected scale, failure behavior, and recovery procedure. In 10 TB backfill, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 4. **Question:** What is the main risk of **incremental loads** in daily batch?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For incremental loads, document the input contract, expected scale, failure behavior, and recovery procedure. In daily batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 5. **Question:** How would you optimize **idempotency** in hourly micro-batch?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For idempotency, document the input contract, expected scale, failure behavior, and recovery procedure. In hourly micro-batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 6. **Question:** How would you test **backfills** in 10 TB backfill?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For backfills, document the input contract, expected scale, failure behavior, and recovery procedure. In 10 TB backfill, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 7. **Question:** What production evidence validates **compaction** in daily batch?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For compaction, document the input contract, expected scale, failure behavior, and recovery procedure. In daily batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 8. **Question:** How do you make **quality** in hourly micro-batch?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For quality, document the input contract, expected scale, failure behavior, and recovery procedure. In hourly micro-batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 9. **Question:** How would you explain **lineage** in 10 TB backfill?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For lineage, document the input contract, expected scale, failure behavior, and recovery procedure. In 10 TB backfill, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 10. **Question:** When would you choose **recovery** in daily batch?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For recovery, document the input contract, expected scale, failure behavior, and recovery procedure. In daily batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 11. **Question:** How would you troubleshoot **cost** in hourly micro-batch?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For cost, document the input contract, expected scale, failure behavior, and recovery procedure. In hourly micro-batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 12. **Question:** What is the main risk of **ingestion** in 10 TB backfill?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For ingestion, document the input contract, expected scale, failure behavior, and recovery procedure. In 10 TB backfill, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 13. **Question:** How would you optimize **object storage** in daily batch?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For object storage, document the input contract, expected scale, failure behavior, and recovery procedure. In daily batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 14. **Question:** How would you test **orchestration** in hourly micro-batch?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For orchestration, document the input contract, expected scale, failure behavior, and recovery procedure. In hourly micro-batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 15. **Question:** What production evidence validates **incremental loads** in 10 TB backfill?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For incremental loads, document the input contract, expected scale, failure behavior, and recovery procedure. In 10 TB backfill, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 16. **Question:** How do you make **idempotency** in daily batch?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For idempotency, document the input contract, expected scale, failure behavior, and recovery procedure. In daily batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 17. **Question:** How would you explain **backfills** in hourly micro-batch?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For backfills, document the input contract, expected scale, failure behavior, and recovery procedure. In hourly micro-batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 18. **Question:** When would you choose **compaction** in 10 TB backfill?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For compaction, document the input contract, expected scale, failure behavior, and recovery procedure. In 10 TB backfill, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 19. **Question:** How would you troubleshoot **quality** in daily batch?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For quality, document the input contract, expected scale, failure behavior, and recovery procedure. In daily batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 20. **Question:** What is the main risk of **lineage** in hourly micro-batch?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For lineage, document the input contract, expected scale, failure behavior, and recovery procedure. In hourly micro-batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 21. **Question:** How would you optimize **recovery** in 10 TB backfill?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For recovery, document the input contract, expected scale, failure behavior, and recovery procedure. In 10 TB backfill, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 22. **Question:** How would you test **cost** in daily batch?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For cost, document the input contract, expected scale, failure behavior, and recovery procedure. In daily batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 23. **Question:** What production evidence validates **ingestion** in hourly micro-batch?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For ingestion, document the input contract, expected scale, failure behavior, and recovery procedure. In hourly micro-batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 24. **Question:** How do you make **object storage** in 10 TB backfill?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For object storage, document the input contract, expected scale, failure behavior, and recovery procedure. In 10 TB backfill, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 25. **Question:** How would you explain **orchestration** in daily batch?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For orchestration, document the input contract, expected scale, failure behavior, and recovery procedure. In daily batch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
