import streamlit as st

from src.classifier import classify_persona
from src.rag_pipeline import search_documents
from src.generator import generate_adaptive_response
from src.escalator import (
    should_escalate,
    generate_handoff
)

st.set_page_config(
    page_title="Persona Support Agent"
)

st.title("😊 Persona Support Agent")

question = st.text_input(
    "Ask a support question"
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if st.button("Ask"):

    if question:

        persona = classify_persona(
            question
        )

        results = search_documents(
            question
        )

        # Confidence Score
        try:
            distance = results["distances"][0][0]

            st.metric(
                "Confidence Score",
                f"{round((1 - distance) * 100, 2)}%"
            )
        except:
            pass

        answer = generate_adaptive_response(
            question,
            persona,
            results
        )

        st.success(
            "Answer Generated"
        )

        st.subheader(
            "Detected Persona"
        )
        st.write(persona)

        st.subheader(
            "Retrieved Sources"
        )

        try:
            st.text_area(
                "Source Documents",
                "\n\n".join(
                    results["documents"][0]
                ),
                height=200
            )
        except:
            st.text_area(
                "Source Documents",
                str(results),
                height=200
            )

        escalate = should_escalate(
            question
        )

        st.subheader(
            "Escalation Status"
        )

        if escalate:

            st.error(
                "Escalated To Human Agent"
            )

            handoff = generate_handoff(
                persona,
                question,
                results
            )

            st.subheader(
                "Human Handoff Summary"
            )

            st.json(handoff)

        else:

            st.success(
                "No Escalation Required"
            )

        st.subheader(
            "Response"
        )
        st.write(answer)

        st.session_state.chat_history.append(
            {
                "question": question,
                "persona": persona,
                "answer": answer
            }
        )

st.subheader("📜 Chat History")

for chat in st.session_state.chat_history:

    st.write(
        f"👤 User: {chat['question']}"
    )

    st.write(
        f"🐦 Persona: {chat['persona']}"
    )

    st.write(
        f"💬 Answer: {chat['answer']}"
    )

    st.divider()