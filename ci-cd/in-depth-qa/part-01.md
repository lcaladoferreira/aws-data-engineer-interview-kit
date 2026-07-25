# CI/CD for Data Engineers — 55 In-depth Q&A — Part 1

Deployment and data-specific controls.

<!-- item -->
## 1. **Question:** How would you explain **build** in GitHub Actions?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For build, document the input contract, expected scale, failure behavior, and recovery procedure. In GitHub Actions, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 2. **Question:** When would you choose **unit tests** in a regulated pipeline?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For unit tests, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 3. **Question:** How would you troubleshoot **integration tests** in multi-account AWS?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For integration tests, document the input contract, expected scale, failure behavior, and recovery procedure. In multi-account AWS, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 4. **Question:** What is the main risk of **linting** in a lakehouse?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For linting, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 5. **Question:** How would you optimize **artifact versioning** in GitHub Actions?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For artifact versioning, document the input contract, expected scale, failure behavior, and recovery procedure. In GitHub Actions, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 6. **Question:** How would you test **promotion** in a regulated pipeline?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For promotion, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 7. **Question:** What production evidence validates **rollback** in multi-account AWS?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For rollback, document the input contract, expected scale, failure behavior, and recovery procedure. In multi-account AWS, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 8. **Question:** How do you make **secrets** in a lakehouse?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For secrets, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 9. **Question:** How would you explain **OIDC** in GitHub Actions?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For OIDC, document the input contract, expected scale, failure behavior, and recovery procedure. In GitHub Actions, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 10. **Question:** When would you choose **IaC** in a regulated pipeline?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For IaC, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 11. **Question:** How would you troubleshoot **database migrations** in multi-account AWS?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For database migrations, document the input contract, expected scale, failure behavior, and recovery procedure. In multi-account AWS, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 12. **Question:** What is the main risk of **data tests** in a lakehouse?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For data tests, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 13. **Question:** How would you optimize **canary releases** in GitHub Actions?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For canary releases, document the input contract, expected scale, failure behavior, and recovery procedure. In GitHub Actions, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 14. **Question:** How would you test **blue-green** in a regulated pipeline?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For blue-green, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 15. **Question:** What production evidence validates **observability** in multi-account AWS?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For observability, document the input contract, expected scale, failure behavior, and recovery procedure. In multi-account AWS, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 16. **Question:** How do you make **build** in a lakehouse?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For build, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 17. **Question:** How would you explain **unit tests** in GitHub Actions?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For unit tests, document the input contract, expected scale, failure behavior, and recovery procedure. In GitHub Actions, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 18. **Question:** When would you choose **integration tests** in a regulated pipeline?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For integration tests, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 19. **Question:** How would you troubleshoot **linting** in multi-account AWS?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For linting, document the input contract, expected scale, failure behavior, and recovery procedure. In multi-account AWS, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 20. **Question:** What is the main risk of **artifact versioning** in a lakehouse?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For artifact versioning, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 21. **Question:** How would you optimize **promotion** in GitHub Actions?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For promotion, document the input contract, expected scale, failure behavior, and recovery procedure. In GitHub Actions, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 22. **Question:** How would you test **rollback** in a regulated pipeline?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For rollback, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 23. **Question:** What production evidence validates **secrets** in multi-account AWS?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For secrets, document the input contract, expected scale, failure behavior, and recovery procedure. In multi-account AWS, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 24. **Question:** How do you make **OIDC** in a lakehouse?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For OIDC, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 25. **Question:** How would you explain **IaC** in GitHub Actions?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For IaC, document the input contract, expected scale, failure behavior, and recovery procedure. In GitHub Actions, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
