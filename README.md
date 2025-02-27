# RPi Resource Logging

RPi Resource Logging is a tool for monitoring and collecting system resource statistics on Raspberry Pi. The program logs information about CPU, memory, disk, and network usage, helping track system performance and react to potential issues.

## Features

- Logging system resource usage:
  - CPU
  - Memory
  - Disk
  - Network connections
- Display logs on screen
- Ability to configure the data collection interval.
- Easy integration with external analytics tools or databases for log storage.

## Requirements

- Raspberry Pi running Raspbian or similar OS.
- Python 3.x.
- Libraries:
  - psutil — for collecting system resource data.
  - time — for scheduling data collection intervals.

## Installation

1. Clone the repository:
   

bash
   git clone https://github.com/OleksandrPodynihlazov/RPi_resource_logging.git
   cd RPi_resource_logging

    Install dependencies:

    pip install -r requirements.txt

## Usage

Run the script to start logging system resources:

python3 resource_logging.py

