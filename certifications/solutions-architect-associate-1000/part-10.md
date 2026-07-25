# AWS Solutions Architect – Associate — 1000 Original Practice Q&A — Part 10

Original study questions—not exam dumps or recalled exam content. Verify changing details against AWS documentation.

<!-- item -->
## 226. **Question:** When would you choose **storage** in a startup?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For storage, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 227. **Question:** How would you troubleshoot **databases** in an enterprise?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For databases, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 228. **Question:** What is the main risk of **serverless** in a regulated workload?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For serverless, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 229. **Question:** How would you optimize **migration** in a multi-account environment?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For migration, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 230. **Question:** How would you test **decoupling** in a disaster-recovery design?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For decoupling, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 231. **Question:** What production evidence validates **observability** in a startup?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For observability, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 232. **Question:** How do you make **resilience** in an enterprise?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For resilience, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 233. **Question:** How would you explain **performance** in a regulated workload?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For performance, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 234. **Question:** When would you choose **security** in a multi-account environment?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For security, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 235. **Question:** How would you troubleshoot **cost** in a disaster-recovery design?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For cost, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 236. **Question:** What is the main risk of **networking** in a startup?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For networking, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 237. **Question:** How would you optimize **storage** in an enterprise?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For storage, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 238. **Question:** How would you test **databases** in a regulated workload?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For databases, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 239. **Question:** What production evidence validates **serverless** in a multi-account environment?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For serverless, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 240. **Question:** How do you make **migration** in a disaster-recovery design?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For migration, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 241. **Question:** How would you explain **decoupling** in a startup?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For decoupling, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 242. **Question:** When would you choose **observability** in an enterprise?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For observability, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 243. **Question:** How would you troubleshoot **resilience** in a regulated workload?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For resilience, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 244. **Question:** What is the main risk of **performance** in a multi-account environment?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For performance, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 245. **Question:** How would you optimize **security** in a disaster-recovery design?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For security, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 246. **Question:** How would you test **cost** in a startup?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For cost, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 247. **Question:** What production evidence validates **networking** in an enterprise?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For networking, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 248. **Question:** How do you make **storage** in a regulated workload?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For storage, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 249. **Question:** How would you explain **databases** in a multi-account environment?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For databases, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 250. **Question:** When would you choose **serverless** in a disaster-recovery design?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For serverless, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
