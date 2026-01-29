import pandas as pd

def export_excel(data, filename="report.xlsx"):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    return filename
