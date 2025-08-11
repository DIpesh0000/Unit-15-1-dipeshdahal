""" Read OHRU.csv (FRED national unemployment rate), analyze header lines
         with enumerate(), parse dates with datetime, and plot the series. BY dipesh dahal 8-10-2025
"""

from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt

def main():
    print("Reading OHUR.csv ...")
    here = Path(__file__).parent
    csv_path = here / "OHUR.csv"
    if not csv_path.exists():
        print("OHUR.csv not found in this folder.")
        return

    header_lines = []
    header = []
    rows = []

    with csv_path.open("r", encoding="utf-8-sig") as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            if "," not in s and not header:
                header_lines.append(s)
                continue
            if not header:
                header = [c.strip() for c in s.split(",")]
                continue
            parts = [p.strip() for p in s.split(",")]
            if len(parts) >= 2:
                rows.append((parts[0], parts[1]))
    print("\n=== Header Lines ===")
    for i, txt in enumerate(header_lines, 1):
        print(f"{i}: {txt}")
    print("\n=== Column Header ===")
    for i, col in enumerate(header, 1):
        print(f"{i}: {col}")
    dates = []
    vals = []
    for d_str, v_str in rows:
        dt = None
        for fmt in ("%Y-%m-%d", "%Y-%m"):
            try:
                dt = datetime.strptime(d_str, fmt)
                break
            except ValueError:
                pass
        if not dt:
            continue
        if v_str in (".", ""):
            continue
        try:
            y = float(v_str)
        except ValueError:
            continue
        dates.append(dt)
        vals.append(y)
    print(f"\nLoaded {len(dates)} points.")
    if not dates:
        print("No data to plot.")
        return
    plt.figure()
    plt.plot(dates, vals, linewidth=2)
    plt.title("U.S. Unemployment Rate (OHUR)")
    plt.xlabel("Date")
    plt.ylabel("Unemployment Rate (%)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    main()
