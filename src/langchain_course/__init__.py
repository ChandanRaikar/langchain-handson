from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
load_dotenv()


def main():
    print("Hello world")
    information = """how is the weather in Bengaluru now?"""
    summary_template = """ "You are a helpful assistant that can answer questions about the weather."""
    
    summary_prompt_template = PromptTemplate(template=summary_template, input_variables=["input"])
    csummary_prompt = summary_prompt_template.format(information=information)
    
    print(csummary_prompt)
    
    model = ChatOpenAI(temperature=0, model="gpt-5.4-mini")
    chain = summary_prompt_template | model
    response = chain.invoke(input={"information": information})
    print(response.content)


if __name__ == "__main__":
    main()
