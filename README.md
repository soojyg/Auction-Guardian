# Auction-Guardian
Developing Deep Learning Models to Detect Robot Bidders in Online Auctions for UM FCSIT WID3001 Deep Learning group assignment.

## Project Overview

Auction-Guardian is a deep learning project focused on identifying automated bidding systems (bots) in online auctions. The project implements and compares several deep learning approaches:

- Multi-Layer Perceptron (MLP)
- 1D Convolutional Neural Network (1D CNN)
- Recurrent Neural Network with LSTM (RNN-LSTM)

## Repository Structure

```
├── data/
│   ├── engineered/       # Feature engineered datasets
│   ├── processed/        # Cleaned datasets
│   └── raw/              # Original datasets
├── model/                # Trained model files
├── notebooks/           
│   ├── 1DCNN_Model_Training.ipynb
│   ├── DL_EDA.ipynb      # Exploratory Data Analysis
│   ├── MLP_Model_Traininig.ipynb
│   └── RNN_LSTM_Model_Training.ipynb
└── src/                  # Source code
    └── data_preprocessing.py
```

## Setup Instructions

### 1. Git Large File Storage (Git LFS)

This project uses Git LFS to track large CSV files.

Install and initialize Git LFS:
```bash
git lfs install
```
✅ Note: Git LFS only needs to be installed and initialized once per machine.

### 2. Python Virtual Environment Setup
It is recommended to use a virtual environment to manage Python dependencies.

#### Creating a virtual environment:

Run the following command to create a virtual environment named venv:
```bash
python -m venv venv
```

#### Activating the virtual environment:
On Windows (PowerShell):
```bash
.\venv\Scripts\Activate.ps1
```

On Windows (Command Prompt):
```bash
.\venv\Scripts\activate.bat
```

On macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Installing Dependencies
After activating the virtual environment, install the required Python packages using:
```bash
pip install -r requirements.txt
```

### 4. Usage
Always activate the virtual environment before running your scripts.

## Usage

1. Start by exploring the data analysis notebook at [notebooks/DL_EDA.ipynb](notebooks/DL_EDA.ipynb)
2. Review the different model training approaches:
   - [MLP Model Training](notebooks/MLP_Model_Traininig.ipynb)
   - [1D CNN Model Training](notebooks/1DCNN_Model_Training.ipynb)
   - [RNN-LSTM Model Training](notebooks/RNN_LSTM_Model_Training.ipynb)
3. Trained models are saved in the [model](model/) directory

## Models

The project implements three deep learning approaches:

1. **Multi-Layer Perceptron (MLP)**: A traditional neural network approach for classification
2. **1D Convolutional Neural Network (1DCNN)**: Leverages temporal patterns in bidding behavior
3. **Recurrent Neural Network with LSTM**: Designed to capture sequential patterns in bidding history

## Data

The dataset includes auction bidding information with the following characteristics:
- Raw auction data in CSV format
- Processed and cleaned versions for training and testing
- Engineered features to improve model performance