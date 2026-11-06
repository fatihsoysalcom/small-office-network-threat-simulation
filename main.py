import random
import time

# This script simulates a very basic, vulnerable small office network.
# It demonstrates how common, easily exploitable vulnerabilities can be.

class NetworkDevice:
    def __init__(self, name, vulnerability_level):
        self.name = name
        self.vulnerability_level = vulnerability_level # 0-10, higher is more vulnerable
        self.is_compromised = False

    def __str__(self):
        status = "Compromised" if self.is_compromised else "Secure"
        return f"{self.name} ({status})"

def simulate_attack(devices):
    """Simulates a random attack attempt on a device."""
    target_device = random.choice(devices)

    # Attack success is more likely on more vulnerable devices
    attack_chance = random.randint(1, 10) + target_device.vulnerability_level

    if attack_chance > 7: # Threshold for successful compromise
        if not target_device.is_compromised:
            print(f"\n*** ATTACK SUCCESSFUL! ***")
            print(f"Attacker exploited a vulnerability on: {target_device.name}")
            target_device.is_compromised = True
            return True
    else:
        print(f"Attack attempt on {target_device.name} failed.")
    return False

def main():
    print("--- Small Office Network Threat Simulation ---")
    print("Simulating a network with common vulnerabilities.")

    # Devices representing typical small office equipment
    devices = [
        NetworkDevice("Router", 5),          # Moderate vulnerability
        NetworkDevice("Printer", 8),         # High vulnerability (often unpatched)
        NetworkDevice("Workstation 1", 3),   # Lower vulnerability (but still a target)
        NetworkDevice("Workstation 2", 4),
        NetworkDevice("File Server", 6)      # Moderate to high vulnerability
    ]

    print("\nInitial Network State:")
    for device in devices:
        print(device)

    print("\nStarting attack simulation (Ctrl+C to stop)...")

    compromised_count = 0
    try:
        while True:
            if simulate_attack(devices):
                compromised_count += 1
                # A compromised device can lead to further compromises (not simulated here for simplicity)

            # Check if all devices are compromised
            if all(d.is_compromised for d in devices):
                print("\nAll devices have been compromised! Network is fully breached.")
                break

            time.sleep(random.uniform(1, 3)) # Wait before next attack attempt

    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")

    print("\nFinal Network State:")
    for device in devices:
        print(device)

    print(f"\nTotal devices compromised: {compromised_count}")

if __name__ == "__main__":
    main()
