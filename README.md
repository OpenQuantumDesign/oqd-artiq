# OQD ARTIQ

A Nix flake for installing ARTIQ (Advanced Real-Time Infrastructure for Quantum physics) and all its dependencies.

## Overview

This repository provides a standalone Nix flake configuration that installs ARTIQ and all required dependencies. The flake fetches ARTIQ from the original [m-labs/artiq](https://github.com/m-labs/artiq) repository, ensuring you always get the latest version.

## Installation

### Using Nix Flakes

To enter a development shell with ARTIQ:

```bash
nix develop
```

To use ARTIQ in your shell:

```bash
nix shell github:OpenQuantumDesign/oqd-artiq
```

### Building ARTIQ

To build ARTIQ:

```bash
nix build github:OpenQuantumDesign/oqd-artiq
```

## Documentation

Documentation for features and enhancements is available via MkDocs. To view the documentation:

```bash
nix develop
mkdocs serve
```

Then open http://127.0.0.1:8000 in your browser.

## Features

This repository extends the original ARTIQ system with additional features and enhancements. See the [documentation](docs/index.md) for details.

## About ARTIQ

ARTIQ is a leading-edge control and data acquisition system for quantum information experiments. It features:

- High-level programming language for describing complex experiments
- Nanosecond timing resolution
- Sub-microsecond latency
- Graphical user interfaces for experiment parametrization and visualization

For more information, visit the [official ARTIQ website](https://m-labs.hk/artiq).

## License

This flake configuration is provided under the same license as ARTIQ (LGPLv3+).
