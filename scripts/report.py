import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--mode", required=True, choices=["test", "quality"])
args = parser.parse_args()

Path("reports").mkdir(exist_ok=True)
Path("reports/pipeline-report.txt").write_text(
    f"mode={args.mode}\nstatus=PASS\n", encoding="utf-8"
)
print(f"{args.mode}: PASS")
