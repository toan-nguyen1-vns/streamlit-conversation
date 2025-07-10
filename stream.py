import streamlit as st
import json

st.set_page_config(layout="wide")
st.title("💬 Minimal Chat Viewer")

left_col, right_col = st.columns([1, 2])

with left_col:
    st.header("Input JSON")
    user_input = st.text_area(
        "Paste your JSON here:", height=300, placeholder="Paste JSON data here..."
    )
    process = st.button("Process")

with right_col:
    if process:
        if user_input:
            try:
                data = json.loads(user_input)

                st.write(f"**ID:** {data.get('id')}")
                st.write(f"**Language:** {data.get('language')}")
                st.markdown("---")

                for message in data.get("messages", []):
                    role = message.get("role", "unknown").lower()
                    content = message.get("content", "")
                    image_urls = message.get("image_urls", [])

                    align = "flex-end" if role == "user" else "flex-start"
                    bg_color = "#007bff" if role == "user" else "#f1f0f0"
                    text_color = "white" if role == "user" else "black"

                    # Chat bubble
                    st.markdown(
                        f"""
                        <div style='display: flex; justify-content: {align}; margin: 8px 0;'>
                            <div style='background: {bg_color}; color: {text_color};
                                        padding: 10px 15px; border-radius: 20px;
                                        max-width: 75%;'>
                                {content}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    # Ảnh bên phải hoặc trái
                    if image_urls and isinstance(image_urls, list):
                        images_html = ""
                        for img in image_urls:
                            images_html += (
                                f"<img src='{img['url']}' width='180' style='margin:0 0 0 10px;'/>"
                                if align == "flex-end"
                                else f"<img src='{img['url']}' width='180' style='margin:0 10px 0 0;'/>"
                            )
                        st.markdown(
                            f"""
                            <div style='display: flex; justify-content: {align}; margin: 5px 0;'>
                                {images_html}
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )

                st.markdown("---")
            except json.JSONDecodeError:
                st.error("❌ Invalid JSON. Please check your input.")
        else:
            st.warning("👈 Please paste your JSON on the left and click Process.")
    else:
        st.info("👈 Paste JSON on the left and click Process to display chat.")
