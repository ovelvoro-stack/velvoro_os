from datetime import date

class CompanyPlan:
    def __init__(self, plan_type: str, trial_end: date | None = None):
        self.plan_type = plan_type  # "trial" or "paid"
        self.trial_end = trial_end

    def is_trial_expired(self) -> bool:
        if self.plan_type != "trial":
            return False
        if not self.trial_end:
            return False
        return date.today() > self.trial_end
