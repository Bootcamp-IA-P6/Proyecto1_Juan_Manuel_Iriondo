import os

import pandas as pd
import streamlit as st

import logs
import poo_main

st.set_page_config(page_title="F5 Taximeter", page_icon="🚕", layout="centered")

CAR_TRACK_CSS = """
<style>
.track {
    position: relative;
    width: 100%;
    height: 60px;
    background: linear-gradient(to bottom, #cfd8dc 55%, #607d8b 55%);
    border-radius: 8px;
    overflow: hidden;
    margin: 10px 0 20px 0;
}
.car {
    position: absolute;
    bottom: 8px;
    left: 0;
    font-size: 32px;
}
.car.moving {
    animation: drive 2.2s linear infinite;
}
@keyframes drive {
    0%   { left: 0%; }
    50%  { left: calc(100% - 40px); }
    100% { left: 0%; }
}
</style>
"""

# --- Inicialización de la app (solo una vez por sesión) ---
if "app" not in st.session_state:
    logger = logs.init_log()
    logger.debug("LOG started.")

    historical_path = os.path.join("historical", "historical.csv")
    os.makedirs(os.path.dirname(historical_path), exist_ok=True)
    open(historical_path, "a", encoding="utf-8").close()

    st.session_state.app = poo_main.TaximeterApp(logger, historical_path)
    st.session_state.last_summary = None

app = st.session_state.app
trip = app.trip

st.title("🚕 F5 Taximeter")

col_start, col_move, col_stop, col_finish = st.columns(4)

if col_start.button("▶️ Start", width="stretch"):
    try:
        trip.start()
        st.session_state.last_summary = None
    except RuntimeError as e:
        st.error(str(e))

if col_move.button("🟢 Move", width="stretch"):
    try:
        trip.change_state("moving")
    except RuntimeError as e:
        st.error(str(e))

if col_stop.button("🔴 Stop", width="stretch"):
    try:
        trip.change_state("stopped")
    except RuntimeError as e:
        st.error(str(e))

if col_finish.button("🏁 Finish", width="stretch"):
    try:
        summary = trip.finish()
        app.log_historical(summary)
        st.session_state.last_summary = summary
    except RuntimeError as e:
        st.error(str(e))

if trip.active:
    st.info(f"Viaje en curso — estado actual: **{trip.state}**")
else:
    st.warning("No hay ningún viaje activo. Pulsa **Start** para comenzar.")

is_moving = trip.active and trip.state == "moving"
car_class = "car moving" if is_moving else "car"

st.markdown(CAR_TRACK_CSS, unsafe_allow_html=True)
st.markdown(f'<div class="track"><div class="{car_class}">🚕</div></div>', unsafe_allow_html=True)

if st.session_state.last_summary:
    summary = st.session_state.last_summary
    st.subheader("Resumen del último viaje")
    c1, c2, c3 = st.columns(3)
    c1.metric("Tiempo parado", f"{summary['stopped']:.1f} s")
    c2.metric("Tiempo en movimiento", f"{summary['moving']:.1f} s")
    c3.metric("Importe total", f"€{summary['fare']:.2f}")

st.divider()

st.subheader("📋 Histórico de viajes")
if os.path.getsize(app.historical_path) > 0:
    df = pd.read_csv(app.historical_path)
    df.columns = df.columns.str.strip().str.replace(" ", "")
    st.dataframe(df, width="stretch")
else:
    st.caption("Todavía no hay viajes registrados.")

st.subheader("📄 Histórico de logs")
log_path = os.path.join("logs", "app.log")
if os.path.exists(log_path) and os.path.getsize(log_path) > 0:
    with open(log_path, "r", encoding="utf-8") as f:
        log_lines = f.readlines()

    num_lines = st.slider("Número de líneas a mostrar", 10, 200, 50)
    st.code("".join(log_lines[-num_lines:]), language="log")
else:
    st.caption("Todavía no hay logs registrados.")
