"""Minimal PSSM window simulator for research demos."""
import json
import random

def generate_window(mode='normal', steps=4):
  window = []
  base_kappa = 0.8 if mode == 'normal' else 0.6
  base_c = 0.9 if mode == 'normal' else 0.75
  for i in range(steps):
      dphi = random.uniform(0.05, 0.4) if mode == 'normal' else random.uniform(0.2, 0.9)
      kappa = base_kappa + random.uniform(-0.05, 0.05)
      c = base_c + random.uniform(-0.05, 0.05)
      window.append({
          "step": i+1,
          "kappa": kappa,
          "coherence": c,
          "phase_delta": dphi,
      })
  return window

def main():
  payload = {
      "session": "demo-research-1",
      "window": generate_window(mode='drift')
  }
  print(json.dumps(payload))

if __name__ == "__main__":
  main()
