import streamlit as st
import time
import random

st.set_page_config(page_title="For Shona ❤️", page_icon="💘", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = 1

# ---------------- PAGE 1 ----------------
if st.session_state.page == 1:
    st.markdown("<h1 style='text-align:center;'>Welcome Shona 😏</h1>", unsafe_allow_html=True)
    time.sleep(2)
    st.session_state.page = 2
    st.rerun()


# ---------------- PAGE 2 ----------------
elif st.session_state.page == 2:
    st.markdown("<h2 style='text-align:center;'>Loading important content…</h2>", unsafe_allow_html=True)
    bar = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        bar.progress(i+1)

    st.success("Loaded: Shona.exe ❤️")

    if st.button("Open"):
        st.session_state.page = 3
        st.rerun()


# ---------------- PAGE 3 ----------------
elif st.session_state.page == 3:
    st.markdown("<h1 style='text-align:center;'>Fact Check Time 🧐</h1>", unsafe_allow_html=True)
    st.write("True or False:")
    st.write("『 Shona is the cutest person alive 』")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("True 😌"):
            st.session_state.page = 4
            st.rerun()

    with col2:
        if st.button("False 🙄"):
            st.warning("Wrong answer detected 🚨")
            st.info("System override: Forcing TRUE 😏")


# ---------------- PAGE 4 ----------------
elif st.session_state.page == 4:
    st.markdown("<h1 style='text-align:center;'>Breaking News 📰</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>A guy has been thinking about Shona a little too much.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Authorities say: it's me 😔💖</p>", unsafe_allow_html=True)

    if st.button("Go to next disaster 👉"):
        st.session_state.page = 5
        st.rerun()


# ---------------- PAGE 5 ----------------
elif st.session_state.page == 5:
    st.markdown("<h1 style='text-align:center;'>Important Question ⚠️</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;color:pink;'>Shona, will you be my Valentine? 💌</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("YES 💖"):
            st.session_state.page = 6
            st.rerun()

    with col2:
        st.markdown("""
        <style>
        #noBtn {
            position: relative;
            padding: 10px 25px;
            background-color: #ff4b4b;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
        }
        </style>

        <button id="noBtn">NO ❌</button>

        <script>
        const btn = document.getElementById("noBtn");
        btn.onmouseover = function() {
            const x = Math.floor(Math.random() * 200) - 100;
            const y = Math.floor(Math.random() * 200) - 100;
            btn.style.transform = `translate(${x}px, ${y}px)`;
        };
        </script>
        """, unsafe_allow_html=True)


# ---------------- PAGE 6 (FINAL) ----------------
elif st.session_state.page == 6:
    st.balloons()
    st.markdown("<h1 style='text-align:center;'>LET'S GOOOOOO 🎉💖</h1>", unsafe_allow_html=True)

    st.markdown("""
    <h2 style='text-align:center;'>Shona ❤️</h2>

    <p style='text-align:center;'>If you’re seeing this on Valentine’s Day, then here’s something I want you to know…</p>

    <p style='text-align:center;'>I might not be able to be with you today, but you’re still the one I want to be with.<br>
    I miss you, your voice, and all the little things about you.</p>

    <p style='text-align:center;'>Distance just means I have more love saved up for you when I see you again.</p>

    <h3 style='text-align:center;'>Happy Valentine’s, Shona 💖</h3>
    <p style='text-align:center;'>You’re always my Valentine.</p>
    """, unsafe_allow_html=True)
