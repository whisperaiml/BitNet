from __future__ import annotations

from pathlib import Path
import platform
import shutil


def _unsupported_platform_message(context: str) -> str:
    system = platform.system()
    machine = platform.machine()
    return (
        f"{context} only supports Linux on an NVIDIA GPU with CUDA. "
        f"Detected {system} ({machine}). "
        "If you are on macOS, use the CPU path documented in the repository root README."
    )


def ensure_cuda_runtime(context: str):
    if platform.system() != "Linux":
        raise SystemExit(_unsupported_platform_message(context))

    try:
        import torch
    except ModuleNotFoundError as exc:
        raise SystemExit(
            f"PyTorch is not installed in the active environment. Install `gpu/requirements.txt` first before running {context}."
        ) from exc

    if not torch.cuda.is_available():
        raise SystemExit(
            f"{context} requires a CUDA-enabled PyTorch build and a visible NVIDIA GPU. "
            "Check your PyTorch install, CUDA driver, and selected device."
        )

    return torch


def ensure_kernel_library(path: Path, context: str) -> None:
    if path.exists():
        return

    raise SystemExit(
        f"Missing compiled kernel library at `{path}`. "
        f"Run `cd gpu/bitnet_kernels && bash compile.sh` before starting {context}."
    )


def ensure_nvcc_available(context: str) -> None:
    if platform.system() != "Linux":
        raise SystemExit(_unsupported_platform_message(context))

    if shutil.which("nvcc") is None:
        raise SystemExit(
            f"`nvcc` was not found on PATH. Install the CUDA toolkit before running {context}."
        )
