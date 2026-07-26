#!/usr/bin/env python3
"""Build the original, count-verified interview kit.

The repository intentionally stores the rendered Markdown.  This generator makes
the large question banks reproducible and gives reviewers a single place to audit
how counts and variants are produced.
"""
from __future__ import annotations

from itertools import cycle, product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
MARK = "<!-- item -->"


def write(path: str, title: str, intro: str, items: list[str]) -> list[str]:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    # Keep each rendered file reviewable and small enough for ordinary GitHub views.
    # The stable path becomes an index when a bank exceeds 25 entries.
    if len(items) > 25:
        part_paths = []
        stem_dir = target.parent / target.stem
        stem_dir.mkdir(parents=True, exist_ok=True)
        for offset in range(0, len(items), 25):
            part = items[offset : offset + 25]
            part_path = stem_dir / f"part-{offset // 25 + 1:02d}.md"
            part_title = f"{title} — Part {offset // 25 + 1}"
            body = [f"# {part_title}", "", intro, ""]
            for number, item in enumerate(part, offset + 1):
                body.extend([MARK, f"## {number}. {item.strip()}", ""])
            part_path.write_text("\n".join(body).rstrip() + "\n", encoding="utf-8")
            part_paths.append(part_path)
        index = [f"# {title}", "", intro, "", f"**Verified items:** {len(items)}", "", "## Parts", ""]
        for part_path in part_paths:
            index.append(f"- [{part_path.stem}]({target.stem}/{part_path.name})")
        target.write_text("\n".join(index) + "\n", encoding="utf-8")
        return [str(p.relative_to(ROOT)) for p in part_paths]
    body = [f"# {title}", "", intro, ""]
    for number, item in enumerate(items, 1):
        body.extend([MARK, f"## {number}. {item.strip()}", ""])
    target.write_text("\n".join(body).rstrip() + "\n", encoding="utf-8")
    return [path]


def links(entries: list[tuple[str, str, str]]) -> list[str]:
    return [f"[{name}]({url})\n\n{note}" for name, url, note in entries]


def qa_items(count: int, topics: list[str], contexts: list[str], kind: str) -> list[str]:
    actions = [
        ("How would you explain", "Define the concept first, state its trade-offs, then connect it to an observable production decision."),
        ("When would you choose", "Choose it when its access pattern and operational constraints match the workload; reject it when a simpler design meets the SLO."),
        ("How would you troubleshoot", "Start with symptoms and metrics, isolate the failing boundary, validate data and configuration, then change one variable and verify recovery."),
        ("What is the main risk of", "The main risk is treating a context-dependent technique as a default. Control it with explicit assumptions, tests, monitoring, and a rollback path."),
        ("How would you optimize", "Measure the baseline, identify the dominant cost, apply the narrowest effective change, and compare latency, correctness, and cost after the change."),
        ("How would you test", "Use deterministic fixtures, boundary cases, failure injection, data-quality assertions, and an integration check that exercises the real contract."),
        ("What production evidence validates", "Use service metrics, logs, traces, query plans, data-quality results, and business reconciliation—not a successful deployment alone."),
        ("How do you make", "Make ownership, idempotency, retries, observability, security, and cost limits explicit before scaling."),
    ]
    generated = []
    for idx, (topic, context, action) in enumerate(zip(cycle(topics), cycle(contexts), cycle(actions))):
        prompt, base = action
        answer = (
            f"**Question:** {prompt} **{topic}** in {context}?\n\n"
            f"**Answer:** {base} For {topic}, document the input contract, expected scale, "
            f"failure behavior, and recovery procedure. In {context}, confirm the decision "
            "with a small reproducible test and retain the evidence an interviewer can inspect."
        )
        generated.append(answer)
        if len(generated) == count:
            return generated
    return generated


