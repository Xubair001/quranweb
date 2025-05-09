import os

import requests

# Folder to save PDFs
output_folder = "quran_pdf"
os.makedirs(output_folder, exist_ok=True)

# Download all 30 Paras
for para_num in range(1, 31):
    url = f"https://onlinemadrasa.org/wp-content/uploads/2024/01/Holy-Quran-Para-{para_num}.pdf"
    filename = f"Para-{para_num}.pdf"
    output_path = os.path.join(output_folder, filename)

    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Downloaded: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to download Para {para_num}: {e}")
