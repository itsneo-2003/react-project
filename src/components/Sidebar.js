import pandas as pd
import os

# 🔒 PATHS — SAME AS BEFORE
INPUT_FOLDER = "data"
OUTPUT_FILE = "output_unique.xlsx"

print("🚀 Script started")

seen = set()
output_chunks = []

files = os.listdir(INPUT_FOLDER)
print("📄 Files found:", files)

for file_name in files:
    # Your files are CSVs (even if Excel opens them)
    if not file_name.endswith(".csv"):
        continue

    file_path = os.path.join(INPUT_FOLDER, file_name)
    print(f"\n📄 Processing {file_name}")

    df = pd.read_csv(file_path)
    print("   Rows read:", len(df))
    print("   Columns found:", len(df.columns))

    # 🔒 SAFETY: need at least 5 columns for B, D, E
    if len(df.columns) < 5:
        print("   ⚠ Skipped (less than 5 columns)")
        continue

    keep_mask = []
    kept = 0

    # B, D, E → indexes 1, 3, 4
    for b, d, e in zip(df.iloc[:, 1], df.iloc[:, 3], df.iloc[:, 4]):
        key = (b, d, e)
        if key in seen:
            keep_mask.append(False)
        else:
            seen.add(key)
            keep_mask.append(True)
            kept += 1

    unique_rows = df[keep_mask]
    print("   Unique rows kept:", kept)

    if not unique_rows.empty:
        output_chunks.append(unique_rows)

if output_chunks:
    final_df = pd.concat(output_chunks, ignore_index=True)
    final_df.to_excel(OUTPUT_FILE, index=False)
    print("\n✅ Output written to", OUTPUT_FILE)
else:
    print("\n❌ No valid data to write")

print("🏁 Script finished")





*********



    import pandas as pd
import os
from collections import Counter

INPUT_FOLDER = "data"
UNIQUE_FILE = "output_unique.xlsx"
OUTPUT_VERIFY_FILE = "verification.xlsx"

print("🚀 Verification started")

# ----------------------------
# Step 1: Read unique output
# ----------------------------
unique_df = pd.read_excel(UNIQUE_FILE)
print("📄 Unique rows read:", len(unique_df))

# Extract unique keys (B, D, E)
unique_keys = list(
    zip(
        unique_df.iloc[:, 1],
        unique_df.iloc[:, 3],
        unique_df.iloc[:, 4]
    )
)

# Prepare counter for occurrences
occurrence_counter = Counter()

total_original_rows = 0

# ----------------------------
# Step 2: Count occurrences in original data
# ----------------------------
files = os.listdir(INPUT_FOLDER)
print("📂 Files found:", files)

for file_name in files:
    if not file_name.endswith(".csv"):
        continue

    file_path = os.path.join(INPUT_FOLDER, file_name)
    print(f"📄 Scanning {file_name}")

    df = pd.read_csv(file_path)
    total_original_rows += len(df)

    # Safety check
    if len(df.columns) < 5:
        print("   ⚠ Skipped (less than 5 columns)")
        continue

    keys = zip(df.iloc[:, 1], df.iloc[:, 3], df.iloc[:, 4])
    occurrence_counter.update(keys)

# ----------------------------
# Step 3: Build verification table
# ----------------------------
verify_df = unique_df.copy()
verify_df["occurrence_count"] = [
    occurrence_counter.get(key, 0) for key in unique_keys
]

# ----------------------------
# Step 4: Validation check
# ----------------------------
sum_of_occurrences = verify_df["occurrence_count"].sum()

print("\n🧮 Verification summary")
print("Total original rows:", total_original_rows)
print("Sum of occurrence counts:", sum_of_occurrences)

if sum_of_occurrences == total_original_rows:
    print("✅ PASS: Deduplication is correct")
else:
    print("❌ FAIL: Mismatch detected")

# ----------------------------
# Step 5: Write verification output
# ----------------------------
verify_df.to_excel(OUTPUT_VERIFY_FILE, index=False)
print("📊 Verification file written to:", OUTPUT_VERIFY_FILE)

print("🏁 Verification finished")







*************
import pandas as pd
import ipaddress

# -------- CONFIG --------
input_file = "input.csv"            # your CSV file
output_file = "output_ipv6_only.csv"
ip_column_index = 1                 # 0-based index (1 = second column)
# ------------------------

def is_ipv6(ip):
    try:
        return isinstance(
            ipaddress.ip_address(str(ip).strip()),
            ipaddress.IPv6Address
        )
    except ValueError:
        return False  # IPv4, invalid, or empty values

# Read CSV
df = pd.read_csv(input_file)

# Keep only rows with IPv6 in column 2
df_ipv6 = df[df.iloc[:, ip_column_index].apply(is_ipv6)]

# Write CSV
df_ipv6.to_csv(output_file, index=False)

print("Done!")
print(f"Original rows: {len(df)}")
print(f"IPv6 rows kept: {len(df_ipv6)}")
print(f"IPv4/invalid rows removed: {len(df) - len(df_ipv6)}")




**************

import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import PatternFill

# -------- CONFIG --------
sheet1_file = "sheet1.xlsx"          # full IPv4s
sheet2_file = "sheet2.xlsx"          # baseline (2 octets only)
output_file = "sheet1_highlighted.xlsx"

col_index = 0                        # first column
# ------------------------

def first_two_octets(ip):
    try:
        parts = str(ip).strip().split(".")
        if len(parts) == 4:
            return f"{parts[0]}.{parts[1]}"
    except:
        pass
    return None

# Read files
df1 = pd.read_excel(sheet1_file)
df2 = pd.read_excel(sheet2_file)

# Baseline prefixes (already 2 octets)
baseline_prefixes = set(
    df2.iloc[:, col_index]
    .astype(str)
    .str.strip()
)

# Load workbook for highlighting
wb = load_workbook(sheet1_file)
ws = wb.active

# Highlight style
highlight = PatternFill(
    start_color="FFFF9999",
    end_color="FFFF9999",
    fill_type="solid"
)

missing = 0

# Compare and highlight
for row_idx, ip in enumerate(df1.iloc[:, col_index], start=2):
    prefix = first_two_octets(ip)
    if prefix and prefix not in baseline_prefixes:
        ws.cell(row=row_idx, column=col_index + 1).fill = highlight
        missing += 1

# Save result
wb.save(output_file)

print("Done!")
print(f"Total IPs checked: {len(df1)}")
print(f"IPs with missing prefixes: {missing}")
print(f"Output file created: {output_file}")
