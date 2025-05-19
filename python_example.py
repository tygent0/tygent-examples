"""
Example usage of the Tygent Python package.
"""

import os
import asyncio
import sys
sys.path.append('./tygent-py')
from tygent import DAG, ToolNode, LLMNode, MemoryNode, Scheduler, AdaptiveExecutor

# Set your API key - in production use environment variables
# os.environ["OPENAI_API_KEY"] = "your-api-key"  # Uncomment and set your API key

async def search_function(inputs):
    """Example search tool function."""
    query = inputs.get("query", "default query")
    print(f"Searching for: {query}")
    # In real implementation, this would call a search API
    return {"results": f"Search results for '{query}'"}

async def weather_function(inputs):
    """Example weather tool function."""
    location = inputs.get("location", "San Francisco")
    print(f"Getting weather for: {location}")
    # In real implementation, this would call a weather API
    return {"temperature": 72, "conditions": "Sunny", "location": location}

async def main():
    # Create a DAG
    dag = DAG("example_workflow")
    
    # Create nodes
    search_node = ToolNode("search", search_function)
    weather_node = ToolNode("weather", weather_function)
    process_node = LLMNode(
        "process", 
        "gpt-4o",  # Use the latest OpenAI model
        "Analyze the following information:\nSearch results: {search_results}\nWeather: {temperature}°F in {location}, conditions: {conditions}"
    )
    
    # Add nodes to the DAG
    dag.add_node(search_node)
    dag.add_node(weather_node)
    dag.add_node(process_node)
    
    # Connect nodes with edges
    dag.add_edge("search", "process", {"results": "search_results"})
    dag.add_edge("weather", "process", {
        "temperature": "temperature",
        "conditions": "conditions",
        "location": "location"
    })
    
    # Create a scheduler that can execute the DAG
    scheduler = Scheduler(dag)
    
    # Execute the DAG with input data
    result = await scheduler.execute({
        "query": "artificial intelligence advancements",
        "location": "New York"
    })
    
    # Print the results
    print("\n--- Execution Results ---")
    print(f"Total execution time: {result['total_time']:.2f} seconds")
    print("\nNode execution times:")
    for node_id, time_taken in result['execution_times'].items():
        print(f"  - {node_id}: {time_taken:.2f} seconds")
    
    print("\nProcessed Result:")
    if "process" in result["results"]:
        process_result = result["results"]["process"]
        if "response" in process_result:
            print(process_result["response"])
        elif "error" in process_result:
            print(f"Error: {process_result['error']}")

if __name__ == "__main__":
    asyncio.run(main())