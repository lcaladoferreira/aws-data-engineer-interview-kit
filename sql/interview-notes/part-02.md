# SQL Interview-ready Tips — Part 2

Short reminders for live interviews.

<!-- item -->
## 26. **Question:** When would you choose **query plans** in a take-home test?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For query plans, document the input contract, expected scale, failure behavior, and recovery procedure. In a take-home test, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 27. **Question:** How would you troubleshoot **transactions** in production debugging?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For transactions, document the input contract, expected scale, failure behavior, and recovery procedure. In production debugging, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 28. **Question:** What is the main risk of **isolation** in a whiteboard interview?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For isolation, document the input contract, expected scale, failure behavior, and recovery procedure. In a whiteboard interview, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 29. **Question:** How would you optimize **normalization** in a take-home test?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For normalization, document the input contract, expected scale, failure behavior, and recovery procedure. In a take-home test, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 30. **Question:** How would you test **constraints** in production debugging?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For constraints, document the input contract, expected scale, failure behavior, and recovery procedure. In production debugging, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
