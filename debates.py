import streamlit as st

from graph import graph

st.title("🦜🔗 К коллайдеру!")


def generate_response(input_text, max):
    # model = ChatOpenAI(temperature=0.7, api_key=openai_api_key)
    # st.info(model.invoke(input_text))
    inputs = {"main_topic": input_text, "messages": [], "max_count": max}
    for update in graph.stream(inputs, {"recursion_limit": 100}, stream_mode="updates"):
        if "🚀 Elon" in update:
            st.info(update["🚀 Elon"]["messages"][0], icon="🚀")
        if "🧑‍💻 Sam" in update:
            st.info(update["🧑‍💻 Sam"]["messages"][0], icon="🧑‍💻")
        # if len(output["messages"]) == 0:
        #     continue
        # resp = output["messages"][-1].content
        # person = output["last_person"]
        # icon = "👨"
        # if person == "Илон":
        #     icon = "🚀"
        # if person == "Сэм":
        #     icon = "🧑‍💻"
        # st.info(resp, icon=icon)


with st.form("my_form"):
    text = st.text_area(
        "Вопрос для обсуждения:",
        "Уничтожит ли AGI человечество?",
    )
    max_count = st.number_input("Количество сообщений", 5, 50, 10)
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text, max_count)
