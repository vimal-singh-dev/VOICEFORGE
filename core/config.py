import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SAMPLES_DIR = os.path.join(BASE_DIR, "storage", "samples")
OUTPUTS_DIR = os.path.join(BASE_DIR, "storage", "outputs")

os.makedirs(SAMPLES_DIR, exist_ok=True)
os.makedirs(OUTPUTS_DIR, exist_ok=True)
