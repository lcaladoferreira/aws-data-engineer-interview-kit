# Data Modeling — 30 In-depth Q&A — Part 2

Conceptual through physical modeling.

<!-- item -->
## 26. **Question:** When would you choose **relationships** in analytics?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For relationships, document the input contract, expected scale, failure behavior, and recovery procedure. In analytics, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 27. **Question:** How would you troubleshoot **cardinality** in streaming?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For cardinality, document the input contract, expected scale, failure behavior, and recovery procedure. In streaming, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 28. **Question:** What is the main risk of **normal forms** in OLTP?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For normal forms, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 29. **Question:** How would you optimize **denormalization** in analytics?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For denormalization, document the input contract, expected scale, failure behavior, and recovery procedure. In analytics, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 30. **Question:** How would you test **Data Vault** in streaming?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For Data Vault, document the input contract, expected scale, failure behavior, and recovery procedure. In streaming, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
