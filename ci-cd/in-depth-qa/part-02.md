# CI/CD for Data Engineers — 55 In-depth Q&A — Part 2

Deployment and data-specific controls.

<!-- item -->
## 26. **Question:** When would you choose **database migrations** in a regulated pipeline?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For database migrations, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 27. **Question:** How would you troubleshoot **data tests** in multi-account AWS?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For data tests, document the input contract, expected scale, failure behavior, and recovery procedure. In multi-account AWS, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 28. **Question:** What is the main risk of **canary releases** in a lakehouse?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For canary releases, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 29. **Question:** How would you optimize **blue-green** in GitHub Actions?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For blue-green, document the input contract, expected scale, failure behavior, and recovery procedure. In GitHub Actions, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 30. **Question:** How would you test **observability** in a regulated pipeline?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For observability, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 31. **Question:** What production evidence validates **build** in multi-account AWS?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For build, document the input contract, expected scale, failure behavior, and recovery procedure. In multi-account AWS, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 32. **Question:** How do you make **unit tests** in a lakehouse?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For unit tests, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 33. **Question:** How would you explain **integration tests** in GitHub Actions?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For integration tests, document the input contract, expected scale, failure behavior, and recovery procedure. In GitHub Actions, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 34. **Question:** When would you choose **linting** in a regulated pipeline?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For linting, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 35. **Question:** How would you troubleshoot **artifact versioning** in multi-account AWS?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For artifact versioning, document the input contract, expected scale, failure behavior, and recovery procedure. In multi-account AWS, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 36. **Question:** What is the main risk of **promotion** in a lakehouse?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For promotion, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 37. **Question:** How would you optimize **rollback** in GitHub Actions?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For rollback, document the input contract, expected scale, failure behavior, and recovery procedure. In GitHub Actions, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 38. **Question:** How would you test **secrets** in a regulated pipeline?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For secrets, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 39. **Question:** What production evidence validates **OIDC** in multi-account AWS?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For OIDC, document the input contract, expected scale, failure behavior, and recovery procedure. In multi-account AWS, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 40. **Question:** How do you make **IaC** in a lakehouse?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For IaC, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 41. **Question:** How would you explain **database migrations** in GitHub Actions?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For database migrations, document the input contract, expected scale, failure behavior, and recovery procedure. In GitHub Actions, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 42. **Question:** When would you choose **data tests** in a regulated pipeline?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For data tests, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 43. **Question:** How would you troubleshoot **canary releases** in multi-account AWS?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For canary releases, document the input contract, expected scale, failure behavior, and recovery procedure. In multi-account AWS, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 44. **Question:** What is the main risk of **blue-green** in a lakehouse?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For blue-green, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 45. **Question:** How would you optimize **observability** in GitHub Actions?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For observability, document the input contract, expected scale, failure behavior, and recovery procedure. In GitHub Actions, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 46. **Question:** How would you test **build** in a regulated pipeline?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For build, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 47. **Question:** What production evidence validates **unit tests** in multi-account AWS?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For unit tests, document the input contract, expected scale, failure behavior, and recovery procedure. In multi-account AWS, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 48. **Question:** How do you make **integration tests** in a lakehouse?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For integration tests, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 49. **Question:** How would you explain **linting** in GitHub Actions?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For linting, document the input contract, expected scale, failure behavior, and recovery procedure. In GitHub Actions, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 50. **Question:** When would you choose **artifact versioning** in a regulated pipeline?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For artifact versioning, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
