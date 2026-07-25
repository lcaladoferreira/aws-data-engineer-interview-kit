# AWS Solutions Architect – Associate — 1000 Original Practice Q&A — Part 6

Original study questions—not exam dumps or recalled exam content. Verify changing details against AWS documentation.

<!-- item -->
## 126. **Question:** How would you test **networking** in a startup?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For networking, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 127. **Question:** What production evidence validates **storage** in an enterprise?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For storage, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 128. **Question:** How do you make **databases** in a regulated workload?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For databases, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 129. **Question:** How would you explain **serverless** in a multi-account environment?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For serverless, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 130. **Question:** When would you choose **migration** in a disaster-recovery design?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For migration, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 131. **Question:** How would you troubleshoot **decoupling** in a startup?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For decoupling, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 132. **Question:** What is the main risk of **observability** in an enterprise?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For observability, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 133. **Question:** How would you optimize **resilience** in a regulated workload?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For resilience, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 134. **Question:** How would you test **performance** in a multi-account environment?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For performance, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 135. **Question:** What production evidence validates **security** in a disaster-recovery design?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For security, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 136. **Question:** How do you make **cost** in a startup?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For cost, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 137. **Question:** How would you explain **networking** in an enterprise?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For networking, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 138. **Question:** When would you choose **storage** in a regulated workload?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For storage, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 139. **Question:** How would you troubleshoot **databases** in a multi-account environment?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For databases, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 140. **Question:** What is the main risk of **serverless** in a disaster-recovery design?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For serverless, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 141. **Question:** How would you optimize **migration** in a startup?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For migration, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 142. **Question:** How would you test **decoupling** in an enterprise?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For decoupling, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 143. **Question:** What production evidence validates **observability** in a regulated workload?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For observability, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 144. **Question:** How do you make **resilience** in a multi-account environment?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For resilience, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 145. **Question:** How would you explain **performance** in a disaster-recovery design?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For performance, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 146. **Question:** When would you choose **security** in a startup?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For security, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 147. **Question:** How would you troubleshoot **cost** in an enterprise?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For cost, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 148. **Question:** What is the main risk of **networking** in a regulated workload?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For networking, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 149. **Question:** How would you optimize **storage** in a multi-account environment?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For storage, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 150. **Question:** How would you test **databases** in a disaster-recovery design?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For databases, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
