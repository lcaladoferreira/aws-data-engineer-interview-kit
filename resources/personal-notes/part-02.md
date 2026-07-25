# Legacy Ecosystem Notes: HBase, Hive, Scala, Spark, Sqoop — Part 2

Compact migration-oriented notes.

<!-- item -->
## 26. **Question:** When would you choose **Hive partitions** in AWS migration?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For Hive partitions, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS migration, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 27. **Question:** How would you troubleshoot **Hive SerDes** in interview comparison?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For Hive SerDes, document the input contract, expected scale, failure behavior, and recovery procedure. In interview comparison, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 28. **Question:** What is the main risk of **Scala collections** in legacy Hadoop?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For Scala collections, document the input contract, expected scale, failure behavior, and recovery procedure. In legacy Hadoop, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 29. **Question:** How would you optimize **Scala case classes** in AWS migration?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For Scala case classes, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS migration, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 30. **Question:** How would you test **Spark RDDs** in interview comparison?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For Spark RDDs, document the input contract, expected scale, failure behavior, and recovery procedure. In interview comparison, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 31. **Question:** What production evidence validates **Spark SQL** in legacy Hadoop?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For Spark SQL, document the input contract, expected scale, failure behavior, and recovery procedure. In legacy Hadoop, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 32. **Question:** How do you make **Sqoop imports** in AWS migration?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For Sqoop imports, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS migration, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 33. **Question:** How would you explain **Sqoop incremental mode** in interview comparison?

**Answer:** Define the concept first, state its trade-offs, then connect it to an observable production decision. For Sqoop incremental mode, document the input contract, expected scale, failure behavior, and recovery procedure. In interview comparison, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 34. **Question:** When would you choose **HBase row keys** in legacy Hadoop?

**Answer:** Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO. For HBase row keys, document the input contract, expected scale, failure behavior, and recovery procedure. In legacy Hadoop, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 35. **Question:** How would you troubleshoot **HBase regions** in AWS migration?

**Answer:** Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery. For HBase regions, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS migration, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 36. **Question:** What is the main risk of **Hive metastore** in interview comparison?

**Answer:** The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path. For Hive metastore, document the input contract, expected scale, failure behavior, and recovery procedure. In interview comparison, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 37. **Question:** How would you optimize **Hive partitions** in legacy Hadoop?

**Answer:** Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change. For Hive partitions, document the input contract, expected scale, failure behavior, and recovery procedure. In legacy Hadoop, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 38. **Question:** How would you test **Hive SerDes** in AWS migration?

**Answer:** Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract. For Hive SerDes, document the input contract, expected scale, failure behavior, and recovery procedure. In AWS migration, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 39. **Question:** What production evidence validates **Scala collections** in interview comparison?

**Answer:** Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone. For Scala collections, document the input contract, expected scale, failure behavior, and recovery procedure. In interview comparison, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.

<!-- item -->
## 40. **Question:** How do you make **Scala case classes** in legacy Hadoop?

**Answer:** Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling. For Scala case classes, document the input contract, expected scale, failure behavior, and recovery procedure. In legacy Hadoop, confirm the decision with a small reproducible test and retain the evidence an interviewer can inspect.
