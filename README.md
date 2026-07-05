# Wavelet Analysis of Schlieren Flame Images

> Multi-resolution analysis of Schlieren combustion images using Fourier and wavelet transforms for frequency-domain flame diagnostics.

[![Python](https://img.shields.io/badge/Python-3-blue)](#)
[![PyWavelets](https://img.shields.io/badge/PyWavelets-Wavelet%20Analysis-success)](#)
[![Research](https://img.shields.io/badge/Status-Research-orange)](#)

This repository investigates the use of **Fourier** and **Wavelet Transforms** for analysing Schlieren images of combustion flames. The objective is to characterise spatial frequency content at multiple scales and explore how different transform methods capture combustion structures that are not readily visible in the spatial domain.

The project forms part of a broader research effort on combustion diagnostics and complements my work on laser absorption spectroscopy and temperature reconstruction.

---

## Overview

Schlieren imaging is a widely used optical technique for visualising density gradients in combustion flows.

While raw Schlieren images provide qualitative information, transform-domain analysis enables quantitative investigation of:

- flame front structures
- spatial frequency distribution
- turbulent scales
- localised combustion features

This repository explores both global and local frequency analysis using Fourier and wavelet methods.

---

## Methodology

The analysis pipeline consists of:

1. Image preprocessing
2. Fourier Transform (FFT)
3. Wavelet decomposition
4. Multi-scale feature extraction
5. Frequency-domain visualisation
6. Comparative analysis

---

## Features

- Schlieren image processing
- 2D Fourier Transform
- Multi-level wavelet decomposition
- Frequency-domain visualisation
- Multi-scale image analysis
- Python implementation

---

## Repository Structure

```text
.
├── notebooks/
├── images/
├── figures/
├── utilities/
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/CaffineAddic/Wavelet_transforms_in_schlieren_flame_images.git
cd Wavelet_transforms_in_schlieren_flame_images
```

Install the required dependencies

```bash
pip install numpy scipy matplotlib opencv-python pywavelets jupyter
```

---

## Usage

Launch Jupyter Notebook

```bash
jupyter notebook
```

The notebooks demonstrate:

- image preprocessing
- FFT analysis
- wavelet decomposition
- coefficient visualisation
- frequency comparison

---

## Results

The project demonstrates how wavelet transforms provide spatially localised frequency information that complements conventional Fourier analysis for combustion image diagnostics.

The resulting decomposition enables investigation of combustion structures across multiple spatial scales.

---

## Applications

The techniques explored here are applicable to:

- combustion diagnostics
- turbulent flame analysis
- image feature extraction
- scientific image processing
- optical flow visualisation

---

## Related Work

This repository complements:

- **Temperature Profile Estimation using Laser Absorption Spectroscopy and Multi-Output Gaussian Processes**
- **Complex-Valued Neural Networks for PolSAR**
- **MAML and First-Order MAML**

---

## Author

**Saumya Roy**

---

## License

See the repository license.
