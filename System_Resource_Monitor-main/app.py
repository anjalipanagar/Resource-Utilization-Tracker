import streamlit as st
import psutil
import pandas as pd
import time
import matplotlib.pyplot as plt

st.set_page_config(page_title="Advanced System Monitor", layout="wide")

st.title("Advanced System Monitor + Memory Simulator")

# =========================
# SESSION STATE (for graphs)
# =========================
if "cpu_history" not in st.session_state:
    st.session_state.cpu_history = []

if "mem_history" not in st.session_state:
    st.session_state.mem_history = []

# =========================
# CPU + MEMORY DATA
# =========================
cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()

st.session_state.cpu_history.append(cpu)
st.session_state.mem_history.append(memory.percent)

# Keep last 20 values
st.session_state.cpu_history = st.session_state.cpu_history[-20:]
st.session_state.mem_history = st.session_state.mem_history[-20:]

# =========================
# ALERTS 🚨
# =========================
if cpu > 80:
    st.error(f"⚠️ High CPU Usage: {cpu}%")

if memory.percent > 80:
    st.error(f"⚠️ High Memory Usage: {memory.percent}%")

# =========================
# GRAPH SECTION
# =========================
st.subheader("Live CPU & Memory Usage")

chart_data = pd.DataFrame({
    "CPU %": st.session_state.cpu_history,
    "Memory %": st.session_state.mem_history,
})

# Animated/streaming style chart from Streamlit; updates each rerun.
st.line_chart(chart_data, height=300, use_container_width=True)

# add stats cards for peaks and average values
col_cpu, col_mem = st.columns(2)
with col_cpu:
    st.metric("CPU Current", f"{cpu}%", delta=f"{cpu - (st.session_state.cpu_history[-2] if len(st.session_state.cpu_history) > 1 else cpu)}%")
    st.write(f"Max CPU (last 20s): {max(st.session_state.cpu_history)}%")
    st.write(f"Avg CPU (last 20s): {sum(st.session_state.cpu_history)/len(st.session_state.cpu_history):.1f}%")
with col_mem:
    st.metric("Memory Current", f"{memory.percent}%", delta=f"{memory.percent - (st.session_state.mem_history[-2] if len(st.session_state.mem_history) > 1 else memory.percent)}%")
    st.write(f"Max Memory (last 20s): {max(st.session_state.mem_history)}%")
    st.write(f"Avg Memory (last 20s): {sum(st.session_state.mem_history)/len(st.session_state.mem_history):.1f}%")

# =========================
# BASIC STATS
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("CPU Usage", f"{cpu}%")

with col2:
    st.metric("Memory Usage", f"{memory.percent}%")

with col3:
    disk = psutil.disk_usage('/')
    st.metric("Disk Usage", f"{disk.percent}%")

# =========================
# PROCESS TABLE
# =========================
st.subheader("Process & Thread Analysis")

process_list = []

for proc in psutil.process_iter(['pid','name','cpu_percent','memory_percent','num_threads']):
    try:
        process_list.append(proc.info)
    except:
        pass

df = pd.DataFrame(process_list)
df = df.sort_values(by="cpu_percent", ascending=False)

st.dataframe(df[['pid','name','cpu_percent','memory_percent','num_threads']].head(10), use_container_width=True)

# =========================
# MEMORY SIMULATOR
# =========================
st.subheader("🧠 Page Replacement Simulator")

pages_input = st.text_input("Enter Page Reference (space separated)", "7 0 1 2 0 3 0 4")
frames = st.number_input("Number of Frames", min_value=1, max_value=10, value=3)

pages = list(map(int, pages_input.split()))

# FIFO
def fifo(pages, frames):
    frame = []
    faults = 0
    for p in pages:
        if p not in frame:
            if len(frame) < frames:
                frame.append(p)
            else:
                frame.pop(0)
                frame.append(p)
            faults += 1
    return faults

# LRU
def lru(pages, frames):
    frame = []
    recent = []
    faults = 0
    for p in pages:
        if p not in frame:
            if len(frame) < frames:
                frame.append(p)
            else:
                lru_page = recent.pop(0)
                frame.remove(lru_page)
                frame.append(p)
            faults += 1
        else:
            recent.remove(p)
        recent.append(p)
    return faults

fifo_faults = fifo(pages, frames)
lru_faults = lru(pages, frames)

st.write(f"FIFO Page Faults: {fifo_faults}")
st.write(f"LRU Page Faults: {lru_faults}")

# =========================
# AUTO REFRESH
# =========================
time.sleep(2)
st.rerun()