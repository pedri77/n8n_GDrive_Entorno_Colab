# ============================================
# 5️⃣ INFORME VISUAL (HTML + TXT)
# ============================================

import datetime
import json
from IPython.display import HTML, display

drive.mount('/content/drive', force_remount=True)

base_dir = "/content/drive/MyDrive/n8n_data/reports"
os.makedirs(base_dir, exist_ok=True)

fecha = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
json_temp = f"/content/workflows_temp_{fecha}.json"
html_report = f"{base_dir}/informe_workflows_{fecha}.html"
txt_report = f"{base_dir}/informe_workflows_{fecha}.txt"

print("📤 Exportando flujos para generar informe...")
!n8n export:workflow --all --output="{json_temp}"

with open(json_temp, "r") as f:
    data = json.load(f)

html_content = f"<h2>📊 Informe de Workflows n8n ({fecha})</h2>"
html_content += "<table border='1' cellspacing='0' cellpadding='6'><tr><th>ID</th><th>Nombre</th><th>Activo</th><th>Fecha Creación</th><th>Última actualización</th></tr>"
txt_content = f"📊 INFORME DE WORKFLOWS n8n ({fecha})\n\n"
txt_content += f"{'ID':<10} | {'Nombre':<35} | {'Activo':<8} | {'Creado':<20} | {'Actualizado':<20}\n"
txt_content += "-"*110 + "\n"

for wf in data:
    wf_id = wf.get('id', 'N/A')
    name = wf.get('name', 'Sin nombre')
    active = "✅ Sí" if wf.get('active', False) else "❌ No"
    created = wf.get('createdAt', 'N/D').replace('T', ' ').replace('Z', '')
    updated = wf.get('updatedAt', 'N/D').replace('T', ' ').replace('Z', '')

    html_content += f"<tr><td>{wf_id}</td><td>{name}</td><td>{active}</td><td>{created}</td><td>{updated}</td></tr>"
    txt_content += f"{wf_id:<10} | {name:<35} | {active:<8} | {created:<20} | {updated:<20}\n"

html_content += "</table>"

with open(html_report, "w") as f:
    f.write(html_content)

with open(txt_report, "w") as f:
    f.write(txt_content)

print(f"✅ Informe generado:\n- HTML: {html_report}\n- TXT: {txt_report}")
display(HTML(html_content))  # 👁️ Abre el informe automáticamente en Colab
