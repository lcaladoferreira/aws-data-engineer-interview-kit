# AWS Data Engineer Interview Kit

An open, count-verified study repository for data-engineering interviews and AWS certification preparation.

> **4,868 indexed learning items across 226 count-verified content parts.** Every published count is checked by `tools/verify_counts.py`; the source of truth is `manifest.json`.

## What is inside

| Area | Verified coverage |
|---|---|
| SQL | 5 books, 3 cheatsheets, 180 solved coding problems, concepts notes, interview tips, 175 theoretical Q&A |
| Python | 5 books, 6 cheatsheets, 40 NumPy problems, 70 pandas problems, 29 frequent DE programs, 85 fundamentals, hands-on notes, 40 theoretical Q&A |
| PySpark | 1 book, 1 cheatsheet, 105 hands-on problems, 5 note sets, 160 theoretical Q&A |
| Warehousing & modeling | 30 warehousing Q&A and 30 modeling Q&A |
| Linux, Git & CI/CD | 100 Linux commands, 2 Git cheatsheets, 65 Git Q&A, 55 CI/CD Q&A |
| DSA & system design | DSA notes, 54 solved problems, batch and streaming design guides |
| AWS certification practice | Cloud Practitioner 700, Data Engineer Associate 240, Solutions Architect Associate 1,000 |
| AWS services | 1,170 scenario and theoretical Q&A across Glue, Redshift, EMR, Athena, DynamoDB, Kinesis Data Analytics, S3, Lambda and Step Functions |
| Projects & career | 21 project paths, 6 resume templates, job-ready guides, 30 interview simulations |
| Further practice | Tech blogs, 14 repositories, legacy notes, 105 free-dataset practice paths |

## Start here

- [SQL](sql/) · [Python](python/) · [PySpark](pyspark/)
- [Data warehousing](data-warehousing/) · [Data modeling](data-modeling/)
- [Linux](linux/) · [Git](git/) · [CI/CD](ci-cd/) · [DSA](dsa/)
- [Batch and stream system design](system-design/)
- [AWS certifications](certifications/) · [AWS services](aws-services/)
- [21 mini-projects](projects/21-mini-projects.md)
- [Career resources](career/) · [Datasets and references](resources/)

## Recommended study loop

1. Read one concept or service file.
2. Answer each question aloud before revealing the answer.
3. Run or adapt coding examples in a disposable environment.
4. Build one mini-project and retain reproducible evidence.
5. Revisit missed questions after 1, 3, 7 and 14 days.

## Verify the repository

```bash
python tools/verify_counts.py
python -m compileall -q tools
```

Expected count check:

```text
PASS: 226 files, 4868 count-verified items
```

## Content policy

- Questions and explanations in this repository are original study material.
- Certification sections are **not exam dumps** and do not contain recalled live-exam questions.
- “Books” are curated recommendations linking to legitimate author, publisher or official pages; copyrighted books are not redistributed.
- External projects, videos, datasets and repositories remain the work of their respective owners. Check each license and current documentation before reuse.
- AWS products and exam blueprints change. Use the linked official documentation as the final authority.

## Scope and license

Code and original prose are provided under the [MIT License](LICENSE). External links and names do not transfer ownership of third-party material. AWS and service names are trademarks of Amazon.com, Inc. or its affiliates.
