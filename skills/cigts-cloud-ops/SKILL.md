---
name: cigts-cloud-ops
description: Develop and evaluate this CIG-TS Cloud Operations Python prototype, including Bayesian diagnosis, adaptive tool selection, simulated incidents, and research baselines. Use for work in this project and its M.Tech case study.
---

# CIG-TS Cloud Operations

Resolve the project root from this file as `../..`. Read `README.md` and the relevant source before changing behavior. Read `PROJECT_ROADMAP.md` when planning experiments or prioritizing work; its results are a dated snapshot, not permanent performance guarantees.

## Project map

- `app.py`: interactive terminal demo; currently executes on import.
- `algorithms/hypothesis_engine.py`: six root causes, uniform prior, Bayesian update.
- `algorithms/information_gain.py`: entropy and binary expected information gain.
- `algorithms/cig_ts.py`: weighted information gain, context, dependency, reliability, cost, and risk scoring. Information gain is normalized against remaining tools.
- `algorithms/replanner.py`: select, execute, update, rerank, and stop. Defaults: confidence 0.75 and at most six calls; each tool runs at most once.
- `simulator/diagnostic_tools.py`: tool-to-component mapping, likelihoods, and synthetic observations.
- `baselines/`: fixed ordering and context/reliability/cost selection.
- `evaluation/experiment.py`: shared incident evaluation; prints aggregate accuracy/calls and returns per-incident rows.
- `data/`: incidents, tool metadata, and directed dependency adjacency lists.
- `tests/test_cigts.py`: one test covering the six supplied scenarios.

## Model and research constraints

The existing system is a deterministic local simulator, with no LLM integration or live cloud diagnostics. Incident `root_cause` is used by the simulator to generate observations and by evaluation as ground truth. Keep it out of selector inputs and any future LLM prompt.

The simulator currently returns a perfect binary signal, whereas inference assumes abnormal probabilities of 0.92 for a matching cause and 0.08 otherwise. Tool metadata reliability affects ranking but does not control observation noise. Distinguish these quantities when interpreting results or extending simulation.

The supplied contexts always contain the true cause. Include absent, ambiguous, and misleading context when testing generalization. Keep calibration/tuning scenarios separate from held-out evaluation. Use seeded sampling for noisy experiments and apply comparable observations, stopping rules, and budgets to all methods.

Dependency relevance currently examines direct neighbors only; the graph is a ranking heuristic, not a model of propagated failures. Do not describe it as causal inference or recursive dependency traversal.

When adding a component or tool, reconcile root names, tool mapping, observation messages, likelihood coverage, metadata, graph, and fixtures. Root lists are currently duplicated in the hypothesis engine and simulator.

Report sample size and scenario assumptions with results. Compare CIG-TS with both baselines; matching relevance-only performance is not evidence of an information-gain improvement. Treat posterior confidence as model output, not measured calibration.

## Validation

From the project root, use:

```bash
python3 -m pytest -q
python3 -m evaluation.experiment
python3 app.py
```

`requirements.txt` currently contains pytest only; core execution uses the standard library. Report missing dependencies accurately. For algorithm changes, test informative versus uninformative observations, normalized posteriors, stopping/budget behavior, and failure cases relevant to the change. For evaluation changes, check reproducibility and baseline fairness.

Keep ordinary development local. Adding a live connector, sending incident data to an LLM, or changing cloud resources is separate work governed by the user's requested scope.
