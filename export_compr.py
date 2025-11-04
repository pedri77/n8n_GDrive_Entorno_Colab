# ============================================
# 4️⃣ EXPORTAR Y COMPRIMIR FLUJOS A ZIP
# ============================================

import datetime

drive.mount('/content/drive', force_remount=True)

base_dir = "/content/drive/MyDrive/n8n_data"
export_dir = f"{base_dir}/exports"
os.makedirs(export_dir, exist_ok=True)

fecha = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
json_file = f"{export_dir}/workflows_{fecha}.json"
zip_file = f"{export_dir}/n8n_export_{fecha}.zip"

print("📤 Exportando flujos...")
!n8n export:workflow --all --output="{json_file}"

print("🗜️ Comprimiendo...")
!zip -j "{zip_file}" "{json_file}"

print(f"✅ ZIP generado en Drive: {zip_file}")
