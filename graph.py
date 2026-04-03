import matplotlib.pyplot as plt
import os

def generate_graph(vehicles, hour, prediction):

    os.makedirs("static", exist_ok=True)

    plt.figure()

    # 🎨 Set color based on prediction
    if prediction == "High":
        color = "red"
    elif prediction == "Medium":
        color = "orange"
    else:
        color = "green"

    # ✅ Plot ONLY ONE POINT (user input)
    plt.scatter(hour, vehicles, color=color, s=200)

    # Labels
    plt.xlabel("Hour (0-23)")
    plt.ylabel("Vehicle Count")
    plt.title("Traffic Prediction (Live Input)")

    # Highlight the exact point
    plt.annotate(f"({hour}, {vehicles})", (hour, vehicles))

    # Make graph clean
    plt.xlim(0, 24)
    plt.ylim(0, 200)
    plt.grid(True)

    # Save graph
    plt.savefig("static/output_graph.png")
    plt.close()