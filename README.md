# Energy Market Insights Assistant

An interactive Streamlit dashboard for analyzing North American natural gas prices, with a focus on AECO-C and Henry Hub. An LLM-powered Q&A assistant is built using LangChain.

### Setup
1. Install the dependencies
    ```
    pip install -r code/requirements.txt
    ```
    * **Note**: An OpenAI API key is required to use the LLM assistant
2. Run the following command in the terminal:
    ```
    streamlit run code/app.py
    ```

### Data
Data comes from Alberta Energy Outlook report, which is updated annually by the Alberta Energy Regulator. The raw dataset is included in the ```data``` folder, which can also be downloaded [here](https://www.aer.ca/data-and-performance-reports/statistical-reports/alberta-energy-outlook-st98/prices-and-capital-expenditure)
