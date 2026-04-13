from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)
df = pd.read_csv("final_dataset.csv")
df["state"]    = df["state"].astype(str).str.lower().str.strip()
df["district"] = df["district"].astype(str).str.lower().str.strip()
def simulate(df, district, cut):
    row = df[df["district"] == district].iloc[0]
    impact = cut / 100

    st          = 0.25 * row["st_pct"]
    sc          = 0.15 * row["sc_pct"]
    literacy    = 0.2  * (1 - row["literacy_rate"])
    deprivation = 0.2  * row["deprivation_score"]  * (1 + impact)
    mgnrega     = 0.2  * row["mgnrega_dependency"] * (1 + impact)
    total       = st + sc + literacy + deprivation + mgnrega

    if total < 0.2:   risk = "Low"
    elif total < 0.4: risk = "Moderate"
    elif total < 0.6: risk = "High"
    else:             risk = "Very High"

    breakdown = {
        "ST population":      round(st, 4),
        "SC population":      round(sc, 4),
        "Low literacy":       round(literacy, 4),
        "Deprivation":        round(deprivation, 4),
        "MGNREGA dependency": round(mgnrega, 4),
    }

    return {
        "total":     round(total, 4),
        "risk":      risk,
        "top_group": max(breakdown, key=breakdown.get),
        "breakdown": breakdown,
        "district":  district.title(),
        "cut":       int(cut),
        "st_pct":    round(float(row["st_pct"]) * 100, 1),
        "sc_pct":    round(float(row["sc_pct"]) * 100, 1),
        "literacy":  round(float(row["literacy_rate"]) * 100, 1),
        "dep_score": round(float(row["deprivation_score"]), 3),
        "mgn_dep":   round(float(row["mgnrega_dependency"]), 2),
    }

@app.route("/", methods=["GET", "POST"])
def home():
    result            = None
    selected_district = None
    if request.method == "POST":
        district          = request.form["district"]
        cut               = float(request.form["cut"])
        selected_district = district
        result            = simulate(df, district, cut)
    districts = sorted(df["district"].dropna().unique())
    return render_template(
        "index.html",
        districts=districts,
        result=result,
        selected_district=selected_district,
    )
if __name__ == "__main__":
    app.run(debug=True)