# Metrics & Benchmarking

This project reports **model performance and timing metrics** that are stored as `.json` files inside the `artifacts/metrics/` directory.

These metrics were **computed on Kaggle** using both **CPU and GPU** environments in order to ensure fair, reproducible, and hardware-aware evaluation.

---

## What metrics are included

Each `.json` file contains:

### Classification metrics
Computed on the test set:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-score**

### Timing metrics
- **Training time**
  - Total time required to fit the model
  - Reported in **seconds** and **minutes**
- **Inference time**
  - Mean time required to produce a prediction
  - Measured per sample (single input)

---

## CPU vs GPU evaluation (Kaggle)

All benchmarks were executed on **Kaggle Notebooks**, using two separate configurations:

- **CPU runs**
  - Used for classical ML models (e.g. TF-IDF + SVM, TF-IDF + MLP)
- **GPU runs**
  - Used for deep learning models (e.g. CNNs, Transformers)

Because Kaggle does not allow switching hardware during execution, **each benchmark was run in a separate notebook session**:
- CPU metrics → Kaggle Accelerator set to **None**
- GPU metrics → Kaggle Accelerator set to **GPU**

The resulting metrics were saved as `.json` files and committed to this repository.

---

## Why results are stored as `.json`

Storing metrics as `.json` provides:
- Reproducibility
- Easy comparison between models
- Simple integration with reports, plots, and dashboards
- Clear separation between **training/evaluation** and **analysis**

---

## Reproducing the metrics locally

All metrics **can be recomputed** using the code in this repository by running the training and evaluation scripts/notebooks.

⚠️ **Important note**  
Reproducing the results locally may:
- Take **significantly more time**
- Produce **different timing results** depending on:
  - CPU/GPU hardware
  - Available memory
  - Parallelism and system load

For this reason, the Kaggle benchmarks are considered the **reference measurements** for this project.

---

## Summary

- Metrics were computed on **Kaggle (CPU & GPU)** and saved as `.json`
- They include **performance** and **timing** information
- Local reproduction is possible but **computationally expensive**
- Kaggle results are used as the **official benchmark**
