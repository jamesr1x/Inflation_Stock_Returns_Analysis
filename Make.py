import os
import papermill as pm

os.makedirs("Data/Raw_data", exist_ok=True)
os.makedirs("Data/Cleaned_data", exist_ok=True)
os.makedirs("Outputs/Figures", exist_ok=True)
os.makedirs("Outputs/Tables", exist_ok=True)
os.makedirs("Executed_scripts", exist_ok=True)

# 1. Get raw data
pm.execute_notebook("Scripts/Get_raw_data.ipynb","Executed_scripts/Get_raw_data_output.ipynb",cwd="Scripts")

# 2. Clean data
pm.execute_notebook("Scripts/Clean.ipynb","Executed_scripts/Clean_output.ipynb",cwd="Scripts")

# 3. Run analysis
pm.execute_notebook("Scripts/Analysis.ipynb","Executed_scripts/Analysis_output.ipynb",cwd="Scripts")

print("Project build complete.")