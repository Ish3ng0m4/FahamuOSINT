import pandas as pd
from rich import print

def export_results(data, filename="output", fmt="csv"):
    if not data:
        print("[red]No data to export[/red]")
        return
    df = pd.DataFrame(data)
    if fmt == "csv":
        df.to_csv(f"{filename}.csv", index=False)
    else:
        df.to_json(f"{filename}.json", orient="records")
    print(f"[bold green]Results saved to {filename}.{fmt}[/bold green]")
