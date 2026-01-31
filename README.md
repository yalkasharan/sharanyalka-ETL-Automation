This template is designed for:
- Data Engineers
- Analytics Engineers
- BI & Reporting pipelines (Power BI, SQL, APIs)
- Automation-focused ETL workflows

---

## 🚀 Features

- Clean `extract / transform / load` separation
- Standard `src/` layout (production best practice)
- Built-in logging (console + per-run log files)
- Environment-based configuration (`dev / qa / prod`)
- Ready for scheduling (Task Scheduler, Airflow, CI)
- No Docker required

---

## 📁 Project Structure

```text
etl_project/
├── configs/
│   ├── base.yaml
│   ├── dev.yaml
│   ├── qa.yaml
│   └── prod.yaml
│
├── src/
│   └── etl_project/
│       ├── extract/
│       ├── transform/
│       ├── load/
│       ├── orchestration/
│       ├── quality/
│       └── utils/
│
├── tests/
├── logs/
├── reports/
└── run_etl.py
