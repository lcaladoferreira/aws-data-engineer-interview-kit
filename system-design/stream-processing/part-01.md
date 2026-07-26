# System Design — Stream Processing — Part 1

End-to-end streaming design questions.

<!-- item -->
## 1. **Question:** How would you explain **brokers** in clickstream?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For brokers, document the input contract, expected scale, failure behavior, and recovery procedure. In clickstream, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 2. **Question:** When would you choose **partition keys** in IoT?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For partition keys, document the input contract, expected scale, failure behavior, and recovery procedure. In IoT, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 3. **Question:** How would you troubleshoot **consumer groups** in payments?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For consumer groups, document the input contract, expected scale, failure behavior, and recovery procedure. In payments, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 4. **Question:** What is the main risk of **watermarks** in clickstream?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For watermarks, document the input contract, expected scale, failure behavior, and recovery procedure. In clickstream, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 5. **Question:** How would you optimize **late data** in IoT?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For late data, document the input contract, expected scale, failure behavior, and recovery procedure. In IoT, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 6. **Question:** How would you test **state** in payments?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For state, document the input contract, expected scale, failure behavior, and recovery procedure. In payments, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 7. **Question:** What production evidence validates **exactly-once semantics** in clickstream?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For exactly-once semantics, document the input contract, expected scale, failure behavior, and recovery procedure. In clickstream, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 8. **Question:** How do you make **schema registry** in IoT?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For schema registry, document the input contract, expected scale, failure behavior, and recovery procedure. In IoT, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 9. **Question:** How would you explain **DLQ** in payments?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For DLQ, document the input contract, expected scale, failure behavior, and recovery procedure. In payments, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 10. **Question:** When would you choose **replay** in clickstream?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For replay, document the input contract, expected scale, failure behavior, and recovery procedure. In clickstream, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 11. **Question:** How would you troubleshoot **backpressure** in IoT?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For backpressure, document the input contract, expected scale, failure behavior, and recovery procedure. In IoT, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 12. **Question:** What is the main risk of **brokers** in payments?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For brokers, document the input contract, expected scale, failure behavior, and recovery procedure. In payments, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 13. **Question:** How would you optimize **partition keys** in clickstream?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For partition keys, document the input contract, expected scale, failure behavior, and recovery procedure. In clickstream, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 14. **Question:** How would you test **consumer groups** in IoT?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For consumer groups, document the input contract, expected scale, failure behavior, and recovery procedure. In IoT, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 15. **Question:** What production evidence validates **watermarks** in payments?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For watermarks, document the input contract, expected scale, failure behavior, and recovery procedure. In payments, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 16. **Question:** How do you make **late data** in clickstream?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For late data, document the input contract, expected scale, failure behavior, and recovery procedure. In clickstream, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 17. **Question:** How would you explain **state** in IoT?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For state, document the input contract, expected scale, failure behavior, and recovery procedure. In IoT, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 18. **Question:** When would you choose **exactly-once semantics** in payments?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For exactly-once semantics, document the input contract, expected scale, failure behavior, and recovery procedure. In payments, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 19. **Question:** How would you troubleshoot **schema registry** in clickstream?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For schema registry, document the input contract, expected scale, failure behavior, and recovery procedure. In clickstream, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 20. **Question:** What is the main risk of **DLQ** in IoT?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For DLQ, document the input contract, expected scale, failure behavior, and recovery procedure. In IoT, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 21. **Question:** How would you optimize **replay** in payments?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For replay, document the input contract, expected scale, failure behavior, and recovery procedure. In payments, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 22. **Question:** How would you test **backpressure** in clickstream?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For backpressure, document the input contract, expected scale, failure behavior, and recovery procedure. In clickstream, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 23. **Question:** What production evidence validates **brokers** in IoT?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For brokers, document the input contract, expected scale, failure behavior, and recovery procedure. In IoT, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 24. **Question:** How do you make **partition keys** in payments?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For partition keys, document the input contract, expected scale, failure behavior, and recovery procedure. In payments, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 25. **Question:** How would you explain **consumer groups** in clickstream?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For consumer groups, document the input contract, expected scale, failure behavior, and recovery procedure. In clickstream, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
