**Project Description**

This project implements a modular, production-ready ETL pipeline using Python. It extracts data from multiple source systems, applies standardized business transformations and data quality checks, and loads curated data into downstream analytical platforms for reporting and decision-making.

The project follows a clean, scalable architecture with clear separation between extract, transform, load, orchestration, and utilities, making it easy to maintain, test, and automate across environments (dev, QA, prod).

---

## Project Structure

The directory structure of the project looks like this:

etl_project/
├── .github/                         # GitHub automation
│   ├── dependabot.yaml              # Dependency updates
│   └── workflows/
│       └── tests.yaml               # CI tests (pytest, linting)
│
├── configs/                         # Configuration files
│   ├── base.yaml                    # Shared config
│   ├── dev.yaml                     # Dev overrides
│   ├── qa.yaml                      # QA overrides
│   └── prod.yaml                    # Prod overrides
│
├── data/                            # Local data (optional, ignored in prod)
│   ├── raw/                         # Raw extracted data
│   └── processed/                   # Transformed data
│
├── docs/                            # Documentation
│   ├── README.md                    # High-level docs
│   └── architecture.md              # ETL architecture & flow
│
├── notebooks/                       # Exploration / debugging notebooks
│
├── reports/                         # Outputs / reports
│   └── figures/
│
├── logs/                            # Runtime logs (gitignored)
│
├── src/                             # Source code (src layout)
│   └── etl_project/
│       ├── __init__.py
│       │
│       ├── extract/                 # Data ingestion
│       │   ├── __init__.py
│       │   ├── salesforce.py
│       │   └── database.py
│       │
│       ├── transform/               # Business logic
│       │   ├── __init__.py
│       │   └── business_rules.py
│       │
│       ├── load/                    # Data persistence
│       │   ├── __init__.py
│       │   └── data_warehouse.py
│       │
│       ├── quality/                 # Data quality checks
│       │   ├── __init__.py
│       │   └── validations.py
│       │
│       ├── orchestration/           # Pipeline control
│       │   ├── __init__.py
│       │   └── pipeline.py
│       │
│       └── utils/                   # Shared utilities
│           ├── __init__.py
│           ├── logger.py
│           └── config_loader.py
│
├── tests/                           # Automated tests
│   ├── __init__.py
│   ├── test_extract.py
│   ├── test_transform.py
│   ├── test_load.py
│   └── test_pipeline.py
│
├── .gitignore
├── .pre-commit-config.yaml          # Formatting & lint hooks
├── pyproject.toml                   # Python dependencies & tooling
├── README.md                        # MAIN project README (GitHub front)
├── run_etl.py                       # Entry point
└── tasks.py                         # Task runner (optional)

