from algorithms.hypothesis_engine import uniform_prior, update
from algorithms.cig_ts import score_tools
from simulator.diagnostic_tools import execute, likelihoods

def diagnose(incident, metadata, graph, threshold=0.75, max_calls=6):
    prior=uniform_prior(); remaining=list(metadata); history=[]
    for _ in range(max_calls):
        scores,details=score_tools(prior,remaining,incident.get("context",[]),metadata,graph)
        tool=max(scores,key=scores.get)
        result=execute(tool,incident)
        prior=update(prior,likelihoods(tool),result["abnormal"])
        history.append({"tool":tool,"score":scores[tool],"details":details[tool],"observation":result["observation"],"posterior":prior.copy()})
        remaining.remove(tool)
        pred=max(prior,key=prior.get); conf=prior[pred]
        if conf>=threshold or not remaining:
            return {"prediction":pred,"confidence":conf,"calls":len(history),"history":history}
    pred=max(prior,key=prior.get)
    return {"prediction":pred,"confidence":prior[pred],"calls":len(history),"history":history}
