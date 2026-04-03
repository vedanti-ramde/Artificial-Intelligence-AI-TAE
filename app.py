from flask import Flask, request
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from graph import generate_graph

app = Flask(__name__)

data = pd.read_csv("traffic_data.csv")

X = data[["vehicle_count", "hour"]]
y = data["congestion"]

model = GaussianNB()
model.fit(X, y)

@app.route("/")
def home():
    return"""

    <head>
    <style>
    body{
    font-family: Arial;
    background:url('/static/veda.png');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;

    text-align:center;
    padding:50px;
    }
        .box{
            background:pink;
            padding:30px;
            width:400px;
            margin:auto;
            border-radius:15px;
            box-shadow:0px 5px 15px gray;
        }

        h1{
            color:#333;
        }

        input{
            width:80%;
            padding:10px;
            margin:10px;
            border-radius:8px;
            border:1px solid gray;
        }

        button{
            padding:12px 20px;
            background:#4CAF50;
            color:white;
            border:none;
            border-radius:8px;
            font-size:16px;
            cursor:pointer;
        }

        button:hover{
            background:red;
        }
    </style>
</head>

    <body>
        <div class="box">
        <h1>🚦 Intelligent Traffic Congestion Predictor</h1>

        <form action="/predict" method="post">

        <label>Location:</label><br> 
        <input type="text" name="location" placeholder="Enter city/area" required><br>

        <label>Vehicle Count:</label><br>
        <input type="number" name="vehicles" required><br><br>

        <label>Hour (0-23):</label><br>
        <input type="number" name="hour" required><br><br>

        <button type="button" onclick="getLocation()">📍Use My Location</button>
        
        <button type="submit">Predict Traffic</button>

        </form>
        </div>
    </body>
    </html>
    </div>

<script>
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            let lat = position.coords.latitude;
            let lon = position.coords.longitude;

            document.querySelector('input[name="location"]').value = lat + "," + lon;
        });
    } else {
        alert("Geolocation not supported");
    }
}
</script>

</body>
</html>

    """

@app.route("/predict", methods=["POST"])
def predict():

    location = request.form["location"]
    vehicles = int(request.form["vehicles"])
    hour = int(request.form["hour"])

    # CREATE GRAPH 
    # First decide result
    if vehicles > 120 or (7 <= hour <= 9): 
        prediction = "High"
        result = "🚨 High Traffic Congestion" 
        color = "red"

    elif vehicles > 60: 
        prediction = "Medium"
        result = "⚠ Medium Traffic" 
        color = "orange"

    else: 
        prediction = "Low"
        result = "✅ Low Traffic" 
        color = "green"

# THEN generate graph
    generate_graph(vehicles, hour, prediction)

# Only one graph now
    graph = "output_graph.png"


    return f"""
    <html> 
    <body style="font-family:Arial;text-align:center;background:#f2f2f2;padding-top:100px;"> 
    <h2>📍 Location: {location}</h2>
    <h1 style="color:red;">{result}</h1> 
    <img src="/static/{graph}" width="500">
    <br><br>
    <a href="/" style=" 
        padding:12px 20px; 
        background:;
        color:white; red
        text-decoration:none; 
        border-radius:8px; 
        font-size:16px; 

    "">Go Back</a> 
    </body> 
    </html> 
    """
if __name__ == "__main__":
    app.run(debug=True)