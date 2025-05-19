"""
Example of integrating Tygent with LangGraph.
"""

import sys
sys.path.append('./tygent-py')
import tygent as tg
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langgraph.graph import StateGraph, END

def main():
    """Run the LangGraph integration example."""
    
    print("\nTygent + LangGraph Integration Example")
    print("======================================\n")
    
    # Create a LangGraph workflow
    print("Creating a LangGraph workflow...")
    workflow = StateGraph("research_workflow")
    
    # Define states
    def search_state(state):
        """Perform search operation."""
        print(f"  - Executing search state with query: {state.get('query', 'No query')}")
        return {"search_results": "Simulated search results for renewable energy"}
    
    def synthesize_state(state):
        """Synthesize findings."""
        print(f"  - Executing synthesize state with results: {state.get('search_results', 'No results')}")
        return {"synthesis": "Synthesized information about renewable energy trends"}
    
    # Add states to the graph
    print("Adding states to the LangGraph workflow...")
    workflow.add_node("search", search_state)
    workflow.add_node("synthesize", synthesize_state)
    
    # Add edges
    print("Adding edges between states...")
    workflow.add_edge("search", "synthesize")
    workflow.add_edge("synthesize", END)
    
    print("\nConverting LangGraph workflow to Tygent DAG...")
    
    # Convert LangGraph workflow to Tygent DAG
    def langgraph_to_tygent(workflow):
        """Convert a LangGraph workflow to a Tygent DAG."""
        dag = tg.DAG(workflow.name)
        
        # Convert LangGraph nodes to Tygent nodes
        for node_name in workflow.nodes:
            if node_name == END:
                continue
                
            # Create a tool node for the LangGraph state function
            node = tg.ToolNode(
                id=node_name,
                tool_fn=workflow.nodes[node_name],
                input_schema={"state": dict},
                output_schema={"result": dict}
            )
            dag.add_node(node)
        
        # Add edges based on LangGraph transitions
        for source, targets in workflow.edges.items():
            if source == END:
                continue
                
            for target in targets:
                if target == END:
                    continue
                    
                dag.add_edge(source, target)
        
        return dag
    
    # Convert and execute
    tygent_dag = langgraph_to_tygent(workflow)
    
    print("Executing the converted DAG with Tygent's scheduler...")
    scheduler = tg.Scheduler()
    result = scheduler.execute(tygent_dag, {"query": "renewable energy"})
    
    print("\nResults:")
    for node_id, outputs in result.items():
        if node_id != "__inputs":
            print(f"  - Node: {node_id}")
            for key, value in outputs.items():
                print(f"    - {key}: {value}")
    
    print("\nDAG Execution completed successfully.")

if __name__ == "__main__":
    main()