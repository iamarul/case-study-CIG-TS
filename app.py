import json, pathlib
from algorithms.replanner import diagnose
BASE=pathlib.Path(__file__).parent
metadata=json.loads((BASE/'data/tool_metadata.json').read_text()); graph=json.loads((BASE/'data/dependency_graph.json').read_text()); incidents=json.loads((BASE/'data/incidents.json').read_text())
print('CIG-TS Cloud Operations Demo')
for i,x in enumerate(incidents,1): print(i,x['id'],x['symptom'])
choice=int(input('Select incident: '))-1
inc=incidents[choice]; r=diagnose(inc,metadata,graph)
print('\nActual root cause:',inc['root_cause'])
for n,h in enumerate(r['history'],1):
    print(f"\nStep {n}: {h['tool']} score={h['score']:.3f}")
    print('Observation:',h['observation'])
    top=sorted(h['posterior'].items(),key=lambda x:x[1],reverse=True)[:3]
    print('Top hypotheses:',', '.join(f'{k}={v:.2f}' for k,v in top))
print(f"\nPrediction: {r['prediction']} confidence={r['confidence']:.2f} tool_calls={r['calls']}")
