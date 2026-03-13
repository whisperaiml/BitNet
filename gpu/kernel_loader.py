from __future__ import annotations

import ctypes
import platform
from pathlib import Path


def load_bitnet_kernel() -> ctypes.CDLL:
    kernel_dir = Path(__file__).resolve().parent / "bitnet_kernels"

    if platform.system() == "Windows":
        patterns = ["libbitnet.dll", "libbitnet.dll*"]
    else:
        patterns = ["libbitnet.so", "libbitnet.so*"]

    for pattern in patterns:
        for candidate in sorted(kernel_dir.glob(pattern)):
            if candidate.is_file():
                return ctypes.CDLL(str(candidate))

    expected = ", ".join(patterns)
    raise FileNotFoundError(
        f"Could not find a compiled BitNet kernel in {kernel_dir} "
        f"(looked for {expected}). Build the kernel first."
    )
