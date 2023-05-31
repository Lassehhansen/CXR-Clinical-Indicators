# CXR-Clinical-Indicators

This repository contains code used to uncover distinct clinical indicators pertaining to Chronic Obstructive Pulmonary Disease (COPD) and heart failure (HF) by means of text mining of patients' medical histories and their correlation with radiological observations in chest x-ray examinations.

The code provided in this repository is designed to be used in conjunction with the ImaGenome dataset, which requires a CITI Certificate to access. If you have obtained the necessary certificate, you can run the code by following these steps:

- Download the scene_graph data from the following location: [https://physionet.org/content/chest-imagenome/1.0.0/#files](https://physionet.org/content/chest-imagenome/1.0.0/#files).
- Place the downloaded scene_graph data in the appropriate directory within your project.
- Make sure you have the required dependencies and libraries installed as specified in the code.
- Adjust any necessary configuration settings or paths within the code to match your setup.

Please note that without the CITI Certificate and access to the ImaGenome dataset, the code provided in this repository cannot be executed.

## Project Organization
The organization of the project is as follows:

```
├── LICENSE                                 <- the license of this code
├── README.md                               <- The top-level README for this project.
├── Paper Text                              <- Folder containing exam paper.
└── Scripts                                 <- The main folder for scripts
    ├── Visualizations                      <- Folder for visualizations
    │       └── Dendogram_vis.rmd           <- R Markdown for making Dendogram
    │       └── TopicDist_vis.rmd           <- R Markdown for making topic distribution 
    │       └── scattertext.ipynb           <- A Python notebook containing scattertext visualization code
    │       └── SHAPvalues.ipynb            <- A Python notebook containing SHAP Value visualization code
    ├── TopicModel   
    │       └── TopicModel.ipynb            <- Python Notebook for making Topic Model
    ├── LogReg                              
    │       └── LogModel_Plot_Tables.Rmd    <- R Markdown for making Logistic Regression (visualizations / tables included)
    ├── Preprocessing         
    │       └── Preprocessing_ImaGenome.py  <- Python script for preprocessing ImaGenome .json files
    └── RadBERT       
            └── finetuneRadBERT.ipynb       <- Notebook for fine-tuning RadBERT for Disease classification
```
