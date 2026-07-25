# Data Warehousing — 30 In-depth Q&A — Part 2

Dimensional, operational, and cloud warehouse coverage.

<!-- item -->
## 26. **Question:** When would you choose **OLAP** in Redshift?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For OLAP, document the input contract, expected scale, failure behavior, and recovery procedure. In Redshift, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 27. **Question:** How would you troubleshoot **MPP** in a lakehouse?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For MPP, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 28. **Question:** What is the main risk of **workload management** in enterprise warehouse?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For workload management, document the input contract, expected scale, failure behavior, and recovery procedure. In enterprise warehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 29. **Question:** How would you optimize **semantic layers** in Redshift?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For semantic layers, document the input contract, expected scale, failure behavior, and recovery procedure. In Redshift, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 30. **Question:** How would you test **data marts** in a lakehouse?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For data marts, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
