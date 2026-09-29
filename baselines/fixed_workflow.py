from algorithms.hypothesis_engine import uniform_prior, update
from simulator.diagnostic_tools import execute, likelihoods
ORDER=["dig","traceroute","avi_lookup","firewall_check","server_health","application_health"]
def diagnose(incident, threshold=0.75):
    prior=uniform_prior(); history=[]
    for tool in ORDER:
        r=execute(tool,incident); prior=update(prior,likelihoods(tool),r["abnormal"])
        history.append({"tool":tool,"observation":r["observation"],"posterior":prior.copy()})
        pred=max(prior,key=prior.get)
        if prior[pred]>=threshold: break
    return {"prediction":pred,"confidence":prior[pred],"calls":len(history),"history":history}
