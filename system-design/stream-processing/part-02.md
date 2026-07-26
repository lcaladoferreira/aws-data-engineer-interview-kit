# System Design — Stream Processing — Part 2

End-to-end streaming design questions.

<!-- item -->
## 26. **Question:** When would you choose **watermarks** in IoT?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For watermarks, document the input contract, expected scale, failure behavior, and recovery procedure. In IoT, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 27. **Question:** How would you troubleshoot **late data** in payments?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For late data, document the input contract, expected scale, failure behavior, and recovery procedure. In payments, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 28. **Question:** What is the main risk of **state** in clickstream?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For state, document the input contract, expected scale, failure behavior, and recovery procedure. In clickstream, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 29. **Question:** How would you optimize **exactly-once semantics** in IoT?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For exactly-once semantics, document the input contract, expected scale, failure behavior, and recovery procedure. In IoT, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 30. **Question:** How would you test **schema registry** in payments?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For schema registry, document the input contract, expected scale, failure behavior, and recovery procedure. In payments, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 31. **Question:** What production evidence validates **DLQ** in clickstream?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For DLQ, document the input contract, expected scale, failure behavior, and recovery procedure. In clickstream, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 32. **Question:** How do you make **replay** in IoT?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For replay, document the input contract, expected scale, failure behavior, and recovery procedure. In IoT, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 33. **Question:** How would you explain **backpressure** in payments?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For backpressure, document the input contract, expected scale, failure behavior, and recovery procedure. In payments, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 34. **Question:** When would you choose **brokers** in clickstream?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For brokers, document the input contract, expected scale, failure behavior, and recovery procedure. In clickstream, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 35. **Question:** How would you troubleshoot **partition keys** in IoT?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For partition keys, document the input contract, expected scale, failure behavior, and recovery procedure. In IoT, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