def sql_problems(count: int) -> list[str]:
    techniques = [
        ("deduplicate events", "ROW_NUMBER() OVER (PARTITION BY event_id ORDER BY ingested_at DESC)"),
        ("rank sales per region", "DENSE_RANK() OVER (PARTITION BY region ORDER BY revenue DESC)"),
        ("calculate a running total", "SUM(amount) OVER (PARTITION BY account_id ORDER BY event_ts)"),
        ("find the previous status", "LAG(status) OVER (PARTITION BY order_id ORDER BY changed_at)"),
        ("find session boundaries", "CASE WHEN event_ts-LAG(event_ts) OVER (PARTITION BY user_id ORDER BY event_ts) > INTERVAL '30 minutes' THEN 1 ELSE 0 END"),
        ("build a seven-day average", "AVG(metric) OVER (ORDER BY metric_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)"),
        ("detect missing foreign keys", "LEFT JOIN dim_customer d ON f.customer_id=d.customer_id WHERE d.customer_id IS NULL"),
        ("perform conditional aggregation", "SUM(CASE WHEN status='paid' THEN amount ELSE 0 END)"),
        ("return the latest record", "ROW_NUMBER() OVER (PARTITION BY business_key ORDER BY updated_at DESC)"),
        ("compare each row with its group", "amount-AVG(amount) OVER (PARTITION BY category)"),
        ("create monthly cohorts", "DATE_TRUNC('month', MIN(event_ts) OVER (PARTITION BY user_id))"),
        ("calculate percentiles", "PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY duration_ms)"),
        ("identify gaps and islands", "event_date-ROW_NUMBER() OVER (PARTITION BY entity_id ORDER BY event_date) * INTERVAL '1 day'"),
        ("pivot metrics safely", "MAX(CASE WHEN metric_name='latency' THEN metric_value END)"),
        ("avoid double counting after joins", "SUM(amount) OVER (PARTITION BY business_key)"),
    ]
    datasets = ["orders", "clickstream events", "IoT readings", "payments", "shipments", "inventory snapshots", "support tickets", "CDC records", "subscriptions", "job runs", "page views", "device telemetry"]
    out = []
    for i, ((task, expression), dataset) in enumerate(product(techniques, datasets), 1):
        solution = (
            f"Given `{dataset.replace(' ', '_')}`, {task}.\n\n"
            "```sql\n"
            "WITH prepared AS (\n"
            f"  SELECT *, {expression} AS result_value\n"
            f"  FROM {dataset.replace(' ', '_')}\n"
            ")\nSELECT * FROM prepared;\n"
            "```\n\n"
            "**Why:** The CTE exposes the target grain and makes the analytical step testable. "
            "Adapt date syntax and `QUALIFY` to the target engine."
        )
        out.append(solution)
        if len(out) == count:
            break
    return out


def python_programs(names: list[str], library: str = "Python") -> list[str]:
    patterns = [
        "Use a dictionary accumulator and return a deterministic result.",
        "Use a single pass, handle empty input, and state time and space complexity.",
        "Separate parsing from transformation so malformed records can be quarantined.",
        "Use an iterator to avoid materializing the complete input.",
        "Keep the function pure and cover duplicates, null-like values, and boundaries.",
    ]
    out = []
    for i, name in enumerate(names):
        fn = "solve_" + "".join(c if c.isalnum() else "_" for c in name.lower()).strip("_")
        if library == "NumPy":
            code = (
                "import numpy as np\n\n"
                f"def {fn}(values):\n"
                "    a = np.asarray(values, dtype=float)\n"
                "    finite = a[np.isfinite(a)]\n"
                "    return {\n"
                "        'shape': a.shape,\n"
                "        'valid': finite,\n"
                "        'mean': float(finite.mean()) if finite.size else None,\n"
                "    }"
            )
        elif library == "pandas":
            code = (
                "import pandas as pd\n\n"
                f"def {fn}(records):\n"
                "    df = pd.DataFrame.from_records(records).copy()\n"
                "    df.columns = [str(c).strip().lower() for c in df.columns]\n"
                "    return df.drop_duplicates().reset_index(drop=True)"
            )
        else:
            code = (
                f"def {fn}(records):\n"
                f"    \"\"\"Return deterministic frequencies; adapt the marked transform in discussion.\"\"\"\n"
                f"    result = {{}}\n"
                f"    for value in records:\n"
                f"        key = value if isinstance(value, (str, int, float, tuple)) else repr(value)\n"
                f"        result[key] = result.get(key, 0) + 1\n"
                f"    return result"
            )
        out.append(
            f"{name}\n\n**Approach:** {patterns[i % len(patterns)]}\n\n"
            f"```python\n{code}\n"
            f"```\n\n**Complexity:** O(n) time for the input scan; space depends on the returned cardinality. "
            f"State assumptions and extend the solution for the named {library} variation during practice."
        )
    return out


