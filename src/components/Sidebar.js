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
