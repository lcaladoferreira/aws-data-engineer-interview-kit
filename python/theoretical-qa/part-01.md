# Python — 40 Theoretical Q&A — Part 1

Original interview answers.

<!-- item -->
## 1. **Question:** How would you explain **iterators** in batch ETL?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For iterators, document the input contract, expected scale, failure behavior, and recovery procedure. In batch ETL, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 2. **Question:** When would you choose **generators** in stream ingestion?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For generators, document the input contract, expected scale, failure behavior, and recovery procedure. In stream ingestion, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 3. **Question:** How would you troubleshoot **decorators** in an AWS Lambda?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For decorators, document the input contract, expected scale, failure behavior, and recovery procedure. In an AWS Lambda, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 4. **Question:** What is the main risk of **context managers** in data validation?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For context managers, document the input contract, expected scale, failure behavior, and recovery procedure. In data validation, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 5. **Question:** How would you optimize **exceptions** in batch ETL?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For exceptions, document the input contract, expected scale, failure behavior, and recovery procedure. In batch ETL, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 6. **Question:** How would you test **typing** in stream ingestion?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For typing, document the input contract, expected scale, failure behavior, and recovery procedure. In stream ingestion, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 7. **Question:** What production evidence validates **dataclasses** in an AWS Lambda?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For dataclasses, document the input contract, expected scale, failure behavior, and recovery procedure. In an AWS Lambda, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 8. **Question:** How do you make **multiprocessing** in data validation?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For multiprocessing, document the input contract, expected scale, failure behavior, and recovery procedure. In data validation, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 9. **Question:** How would you explain **threading** in batch ETL?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For threading, document the input contract, expected scale, failure behavior, and recovery procedure. In batch ETL, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 10. **Question:** When would you choose **asyncio** in stream ingestion?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For asyncio, document the input contract, expected scale, failure behavior, and recovery procedure. In stream ingestion, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 11. **Question:** How would you troubleshoot **memory management** in an AWS Lambda?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For memory management, document the input contract, expected scale, failure behavior, and recovery procedure. In an AWS Lambda, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 12. **Question:** What is the main risk of **serialization** in data validation?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For serialization, document the input contract, expected scale, failure behavior, and recovery procedure. In data validation, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 13. **Question:** How would you optimize **testing** in batch ETL?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For testing, document the input contract, expected scale, failure behavior, and recovery procedure. In batch ETL, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 14. **Question:** How would you test **packaging** in stream ingestion?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For packaging, document the input contract, expected scale, failure behavior, and recovery procedure. In stream ingestion, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 15. **Question:** What production evidence validates **virtual environments** in an AWS Lambda?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For virtual environments, document the input contract, expected scale, failure behavior, and recovery procedure. In an AWS Lambda, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 16. **Question:** How do you make **logging** in data validation?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For logging, document the input contract, expected scale, failure behavior, and recovery procedure. In data validation, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 17. **Question:** How would you explain **iterators** in batch ETL?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For iterators, document the input contract, expected scale, failure behavior, and recovery procedure. In batch ETL, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 18. **Question:** When would you choose **generators** in stream ingestion?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For generators, document the input contract, expected scale, failure behavior, and recovery procedure. In stream ingestion, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 19. **Question:** How would you troubleshoot **decorators** in an AWS Lambda?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For decorators, document the input contract, expected scale, failure behavior, and recovery procedure. In an AWS Lambda, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 20. **Question:** What is the main risk of **context managers** in data validation?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For context managers, document the input contract, expected scale, failure behavior, and recovery procedure. In data validation, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 21. **Question:** How would you optimize **exceptions** in batch ETL?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For exceptions, document the input contract, expected scale, failure behavior, and recovery procedure. In batch ETL, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 22. **Question:** How would you test **typing** in stream ingestion?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For typing, document the input contract, expected scale, failure behavior, and recovery procedure. In stream ingestion, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 23. **Question:** What production evidence validates **dataclasses** in an AWS Lambda?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For dataclasses, document the input contract, expected scale, failure behavior, and recovery procedure. In an AWS Lambda, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 24. **Question:** How do you make **multiprocessing** in data validation?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For multiprocessing, document the input contract, expected scale, failure behavior, and recovery procedure. In data validation, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 25. **Question:** How would you explain **threading** in batch ETL?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For threading, document the input contract, expected scale, failure behavior, and recovery procedure. In batch ETL, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
