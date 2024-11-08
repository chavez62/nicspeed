# NIC Speed Checker

This Python script allows you to check the Network Interface Card (NIC) speed of a computer. It uses `psutil` to retrieve network interface statistics and provides platform-specific methods for Windows, Linux, and macOS to check NIC speed via command-line tools when necessary.

## Features

- Lists available network interfaces and their speeds (if known) using `psutil`.
- Allows users to select a specific network interface for detailed speed checking.
- Uses OS-specific commands to provide more accurate NIC speeds when possible:
  - **Windows**: PowerShell
  - **Linux**: `ethtool`
  - **macOS**: `networksetup`

## Prerequisites

Make sure you have Python 3.x installed. You'll also need the `psutil` library, which can be installed via pip:

```bash
pip install psutil
```

- git clone https://github.com/yourusername/nic-speed-checker.git
- cd nic-speed-checker

## Run the script
python nic_speed_checker.py
