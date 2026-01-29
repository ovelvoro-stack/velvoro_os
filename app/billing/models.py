from dataclasses import dataclass
from typing import Optional


@dataclass
class CompanyPlan:
    company_id: str
    plan_name: str          # trial / starter / pro / enterprise
    status: str             # active / inactive / expired
    expires_on: Optional[str] = None


@dataclass
class BillingRecord:
    company_id: str
    amount: float
    currency: str
    status: str             # success / failed / pending
    reference_id: str
