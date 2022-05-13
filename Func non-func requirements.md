# Functional and non-functional requirements document

This file outlines the functional and non-functional requirements for our project.
Defining it shortly: 
 1. The first type of requirements describe what our scripts need to be doing, what outcomes we expect and based on what input data,
 2. Non-functional requirements describe the how, the limits and general utility of the system.

## Functional requirements:

### Data exploration and preparation 
- Reads the given input convictions data
- Provides exploratory data analysis outprints, which serve to inform the user of the underlying data distributions and features
- Cleans the data: removes redundancy, drops useless data, handles outliers, missing values
- Checks for collinearity, unimportant features and other factors which will make later supervised learning perform badly
- Generates new features by transforming data present in the dataset (feature enginnering)
- Downloads stock prices data and joins it to the dataset
- Monitors the amount of observations throughout the analysis, data pruning and joins, making sure that enough observations remain to perform a robust analysis
- Saves the final dataset to a file which will be used in further steps

### Simple analysis harness
- Imports proper libraries needed for the analysis making sure there are no conflicts and everything works well
- Opens up the dataset prepared earlier
- Performs further data analysis focused on elements connected to the planned type of regressor to be used
- Further transforms the data to fit the API of used ML library
- Selects a final set of independent features
- Prepares a class and/or method and/or script responsible for performing train, test split and error calculation based on this approach
- Prepares a class and/or method and/or script responsible for performing cross-validation and error calculation based on this approach
- Trains a dummy model, which takes a naive approach to predicting the target variable
- Creates a pdf report summarising everything done by the analysis harness, which outlines the statistical properties of the created model/models

### Initial modelling
- Trains a linear regression model, which would ideally be better than dummy model
- Validates the model by: checking the prediction results on test subdataset, performing crossvalidation
- Saves the result of model creation and evaluation to a pdf report
- Presents results of prediction using statistical means - graphs, numerical statistics

### Advanced modelling
- Trains 3 advanced ML models, possible options: LSTM, RNN, XGBoost, RandomForest, (regression made with RL?) etc.
- Validates the models by: checking the prediction results on test subdataset, performing crossvalidation
- Compares all models between each other, dummy and linear model, observes how do the models perform on different investment horizons
- Chooses the best model based on performance in general, chooses the best model for each investment horizon separately
- Points out where improvements could be made, what went wrong and what are the tools to correct
- Performs stability and sensitivity analysis w.r.t baseline model and investment horizons
- Saves the result of model creation and evaluation to a pdf report
- Presents results of prediction using statistical means - graphs, numerical statistics

## Non-functional requirements:

- All of the analysis and modelling should be able to handle big amounts of data, be prepared to be retrained on a larger dataset, which could be available on a later date (scalability)
- Code needs to be modular, parts of it running in jupyter notebooks when clarity and partial results are important, transformed to script in the end for models
- In notebooks 90% of cells should run under 2 seconds, only model creating and data downloading are allowed take more than 2s to execute
- Code should be structured to enable refactoring, be clear to other users and enable easy maintainability
- Script code should be sufficiently commented where needed, notebooks need to have markdown cells explaining what's going on, summarising steps of the analysis
- Code should be availabale on GitHub, it's aim is to be pulled from the repository and ran on users machine
- Project progression will be tracked in README.md in the repository
- Additions to the repository should be managed using atom-level commits and branches to properly track software development
- Users should regurarly pull the repository and back it up in case anything goes badly
