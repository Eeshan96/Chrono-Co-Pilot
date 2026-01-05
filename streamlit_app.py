import os
import streamlit as st
from dotenv import load_dotenv

from app.ai import get_ai_response
from app.memory import load_memory, save_memory

load_dotenv()

st.set_page_config(page_title="Chrono Copilot")

st.title(" Chrono Copilot")
st.caption("AI pre-interview copilot with modes: past, present, future.")

if "mode" not in st.session_state:
    st.session_state.mode = "present"

if "messages" not in st.session_state:
    st.session_state.messages = load_memory()

# Mode selector
mode = st.radio("Mode", ["past", "present", "future"], index=["past","present","future"].index(st.session_state.mode), horizontal=True)
st.session_state.mode = mode

# Shows chat history
for m in st.session_state.messages:
    if m["role"] == "user":
        st.chat_message("user").write(m["content"])
    elif m["role"] == "assistant":
        st.chat_message("assistant").write(m["content"])

user_input = st.chat_input("Type your message...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": f"[mode={st.session_state.mode}] {user_input}"})
    reply = get_ai_response(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    save_memory(st.session_state.messages)
    st.rerun()

st.divider()
st.write("Tip: Try keywords like **pizza** or **banana** for Easter eggs.")
