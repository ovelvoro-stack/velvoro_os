from datetime import date, timedelta
from app.billing.models import CompanyPlan

# SAFE default — does not block existing users
def get_company_plan(company_name: str) -> CompanyPlan:
    # Trial valid for 14 days (example default)
    return CompanyPlan(
        plan_type="trial",
        trial_end=date.today() + timedelta(days=14)
    )
