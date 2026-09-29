from algorithms.hypothesis_engine import uniform_prior, update
from simulator.diagnostic_tools import execute, likelihoods, TOOL_COMPONENT

def diagnose(incident, metadata, threshold=0.75):
    prior=uniform_prior(); remaining=list(metadata); history=[]; ctx=incident.get("context",[])
    while remaining:
        tool=max(remaining,key=lambda t:(1 if TOOL_COMPONENT[t] in ctx else 0, metadata[t]["reliability"]-metadata[t]["cost"]))
        r=execute(tool,incident); prior=update(prior,likelihoods(tool),r["abnormal"])
        history.append({"tool":tool,"observation":r["observation"],"posterior":prior.copy()}); remaining.remove(tool)
        pred=max(prior,key=prior.get)
        if prior[pred]>=threshold: break
    return {"prediction":pred,"confidence":prior[pred],"calls":len(history),"history":history}
