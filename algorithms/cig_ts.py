from algorithms.information_gain import expected_information_gain
from simulator.diagnostic_tools import TOOL_COMPONENT, likelihoods

DEFAULT_WEIGHTS={"ig":0.35,"context":0.18,"dependency":0.15,"reliability":0.15,"cost":0.09,"risk":0.08}

def dependency_relevance(component, context, graph):
    if component in context: return 1.0
    for c in context:
        if component in graph.get(c,[]): return 0.7
    return 0.25

def score_tools(prior, remaining, context, metadata, graph, weights=None):
    w=weights or DEFAULT_WEIGHTS
    raw_ig={t:expected_information_gain(prior, likelihoods(t)) for t in remaining}
    max_ig=max(raw_ig.values()) if raw_ig else 1
    scores={}
    details={}
    for t in remaining:
        m=metadata[t]; comp=TOOL_COMPONENT[t]
        ig=raw_ig[t]/max_ig if max_ig else 0
        cr=1.0 if comp in context else 0.35
        dr=dependency_relevance(comp,context,graph)
        rel=m["reliability"]
        cost=m["cost"]
        risk=m["risk"]
        s=w["ig"]*ig+w["context"]*cr+w["dependency"]*dr+w["reliability"]*rel-w["cost"]*cost-w["risk"]*risk
        scores[t]=s
        details[t]={"score":s,"IG":ig,"CR":cr,"DR":dr,"Rel":rel,"Cost":cost,"Risk":risk}
    return scores,details
