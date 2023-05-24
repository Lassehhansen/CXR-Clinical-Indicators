# CXR-Clinical-Indicators

## Project Organization
The organization of the project is as follows:

```
├── LICENSE                    <- the license of this code
├── README.md                  <- The top-level README for this project.
├── .github            
│   └── workflows              <- workflows to automatically run when code is pushed
│   │    └── run.sh        
└── NER                        <- The main folder for scripts
    ├── document_similarity    <- Functionf for Document Similarity implementation
    ├── figure                 <- Folder containing figures    
    ├── training   
    │   └── config.cdf         <- The config file used for training
    └── preprocessing          <- Folder containing preprocessing scripts
        └── main.py            <- Main file for running XML preprocessing of legal documents
        └── xml_class.py       <- Class for processing XML files 
```
