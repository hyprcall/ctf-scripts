# CTF Scripts
Welcome to my collection of CTF scripts.

# Purpose
The purpose of this repo is to document a few different scripts that might be useful to other ctf players. As well as having a neat way for me to access my personal scripts across devices.

# netscan.sh
I find that I always type the same commands when starting a CTF challenge. Therefore, I decided to create a simple script that fits most of my needs for network scanning when attempting a challenge and thus, I designed it to fit my specific use cases.
The scan I usually need to perform is a TCP scan with service and version enumeration. However, I find that performing a UDP scan has also given me critical information.

## Features
 - Allows easy selection of what type of scan you want to perform.
 - Might implement some other integrations soon...

## Usage
```shell
Usage: ./netscan.sh -t <TARGET_IP> [-u] [-s]
 -t Target IP address
 -u Run UDP scan (WARNING: Slow)
 -s Skip TCP Scan (Only run UDP if -u is also set)

# Example for both TCP and UDP scan
./netscan.sh -t 127.0.0.1 -u
# You will be prompted whether you would like a full UDP scan or a top-100 fast
```

## Installation
```shell
git clone https://github.com/hyprcall/ctf-scripts
cd ctf-scripts
chmod +x netscan
```
If you would like to add the script to your path there a few methods. However, this is my recommended method:
```shell
sudo ln -s /path/to/netscan.sh /usr/local/bin/netscan
```

# RSA.py
This script was useful to me when solving an RSA challenge during the National Cyber League (NCL) practice. As long as you have the necessary inputs it works decently. It's not quite as powerful as other tools and cannot handle an extremem large modulus. For that you might need special tools that implement sagemath.



