import streamlit as st


def display_dashboard(answer):

    st.header("📊 Contract Analysis")

    st.metric(
        "Overall Risk",
        answer["overall_risk"]["score"]
    )

    st.subheader("Payment Terms")

    st.write(
        answer["payment_terms"]["summary"]
    )

    st.subheader("Financial Risk")

    st.metric(
        "Risk Score",
        answer["financial_risk"]["score"]
    )

    st.write(
        answer["financial_risk"]["reason"]
    )

    st.subheader("Termination Clause")

    st.write(
        answer["termination_clause"]["summary"]
    )

    st.subheader("Red Flags")

    for flag in answer["red_flags"]:

        st.warning(flag)

    st.subheader("Missing Clauses")

    for clause in answer["missing_clauses"]:

        st.info(clause)