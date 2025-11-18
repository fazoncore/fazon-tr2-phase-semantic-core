# FAZON · TR-2 Phase-Semantic Core · Research Release v1

This repository contains the **research-facing snapshot** of the FAZON TR-2
phase-semantic observability stack. It is intended for:

- GitHub (public / semi-public research repo)
- Zenodo (DOI + archival snapshot)
- ResearchGate (research project / dataset link)

## Contents

- `code/` — minimal, self-contained examples (PSSM worker + simulator)
- `dashboards/` — Grafana JSON dashboards for TR-2 (PSSM, Layer-S, PhaseGate, Geometry)
- `telemetry/` — JSON Schemas for events (Layer-S / CEI / Q-Bits)
- `science/` — short scientific overview (Quantonica, Q-Bits, Phase Navigation)
- `meta/` — Zenodo / ResearchGate metadata stubs (JSON/YAML)
- `LICENSE` — placeholder license (to be decided)

The full production system includes additional, private components; this
release is focused on the **observability and metrics side** only.
