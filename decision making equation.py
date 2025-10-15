import streamlit as st
import math

st.title("🧠 Decision Energy Model")
st.write("Quantify how attention, emotions, expectations, memories, and perspective shape your outcome probability.")

# Replace input() with sliders
attention = st.slider("⏱️ How much time can you afford to give? (1=instant, 0=a month)", 0.0, 1.0, 0.5)
emotions = st.slider("💖 What percentage of emotions are in play? (0=risk of awfulness, 1=risk of awesome)", 0.0, 1.0, 0.5)
expectations = st.slider("🎯 Immediate vs delayed gratification (1 vs 0)", 0.0, 1.0, 0.5)
memories = st.slider("🧩 What memories do you have of past outcomes? (0=bad, 1=good)", 0.0, 1.0, 0.5)
perspective = st.slider("🌌 Quantify perspectives (0=superficial, 1=spiritual)", 0.0, 1.0, 0.5)

# Core calculation
weight = attention + emotions + expectations + memories + perspective
bias = -0.5 * weight
Z = weight + bias
p = 1 / (1 + math.exp(-Z))

# Display results
st.write("### Results")
st.write(f"**Z =** {Z:.3f}")
st.write(f"**Probability (p) =** {p:.3f}")

# Optional interpretation
if p < 0.3:
    st.warning("Outcome seems uncertain — more balance may be needed.")
elif p < 0.7:
    st.info("Moderate probability — outcome depends on focus and alignment.")
else:
    st.success("High probability — strong alignment between intent and reality!")



