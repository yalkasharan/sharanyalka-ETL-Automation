from {{ cookiecutter.project_slug }}.extract.salesforce import extract_salesforce
from {{ cookiecutter.project_slug }}.transform.business_rules import apply_business_rules
from {{ cookiecutter.project_slug }}.load.data_warehouse import load_to_warehouse

def run():
    data = extract_salesforce()
    data = apply_business_rules(data)
    load_to_warehouse(data)
