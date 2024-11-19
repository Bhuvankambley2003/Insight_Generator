# **Insight Generator**

The **Insight Generator** is an interactive web-based application that analyzes user-provided text and generates context-specific insights based on user-defined prompts. This tool leverages advanced Natural Language Processing (NLP) techniques to extract meaningful information from text, making it suitable for various use cases like productivity analysis, summarization, and more.

---

## **Features**

- **Custom Insights**: Generate insights based on user-provided prompts.
- **Text Summarization**: Summarizes long-form text to provide concise highlights.
- **Context Matching**: Analyzes the semantic similarity of the text to understand context.
- **User-Friendly Interface**: Built with Streamlit for an intuitive and interactive experience.

---

## **Deployed Application**

The Insight Generator has been deployed and is live at:  
[**https://bhuvan-insight-generator.streamlit.app/**](https://bhuvan-insight-generator.streamlit.app/)

You can access the app, input your text, and test its functionality directly on the web.

---

## **File Structure**

```plaintext
project/
│
├── app.py                # Main application script for Streamlit
├── requirements.txt      # File for managing dependencies
├── text_processor.py     # Script for text preprocessing and segmentation
├── semantic_analysis.py  # Script for semantic similarity and topic classification
├── test_story.txt        # Example input file with a long story
└── utils/
    ├── __init__.py       # Empty file to make utils a module
    └── insight_extractor.py # Script for extracting insights and generating summaries
```
