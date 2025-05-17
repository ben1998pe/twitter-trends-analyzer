from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

def generar_grafico(df):
    top = df["Tendencia"].value_counts().head(10)
    plt.figure(figsize=(8,4))
    top.plot(kind="barh", color="#4CAF50")
    plt.xlabel("Frecuencia")
    plt.title("Tendencias más repetidas")
    plt.gca().invert_yaxis()

    buffer = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    imagen_base64 = base64.b64encode(buffer.read()).decode()
    buffer.close()
    return imagen_base64

@app.route("/", methods=["GET"])
def index():
    try:
        df = pd.read_csv("data/tendencias_peru.csv", encoding="utf-8-sig")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Fecha y hora", "Tendencia"])

    busqueda = request.args.get("busqueda", "").lower()
    fecha = request.args.get("fecha", "")

    if busqueda:
        df = df[df["Tendencia"].str.lower().str.contains(busqueda)]
    if fecha:
        df = df[df["Fecha y hora"].str.contains(fecha)]

    df = df.tail(100)
    grafico = generar_grafico(df)

    return render_template("index.html", data=df.to_dict(orient="records"),
                           busqueda=busqueda, fecha=fecha, grafico=grafico)

if __name__ == "__main__":
    app.run(debug=True)
