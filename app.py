import os
import pandas as pd
import streamlit as st
from serpapi import GoogleSearch
from dotenv import load_dotenv
import json
from groq import Groq

load_dotenv()
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def perform_search(query, api_key):
    """
    Perform a Google search using SerpAPI
    """
    try:
        search = GoogleSearch({
            "q": query,
            "api_key": api_key,
            "num": 3
        })
        results = search.get_dict()
        if "organic_results" in results:
            return [
                {
                    "title": result.get("title", ""),
                    "snippet": result.get("snippet", ""),
                    "link": result.get("link", "")
                }
                for result in results["organic_results"]
            ]
        return []
    except Exception as e:
        st.error(f"Search error: {str(e)}")
        return []

def process_with_llm(company, search_results, custom_prompt):
    """
    Process search results using Groq API
    """
    try:
        formatted_results = "\n".join([
            f"Title: {r['title']}\nSnippet: {r['snippet']}\nLink: {r['link']}\n"
            for r in search_results
        ])
        prompt = f"""
        Based on the following search results about {company}, {custom_prompt}
        Search Results:
        {formatted_results}
        Please extract the requested information in JSON format.
        """
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"LLM processing error: {str(e)}")
        return None

def main():
    st.title("AI Agent")
    uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        column = st.selectbox("Select the company column:", df.columns)
        st.subheader("Data Preview")
        st.dataframe(df.head())
        custom_prompt = st.text_input(
            "Enter your prompt (use {company} as placeholder):",
            "Extract the email address and website of {company}"
        )
        serp_api_key = st.text_input("Enter your SerpAPI key:", type="password")
        if st.button("Process Data") and serp_api_key:
            results = []
            
            progress_bar = st.progress(0)
            
            for idx, row in df.iterrows():
                company = row[column]
                progress = (idx + 1) / len(df)
                progress_bar.progress(progress)
                query = f"{company} contact information"
                search_results = perform_search(query, serp_api_key)
                
                if search_results:
                    extracted_info = process_with_llm(
                        company,
                        search_results,
                        custom_prompt.format(company=company)
                    )
                    results.append({
                        "company": company,
                        "extracted_info": extracted_info
                    })
            if results:
                st.subheader("Extracted Information")
                results_df = pd.DataFrame(results)
                st.dataframe(results_df)
                csv = results_df.to_csv(index=False)
                st.download_button(
                    "Download Results",
                    csv,
                    "results.csv",
                    "text/csv",
                    key='download-csv'
                )

if __name__ == "__main__":
    main()