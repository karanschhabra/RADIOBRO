# RADIOBRO

RADIOBRO is an experimental project for building a radiology workflow that reads DICOM images, trains a model with [MONAI](https://monai.io/) and offers a small UI for displaying differential diagnoses. The repository currently contains planning and documentation for the intended system.

## Intended System Overview

1. **DICOM Ingestion**
   - DICOM studies will be uploaded to a designated input directory.
   - A loader will convert the incoming images into an internal format for preprocessing and training.

2. **MONAI-based Training**
   - The project aims to use MONAI to build deep learning pipelines for classification and segmentation.
   - Training will rely on a curated dataset of annotated radiology images.

3. **Differential Diagnoses**
   - Model outputs will include a ranked list of possible diagnoses for each study.
   - Additional heuristics may be used to highlight critical findings.

4. **User Interface**
   - A lightweight UI will display uploaded studies, predicted labels, and diagnostic probabilities.
   - The UI can be served locally for testing or deployed on a server for broader access.

## Setup

The project expects a Python environment with PyTorch and MONAI installed. Example setup commands are below:

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install core dependencies
pip install monai torch torchvision
```

If additional libraries are required (e.g., for the UI or DICOM parsing), install them as needed:

```bash
pip install pydicom fastapi uvicorn
```

## Example Commands

```bash
# Activate the environment and start a dummy training script
source .venv/bin/activate
python train.py --data ./data/dicom

# Optionally, run the development server for the UI
uvicorn app:app --reload
```

These commands assume that `train.py` and `app.py` (or similar scripts) exist. They demonstrate the expected workflow:
1. Ingest DICOM data into `./data/dicom`.
2. Run the training script to produce a model.
3. Launch the UI to view predictions and differential diagnoses.

## Required Datasets and Resources

You will need access to a set of DICOM-formatted radiology studies with ground-truth labels. Examples include:
- [The Cancer Imaging Archive (TCIA)](https://www.cancerimagingarchive.net/)
- Local hospital datasets (ensure you have proper permissions and anonymization).

The dataset should be organized by patient/study/series to be compatible with the ingestion pipeline.

---

This README outlines the high-level goals and example commands. The actual code for ingestion, training, and the UI is still under development.
