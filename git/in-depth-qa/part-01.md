# Git for Data Engineers — 65 In-depth Q&A — Part 1

Pipeline and collaboration scenarios.

<!-- item -->
## 1. **Question:** How would you explain **commit** in a data pipeline repo?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For commit, document the input contract, expected scale, failure behavior, and recovery procedure. In a data pipeline repo, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 2. **Question:** When would you choose **branch** in a hotfix?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For branch, document the input contract, expected scale, failure behavior, and recovery procedure. In a hotfix, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 3. **Question:** How would you troubleshoot **merge** in a release branch?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For merge, document the input contract, expected scale, failure behavior, and recovery procedure. In a release branch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 4. **Question:** What is the main risk of **rebase** in a migration?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For rebase, document the input contract, expected scale, failure behavior, and recovery procedure. In a migration, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 5. **Question:** How would you optimize **cherry-pick** in a data pipeline repo?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For cherry-pick, document the input contract, expected scale, failure behavior, and recovery procedure. In a data pipeline repo, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 6. **Question:** How would you test **reflog** in a hotfix?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For reflog, document the input contract, expected scale, failure behavior, and recovery procedure. In a hotfix, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 7. **Question:** What production evidence validates **bisect** in a release branch?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For bisect, document the input contract, expected scale, failure behavior, and recovery procedure. In a release branch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 8. **Question:** How do you make **stash** in a migration?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For stash, document the input contract, expected scale, failure behavior, and recovery procedure. In a migration, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 9. **Question:** How would you explain **tag** in a data pipeline repo?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For tag, document the input contract, expected scale, failure behavior, and recovery procedure. In a data pipeline repo, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 10. **Question:** When would you choose **worktree** in a hotfix?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For worktree, document the input contract, expected scale, failure behavior, and recovery procedure. In a hotfix, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 11. **Question:** How would you troubleshoot **hooks** in a release branch?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For hooks, document the input contract, expected scale, failure behavior, and recovery procedure. In a release branch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 12. **Question:** What is the main risk of **submodules** in a migration?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For submodules, document the input contract, expected scale, failure behavior, and recovery procedure. In a migration, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 13. **Question:** How would you optimize **LFS** in a data pipeline repo?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For LFS, document the input contract, expected scale, failure behavior, and recovery procedure. In a data pipeline repo, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 14. **Question:** How would you test **signed commits** in a hotfix?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For signed commits, document the input contract, expected scale, failure behavior, and recovery procedure. In a hotfix, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 15. **Question:** What production evidence validates **protected branches** in a release branch?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For protected branches, document the input contract, expected scale, failure behavior, and recovery procedure. In a release branch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 16. **Question:** How do you make **pull requests** in a migration?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For pull requests, document the input contract, expected scale, failure behavior, and recovery procedure. In a migration, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 17. **Question:** How would you explain **commit** in a data pipeline repo?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For commit, document the input contract, expected scale, failure behavior, and recovery procedure. In a data pipeline repo, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 18. **Question:** When would you choose **branch** in a hotfix?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For branch, document the input contract, expected scale, failure behavior, and recovery procedure. In a hotfix, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 19. **Question:** How would you troubleshoot **merge** in a release branch?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For merge, document the input contract, expected scale, failure behavior, and recovery procedure. In a release branch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 20. **Question:** What is the main risk of **rebase** in a migration?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For rebase, document the input contract, expected scale, failure behavior, and recovery procedure. In a migration, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 21. **Question:** How would you optimize **cherry-pick** in a data pipeline repo?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For cherry-pick, document the input contract, expected scale, failure behavior, and recovery procedure. In a data pipeline repo, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 22. **Question:** How would you test **reflog** in a hotfix?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For reflog, document the input contract, expected scale, failure behavior, and recovery procedure. In a hotfix, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 23. **Question:** What production evidence validates **bisect** in a release branch?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For bisect, document the input contract, expected scale, failure behavior, and recovery procedure. In a release branch, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 24. **Question:** How do you make **stash** in a migration?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For stash, document the input contract, expected scale, failure behavior, and recovery procedure. In a migration, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 25. **Question:** How would you explain **tag** in a data pipeline repo?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For tag, document the input contract, expected scale, failure behavior, and recovery procedure. In a data pipeline repo, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
