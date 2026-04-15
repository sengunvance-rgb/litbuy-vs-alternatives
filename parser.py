"""Simple helper for working with litbuy vs alternatives data."""
import csv, sys

def load(path: str) -> list[dict]:
    with open(path) as f:
        return list(csv.DictReader(f))

if __name__ == "__main__":
    rows = load(sys.argv[1])
    print(f"loaded {len(rows)} rows")
