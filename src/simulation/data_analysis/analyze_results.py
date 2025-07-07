import pandas as pd
import matplotlib.pyplot as plt
import os

# Path to the simulation results CSV
RESULTS_CSV = "../../../data/simulation_results.csv"

# Output directory for plots
PLOTS_DIR = "./plots"

def analyze_and_visualize_results():
    """Reads simulation results, performs analysis, and generates visualizations."""
    if not os.path.exists(RESULTS_CSV):
        print(f"Error: Results file not found at {RESULTS_CSV}. Please run dynamic_tls.py first.")
        return

    df = pd.read_csv(RESULTS_CSV)

    os.makedirs(PLOTS_DIR, exist_ok=True)

    print("Generating plots...")

    # Plot 1: Average Waiting Time over Time
    plt.figure(figsize=(12, 6))
    plt.plot(df["step"], df["avg_waiting_time"], label="Average Waiting Time")
    plt.xlabel("Simulation Step")
    plt.ylabel("Average Waiting Time (s)")
    plt.title("Average Waiting Time Over Simulation Steps")
    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join(PLOTS_DIR, "avg_waiting_time.png"))
    plt.close()
    print(f"Saved {os.path.join(PLOTS_DIR, 'avg_waiting_time.png')}")

    # Plot 2: Average Speed over Time
    plt.figure(figsize=(12, 6))
    plt.plot(df["step"], df["avg_speed"], label="Average Speed")
    plt.xlabel("Simulation Step")
    plt.ylabel("Average Speed (m/s)")
    plt.title("Average Speed Over Simulation Steps")
    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join(PLOTS_DIR, "avg_speed.png"))
    plt.close()
    print(f"Saved {os.path.join(PLOTS_DIR, 'avg_speed.png')}")

    # Plot 3: Vehicle Count over Time
    plt.figure(figsize=(12, 6))
    plt.plot(df["step"], df["vehicle_count"], label="Vehicle Count")
    plt.xlabel("Simulation Step")
    plt.ylabel("Number of Vehicles")
    plt.title("Vehicle Count Over Simulation Steps")
    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join(PLOTS_DIR, "vehicle_count.png"))
    plt.close()
    print(f"Saved {os.path.join(PLOTS_DIR, 'vehicle_count.png')}")

    print("Data analysis and visualization complete.")

if __name__ == "__main__":
    analyze_and_visualize_results()


