# Base image with PyTorch, CUDA, and cuDNN
FROM pytorch/pytorch:2.4.0-cuda12.4-cudnn9-devel

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
RUN pip install --no-cache-dir \
    numpy scipy pandas matplotlib seaborn \
    scikit-learn spectral opencv-python-headless plotly \
    pytorch-lightning torchvision \
    tensorflow \
    h5py

# Copy verify script into the container
COPY ../trials/verify.py /workspace/verify.py

# Default working directory
WORKDIR /workspace

# Run verify script during build to validate installation
RUN python3 verify.py

# Default command
CMD ["/bin/bash"]
