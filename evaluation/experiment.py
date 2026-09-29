import json, pathlib, statistics
from algorithms.replanner import diagnose as cigts
from baselines.fixed_workflow import diagnose as fixed
from baselines.relevance_selector import diagnose as relevance
BASE=pathlib.Path(__file__).resolve().parents[1]
def load(name): return json.loads((BASE/'data'/name).read_text())

def run():
    incidents=load('incidents.json'); metadata=load('tool_metadata.json'); graph=load('dependency_graph.json')
    methods={"Fixed":lambda x:fixed(x),"Relevance":lambda x:relevance(x,metadata),"CIG-TS":lambda x:cigts(x,metadata,graph)}
    rows=[]
    for name,fn in methods.items():
        outs=[]
        for inc in incidents:
            r=fn(inc); outs.append(r)
            rows.append({"method":name,"incident":inc['id'],"actual":inc['root_cause'],"predicted":r['prediction'],"correct":r['prediction']==inc['root_cause'],"calls":r['calls'],"confidence":round(r['confidence'],3)})
        print(f"{name:10s} accuracy={sum(r['prediction']==i['root_cause'] for r,i in zip(outs,incidents))/len(incidents):.2f} avg_calls={statistics.mean(r['calls'] for r in outs):.2f}")
    return rows
if __name__=='__main__': run()
