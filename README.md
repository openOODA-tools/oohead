# oohead: Sovereign PREFIX SLICER

<div align="center">

```
================================================================================
                                oohead
               Sovereign openOODA PREFIX SLICER
================================================================================
```

**Sovereign PREFIX SLICER**  
*Zero-copy prefix line and byte extractor with early pipe closure semantics.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oohead/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oohead-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oohead/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oohead/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oohead-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oohead/uninstall.sh | bash
```

---

## 2. CLI Usage

```
usage: oohead [options] [FILE]...

Zero-copy prefix line and byte extractor with early pipe closure semantics.

Options:
  -n, --lines <[-]NUM>  print first NUM lines (or all except last NUM if negative) [default: 10]
  -c, --bytes <[-]NUM>  print first NUM bytes (or all except last NUM if negative)
  -q, --quiet, --silent never print file name headers
  -v, --verbose         always print file name headers
  -z, --zero-terminated line delimiter is NUL byte, not newline
      --json            output structured JSON with line and byte telemetry
  -D, --demo            run interactive prefix slicer demonstration showcase
      --test            run internal self-verification suite
  -h, --help            display this help and exit
  -V, --version         output version information and exit
      --mcp             run as Model Context Protocol stdio server
```

---

## 3. Model Context Protocol (MCP)

When invoked with `--mcp`, `oohead` runs a JSON-RPC 2.0 stdio server providing capability-bounded prefix slicing tools for AI coding agents:

```bash
oohead --mcp
```

### Supported Tools
1. `head_lines` - Extract leading lines from raw text payload with early break detection.
2. `head_bytes` - Extract leading byte slice from text payload.
3. `head_file` - Inspect leading lines or bytes of a local file under `&FsReadCap`.
4. `head_sample` - Extract preview sample with line/byte telemetry metrics.
5. `head_demo` - Run interactive prefix slicing showcase.

---

## 4. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`). Physical absence of ambient disk/net leakage.
* **Negative-Trust Architecture:** Strict input validation and operational limits.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 5. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
