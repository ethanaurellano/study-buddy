import streamlit as st
import google.generativeai as genai
import PyPDF2

st.title("🇧🇪 My Study Buddy (Auto-Fix Version)")

# 1. API Key
api_key = st.sidebar.text_input("Paste your Google API Key:", type="password")

if api_key:
    # Configure the library
    genai.configure(api_key=api_key)
    
    try:
        # --- THE FIX: We ask Google what models exist ---
        # We get a list of all models that support "generateContent"
        model_list = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                model_list.append(m.name)
        
        # We create a Dropdown box so YOU can pick the one that exists
        selected_model = st.sidebar.selectbox("Select a Model", model_list)
        
        st.sidebar.success(f"✅ Connected to: {selected_model}")
        
        # --- Normal App Logic Below ---
        uploaded_file = st.file_uploader("Upload your PDF", type="pdf")
        
        if uploaded_file:
            # Read PDF
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            pdf_text = ""
            for page in pdf_reader.pages:
                pdf_text += page.extract_text()
                
            st.info("I read the document. Ask away!")
            
            question = st.text_input("Ask a question:")
            
            if question:
                with st.spinner("Thinking..."):
                    # We use the model YOU selected from the list
                    model = genai.GenerativeModel(selected_model)
                    
                    prompt = f"Document: {pdf_text}\n\nQuestion: {question}"
                    response = model.generate_content(prompt)
                    
                    st.write("### Answer:")
                    st.write(response.text)

    except Exception as e:
        st.error(f"Something went wrong: {e}")

else:
    st.warning("👈 Enter your key to start.")