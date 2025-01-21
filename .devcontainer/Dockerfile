# Base image with PyTorch, CUDA, and cuDNN
FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    TZ=Etc/UTC

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip python3-dev python3-tk \
    git wget curl unzip build-essential \
    libopencv-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir --verbose\
    numpy scipy pandas matplotlib seaborn \
    scikit-learn spectral opencv-python plotly \
    pytorch-lightning torchvision \
    tensorflow \
    h5py
# Install PyTorch (with CUDA support)
RUN pip3 install torch torchvision torchaudio

# Copy verify script into the container
COPY ../src/verify.py /workspace/src/verify.py


WORKDIR /workspace/src

# Default command
CMD ["/bin/bash"]
