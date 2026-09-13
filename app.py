import streamlit as st
from ultralytics import YOLO
from PIL import Image
import tempfile
import os
import glob
import subprocess
import imageio_ffmpeg


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Object Detection",
    page_icon="🎯",
    layout="wide"
)


# -----------------------------
# Load YOLO Model
# -----------------------------
@st.cache_resource
def load_model():
    return YOLO("yolo11n.pt")


model = load_model()


# -----------------------------
# Header
# -----------------------------
st.title("🎯 AI Object Detection")
st.subheader(
    "Detect objects in images and videos using YOLO"
)

st.markdown("---")


# -----------------------------
# Choose Input Type
# -----------------------------
input_type = st.radio(
    "📂 Choose Input Type",
    ["📷 Image", "🎥 Video"],
    horizontal=True
)


# =========================================================
# IMAGE DETECTION
# =========================================================

if input_type == "📷 Image":

    st.info("Upload an image to detect objects.")

    uploaded_file = st.file_uploader(
        "📤 Upload Image",
        type=["jpg", "jpeg", "png", "webp"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        if st.button(
            "🔍 Detect Objects",
            type="primary"
        ):

            with st.spinner("Detecting objects..."):

                results = model.predict(
                    source=image,
                    conf=0.25
                )

                result_image = results[0].plot(
                    conf=True
                )

            st.success("✅ Object detection completed!")

            st.image(
                result_image,
                caption="Detected Objects",
                use_container_width=True
            )

            st.markdown(
                "### 📊 Detection Details"
            )

            boxes = results[0].boxes

            if boxes is not None and len(boxes) > 0:

                for box in boxes:

                    class_id = int(
                        box.cls[0]
                    )

                    confidence = float(
                        box.conf[0]
                    )

                    object_name = model.names[
                        class_id
                    ]

                    st.write(
                        f"🔹 **{object_name}** — "
                        f"{confidence * 100:.1f}% confidence"
                    )

            else:

                st.warning(
                    "No objects detected."
                )


# =========================================================
# VIDEO DETECTION
# =========================================================

else:

    st.info("Upload a video to detect objects frame by frame.")

    uploaded_file = st.file_uploader(
        "📤 Upload Video",
        type=[
            "mp4",
            "avi",
            "mov",
            "mkv",
            "mpeg",
            "mpg",
            "webm"
        ]
    )

    if uploaded_file is not None:

        st.video(
            uploaded_file
        )

        if st.button(
            "🔍 Detect Objects in Video",
            type="primary"
        ):

            with st.spinner(
                "Processing video... Please wait."
            ):

                # Save uploaded video
                input_suffix = os.path.splitext(
                    uploaded_file.name
                )[1]

                input_file = tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=input_suffix
                )

                input_file.write(
                    uploaded_file.getbuffer()
                )

                input_file.close()

                # Create temporary output directory
                output_dir = tempfile.mkdtemp()

                # Run YOLO detection
                results = model.predict(
                    source=input_file.name,
                    save=True,
                    conf=0.25,
                    stream=True,
                    project=output_dir,
                    name="detected",
                    exist_ok=True
                )

                # Process all frames
                for _ in results:
                    pass

                # Find YOLO output video
                video_files = glob.glob(
                    os.path.join(
                        output_dir,
                        "detected",
                        "*"
                    )
                )

                if not video_files:

                    st.error(
                        "❌ Could not create detected video."
                    )

                else:

                    detected_video = video_files[0]

                    # Convert YOLO AVI output to MP4
                    # for browser compatibility
                    mp4_output = os.path.join(
                        output_dir,
                        "detected_output.mp4"
                    )

                    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

                    command = [
                        ffmpeg,
                        "-y",
                        "-i",
                        detected_video,
                        "-c:v",
                        "libx264",
                        "-pix_fmt",
                        "yuv420p",
                        "-movflags",
                        "+faststart",
                        mp4_output
                    ]

                    subprocess.run(
                        command,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        check=True
                    )

                    st.success(
                        "✅ Video object detection completed!"
                    )

                    st.markdown(
                        "### 🎥 Detection Result"
                    )

                    with open(
                        mp4_output,
                        "rb"
                    ) as video_file:

                        video_bytes = video_file.read()

                    st.video(
                        video_bytes,
                        format="video/mp4"
                    )

                    st.download_button(
                        label="⬇️ Download Detected Video",
                        data=video_bytes,
                        file_name="detected_video.mp4",
                        mime="video/mp4"
                    )

                # Cleanup input
                try:
                    os.remove(
                        input_file.name
                    )
                except:
                    pass


# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.caption(
    "AI Object Detection | "
    "Built with Python, Streamlit & YOLO"
                  )
