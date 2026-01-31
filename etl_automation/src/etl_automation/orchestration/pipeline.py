from etl_automation.extract.salesforce import extract_salesforce
from etl_automation.transform.business_rules import apply_business_rules
from etl_automation.load.data_warehouse import load_to_warehouse

def run():
    data = extract_salesforce()
    data = apply_business_rules(data)
    load_to_warehouse(data)
