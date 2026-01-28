def get_company_plan(company):
    plans = {
        "Velvoro": "active",
        "AcmeCorp": "trial"
    }
    return plans.get(company, "expired")
