# Project assessment and next steps

Reviewed on 2026-09-28 against the current source.

## What works today

This is a small Python research prototype for adaptive cloud diagnostic tool selection. It offers a terminal demo, six simulated tools (DNS, routing, load balancer, firewall, server, application), Bayesian belief updates across six possible causes, expected information gain, weighted tool ranking, and evidence-driven reranking with confidence/budget stopping. It compares CIG-TS against fixed-workflow and relevance-based baselines.

The experiment command ran successfully with these results:

| Method | Accuracy on six synthetic incidents | Average tool calls |
| --- | --- | --- |
| Fixed workflow | 100% | 4.00 |
| Relevance | 100% | 3.00 |
| CIG-TS | 100% | 3.00 |

The first incident also ran successfully through the interactive demo. The existing test function passed when called directly. `python3 -m pytest -q` could not run because this Python environment lacks pytest; this is not a verified pytest-suite run.

## What it does not yet do

- It does not call an LLM, connect to cloud infrastructure, execute actual diagnostic commands, remediate incidents, or provide a web UI.
- The symptom text is displayed but not interpreted; selection uses manually supplied component context.
- Observations are deterministic and derived from the ground-truth cause. There are no timeouts, tool failures, noisy results, correlated signals, or multiple simultaneous causes.
- Reliability, cost, and risk are static ranking values; runtime, incurred cost, and failures are not measured.
- Replanning means reranking unused tools after each observation; there is no broader workflow generation or recovery planning.
- Evaluation prints accuracy and average calls. It does not persist reports, estimate uncertainty, run ablations, or use held-out scenarios.

## Recommended build order

1. **Make the evaluation credible.** Add balanced scenario families with missing/misleading context, noisy and ambiguous observations, and tool failures. Separate tuning and held-out sets; use reproducible seeds and equivalent scenario observations across methods. Keep single-cause diagnosis as the initial scope, documenting multi-fault incidents as a later extension.
2. **Make results inspectable.** Export per-incident traces and aggregate results to JSON/CSV. Record selected tool, score components, posterior changes, stop reason, correctness, calls, and accumulated simulated cost/risk. Add repeated trials and uncertainty estimates for stochastic scenarios.
3. **Establish what CIG-TS contributes.** Compare against both existing baselines and an information-gain-only selector. Run component ablations and weight/threshold sensitivity experiments. Explain why CIG-TS currently ties the relevance baseline before claiming improvement.
4. **Harden the diagnosis core.** Validate empty metadata, tool/root consistency, probability ranges, impossible evidence, confidence thresholds, and budgets. Handle invalid CLI input. Add a main guard to the demo and meaningful unit tests for Bayesian updates, information gain, and stopping. Expose configuration consistently across methods.
5. **Add the LLM layer required by the research title.** Start with symptom-to-structured-context extraction and evidence explanation behind a replaceable adapter. Validate outputs and compare with manually supplied context. Do not provide ground truth to the model. Keep tool execution bounded by the diagnosis controller.
6. **Demonstrate a realistic integration.** After the experiment framework is reliable, add one read-only diagnostic adapter in a controlled environment with timeouts and structured failure results. A dashboard can follow if needed for presentation.

## Where to focus

For the M.Tech case study, prioritize defensible evidence over additional UI features: realistic scenarios, fair baselines, reproducibility, ablations, and clear limits. The six current cases are useful smoke tests, not proof of general performance. All their contexts contain the correct cause, and symmetric likelihoods make tools equally informative at the initial uniform prior, so context and other score terms drive the first selection.

Keep the deterministic demo as a regression fixture while developing a separate richer evaluation set. Use version control before substantive implementation; this folder was not a Git repository at review time.

## Stored project skill

`skills/cigts-cloud-ops/SKILL.md` contains reusable project-specific development and evaluation instructions. It is stored with this project, not installed as a globally discovered skill. Ask an agent to read that path when continuing project work.
