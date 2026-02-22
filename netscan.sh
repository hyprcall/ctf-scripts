#!/bin/bash
# Rustscan to Nmap script for quick and easy scans during CTFs (e.g.,HTB or THM)

# Default Variables
TARGET=""
RUN_UDP=false
SKIP_TCP=false

# Check if the user has the necessary configuration to utilize the script
permissions_check() {
	# Sanity Check: Is TARGET set?
	if [[ -z "$TARGET" ]]; then
		echo "[X] Logic Error: Target is not defined."
		return 1
	# Pre-Check: Nmap installed?
	fi
	# Dependency Checks
	local missing_dep=0
	for tool in nmap rustscan; do
		if ! command -v "$tool" &> /dev/null; then
			echo "[X] $tool is not installed."
			missing_dep=1
		fi
	done

	if [[ $missing_dep -eq 1 ]]; then
		echo "[!] Please install missing tools."
		return 1
	fi

	# Connectivity Check (Soft-Fail)
	if ! ping -c 1 -W 1 "$TARGET" &> /dev/null; then
		echo "[!] WARNING: Target $TARGET is not responding to Ping."
		echo "	(Proceeding anyway, as firewall might block ICMP)"
	else
		echo "[+] Target is reachable."
	fi

	# Privileges Check
	if ! nmap -sU -p 53 127.0.0.1 -oN /dev/null &> /dev/null; then
		echo "[X] Nmap lacks privileges to run UDP/Raw scans."
		
		# Root?
		if [[ $EUID -ne 0 ]]; then
			echo "    -> You are not running as root (try 'sudo')."
		fi

		# Check specific capabilities on the binary location
		NMAP_PATH=$(command -v nmap)
		if ! getcap "$NMAP_PATH" | grep -q "cat_net_raw"; then
			echo "   -> Nmap binary ($NMAP_PATH) is missing capabilities."
			echo "   -> Fix: sudo setcap cap_net_raw,cap_net_admin,cap_net_bind_service+eip $NAMP_PATH"
		fi

		return 1
	else
		echo "[+] Privileges verified (Ready for TCP & UDP)."
	fi
}

usage() {
	echo "Usage: $0 -t <TARGET_IP> [-u] [-s]"
	echo " -t Target IP address"
	echo " -u Run UDP scan (WARNING: Slow)"
	echo " -s Skip TCP Scan (Only run UDP if -u is also set)"
	exit 1
}

# Argument Parsing
while getopts "t:us" opt; do
	case ${opt} in
		t) TARGET=$OPTARG ;;
		u) RUN_UDP=true ;;
		s) SKIP_TCP=true ;;
		*) usage;;
	esac
done

# Validate Target
if [[ -z "$TARGET" ]]; then
	echo "[!] Target is required."
	usage
fi

# Run Checks
echo "[*]Checking permissions and requirements..."
if ! permissions_check; then
	exit 1
fi

# TCP Scan Logic (Rustscan)
if [[ "$SKIP_TCP" == "false" ]]; then
	echo "[*] Starting TCP Scan with Rustscan..."
	# Rustscan finds ports and passes them to nmap for Service/Version detection
	rustscan --ulimit 5000 -a "$TARGET" -- -sC -sV -oN "tcp_scan_${TARGET}_.txt"
else
	echo "[*] Skipping TCP Scan."
fi

# UDP Scan Logic (Nmap)
if [[ "$RUN_UDP" == "true" ]]; then
	echo "[!] WARNING: UDP scans can take a significant amount of time."
	# Standard UDP scan logic
	read -p "Do you want to run a full UDP scan (y) or fast top-100 (f)? [y/f]: " udp_choice
	if [[ "$udp_choice" == "f" ]]; then
	nmap -sU --top-ports 100 "$TARGET" -oN "udp_scan_top100_${TARGET}_.txt"
	else
		nmap -sU "$TARGET" -oN "udp_scan_${TARGET}_.txt"
	fi
	
fi

echo "[SUCCESS] Scans completed."

