#!/usr/bin/env bash

set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "gpu/bitnet_kernels/compile.sh only supports Linux with an NVIDIA CUDA toolkit." >&2
  echo "Detected $(uname -s). On macOS, use the CPU path from the repository root README instead." >&2
  exit 1
fi

if ! command -v nvcc >/dev/null 2>&1; then
  echo "\`nvcc\` was not found on PATH. Install the CUDA toolkit before compiling the BitNet GPU kernel." >&2
  exit 1
fi

CUDA_ARCH="${CUDA_ARCH:-80}"

nvcc -std=c++17 -Xcudafe --diag_suppress=177 --compiler-options -fPIC -lineinfo --shared bitnet_kernels.cu -lcuda -gencode=arch=compute_"${CUDA_ARCH}",code=compute_"${CUDA_ARCH}" -o libbitnet.so

