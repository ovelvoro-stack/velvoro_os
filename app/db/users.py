from app.db.excel_db import read_users_excel
from app.core.security import verify_password


def get_user_by_credentials(company_name: str, username: str, password: str):
    users = read_users_excel()
    for user in users:
        if (
            user["company_name"] == company_name
            and user["username"] == username
            and user["active_status"] == "active"
            and verify_password(password, user["password"])
        ):
            return user
    return None
