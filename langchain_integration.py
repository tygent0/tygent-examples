"""
Example of integrating Tygent with LangChain.
"""

import sys
sys.path.append('./tygent-py')
import tygent as tg
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

def main():
    """Run the LangChain integration example."""
    
    print("\nTygent + LangChain Integration Example")
    print("======================================\n")
    
    # Create a tygent DAG
    print("Creating a Tygent DAG...")
    dag = tg.DAG("langchain_integration")
    
    # Define an LLM node using a LangChain prompt
    print("Adding an LLM node with a LangChain prompt...")
    template = "Answer the following question: {question}"
    prompt = PromptTemplate(template=template, input_variables=["question"])
    
    llm_node = tg.LLMNode(
        "answer_generator",
        model="gpt-3.5-turbo",
        prompt_template=template,
        input_schema={"question": str},
        output_schema={"response": str}
    )
    dag.add_node(llm_node)
    
    # Execute with Tygent's scheduler
    print("Executing the DAG with Tygent's scheduler...")
    scheduler = tg.Scheduler()
    
    # In a real implementation, this would call an actual LLM API
    # For now, this is a simulation
    question = "How do I integrate LangChain with Tygent?"
    print(f"\nQuestion: {question}")
    
    result = scheduler.execute(dag, {"question": question})
    
    print("\nResult:")
    print(f"  - Node ID: {llm_node.id}")
    print(f"  - Response: {result[llm_node.id].get('response', 'No response')}")
    print("\nDAG Execution completed successfully.")

if __name__ == "__main__":
    main()