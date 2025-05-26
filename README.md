# Auction-Guardian
Developing Deep Learning Models to Detect Robot Bidders in Online Auctions for UM FCSIT WID3001 Deep Learning group assignment.

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