"""
Example of using Tygent's multi-agent capabilities in Python.

This example demonstrates how to:
1. Create multiple agents with different roles
2. Configure optimization settings for parallel execution
3. Execute a conversation between multiple agents
4. Analyze the critical path in the conversation DAG
"""

import asyncio
from typing import Dict, Any
from tygent import (
    MultiAgentManager,
    AgentRole,
    OptimizationSettings,
    ToolNode
)

# Define agent roles
roles = {
    "researcher": AgentRole(
        name="Researcher",
        description="Specializes in finding and analyzing information.",
        system_prompt="You are a skilled researcher who excels at gathering relevant information. Your goal is to provide comprehensive, accurate, and well-sourced information about the topic at hand."
    ),
    "critic": AgentRole(
        name="Critic",
        description="Identifies flaws and suggests improvements.",
        system_prompt="You are a thoughtful critic who evaluates information critically. Your goal is to identify potential flaws, biases, or gaps in reasoning and suggest improvements."
    ),
    "synthesizer": AgentRole(
        name="Synthesizer",
        description="Combines insights into a coherent whole.",
        system_prompt="You are an expert synthesizer who brings together different perspectives. Your goal is to create a cohesive and comprehensive understanding of the topic by incorporating multiple viewpoints."
    )
}

async def main():
    """Run the multi-agent example."""
    print("Tygent Multi-Agent Example")
    print("==========================")
    
    # Create a multi-agent manager
    manager = MultiAgentManager()
    
    # Add agents with their roles
    for agent_id, role in roles.items():
        manager.add_agent(agent_id, role)
        print(f"Added agent: {role.name}")
    
    # Define query and optimization settings
    query = "What are the potential benefits and risks of quantum computing?"
    
    optimization_settings = OptimizationSettings(
        batch_messages=False,
        parallel_thinking=True,  # Agents think in parallel
        shared_memory=True,      # Agents share memory
        early_stop_threshold=0.0  # No early stopping
    )
    
    print(f"\nExecuting conversation with query: '{query}'")
    print("Optimization settings:")
    print(f"- Parallel thinking: {optimization_settings.parallel_thinking}")
    print(f"- Shared memory: {optimization_settings.shared_memory}")
    
    # Create the conversation DAG
    dag = manager.create_conversation_dag(query, optimization_settings)
    
    # Find the critical path
    critical_path = manager.find_critical_path(dag)
    print(f"\nCritical path in conversation DAG: {' -> '.join(critical_path)}")
    
    # Execute the conversation
    print("\nExecuting conversation...")
    results = await manager.execute_conversation(query, optimization_settings)
    
    # Display results
    print("\nConversation results:")
    for node_id, result in results.items():
        if node_id.startswith("agent_"):
            agent_id = node_id[6:]  # Remove "agent_" prefix
            role = roles[agent_id]
            print(f"\n== {role.name}'s response ==")
            if isinstance(result, dict) and "response" in result:
                print(result["response"])
    
    print("\nMulti-agent conversation completed successfully!")

if __name__ == "__main__":
    asyncio.run(main())