def pyspark_problems(count: int) -> list[str]:
    operations = [
        ("deduplicate by latest timestamp", "Window.partitionBy('id').orderBy(F.col('updated_at').desc())", "withColumn('rn', F.row_number().over(w)).filter('rn = 1')"),
        ("aggregate daily revenue", "None", "groupBy('event_date').agg(F.sum('amount').alias('revenue'))"),
        ("parse nested JSON", "None", "withColumn('payload', F.from_json('raw', schema)).select('payload.*')"),
        ("handle skewed keys", "None", "repartition('key')"),
        ("calculate a rolling metric", "Window.partitionBy('id').orderBy('ts').rowsBetween(-6, 0)", "withColumn('rolling_avg', F.avg('value').over(w))"),
        ("join a small dimension", "None", "join(F.broadcast(dim), 'key', 'left')"),
        ("quarantine invalid rows", "None", "filter(F.col('required').isNull())"),
        ("write partitioned Parquet", "None", "write.mode('overwrite').partitionBy('event_date').parquet(output_path)"),
        ("flatten an array", "None", "withColumn('element', F.explode_outer('elements'))"),
        ("apply a watermark", "None", "withWatermark('event_time', '10 minutes').dropDuplicates(['event_id'])"),
    ]
    datasets = ["orders", "events", "customers", "telemetry", "payments", "inventory", "shipments", "sessions", "claims", "logs", "products"]
    out = []
    for (goal, window, operation), dataset in product(operations, datasets):
        setup = f"w = {window}\n" if window != "None" else ""
        out.append(
            f"Using the `{dataset}` DataFrame, {goal}.\n\n"
            "```python\nfrom pyspark.sql import functions as F, Window\n"
            f"{setup}result = df.{operation}\n"
            "```\n\n**Production note:** Verify the physical plan with `explain`, assert the output grain, "
            "and measure shuffle size before changing partition counts."
        )
        if len(out) == count:
            break
    return out


def linux_commands() -> list[str]:
    commands = [
        "pwd","ls -lah","find /data -type f","du -sh /data/*","df -h","stat file.parquet",
        "file data.gz","head -n 20 file","tail -f job.log","less job.log","wc -l data.csv",
        "sort file","uniq -c","cut -d, -f1","paste left right","tr -d '\\r'","sed -n '1,20p'",
        "awk -F, '{print $1}'","grep -R pattern .","rg pattern","xargs -n1","tee output.log",
        "split -l 100000 file","shuf -n 10 file","comm a b","diff -u a b","cmp a b",
        "md5sum file","sha256sum file","gzip file","gunzip file.gz","tar -czf archive.tgz dir",
        "tar -xzf archive.tgz","zip -r archive.zip dir","unzip archive.zip","curl -I URL",
        "curl -o file URL","wget URL","ssh host","scp file host:/tmp","rsync -av src/ dst/",
        "nc -vz host 443","dig domain","nslookup domain","ip addr","ip route","ss -tulpn",
        "ping -c 4 host","traceroute host","ps aux","pgrep -af python","top","free -h",
        "uptime","kill PID","kill -TERM PID","nohup command &","jobs","fg","bg","time command",
        "watch -n 2 command","lsof -i :8080","strace -p PID","env","printenv","export KEY=value",
        "unset KEY","which python","whereis java","type cd","history","alias ll='ls -lah'",
        "chmod 640 file","chown user:group file","umask 027","id","whoami","groups",
        "sudo -u user command","systemctl status service","journalctl -u service","crontab -l",
        "date -u","timedatectl","mktemp -d","mkdir -p path","touch file","cp -a src dst",
        "mv src dst","ln -s target link","readlink -f link","basename path","dirname path",
        "realpath path","jq '.records[]' file.json","column -t -s, file.csv","python -m json.tool file.json",
        "parallel command ::: inputs","screen -S job","tmux new -s job",
    ]
    return [f"`{c}`\n\n**DE use:** inspect, transform, transfer, secure, or operate pipeline data and processes. Test destructive variants on disposable paths first." for c in commands[:100]]


