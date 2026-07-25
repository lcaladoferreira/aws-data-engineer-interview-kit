# AWS Certified Cloud Practitioner — 700 Original Practice Q&A — Part 15

Original study questions—not exam dumps or recalled exam content. Verify changing details against AWS documentation.

<!-- item -->
## 351. **Question:** What production evidence validates **billing** in a startup?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For billing, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 352. **Question:** How do you make **support plans** in an enterprise?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For support plans, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 353. **Question:** How would you explain **global infrastructure** in a regulated workload?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For global infrastructure, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 354. **Question:** When would you choose **Well-Architected** in a multi-account environment?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For Well-Architected, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 355. **Question:** How would you troubleshoot **S3** in a disaster-recovery design?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For S3, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 356. **Question:** What is the main risk of **EC2** in a startup?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For EC2, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 357. **Question:** How would you optimize **RDS** in an enterprise?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For RDS, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 358. **Question:** How would you test **Lambda** in a regulated workload?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For Lambda, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 359. **Question:** What production evidence validates **CloudFront** in a multi-account environment?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For CloudFront, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 360. **Question:** How do you make **CloudWatch** in a disaster-recovery design?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For CloudWatch, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 361. **Question:** How would you explain **shared responsibility** in a startup?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For shared responsibility, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 362. **Question:** When would you choose **IAM** in an enterprise?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For IAM, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 363. **Question:** How would you troubleshoot **billing** in a regulated workload?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For billing, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 364. **Question:** What is the main risk of **support plans** in a multi-account environment?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For support plans, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 365. **Question:** How would you optimize **global infrastructure** in a disaster-recovery design?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For global infrastructure, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 366. **Question:** How would you test **Well-Architected** in a startup?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For Well-Architected, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 367. **Question:** What production evidence validates **S3** in an enterprise?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For S3, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 368. **Question:** How do you make **EC2** in a regulated workload?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For EC2, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 369. **Question:** How would you explain **RDS** in a multi-account environment?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For RDS, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 370. **Question:** When would you choose **Lambda** in a disaster-recovery design?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For Lambda, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 371. **Question:** How would you troubleshoot **CloudFront** in a startup?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For CloudFront, document the input contract, expected scale, failure behavior, and recovery procedure. In a startup, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 372. **Question:** What is the main risk of **CloudWatch** in an enterprise?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For CloudWatch, document the input contract, expected scale, failure behavior, and recovery procedure. In an enterprise, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 373. **Question:** How would you optimize **shared responsibility** in a regulated workload?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For shared responsibility, document the input contract, expected scale, failure behavior, and recovery procedure. In a regulated workload, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 374. **Question:** How would you test **IAM** in a multi-account environment?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For IAM, document the input contract, expected scale, failure behavior, and recovery procedure. In a multi-account environment, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 375. **Question:** What production evidence validates **billing** in a disaster-recovery design?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For billing, document the input contract, expected scale, failure behavior, and recovery procedure. In a disaster-recovery design, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
