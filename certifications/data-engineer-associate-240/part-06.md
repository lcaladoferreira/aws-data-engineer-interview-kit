# AWS Certified Data Engineer – Associate — 240 Original Practice Q&A — Part 6

Original study questions—not exam dumps or recalled exam content. Verify changing details against AWS documentation.

<!-- item -->
## 126. **Question:** How would you test **Glue** in a startup?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For Glue, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 127. **Question:** What production evidence validates **Redshift** in an enterprise?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For Redshift, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 128. **Question:** How do you make **EMR** in a regulated workload?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For EMR, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 129. **Question:** How would you explain **Athena** in a multi-account environment?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For Athena, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 130. **Question:** When would you choose **Kinesis** in a disaster-recovery design?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For Kinesis, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 131. **Question:** How would you troubleshoot **ingestion** in a startup?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For ingestion, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 132. **Question:** What is the main risk of **transformation** in an enterprise?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For transformation, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 133. **Question:** How would you optimize **orchestration** in a regulated workload?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For orchestration, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 134. **Question:** How would you test **data stores** in a multi-account environment?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For data stores, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 135. **Question:** What production evidence validates **operations** in a disaster-recovery design?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For operations, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 136. **Question:** How do you make **security** in a startup?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For security, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 137. **Question:** How would you explain **governance** in an enterprise?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For governance, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 138. **Question:** When would you choose **quality** in a regulated workload?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For quality, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 139. **Question:** How would you troubleshoot **Glue** in a multi-account environment?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For Glue, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 140. **Question:** What is the main risk of **Redshift** in a disaster-recovery design?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For Redshift, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 141. **Question:** How would you optimize **EMR** in a startup?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For EMR, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 142. **Question:** How would you test **Athena** in an enterprise?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For Athena, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 143. **Question:** What production evidence validates **Kinesis** in a regulated workload?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For Kinesis, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 144. **Question:** How do you make **ingestion** in a multi-account environment?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For ingestion, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 145. **Question:** How would you explain **transformation** in a disaster-recovery design?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For transformation, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 146. **Question:** When would you choose **orchestration** in a startup?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For orchestration, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 147. **Question:** How would you troubleshoot **data stores** in an enterprise?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For data stores, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 148. **Question:** What is the main risk of **operations** in a regulated workload?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For operations, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 149. **Question:** How would you optimize **security** in a multi-account environment?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For security, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 150. **Question:** How would you test **governance** in a disaster-recovery design?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For governance, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
