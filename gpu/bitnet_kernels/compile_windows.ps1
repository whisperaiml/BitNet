$ErrorActionPreference = "Stop"

nvcc `
  -std=c++17 `
  -Xcudafe --diag_suppress=177 `
  --shared `
  bitnet_kernels.cu `
  -o libbitnet.dll
