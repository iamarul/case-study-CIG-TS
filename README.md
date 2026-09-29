# CIG-TS Cloud Operations POC

Local M.Tech case-study prototype for **Adaptive Tool Selection and Replanning for LLM-Based Cloud Operations**.

## What is implemented
- Six simulated diagnostic tools: DNS, traceroute, AVI/LB, firewall, server health, application health
- Bayesian root-cause hypothesis updates
- Expected information gain
- CIG-TS multi-objective scoring using IG, context relevance, dependency relevance, reliability, cost, and risk
- Evidence-driven replanning and confidence stopping
- Fixed-workflow and relevance-based baselines
- Experiment runner and tests

## Run
```bash
python app.py
python -m evaluation.experiment
pytest -q
```

## Important research note
The included incidents are deterministic synthetic examples for POC/demo purposes. Numbers produced by them are **intermediate prototype results**, not evidence of production-world performance. For the final case study, expand the scenario set, define/calibrate likelihoods and weights, perform sensitivity/ablation analysis, and evaluate on held-out scenarios.
