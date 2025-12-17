# OQD ARTIQ

## Overview

This repository provides a standalone Nix flake configuration that installs some OQD applications along with ARTIQ and all required dependencies. The flake fetches ARTIQ from the original [m-labs/artiq](https://github.com/m-labs/artiq) repository, ensuring you always get the latest version.

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

### Building the environment

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

This repository extends the original ARTIQ system with additional OQD applications. See the [documentation](docs/index.md) for details.

## About ARTIQ

For more information, visit the [official ARTIQ website](https://m-labs.hk/artiq).

## License

This project is licensed under the Apache 2.0 License - see the LICENSE file for details.