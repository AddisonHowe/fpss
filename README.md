# Fokker-Planck Steady State Inference

## System setup

### Cloning this repo

Run the following command to clone the project repository.

```bash
git clone https://github.com/AddisonHowe/fpss.git
```

### Conda environment

Without GPU:
```bash
conda create -p ./env python=3.9 jax=0.4.26 numpy matplotlib pytorch torchvision equinox optax ipykernel ipywidgets ipympl tqdm watermark pytest
conda activate env
pip install diffrax==0.5.1
```

With GPU, specifying cuda toolkit 11.2:
```bash
conda create -p <env-path> python=3.9 pytorch=1.11[build=cuda112*] numpy=1.25 matplotlib=3.7  ipykernel ipywidgets ipympl tqdm watermark pytest=7.4
conda activate env
pip install --upgrade "jax[cuda11_pip]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
pip install optax==0.1.7 diffrax==0.5.1 equinox==0.11.2
```

Then, to install the project,
```bash
pip install -e .
```
