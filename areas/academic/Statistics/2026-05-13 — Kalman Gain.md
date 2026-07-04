---
name: Kalman Gain
type: note
tags: [statistics, signal-processing, estimation, filtering, bayesian-reasoning]
---

# Kalman Gain

Kalman gain is the weighting coefficient that determines how much a Kalman filter should adjust its state estimate based on a new measurement, relative to its prior prediction.

## What It Is

In the Kalman filter update step, the gain $K$ is a scalar (or matrix) that multiplies the *innovation* — the difference between what the filter predicted and what it actually observed:

$$\hat{x}_k = \hat{x}_k^- + K_k(z_k - H\hat{x}_k^-)$$

where:
- $\hat{x}_k^-$ is the prior (predicted) state
- $z_k$ is the measurement
- $z_k - H\hat{x}_k^-$ is the innovation (residual)
- $K_k$ is the Kalman gain — a number between 0 and 1 (in scalar form)

## Why It Matters

Kalman gain is the principled answer to **"how much should I trust the sensor vs. my model?"** It is:

- **MSE-optimal** — minimizes mean-squared error of the estimate under Gaussian noise
- **Adaptive** — automatically tunes to the noise levels and uncertainty in the system
- **Foundational** — underlies Extended Kalman Filters (EKF), Unscented Kalman Filters (UKF), and particle filters
- **Deeply Bayesian** — it is a dynamic, sequentially updated prior-likelihood balance

## Mechanism

### Scalar Form (Intuition)

For a scalar system:

$$K = \frac{\sigma_{pred}^2}{\sigma_{pred}^2 + \sigma_{meas}^2}$$

where:
- $\sigma_{pred}^2$ is the uncertainty in the model prediction (process noise variance)
- $\sigma_{meas}^2$ is the uncertainty in the measurement (measurement noise variance)

**Logic:**
- When $\sigma_{meas}^2 \gg \sigma_{pred}^2$ (sensor is very noisy), $K \to 0$ → trust the model, ignore the measurement
- When $\sigma_{meas}^2 \ll \sigma_{pred}^2$ (model is very uncertain), $K \to 1$ → trust the sensor, abandon the prediction
- When both are equal, $K = 0.5$ → split the difference

### Matrix Form (Full Derivation)

$$K_k = P_k^- H^\top (H P_k^- H^\top + R)^{-1}$$

where:
- $P_k^-$ is the prior covariance (uncertainty in the state prediction)
- $H$ is the measurement matrix (how measurements relate to state)
- $R$ is the measurement noise covariance
- $H P_k^- H^\top$ is the predicted measurement covariance

**Interpretation:** $K$ is the ratio of predicted uncertainty to total uncertainty (predicted + measurement).

## State Update

Once $K$ is computed, the state is updated:

$$\hat{x}_k = \hat{x}_k^- + K_k(z_k - H\hat{x}_k^-)$$

The term $(z_k - H\hat{x}_k^-)$ is the *innovation* — the surprise, or residual error. Multiplying by $K$ scales how much weight to give that surprise.

## Key Intuition

1. **Kalman gain is a dynamic Bayesian weight.** It is the filter's way of asking: "Given what I know about my uncertainty, how much should I revise my belief when I see new evidence?"

2. **It is self-tuning.** Unlike ad-hoc filters (exponential smoothing with fixed $\alpha$), Kalman gain computes the optimal $\alpha$ at every step based on the actual noise levels.

3. **It degrades gracefully.** If the model is terrible, the filter will lean heavily on the sensor. If the sensor is terrible, the filter will lean on the model. Either way, the estimate is as good as possible under the given constraints.

## Connections

- **[[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Bayesian Reasoning — Updating Beliefs Under Uncertainty|Bayesian Reasoning]]** — Kalman gain is sequential Bayesian updating made mechanical and real-time; $K$ is the exact optimal weight prescribed by Bayes' theorem under Gaussian noise; the innovation $(z_k - H\hat{x}_k^-)$ is the likelihood term, the prior covariance $P^-$ encodes prior uncertainty
- **[[02-Areas/Learning/Self-Study/Philosophy/2026-03-22 — The Aggregation Problem|The Aggregation Problem]]** — Kalman gain is the signal-processing solution to multi-source aggregation: rather than arbitrarily weighting two uncertain sources, it derives the MSE-optimal weight from the noise parameters themselves
- **[[02-Areas/Learning/Self-Study/Statistics/2026-04-17 — Confidence Intervals|Confidence Intervals]]** — the covariance matrices $P$ and $R$ are the Kalman filter's equivalent of confidence intervals; $P_k^-$ is the prior uncertainty and shrinks toward $R$ as measurement noise dominates
- **[[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Normal Distribution|Normal Distribution]]** — Gaussian noise is the foundational assumption for Kalman filter optimality; under non-Gaussian noise, EKF and particle filters are needed
- **[[02-Areas/Learning/Self-Study/Health-Systems/2026-04-04 — Differential Diagnosis Reasoning Under Uncertainty|Differential Diagnosis]]** — DDx is informal Kalman filtering: the clinician updates a prior model of probable diagnoses with each new test result, weighting the signal by the test's reliability vs. the prior confidence in the model
- [[MOC/Statistics]] — estimation & filtering cluster
