# MAML and First-Order MAML: Implementation and Comparison

> Comparative implementation of Model-Agnostic Meta-Learning (MAML) and First-Order MAML (FOMAML) using PyTorch and Learn2Learn on the Omniglot dataset.

[![Python](https://img.shields.io/badge/Python-3-blue)](#)
[![PyTorch](https://img.shields.io/badge/PyTorch-red)](#)
[![Learn2Learn](https://img.shields.io/badge/Learn2Learn-Meta--Learning-success)](#)

This repository investigates two widely used gradient-based meta-learning algorithms:

- **Model-Agnostic Meta-Learning (MAML)**
- **First-Order Model-Agnostic Meta-Learning (FOMAML)**

The objective is to compare their optimisation behaviour, computational cost, and adaptation performance on few-shot image classification tasks using the **Omniglot** benchmark.

The implementation is built using **PyTorch** and the **Learn2Learn** meta-learning library.

---

## Overview

Meta-learning aims to learn models that can rapidly adapt to previously unseen tasks using only a handful of training examples.

This project compares MAML and its first-order approximation under identical experimental settings, measuring both predictive performance and computational efficiency.

---

## Methodology

The experimental pipeline consists of:

1. Sampling episodic few-shot learning tasks from Omniglot.
2. Inner-loop adaptation using support examples.
3. Meta-update using query examples.
4. Comparison between:

   - MAML
   - First-Order MAML

5. Recording training time and convergence behaviour.

---

## Features

- MAML implementation using Learn2Learn
- First-Order MAML implementation
- Omniglot few-shot benchmark
- Episodic task sampling
- Training-time comparison
- Performance evaluation

---

## Repository Structure

```text
.
├── MAML.ipynb
├── report.pdf
├── figures/
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/CaffineAddic/MAML-and-FOMAML-implimentaion-and-comparison.git
cd MAML-and-FOMAML-implimentaion-and-comparison
```

Install the required dependencies

```bash
pip install torch torchvision torchaudio matplotlib scipy learn2learn notebook
```

---

## Running the Notebook

Launch Jupyter Notebook

```bash
jupyter notebook
```

Open the notebook and execute the cells sequentially.

If a CUDA-enabled GPU is unavailable, disable GPU execution by setting:

```python
cuda = False
```

---

## Experiments

The notebook includes:

- episodic few-shot training
- MAML optimisation
- FOMAML optimisation
- execution-time measurements
- convergence comparison

The reference experiments were performed for **10,000 optimisation steps**, allowing direct comparison of training time and learning behaviour.

---

## Results

The project demonstrates the computational trade-off between full second-order MAML and the first-order approximation, highlighting the reduction in training cost achieved by FOMAML while maintaining competitive adaptation performance.

Further discussion and experimental observations are included in the accompanying report.

---

## References

Finn, C., Abbeel, P., & Levine, S. (2017).

**Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks.**

Proceedings of ICML 2017.

https://arxiv.org/abs/1703.03400

---

## Author

**Saumya Roy**
---

## License

See the repository license.
