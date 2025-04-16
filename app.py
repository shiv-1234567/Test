import streamlit as st
import os

# Display welcome and description at the top
st.title("Divide and Chill!")
st.write("Where you can find tutorials, answers, and much more. Let's have a pleasant stay!")

# App description
st.header("File Upload and Download System")
st.write("You can upload and download files. Files will be stored permanently. Supported file types: jpg, png, pdf, txt, csv, docx.")

# Define the directory to store uploaded files
upload_dir = "uploaded_files"
os.makedirs(upload_dir, exist_ok=True)

# List of uploaded files for downloading
uploaded_files = os.listdir(upload_dir)

# Allow users to upload files
new_files = st.file_uploader("Choose files", type=["jpg", "png", "pdf", "txt", "csv", "docx"], accept_multiple_files=True)

if new_files:
    for uploaded_file in new_files:
        save_path = os.path.join(upload_dir, uploaded_file.name)

        # Save each uploaded file permanently
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getvalue())

        # Show upload success
        st.success(f"File {uploaded_file.name} uploaded successfully!")

# Show the list of already uploaded files
if uploaded_files:
    st.subheader("Uploaded Files (Downloadable):")
    for file_name in uploaded_files:
        file_path = os.path.join(upload_dir, file_name)

        # Provide a download button for each uploaded file
        with open(file_path, "rb") as f:
            file_data = f.read()

        st.download_button(
            label=f"Download {file_name}",
            data=file_data,
            file_name=file_name,
            mime="application/octet-stream"  # MIME type for binary files (can adjust for specific file types)
        )
else:
    st.write("No files uploaded yet. Upload a file to see it here.")

# Display message at the end
st.write("Hope we helped you. Feel free to adjust as per your own needs. It's actually a place where we, as friends, can upload and retrieve files.")
