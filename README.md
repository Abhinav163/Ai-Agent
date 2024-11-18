
# 🤖 AI Agent

Welcome to the **AI Agent**, a streamlined Python application that handles data processing, API integrations, and logging with powerful tools like Streamlit, Pandas, and Numpy. This project is designed to deliver efficiency and ease for various data-driven tasks while maintaining robust logging capabilities.

---

## 🚀 Features

- **Interactive Interface:** Built with Streamlit for a user-friendly web application experience.
- **Data Processing:** Efficiently handles data with libraries like Pandas and Numpy.
- **File Support:** Supports `.xlsx` and `.csv` file formats for reading and writing data.
- **Logging:** Monitors application activities with structured and easy-to-read logs.
- **Environment Variables:** Securely manages sensitive configurations using `.env` files.
- **Google Search API Integration:** Seamlessly integrates web search results for specific queries.

---

## 📦 Requirements

To run this application, ensure you have the following dependencies installed:

```
streamlit==1.31.0
pandas==2.2.0
numpy==1.24.3
python-dotenv==1.0.0
google-search-results==2.4.2
groq==0.4.2
openpyxl==3.1.2
xlsxwriter==3.1.2
python-json-logger==2.0.7
typing-extensions==4.7.1
```

---

## 🛠️ Setup and Installation

1. **Clone the Repository**  
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Install Dependencies**  
   Run the following command to install the required packages:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**  
   Update the `.env` file with your API keys and settings:
   ```plaintext
   GROQ_API_KEY=your_groq_key
   SERPAPI_API_KEY=your_serpapi_key
   ```
   > **Note:** Replace `your_groq_key` and `your_serpapi_key` with your actual API keys for GROQ and SerpAPI.

4. **Run the Application**  
   Use Streamlit to launch the app:  
   ```bash
   streamlit run app.py
   ```

---

## 📂 File Structure

- **`app.py`:** Main application script.
- **`requirements.txt`:** Lists all the dependencies.
- **`.env`:** Environment variables for secure configuration.
- **`app.log`:** Log file to track application events.

---

## 📝 Usage

1. **Upload Your Data:** Upload `.xlsx` or `.csv` files through the Streamlit interface.  
2. **Process Data:** Interact with the application to process, analyze, and save your results.  
3. **View Logs:** Monitor logs for activity and troubleshoot issues.

---

## 🤝 Contributions

Contributions are welcome! Feel free to open issues or submit pull requests to enhance this project.

---

## 🛡️ License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## 📧 Contact

For queries or feedback, contact:  
**[Abhinav Sharma]**  
**[sharmaabhinav23736@gmail.com]**
