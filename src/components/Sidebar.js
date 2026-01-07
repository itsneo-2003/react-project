import pandas as pd
import os

INPUT_FOLDER = "data"
OUTPUT_FILE = "output_unique.xlsx"

print("🚀 Script started")

seen = set()
output_chunks = []

files = os.listdir(INPUT_FOLDER)
print("📂 Files found:", files)

for file_name in files:
    if not file_name.endswith(".xlsx"):
        continue

    file_path = os.path.join(INPUT_FOLDER, file_name)
    print(f"\n📄 Processing {file_name}")

    df = pd.read_excel(file_path)
    print("   Rows read:", len(df))
    print("   Columns:", df.columns.tolist())

    keep_mask = []

    # Column B, D, E → indexes 1, 3, 4
    for b, d, e in zip(df.iloc[:, 1], df.iloc[:, 3], df.iloc[:, 4]):
        key = (b, d, e)
        if key in seen:
            keep_mask.append(False)
        else:
            seen.add(key)
            keep_mask.append(True)

    unique_rows = df[keep_mask]
    print("   Unique rows kept:", len(unique_rows))

    if not unique_rows.empty:
        output_chunks.append(unique_rows)

if output_chunks:
    final_df = pd.concat(output_chunks, ignore_index=True)
    print("\n🧮 Total unique rows:", len(final_df))
    final_df.to_excel(OUTPUT_FILE, index=False)
    print("✅ Output written to", OUTPUT_FILE)
else:
    print("❌ No unique rows found")

print("🏁 Script finished")
