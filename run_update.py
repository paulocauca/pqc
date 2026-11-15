
import sys
sys.path.append('/home/rycz/pqc/scripts')
from daily_updater import update_repo

day_str = "57"
date_str = "2026-11-15"
topic_en = "The Role of Formal Methods and Verification in PQC Auditing"
topic_pt = "O Papel dos Métodos Formais e da Verificação na Auditoria de PQC"
file_name_prefix = "pqc_formal_methods_auditing"
category_en = "PQC Security and Implementation"
category_pt = "Segurança e Implementação de PQC"
with open('/home/rycz/pqc/content_en.html', 'r') as f:
    content_en = f.read()
with open('/home/rycz/pqc/content_pt.html', 'r') as f:
    content_pt = f.read()
references_md = "[HACL* Project](https://hacspec.github.io/)"

success = update_repo(day_str, date_str, topic_en, topic_pt, file_name_prefix, category_en, category_pt, content_en, content_pt, references_md)
print("UPDATE STATUS:", success)
