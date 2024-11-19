import streamlit as st
from text_processor import preprocess_text, split_into_chunks
from semanticAnalysis import is_chunk_relevant
from utils.insight_extractor import extract_insights


def main():
    st.title("Dynamic Insight Generator")
    st.write("Paste a story below and provide a topic prompt to extract insights.")
    story = st.text_area("Enter the story text here:")
    prompt = st.text_input("Enter the topic prompt (e.g., productivity, time management):")


    if st.button("Generate Insights"):
        if not story or not prompt:
            st.warning("Please provide both a story and a topic prompt.")
        else:
            chunks = split_into_chunks(preprocess_text(story))
            insights = []
            for chunk in chunks:
                if is_chunk_relevant(chunk, prompt):
                    insights.append(extract_insights(chunk))

            if insights:
                st.success("Insights extracted successfully!")
                st.write("\n### Insights:")
                for i, insight in enumerate(insights, 1):
                    st.write(f"{i}. {insight}")
            else:
                st.info("No relevant insights found for the given prompt.")

if __name__ == "__main__":
    main()
