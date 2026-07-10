import json
from pathlib import Path
p = Path('logic building/rough.ipynb')
nb = json.loads(p.read_text(encoding='utf-8'))
print('cells:', len(nb['cells']))
for i, c in enumerate(nb['cells'], 1):
    src = ''.join(c.get('source', []))
    print('--- cell', i, c['cell_type'])
    print(src)
