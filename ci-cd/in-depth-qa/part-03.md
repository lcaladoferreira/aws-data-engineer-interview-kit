# CI/CD for Data Engineers — 55 In-depth Q&A — Part 3

Deployment and data-specific controls.

<!-- item -->
## 51. **Question:** How would you troubleshoot **promotion** in multi-account AWS?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For promotion, document the input contract, expected scale, failure behavior, and recovery procedure. In multi-account AWS, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 52. **Question:** What is the main risk of **rollback** in a lakehouse?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For rollback, document the input contract, expected scale, failure behavior, and recovery procedure. In a lakehouse, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 53. **Question:** How would you optimize **secrets** in GitHub Actions?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For secrets, document the input contract, expected scale, failure behavior, and recovery procedure. In GitHub Actions, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 54. **Question:** How would you test **OIDC** in a regulated pipeline?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For OIDC, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated pipeline, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 55. **Question:** What production evidence validates **IaC** in multi-account AWS?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For IaC, document the input contract, expected scale, failure behavior, and recovery procedure. In multi-account AWS, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
