import streamlit as st
import time

st.set_page_config(page_title="For Sonia ❤️", page_icon="💘", layout="centered")

# ---------- Floating Hearts CSS ----------
st.markdown("""
<style>
body {
    overflow: hidden;
}
.heart {
    position: fixed;
    width: 20px;
    height: 20px;
    background: pink;
    transform: rotate(45deg);
    animation: float 8s infinite ease-in;
    opacity: 0.7;
}
.heart::before,
.heart::after {
    content: "";
    position: absolute;
    width: 20px;
    height: 20px;
    background: pink;
    border-radius: 50%;
}
.heart::before {
    top: -10px;
    left: 0;
}
.heart::after {
    left: -10px;
    top: 0;
}

@keyframes float {
    0% {
        bottom: -10%;
        opacity: 0;
    }
    50% {
        opacity: 0.8;
    }
    100% {
        bottom: 110%;
        opacity: 0;
    }
}
</style>

<div class="heart" style="left:10%; animation-delay:0s;"></div>
<div class="heart" style="left:25%; animation-delay:2s;"></div>
<div class="heart" style="left:40%; animation-delay:4s;"></div>
<div class="heart" style="left:55%; animation-delay:1s;"></div>
<div class="heart" style="left:70%; animation-delay:3s;"></div>
<div class="heart" style="left:85%; animation-delay:5s;"></div>
""", unsafe_allow_html=True)


if "page" not in st.session_state:
    st.session_state.page = 1

if "error_msg" not in st.session_state:
    st.session_state.error_msg = ""

# ---------------- PAGE 1 ----------------
if st.session_state.page == 1:
    st.markdown("<h1 style='text-align:center;'>Welcome Shona 😏</h1>", unsafe_allow_html=True)

    if st.session_state.error_msg:
        st.warning(st.session_state.error_msg)
        st.session_state.error_msg = ""

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

    st.success("Loaded ❤️")

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
            st.session_state.error_msg = "wrong button pressed babe :("
            st.session_state.page = 1
            st.rerun()


# ---------------- PAGE 4 ----------------
elif st.session_state.page == 4:
    st.markdown("<h1 style='text-align:center;'>Breaking News 📰</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>A girl named Sonia has been on my mind way too much.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Authorities say: it’s serious 😔💖</p>", unsafe_allow_html=True)

    if st.button("Go to next disaster 👉"):
        st.session_state.page = 5
        st.rerun()


# ---------------- PAGE 5 ----------------
elif st.session_state.page == 5:
    st.markdown("<h1 style='text-align:center;'>Important Question ⚠️</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;color:pink;'>Sonia, will you be my Valentine? 💌</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("YES 💖"):
            st.session_state.page = 6
            st.rerun()

    with col2:
        if st.button("NO ❌"):
            st.session_state.error_msg = "wrong button pressed babe :("
            st.session_state.page = 1
            st.rerun()


# ---------------- PAGE 6 (FINAL) ----------------
elif st.session_state.page == 6:
    st.balloons()
    st.markdown("<h1 style='text-align:center;'>LET'S GOOOOOO 🎉💖</h1>", unsafe_allow_html=True)

    st.markdown("""
    <p style='text-align:center;'>If you’re seeing this on Valentine’s Day, then here’s something I want you to know…</p>

    <p style='text-align:center;'>Shona, I might not be able to be with you today, but you’re still the one I want to be with.<br>
    I miss you, your voice, and all the little things about you.</p>

    <p style='text-align:center;'>Distance just means I have more love saved up for you when I see you again.</p>

    <h3 style='text-align:center;'>Happy Valentine’s 💖</h3>
    <p style='text-align:center;'>You’re always my Valentine.</p>
    """, unsafe_allow_html=True)

