# CXR-Clinical-Indicators

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
