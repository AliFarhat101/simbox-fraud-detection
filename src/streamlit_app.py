from pathlib import Path
import duckdb
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "database" / "simbox.duckdb"

# ----------------------------
# DB connection
# ----------------------------
con = duckdb.connect(str(DB_PATH))


st.title("SIMBox Fraud CDR SQL Explorer")

st.write("Run SQL queries directly on your CDR datasets (DuckDB backend).")

# ----------------------------
# SQL input
# ----------------------------
query = st.text_area(
    "Write your SQL query here:",
    height=200,
    value="SELECT * FROM cdr_all LIMIT 10;"
)

# ----------------------------
# Run button
# ----------------------------
if st.button("Run Query"):
    try:
        df = con.execute(query).fetchdf()
        st.success(f"Returned {len(df)} rows")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error: {str(e)}")