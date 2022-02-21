# How to run in a restricted environment
Some workarounds need to be performed when running in a restricted environment with access to the [Python IDLE](https://docs.python.org/3/library/idle.html) but without shell access. Below are *rough* instructions on how to run the `process_dataset.py` script in the IDLE.

## Download the script
Without access to *git*, the script needs to be downloaded by navigating to [this repository](https://github.com/bobluppes/medical-dataset-processor) and by clicking `Code` -> `Download ZIP` (green button in the top right). Unpack all files in the *.zip* file to a location on the PC where you have read/write access.

## Preparing the dataset
The IDLE does not allow the use of program arguments. Therefore, the name of the input dataset needs to EXACTLY match the default filename which is `data.csv`. This *.csv* file needs to be placed in the root directory (same folder as `process_dataset.py`).

> ℹ️ **NOTE**: There is already a dummy `data.csv` in the root directory. This file needs to be replaced by the input dataset. The dummy `result.cvs` is automatically overriden by the script.

> ⚠️ **WARNING**: Even though the script does NOT modify the input dataset, it is always a good idea to have a backup in case something goes wrong. Therefore, only run this script on a COPY of the original dataset.

## Running the script
The following are the *rough* steps required to run the script in the IDLE. These steps are not tested. For specific help see [Python IDLE Manual](https://docs.python.org/3/library/idle.html) and [how to run a python script in IDLE](https://stackoverflow.com/a/17247565).

1. The required Python packages in `requirements.txt` (namely Pandas) need to be installed on your system. Without access to *pip*, this should probably be done by your system administrator or IT department. `pip install -r requirements.txt`
2. Open the script in IDLE: `File` -> `Open` -> select `process_dataset.py` from the folder you just extracted
3. Run the script: `Run` -> `Run Module` command (shortcut F5)
4. The results can be found in `result.csv`
