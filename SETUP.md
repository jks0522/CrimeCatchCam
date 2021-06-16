# Setup Guide

This document describes how to setup all the dependencies, and optionally create a virtual machine,
to run the notebooks in this repository.


## Table of Contents

1. [Installation](#installation)
1. [System Requirements](#system-requirements)

## Installation

1. (optional) Install Anaconda with Python >= 3.6. [Miniconda](https://conda.io/miniconda.html). This step can be skipped if working on a Data Science Virtual Machine (see the compute environment section).

1. Clone the repository
    ```
    git clone https://github.com/Microsoft/computervision-recipes
    ```
1. Install the conda environment, you'll find the `environment.yml` file in the root directory. To build the conda environment:
    ```
    cd computervision-recipes
    conda env create -f environment.yml
    ```
1. Activate the conda environment and register it with Jupyter:
    ```
    conda activate cv
    python -m ipykernel install --user --name cv --display-name "Python (cv)"
    ```
1. Start the Jupyter notebook server
    ```
    jupyter notebook
    ```
1. At this point, you should be able to run the notebooks within the various [scenarios](scenarios) folders.

이후 web폴더에서 README 파일을 읽고 경로설정을 해야합니다

__pip install__

As an alternative to the steps above, and if you only want to install the 'utils_cv' library (without creating a new conda environment), this can be done using pip install. Note that this does not download the notebooks.

```bash
pip install git+https://github.com/microsoft/ComputerVision.git@master#egg=utils_cv
```


## System Requirement

__Requirements__

* A machine running Linux (suggested) >= 16.04 LTS or Windows
* [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or Anaconda with Python version >= 3.6.
    * This is pre-installed on Azure DSVM such that one can run the following steps directly.
    * It is recommended to update conda to the latest version: `conda update -n base -c defaults conda`

Note that PyTorch runs slower on Windows than on Linux. This is a known [issue](https://github.com/pytorch/pytorch/issues/12831) which affects model training and is due to parallelized data loading. For compute-heavy training tasks (e.g. Object Detection) and on standard GPUs this difference is typically below 10%. For image classification however, with fast GPU (e.g. V100) and potentially large images, training on Windows can be multiple times slower than on Linux.

__Dependencies__

Make sure you have CUDA Toolkit version 9.0 or above installed on your machine. You can run the command below in your terminal to check.

```
nvcc --version
```

If you don't have CUDA Toolkit or don't have the right version, please download it from here: [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit)




