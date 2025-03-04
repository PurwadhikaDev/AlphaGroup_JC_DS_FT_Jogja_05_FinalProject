import os
import pandas as pd
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model dari file pickle
with open("best_model.pkl", "rb") as file:
    data = pickle.load(file)

model = data["model"]
threshold = data["threshold"]

# Pastikan folder 'static' ada untuk menyimpan file CSV
if not os.path.exists("static"):
    os.makedirs("static")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    csv_link = None

    if request.method == "POST":
        if "file" in request.files:
            file = request.files["file"]
            if file.filename == "":
                return render_template("index.html", error="Tidak ada file yang diunggah.")

            try:
                df = pd.read_csv(file)

                # Pastikan urutan kolom sesuai dengan model
                features = [
                    "age", "age_group", "job", "marital", "education", "housing", "loan",
                    "contact", "month", "day_of_week", "campaign", "pdays", "previous",
                    "poutcome", "anomali_cpp", "emp.var.rate", "cons.price.idx",
                    "cons.conf.idx", "euribor3m", "nr.employed"
                ]

                # Periksa apakah semua kolom yang dibutuhkan ada di file CSV
                missing_cols = [col for col in features if col not in df.columns]
                if missing_cols:
                    return render_template("index.html", error=f"Kolom berikut hilang di file CSV: {missing_cols}")

                df = df[features]

                # Prediksi probabilitas
                prob = model.predict_proba(df)[:, 1]

                # Tentukan hasil berdasarkan threshold
                df["prediction"] = np.where(prob >= threshold, "Yes", "No")

                # Simpan hasil prediksi
                csv_path = "static/predictions.csv"
                df.to_csv(csv_path, index=False)

                return render_template("index.html", csv_link=csv_path)

            except Exception as e:
                return render_template("index.html", error=f"Terjadi kesalahan: {str(e)}")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)