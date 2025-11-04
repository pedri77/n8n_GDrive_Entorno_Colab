# ============================================
# 3️⃣ RESTAURAR BACKUP DESDE GOOGLE DRIVE
# ============================================

drive.mount('/content/drive', force_remount=True)

backup_dir = "/content/drive/MyDrive/n8n_data/backups"

print("📂 Backups disponibles:")
!ls -lh "$backup_dir" | grep ".json" || echo "No hay backups disponibles."

# Cambia este valor por el archivo que quieras restaurar
backup_to_restore = "backup_2025-10-30.json"

backup_path = f"{backup_dir}/{backup_to_restore}"

if os.path.exists(backup_path):
    print(f"🔄 Restaurando backup: {backup_to_restore}")
    !n8n import:workflow --input="{backup_path}" --separate
    print("✅ Restauración completada.")
else:
    print("❌ Error: archivo no encontrado.")
