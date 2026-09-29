import json, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from algorithms.replanner import diagnose

def test_all_synthetic_incidents():
    metadata=json.loads((ROOT/'data/tool_metadata.json').read_text()); graph=json.loads((ROOT/'data/dependency_graph.json').read_text()); incidents=json.loads((ROOT/'data/incidents.json').read_text())
    for inc in incidents:
        r=diagnose(inc,metadata,graph)
        assert r['prediction']==inc['root_cause']
