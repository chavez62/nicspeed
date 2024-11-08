import psutil
import platform
import subprocess

def get_nic_speed(interface_name=None):
    """Function to get the NIC speed of a specified interface."""
    # Method 1: Using psutil to get network stats
    net_if_stats = psutil.net_if_stats()
    
    if interface_name and interface_name in net_if_stats:
        speed = net_if_stats[interface_name].speed
        print(f"NIC Speed of {interface_name}: {speed} Mbps (using psutil)")
    else:
        print("\nAvailable interfaces and their speeds (if known):")
        for interface, stats in net_if_stats.items():
            print(f"{interface}: {stats.speed} Mbps (using psutil)")

    # Method 2: OS-specific command fallback
    os_type = platform.system()
    if interface_name:
        print(f"\nChecking NIC speed using system command for {os_type}...")
        try:
            if os_type == "Windows":
                # Windows PowerShell command to get NIC speed
                command = f'Get-NetAdapter -Name "{interface_name}" | Select-Object -ExpandProperty LinkSpeed'
                result = subprocess.check_output(["powershell", "-Command", command], text=True)
                print(f"{interface_name} NIC Speed: {result.strip()} (using PowerShell)")

            elif os_type == "Linux":
                # Linux `ethtool` command to get NIC speed
                result = subprocess.check_output(f"ethtool {interface_name} | grep Speed", shell=True, text=True)
                print(f"{interface_name} NIC Speed: {result.strip()} (using ethtool)")

            elif os_type == "Darwin":  # macOS
                # macOS `networksetup` command to check NIC link speed
                command = f"networksetup -getMedia {interface_name}"
                result = subprocess.check_output(command, shell=True, text=True)
                print(f"{interface_name} NIC Speed: {result.strip()} (using networksetup)")

        except Exception as e:
            print(f"Error obtaining NIC speed for {interface_name} using system command: {e}")

if __name__ == "__main__":
    # List available interfaces from psutil
    print("Available network interfaces:")
    for interface in psutil.net_if_stats().keys():
        print(f"- {interface}")

    # Prompt user for interface name
    interface_name = input("\nEnter the exact name of the interface you want to check: ")
    get_nic_speed(interface_name)

    input("\nPress Enter to exit...")
