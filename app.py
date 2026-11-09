import streamlit as st
from PIL import Image
from pathlib import Path

from utils.prediction import predict_disease


# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="Leaf Guard | Plant Disease Detection",
    page_icon="🌿",
    layout="wide"
)


# =====================================
# LOAD CSS
# =====================================

css_path = Path("assets/style.css")

if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as file:
        st.markdown(
            f"<style>{file.read()}</style>",
            unsafe_allow_html=True
        )


# =====================================
# HEADER
# =====================================

st.markdown(
    """
    <div class="hero">
        <h1>🌿 LEAF GUARD</h1>
        <h3>AI-Powered Plant Disease Detection</h3>
        <p>Protecting Plants Through Artificial Intelligence</p>
    </div>
    """,
    unsafe_allow_html=True
)


# =====================================
# SIDEBAR NAVIGATION
# =====================================

st.sidebar.title("🌱 LEAF GUARD")

st.sidebar.write("Your Smart Plant Health Assistant")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Disease Detection",
        "About"
    ]
)


# =====================================
# HOME PAGE
# =====================================

if page == "Home":

    st.title("Welcome to Leaf Guard! 🌿")

    st.write(
        """
        Leaf Guard is an AI-based plant disease detection
        system that uses Deep Learning to identify plant
        diseases through leaf images.

        Upload a leaf photograph and let our AI model
        analyse it.
        """
    )

    st.markdown("### Our Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("🌿 AI Disease Detection")

    with col2:
        st.success("🔍 Image Analysis")

    with col3:
        st.success("🛡️ Plant Health Support")

    st.markdown("### How Does It Work?")

    st.write("1. Upload a plant leaf image.")
    st.write("2. AI analyses the leaf.")
    st.write("3. View the Top 3 predicted diseases.")
    st.write("4. Compare the prediction scores.")

    st.info("Healthy Plants, Healthier Future! 🌱")


# =====================================
# DISEASE DETECTION PAGE
# =====================================

elif page == "Disease Detection":

    st.title("🔍 Plant Disease Detection")

    st.write(
        "Upload a clear photograph of a plant leaf "
        "to identify its possible disease."
    )

    uploaded_file = st.file_uploader(
        "Choose a Leaf Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        try:

            image = Image.open(uploaded_file).convert("RGB")

            col1, col2 = st.columns(2)

            with col1:

                st.image(
                    image,
                    caption="Uploaded Leaf Image",
                    use_container_width=True
                )

            with col2:

                st.markdown("### Analyse Your Leaf")

                if st.button(
                    "🔍 Analyse Leaf",
                    use_container_width=True
                ):

                    with st.spinner(
                        "AI is analysing your leaf..."
                    ):

                        results = predict_disease(image)

                    if not results:

                        st.error("No predictions available.")

                    else:

                        st.markdown(
                            "### 🌿 Top 3 Predictions"
                        )

                        for i, result in enumerate(results):

                            disease = result["disease"]

                            confidence = result["confidence"]

                            formatted_name = (
                                disease
                                .replace("___", " - ")
                                .replace("_", " ")
                            )

                            st.write(
                                f"**{i + 1}. {formatted_name}**"
                            )

                            st.progress(
                                max(0.0, min(1.0, confidence / 100))
                            )

                            st.write(
                                f"Model Score: {confidence:.2f}%"
                            )

                            st.divider()

                        # Main prediction

                        main_disease = results[0]["disease"]

                        main_confidence = results[0]["confidence"]

                        st.markdown("### Detection Summary")

                        st.success(
                            f"Top Prediction: "
                            f"{main_disease.replace('___', ' - ').replace('_', ' ')}"
                        )

                        if main_confidence < 55:

                            st.warning(
                                "The model has low confidence. "
                                "Try uploading a clearer image."
                            )

                        elif main_confidence < 80:

                            st.warning(
                                "The prediction needs further "
                                "verification."
                            )

                        else:

                            st.info(
                                "The model has a high prediction "
                                "score. This does not guarantee "
                                "that the prediction is correct."
                            )

                        if "healthy" in main_disease.lower():

                            st.success(
                                "The model classified this leaf "
                                "as healthy."
                            )

                        else:

                            st.warning(
                                "Possible disease detected. "
                                "Inspect the plant carefully."
                            )

                        st.caption(
                            """
                            Disclaimer: These are AI model scores,
                            not confirmed disease probabilities.
                            Results may differ on real-world images.
                            """
                        )

        except Exception as e:

            st.error(
                "Something went wrong while analysing "
                "the image."
            )

            st.code(str(e))


# =====================================
# ABOUT PAGE
# =====================================

elif page == "About":

    st.title("🌱 About Leaf Guard")

    st.write(
        """
        Leaf Guard is an AI-based plant disease detection
        project developed using Artificial Intelligence
        and Deep Learning.
        """
    )

    st.markdown("### Technologies Used")

    technologies = [
        "Python",
        "TensorFlow",
        "Convolutional Neural Network (CNN)",
        "Streamlit",
        "OpenCV",
        "NumPy",
        "Pandas",
        "Machine Learning"
    ]

    for technology in technologies:

        st.write(f"✔️ {technology}")

    st.markdown("### Our Mission")

    st.write(
        """
        Our mission is to support agriculture by using
        Artificial Intelligence to identify possible
        plant diseases through leaf images.
        """
    )

    st.success(
        "LEAF GUARD - Technology for a Greener Tomorrow 🌿"
    )


# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:gray;">
        🌿 LEAF GUARD | AI-Based Plant Disease Detection
        <br>
        BSc Artificial Intelligence & Machine Learning Project
    </div>
    """,
    unsafe_allow_html=True
)