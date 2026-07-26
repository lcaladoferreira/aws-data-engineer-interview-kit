# Data Modeling — 30 In-depth Q&A — Part 1

Conceptual through physical modeling.

<!-- item -->
## 1. **Question:** How would you explain **entities** in OLTP?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For entities, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 2. **Question:** When would you choose **relationships** in analytics?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For relationships, document the input contract, expected scale, failure behavior, and recovery procedure. In analytics, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 3. **Question:** How would you troubleshoot **cardinality** in streaming?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For cardinality, document the input contract, expected scale, failure behavior, and recovery procedure. In streaming, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 4. **Question:** What is the main risk of **normal forms** in OLTP?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For normal forms, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 5. **Question:** How would you optimize **denormalization** in analytics?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For denormalization, document the input contract, expected scale, failure behavior, and recovery procedure. In analytics, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 6. **Question:** How would you test **Data Vault** in streaming?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For Data Vault, document the input contract, expected scale, failure behavior, and recovery procedure. In streaming, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 7. **Question:** What production evidence validates **dimensional models** in OLTP?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For dimensional models, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 8. **Question:** How do you make **event models** in analytics?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For event models, document the input contract, expected scale, failure behavior, and recovery procedure. In analytics, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 9. **Question:** How would you explain **document models** in streaming?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For document models, document the input contract, expected scale, failure behavior, and recovery procedure. In streaming, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 10. **Question:** When would you choose **wide tables** in OLTP?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For wide tables, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 11. **Question:** How would you troubleshoot **schema evolution** in analytics?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For schema evolution, document the input contract, expected scale, failure behavior, and recovery procedure. In analytics, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 12. **Question:** What is the main risk of **data contracts** in streaming?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For data contracts, document the input contract, expected scale, failure behavior, and recovery procedure. In streaming, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 13. **Question:** How would you optimize **entities** in OLTP?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For entities, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 14. **Question:** How would you test **relationships** in analytics?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For relationships, document the input contract, expected scale, failure behavior, and recovery procedure. In analytics, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 15. **Question:** What production evidence validates **cardinality** in streaming?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For cardinality, document the input contract, expected scale, failure behavior, and recovery procedure. In streaming, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 16. **Question:** How do you make **normal forms** in OLTP?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For normal forms, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 17. **Question:** How would you explain **denormalization** in analytics?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For denormalization, document the input contract, expected scale, failure behavior, and recovery procedure. In analytics, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 18. **Question:** When would you choose **Data Vault** in streaming?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For Data Vault, document the input contract, expected scale, failure behavior, and recovery procedure. In streaming, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 19. **Question:** How would you troubleshoot **dimensional models** in OLTP?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For dimensional models, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 20. **Question:** What is the main risk of **event models** in analytics?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For event models, document the input contract, expected scale, failure behavior, and recovery procedure. In analytics, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 21. **Question:** How would you optimize **document models** in streaming?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For document models, document the input contract, expected scale, failure behavior, and recovery procedure. In streaming, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 22. **Question:** How would you test **wide tables** in OLTP?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For wide tables, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 23. **Question:** What production evidence validates **schema evolution** in analytics?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For schema evolution, document the input contract, expected scale, failure behavior, and recovery procedure. In analytics, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 24. **Question:** How do you make **data contracts** in streaming?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For data contracts, document the input contract, expected scale, failure behavior, and recovery procedure. In streaming, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 25. **Question:** How would you explain **entities** in OLTP?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For entities, document the input contract, expected scale, failure behavior, and recovery procedure. In OLTP, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
