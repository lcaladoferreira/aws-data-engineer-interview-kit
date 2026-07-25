# AWS Solutions Architect – Associate — 1000 Original Practice Q&A — Part 32

Original study questions—not exam dumps or recalled exam content. Verify changing details against AWS documentation.

<!-- item -->
## 776. **Question:** How do you make **storage** in a startup?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For storage, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 777. **Question:** How would you explain **databases** in an enterprise?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For databases, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 778. **Question:** When would you choose **serverless** in a regulated workload?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For serverless, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 779. **Question:** How would you troubleshoot **migration** in a multi-account environment?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For migration, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 780. **Question:** What is the main risk of **decoupling** in a disaster-recovery design?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For decoupling, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 781. **Question:** How would you optimize **observability** in a startup?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For observability, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 782. **Question:** How would you test **resilience** in an enterprise?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For resilience, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 783. **Question:** What production evidence validates **performance** in a regulated workload?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For performance, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 784. **Question:** How do you make **security** in a multi-account environment?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For security, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 785. **Question:** How would you explain **cost** in a disaster-recovery design?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For cost, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 786. **Question:** When would you choose **networking** in a startup?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For networking, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 787. **Question:** How would you troubleshoot **storage** in an enterprise?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For storage, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 788. **Question:** What is the main risk of **databases** in a regulated workload?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For databases, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 789. **Question:** How would you optimize **serverless** in a multi-account environment?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For serverless, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 790. **Question:** How would you test **migration** in a disaster-recovery design?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For migration, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 791. **Question:** What production evidence validates **decoupling** in a startup?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For decoupling, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 792. **Question:** How do you make **observability** in an enterprise?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For observability, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 793. **Question:** How would you explain **resilience** in a regulated workload?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For resilience, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 794. **Question:** When would you choose **performance** in a multi-account environment?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For performance, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 795. **Question:** How would you troubleshoot **security** in a disaster-recovery design?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For security, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 796. **Question:** What is the main risk of **cost** in a startup?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For cost, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 797. **Question:** How would you optimize **networking** in an enterprise?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For networking, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 798. **Question:** How would you test **storage** in a regulated workload?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For storage, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 799. **Question:** What production evidence validates **databases** in a multi-account environment?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For databases, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 800. **Question:** How do you make **serverless** in a disaster-recovery design?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For serverless, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
