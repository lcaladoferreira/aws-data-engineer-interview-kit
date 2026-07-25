# Legacy Ecosystem Notes: HBase, Hive, Scala, Spark, Sqoop — Part 1

Compact migration-oriented notes.

<!-- item -->
## 1. **Question:** How would you explain **HBase row keys** in legacy Hadoop?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For HBase row keys, document the input contract, expected scale, failure behavior, and recovery procedure. In legacy Hadoop, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 2. **Question:** When would you choose **HBase regions** in AWS migration?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For HBase regions, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS migration, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 3. **Question:** How would you troubleshoot **Hive metastore** in interview comparison?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For Hive metastore, document the input contract, expected scale, failure behavior, and recovery procedure. In interview comparison, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 4. **Question:** What is the main risk of **Hive partitions** in legacy Hadoop?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For Hive partitions, document the input contract, expected scale, failure behavior, and recovery procedure. In legacy Hadoop, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 5. **Question:** How would you optimize **Hive SerDes** in AWS migration?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For Hive SerDes, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS migration, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 6. **Question:** How would you test **Scala collections** in interview comparison?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For Scala collections, document the input contract, expected scale, failure behavior, and recovery procedure. In interview comparison, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 7. **Question:** What production evidence validates **Scala case classes** in legacy Hadoop?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For Scala case classes, document the input contract, expected scale, failure behavior, and recovery procedure. In legacy Hadoop, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 8. **Question:** How do you make **Spark RDDs** in AWS migration?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For Spark RDDs, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS migration, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 9. **Question:** How would you explain **Spark SQL** in interview comparison?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For Spark SQL, document the input contract, expected scale, failure behavior, and recovery procedure. In interview comparison, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 10. **Question:** When would you choose **Sqoop imports** in legacy Hadoop?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For Sqoop imports, document the input contract, expected scale, failure behavior, and recovery procedure. In legacy Hadoop, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 11. **Question:** How would you troubleshoot **Sqoop incremental mode** in AWS migration?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For Sqoop incremental mode, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS migration, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 12. **Question:** What is the main risk of **HBase row keys** in interview comparison?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For HBase row keys, document the input contract, expected scale, failure behavior, and recovery procedure. In interview comparison, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 13. **Question:** How would you optimize **HBase regions** in legacy Hadoop?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For HBase regions, document the input contract, expected scale, failure behavior, and recovery procedure. In legacy Hadoop, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 14. **Question:** How would you test **Hive metastore** in AWS migration?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For Hive metastore, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS migration, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 15. **Question:** What production evidence validates **Hive partitions** in interview comparison?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For Hive partitions, document the input contract, expected scale, failure behavior, and recovery procedure. In interview comparison, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 16. **Question:** How do you make **Hive SerDes** in legacy Hadoop?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For Hive SerDes, document the input contract, expected scale, failure behavior, and recovery procedure. In legacy Hadoop, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 17. **Question:** How would you explain **Scala collections** in AWS migration?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For Scala collections, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS migration, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 18. **Question:** When would you choose **Scala case classes** in interview comparison?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For Scala case classes, document the input contract, expected scale, failure behavior, and recovery procedure. In interview comparison, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 19. **Question:** How would you troubleshoot **Spark RDDs** in legacy Hadoop?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For Spark RDDs, document the input contract, expected scale, failure behavior, and recovery procedure. In legacy Hadoop, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 20. **Question:** What is the main risk of **Spark SQL** in AWS migration?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For Spark SQL, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS migration, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 21. **Question:** How would you optimize **Sqoop imports** in interview comparison?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For Sqoop imports, document the input contract, expected scale, failure behavior, and recovery procedure. In interview comparison, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 22. **Question:** How would you test **Sqoop incremental mode** in legacy Hadoop?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For Sqoop incremental mode, document the input contract, expected scale, failure behavior, and recovery procedure. In legacy Hadoop, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 23. **Question:** What production evidence validates **HBase row keys** in AWS migration?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For HBase row keys, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS migration, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 24. **Question:** How do you make **HBase regions** in interview comparison?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For HBase regions, document the input contract, expected scale, failure behavior, and recovery procedure. In interview comparison, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 25. **Question:** How would you explain **Hive metastore** in legacy Hadoop?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For Hive metastore, document the input contract, expected scale, failure behavior, and recovery procedure. In legacy Hadoop, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
