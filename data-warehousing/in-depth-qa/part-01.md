# Data Warehousing — 30 In-depth Q&A — Part 1

Dimensional, operational, and cloud warehouse coverage.

<!-- item -->
## 1. **Question:** How would you explain **facts** in enterprise warehouse?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For facts, document the input contract, expected scale, failure behavior, and recovery procedure. In enterprise warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 2. **Question:** When would you choose **dimensions** in Redshift?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For dimensions, document the input contract, expected scale, failure behavior, and recovery procedure. In Redshift, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 3. **Question:** How would you troubleshoot **grain** in a lakehouse?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For grain, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 4. **Question:** What is the main risk of **star schema** in enterprise warehouse?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For star schema, document the input contract, expected scale, failure behavior, and recovery procedure. In enterprise warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 5. **Question:** How would you optimize **snowflake schema** in Redshift?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For snowflake schema, document the input contract, expected scale, failure behavior, and recovery procedure. In Redshift, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 6. **Question:** How would you test **SCD** in a lakehouse?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For SCD, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 7. **Question:** What production evidence validates **surrogate keys** in enterprise warehouse?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For surrogate keys, document the input contract, expected scale, failure behavior, and recovery procedure. In enterprise warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 8. **Question:** How do you make **conformed dimensions** in Redshift?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For conformed dimensions, document the input contract, expected scale, failure behavior, and recovery procedure. In Redshift, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 9. **Question:** How would you explain **late facts** in a lakehouse?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For late facts, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 10. **Question:** When would you choose **snapshots** in enterprise warehouse?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For snapshots, document the input contract, expected scale, failure behavior, and recovery procedure. In enterprise warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 11. **Question:** How would you troubleshoot **OLAP** in Redshift?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For OLAP, document the input contract, expected scale, failure behavior, and recovery procedure. In Redshift, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 12. **Question:** What is the main risk of **MPP** in a lakehouse?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For MPP, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 13. **Question:** How would you optimize **workload management** in enterprise warehouse?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For workload management, document the input contract, expected scale, failure behavior, and recovery procedure. In enterprise warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 14. **Question:** How would you test **semantic layers** in Redshift?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For semantic layers, document the input contract, expected scale, failure behavior, and recovery procedure. In Redshift, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 15. **Question:** What production evidence validates **data marts** in a lakehouse?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For data marts, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 16. **Question:** How do you make **facts** in enterprise warehouse?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For facts, document the input contract, expected scale, failure behavior, and recovery procedure. In enterprise warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 17. **Question:** How would you explain **dimensions** in Redshift?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For dimensions, document the input contract, expected scale, failure behavior, and recovery procedure. In Redshift, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 18. **Question:** When would you choose **grain** in a lakehouse?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For grain, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 19. **Question:** How would you troubleshoot **star schema** in enterprise warehouse?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For star schema, document the input contract, expected scale, failure behavior, and recovery procedure. In enterprise warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 20. **Question:** What is the main risk of **snowflake schema** in Redshift?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For snowflake schema, document the input contract, expected scale, failure behavior, and recovery procedure. In Redshift, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 21. **Question:** How would you optimize **SCD** in a lakehouse?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For SCD, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 22. **Question:** How would you test **surrogate keys** in enterprise warehouse?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For surrogate keys, document the input contract, expected scale, failure behavior, and recovery procedure. In enterprise warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 23. **Question:** What production evidence validates **conformed dimensions** in Redshift?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For conformed dimensions, document the input contract, expected scale, failure behavior, and recovery procedure. In Redshift, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 24. **Question:** How do you make **late facts** in a lakehouse?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For late facts, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 25. **Question:** How would you explain **snapshots** in enterprise warehouse?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For snapshots, document the input contract, expected scale, failure behavior, and recovery procedure. In enterprise warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