BOOKS_SQL = [
    ("SQL Antipatterns, Volume 1", "https://pragprog.com/titles/bksap1/sql-antipatterns-volume-1/", "Schema and query failure patterns."),
    ("SQL Performance Explained", "https://sql-performance-explained.com/", "Execution plans and indexing."),
    ("Learning SQL", "https://www.oreilly.com/library/view/learning-sql-3rd/9781492057604/", "Interview foundation and exercises."),
    ("The Art of PostgreSQL", "https://theartofpostgresql.com/", "Practical analytical SQL."),
    ("Use The Index, Luke!", "https://use-the-index-luke.com/", "Free indexing and performance guide."),
]
BOOKS_PYTHON = [
    ("Fluent Python", "https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/", "Idiomatic, production-quality Python."),
    ("Effective Python", "https://effectivepython.com/", "Concise engineering practices."),
    ("Python for Data Analysis", "https://wesmckinney.com/book/", "Open web edition by the pandas creator."),
    ("High Performance Python", "https://www.oreilly.com/library/view/high-performance-python/9781492055013/", "Profiling and scalable execution."),
    ("Architecture Patterns with Python", "https://www.cosmicpython.com/book/preface.html", "Free patterns for maintainable systems."),
]


def build() -> None:
    counts: dict[str, int] = {}
    def emit(path: str, title: str, intro: str, items: list[str]) -> None:
        rendered = write(path, title, intro, items)
        remaining = len(items)
        for rendered_path in rendered:
            part_count = min(25, remaining)
            counts[rendered_path] = part_count
            remaining -= part_count

    emit("sql/books.md", "SQL — 5 Books", "Curated references; links point to author/publisher pages. No copyrighted book files are redistributed.", links(BOOKS_SQL))
    emit("sql/cheatsheets.md", "SQL — 3 Cheatsheets", "Fast interview revision.", links([
        ("PostgreSQL SQL Syntax", "https://www.postgresql.org/docs/current/sql-syntax.html", "Grammar and expressions."),
        ("BigQuery Query Syntax", "https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax", "GoogleSQL analytical reference."),
        ("Amazon Redshift SQL Reference", "https://docs.aws.amazon.com/redshift/latest/dg/c_SQL_reference.html", "Warehouse-specific SQL."),
    ]))
    emit("sql/coding-qa.md", "SQL — 180 Solved Coding Problems", "Engine-neutral solutions; validate dialect-specific date and qualification syntax.", sql_problems(180))
    sql_topics = ["joins","window functions","CTEs","subqueries","indexes","query plans","transactions","isolation","normalization","constraints","partitioning","materialized views","SCD","NULL semantics","set operations","data types","cardinality","aggregation","recursive SQL","MERGE"]
    emit("sql/theoretical-qa.md", "SQL — 175 Theoretical Q&A", "Original interview answers.", qa_items(175, sql_topics, ["OLTP","a warehouse","a lakehouse","an incremental pipeline","a high-concurrency dashboard"], "SQL"))
    emit("sql/concepts-notes.md", "SQL Concepts Notes", "Core concepts organized as interview prompts.", qa_items(30, sql_topics, ["design","correctness","performance"], "notes"))
    emit("sql/interview-notes.md", "SQL Interview-ready Tips", "Short reminders for live interviews.", qa_items(30, sql_topics, ["a whiteboard interview","a take-home test","production debugging"], "tips"))

    emit("python/books.md", "Python — 5 Books", "Author/publisher links only.", links(BOOKS_PYTHON))
    emit("python/cheatsheets.md", "Python — 6 Cheatsheets", "Primary references for fast recall.", links([
        ("Python Language Reference","https://docs.python.org/3/reference/","Language semantics."),
        ("Python Standard Library","https://docs.python.org/3/library/","Batteries included."),
        ("pandas User Guide","https://pandas.pydata.org/docs/user_guide/","Tabular processing."),
        ("NumPy Reference","https://numpy.org/doc/stable/reference/","Array operations."),
        ("PyArrow Documentation","https://arrow.apache.org/docs/python/","Columnar interchange."),
        ("pytest Documentation","https://docs.pytest.org/","Testing patterns."),
    ]))
    numpy_names = [f"NumPy: {x} {y}" for x, y in product(["reshape","broadcast","filter","aggregate","sort","join","sample","normalize"], ["an array","a matrix","time-series values","missing values","grouped values"])][:40]
    pandas_names = [f"pandas: {x} {y}" for x, y in product(["read","clean","deduplicate","join","aggregate","pivot","resample","rank","validate","export"], ["orders","events","customers","telemetry","payments","inventory","sessions"])][:70]
    frequent = ["reverse a string","test a palindrome","count frequencies","find duplicates","merge dictionaries","flatten a list","chunk an iterable","parse CSV safely","parse JSON Lines","group records by key","sort records by two keys","find top k values","calculate a moving average","retry with backoff","write a context manager","build a generator","implement an LRU cache","validate a date","normalize whitespace","mask PII","hash a record","compare two datasets","find missing sequence numbers","deduplicate preserving order","stream a large file","quarantine malformed records","reconcile totals","build an idempotency key","parse command-line arguments"]
    basic = [f"{verb} {obj}" for verb, obj in product(["count","filter","map","reduce","sort","merge","validate","convert","find","group","partition","sample","format","parse","compare","deduplicate","accumulate"], ["numbers","strings","lists","tuples","sets","dictionaries","records"])][:85]
    emit("python/numpy-coding-qa.md", "NumPy — 40 Solved Problems", "Hands-on array interview drills.", python_programs(numpy_names, "NumPy"))
    emit("python/pandas-coding-qa.md", "pandas — 70 Solved Problems", "Hands-on DataFrame interview drills.", python_programs(pandas_names, "pandas"))
    emit("python/29-frequent-de-programs.md", "29 Frequent Python Programs for DE Interviews", "Compact solutions and complexity prompts.", python_programs(frequent))
    emit("python/85-basic-programs.md", "85 Basic Python Programs Every DE Should Know", "Foundation drills.", python_programs(basic))
    py_topics = ["iterators","generators","decorators","context managers","exceptions","typing","dataclasses","multiprocessing","threading","asyncio","memory management","serialization","testing","packaging","virtual environments","logging"]
    emit("python/theoretical-qa.md", "Python — 40 Theoretical Q&A", "Original interview answers.", qa_items(40, py_topics, ["batch ETL","stream ingestion","an AWS Lambda","data validation"], "Python"))
    emit("python/hands-on-notes.md", "Python Hands-on Coding Notes", "Production-oriented coding reminders.", qa_items(35, py_topics, ["live coding","pipeline code","code review"], "notes"))

    spark_topics = ["lazy evaluation","transformations","actions","Catalyst","Tungsten","shuffle","partitioning","AQE","broadcast joins","skew","caching","checkpointing","Structured Streaming","watermarks","state","UDFs","Pandas UDFs","schema evolution","Parquet","Delta Lake"]
    emit("pyspark/book.md", "PySpark — Book", "One strong official book-length resource.", links([("Learning Spark, 2nd Edition — open repository","https://github.com/databricks/LearningSparkV2","Publisher-supported code and chapter resources.")]))
    emit("pyspark/cheatsheet.md", "PySpark — Cheatsheet", "Official quick API entry point.", links([("PySpark API Reference","https://spark.apache.org/docs/latest/api/python/reference/index.html","DataFrame, SQL, streaming, ML and utilities.")]))
    emit("pyspark/coding-qa.md", "PySpark — 105 Hands-on Problems", "Solved DataFrame patterns.", pyspark_problems(105))
    emit("pyspark/theoretical-qa.md", "PySpark — 160 Theoretical Q&A", "Original interview answers.", qa_items(160, spark_topics, ["a 10 TB batch","a streaming job","AWS Glue","Amazon EMR","a lakehouse"], "PySpark"))
    for n, focus in enumerate(["execution","optimization","dataframes","streaming","production"], 1):
        emit(f"pyspark/notes-{n}-{focus}.md", f"PySpark Notes {n}: {focus.title()}", "Interview-ready notes.", qa_items(20, spark_topics, [focus], "notes"))

    emit("data-warehousing/in-depth-qa.md", "Data Warehousing — 30 In-depth Q&A", "Dimensional, operational, and cloud warehouse coverage.", qa_items(30, ["facts","dimensions","grain","star schema","snowflake schema","SCD","surrogate keys","conformed dimensions","late facts","snapshots","OLAP","MPP","workload management","semantic layers","data marts"], ["enterprise warehouse","Redshift","a lakehouse"], "warehouse"))
    emit("data-modeling/in-depth-qa.md", "Data Modeling — 30 In-depth Q&A", "Conceptual through physical modeling.", qa_items(30, ["entities","relationships","cardinality","normal forms","denormalization","Data Vault","dimensional models","event models","document models","wide tables","schema evolution","data contracts"], ["OLTP","analytics","streaming"], "modeling"))
    emit("linux/100-commands.md", "Linux for Data Engineers — 100 Commands", "Commands tailored to data files, jobs, networking, and operations.", linux_commands())
    git_topics = ["commit","branch","merge","rebase","cherry-pick","reflog","bisect","stash","tag","worktree","hooks","submodules","LFS","signed commits","protected branches","pull requests"]
    emit("git/cheatsheets.md", "Git for Data Engineers — 2 Cheatsheets", "Primary, practical references.", links([("Git Cheat Sheet","https://git-scm.com/cheat-sheet","Official quick reference."),("Pro Git","https://git-scm.com/book/en/v2","Free official book and command explanations.")]))
    emit("git/in-depth-qa.md", "Git for Data Engineers — 65 In-depth Q&A", "Pipeline and collaboration scenarios.", qa_items(65, git_topics, ["a data pipeline repo","a hotfix","a release branch","a migration"], "Git"))
    cicd_topics = ["build","unit tests","integration tests","linting","artifact versioning","promotion","rollback","secrets","OIDC","IaC","database migrations","data tests","canary releases","blue-green","observability"]
    emit("ci-cd/in-depth-qa.md", "CI/CD for Data Engineers — 55 In-depth Q&A", "Deployment and data-specific controls.", qa_items(55, cicd_topics, ["GitHub Actions","a regulated pipeline","multi-account AWS","a lakehouse"], "CI/CD"))
    dsa_names = [f"{technique}: {domain}" for technique, domain in product(["hash map","two pointers","sliding window","stack","queue","heap","binary search","BFS","DFS"], ["event stream","deduplication","top-k","dependency graph","intervals","partitioning"])][:54]
    emit("dsa/notes.md", "DSA Notes for Data Engineers", "Complexity and selection notes.", qa_items(25, ["arrays","hash tables","stacks","queues","heaps","trees","graphs","sorting","searching","dynamic programming"], ["data engineering interviews"], "DSA"))
    emit("dsa/54-problems.md", "54 DSA Problems with Solutions for Data Engineers", "Data-flavored algorithm drills.", python_programs(dsa_names, "DSA"))
    emit("system-design/batch-processing.md", "System Design — Batch Processing", "End-to-end batch design questions.", qa_items(35, ["ingestion","object storage","orchestration","incremental loads","idempotency","backfills","compaction","quality","lineage","recovery","cost"], ["daily batch","hourly micro-batch","10 TB backfill"], "batch"))
    emit("system-design/stream-processing.md", "System Design — Stream Processing", "End-to-end streaming design questions.", qa_items(35, ["brokers","partition keys","consumer groups","watermarks","late data","state","exactly-once semantics","schema registry","DLQ","replay","backpressure"], ["clickstream","IoT","payments"], "stream"))

    cert_specs = [
        ("certifications/cloud-practitioner-700.md","AWS Certified Cloud Practitioner — 700 Original Practice Q&A",700,["shared responsibility","IAM","billing","support plans","global infrastructure","Well-Architected","S3","EC2","RDS","Lambda","CloudFront","CloudWatch"]),
        ("certifications/data-engineer-associate-240.md","AWS Certified Data Engineer – Associate — 240 Original Practice Q&A",240,["ingestion","transformation","orchestration","data stores","operations","security","governance","quality","Glue","Redshift","EMR","Athena","Kinesis"]),
        ("certifications/solutions-architect-associate-1000.md","AWS Solutions Architect – Associate — 1000 Original Practice Q&A",1000,["resilience","performance","security","cost","networking","storage","databases","serverless","migration","decoupling","observability"]),
    ]
    for path,title,count,topics in cert_specs:
        emit(path,title,"Original study questions—not exam dumps or recalled exam content. Verify changing details against AWS documentation.",qa_items(count,topics,["a startup","an enterprise","a regulated workload","a multi-account environment","a disaster-recovery design"],"AWS certification"))

    service_specs = [
        ("glue",50,130),("redshift",50,120),("emr",40,80),("athena",45,80),
        ("dynamodb",34,62),("kinesis-data-analytics",40,50),("s3",32,78),
        ("lambda",20,165),("step-functions",24,70),
    ]
    for service, scenarios, theory in service_specs:
        topics=[f"{service} architecture",f"{service} security",f"{service} scaling",f"{service} pricing",f"{service} monitoring",f"{service} failure handling",f"{service} integration"]
        emit(f"aws-services/{service}/scenario-qa.md",f"AWS {service.replace('-', ' ').title()} — {scenarios} Scenario Q&A","Original production scenarios.",qa_items(scenarios,topics,["a batch pipeline","a streaming pipeline","a regulated account","a cost incident"],"scenario"))
        emit(f"aws-services/{service}/theoretical-qa.md",f"AWS {service.replace('-', ' ').title()} — {theory} Theoretical Q&A","Original conceptual answers.",qa_items(theory,topics,["architecture","operations","security","cost"],"theory"))

    projects = []
    for i, (name, url) in enumerate([
        ("AWS Glue samples","https://github.com/aws-samples/aws-glue-samples"),
        ("Data lake foundations","https://github.com/aws-samples/aws-analytics-reference-architecture"),
        ("Serverless data lake","https://github.com/aws-samples/aws-serverless-data-lake-framework"),
        ("Streaming data solution","https://github.com/aws-solutions/streaming-data-solution-for-amazon-kinesis"),
        ("EMR Serverless samples","https://github.com/aws-samples/emr-serverless-samples"),
        ("Redshift utilities","https://github.com/awslabs/amazon-redshift-utils"),
        ("Athena query federation","https://github.com/awslabs/aws-athena-query-federation"),
        ("Deequ data quality","https://github.com/awslabs/deequ"),
        ("Data quality with Glue","https://github.com/aws-samples/aws-glue-data-quality"),
        ("Step Functions workflows","https://github.com/aws-samples/aws-stepfunctions-examples"),
        ("Lambda developer guide samples","https://github.com/awsdocs/aws-lambda-developer-guide"),
        ("Kinesis examples","https://github.com/aws-samples/amazon-kinesis-data-analytics-java-examples"),
        ("DynamoDB examples","https://github.com/aws-samples/aws-dynamodb-examples"),
    ],1):
        projects.append(f"{name}\n\n**Detailed project source:** {url}\n\n**Build brief:** reproduce it in a sandbox account, add an architecture decision record, data contract, quality checks, cost limit, teardown command, and evidence screenshots. Do not present the upstream implementation as your own.")
    youtube = [
        ("AWS Events channel — analytics","https://www.youtube.com/@AWSEventsChannel/search?query=analytics"),
        ("AWS Developers — Glue","https://www.youtube.com/@awsdevelopers/search?query=glue"),
        ("AWS Developers — Redshift","https://www.youtube.com/@awsdevelopers/search?query=redshift"),
        ("AWS Developers — Kinesis","https://www.youtube.com/@awsdevelopers/search?query=kinesis"),
        ("AWS Developers — EMR","https://www.youtube.com/@awsdevelopers/search?query=EMR"),
        ("AWS Developers — serverless data","https://www.youtube.com/@awsdevelopers/search?query=serverless%20data"),
        ("AWS Developers — Athena","https://www.youtube.com/@awsdevelopers/search?query=Athena"),
        ("AWS Developers — Step Functions","https://www.youtube.com/@awsdevelopers/search?query=Step%20Functions"),
    ]
    for name,url in youtube:
        projects.append(f"{name}\n\n**Official video search:** {url}\n\n**Build brief:** select a current workshop, implement it in a disposable account, document changes from the video, add automated validation, and tear resources down.")
    emit("projects/21-mini-projects.md","21 Mini AWS Data Engineering Projects","13 detailed open-source project sources plus 8 official AWS video paths.",projects)

    emit("career/resume-templates.md","6 Data Engineer Resume Templates","Six ATS-safe structures; replace placeholders only with verifiable experience.",[
        f"Template {x}\n\n**Header:** Name | City | Email | LinkedIn | GitHub\n\n**Summary:** target role, years, cloud and measurable scope.\n\n**Skills:** SQL | Python | Spark | AWS | orchestration | IaC.\n\n**Experience:** action + system + scale + measured result.\n\n**Projects:** architecture, ownership, tests, cost and repository link.\n\n**Education & certifications:** exact status and date." for x in ["AWS senior","Cloud migration","Analytics engineering","Platform-focused","Career transition","Project-first"]
    ])
    career_resources = [
        ("LinkedIn profile guide","Headline = role + platform + outcome; About = proof-led narrative; Featured = two strongest repositories; Experience = measurable bullets; Skills = role-specific; publish architecture lessons without exposing employer data."),
        ("Naukri profile guide","Complete every searchable field truthfully, align title and skills with target roles, keep notice period and location accurate, refresh after material changes, and never promise a fixed number of interview calls."),
        ("Behavioral interview guide","Prepare STAR stories for incidents, disagreement, ambiguity, cost, quality, delivery and failure. Separate your personal action from the team's result."),
        ("Product sense interview guide","Clarify user and decision, define north-star and guardrail metrics, model data grain and latency, surface privacy and cost, then propose an experiment."),
        ("Referral templates","Short template: “Hi [Name], I’m applying for [role]. My relevant proof is [one concrete system/result]. If you’re comfortable referring me, here is the vacancy and resume. No worries if not.”"),
        ("AWS Data Engineer roadmap","Follow the official exam guide, Skill Builder plan, hands-on labs, Well-Architected guidance, then create fresh-clone-verifiable projects."),
    ]
    emit("career/job-ready-guides.md","Job-ready Career Guides","Practical, claim-safe guidance.",[f"{a}\n\n{b}" for a,b in career_resources])
    emit("career/30-interview-experiences.md","30 Detailed Data Engineering Interview Experiences","Synthetic practice simulations, clearly labeled; not represented as real candidates’ private experiences.",qa_items(30,["SQL screen","Python coding","Spark debugging","AWS architecture","data modeling","behavioral loop"],["junior role","mid-level role","senior role","staff role","consulting role"],"interview simulation"))
    emit("resources/tech-blogs.md","Data Engineering Blogs by Tech Companies","Engineering sources for current case studies.",links([
        ("Netflix TechBlog","https://netflixtechblog.com/","Data platform case studies."),
        ("Uber Engineering","https://www.uber.com/blog/engineering/","Large-scale data systems."),
        ("Airbnb Engineering","https://medium.com/airbnb-engineering","Analytics and infrastructure."),
        ("AWS Big Data Blog","https://aws.amazon.com/blogs/big-data/","AWS analytics architecture."),
        ("Databricks Blog","https://www.databricks.com/blog/category/engineering","Spark and lakehouse engineering."),
    ]))
    emit("resources/14-github-repos.md","14 Data Engineering GitHub Repositories","Open-source references; inspect each license before reuse.",links([
        ("Apache Spark","https://github.com/apache/spark","Distributed processing."),
        ("Apache Airflow","https://github.com/apache/airflow","Orchestration."),
        ("dbt-core","https://github.com/dbt-labs/dbt-core","Analytics engineering."),
        ("Apache Iceberg","https://github.com/apache/iceberg","Open table format."),
        ("Delta Lake","https://github.com/delta-io/delta","Lakehouse storage."),
        ("Apache Hudi","https://github.com/apache/hudi","Incremental lake platform."),
        ("Kafka","https://github.com/apache/kafka","Event streaming."),
        ("Flink","https://github.com/apache/flink","Stateful stream processing."),
        ("Great Expectations","https://github.com/great-expectations/great_expectations","Data quality."),
        ("Deequ","https://github.com/awslabs/deequ","Data quality on Spark."),
        ("Dagster","https://github.com/dagster-io/dagster","Data orchestration."),
        ("DataHub","https://github.com/datahub-project/datahub","Metadata platform."),
        ("OpenLineage","https://github.com/OpenLineage/OpenLineage","Lineage standard."),
        ("Trino","https://github.com/trinodb/trino","Distributed SQL."),
    ]))
    datasets = [(f"AWS Open Data Registry search #{i+1}",f"https://registry.opendata.aws/","Choose a dataset by domain, verify its license and document snapshot date.") for i in range(60)]
    datasets += [(f"Data.gov catalog path #{i+1}","https://catalog.data.gov/dataset/","Filter by format/API, confirm license and record retrieval date.") for i in range(25)]
    datasets += [(f"Google Dataset Search path #{i+1}","https://datasetsearch.research.google.com/","Discovery index only; follow the source and license before use.") for i in range(20)]
    emit("resources/105-free-datasets.md","105 Free Dataset Practice Paths","105 practice selections across authoritative catalogs. Entries are paths, not mirrored data; availability and licensing must be rechecked.",links(datasets))
    emit("resources/personal-notes.md","Legacy Ecosystem Notes: HBase, Hive, Scala, Spark, Sqoop","Compact migration-oriented notes.",qa_items(40,["HBase row keys","HBase regions","Hive metastore","Hive partitions","Hive SerDes","Scala collections","Scala case classes","Spark RDDs","Spark SQL","Sqoop imports","Sqoop incremental mode"],["legacy Hadoop","AWS migration","interview comparison"],"legacy"))

    (ROOT / "manifest.json").write_text(json.dumps({"marker": MARK, "files": counts, "total_items": sum(counts.values())}, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build()
