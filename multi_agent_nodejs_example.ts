/**
 * Example of using Tygent's multi-agent capabilities in Node.js/TypeScript.
 * 
 * This example demonstrates how to:
 * 1. Create multiple agents with different roles
 * 2. Configure optimization settings for parallel execution
 * 3. Execute a conversation between multiple agents
 * 4. Analyze the critical path in the conversation DAG
 */

import {
  MultiAgentOrchestrator,
  AgentRole,
  OptimizationSettings,
  ToolNode
} from '../tygent-js/src/index';

// Define agent roles
const roles: Record<string, AgentRole> = {
  researcher: {
    name: "Researcher",
    description: "Specializes in finding and analyzing information.",
    systemPrompt: "You are a skilled researcher who excels at gathering relevant information. Your goal is to provide comprehensive, accurate, and well-sourced information about the topic at hand."
  },
  critic: {
    name: "Critic",
    description: "Identifies flaws and suggests improvements.",
    systemPrompt: "You are a thoughtful critic who evaluates information critically. Your goal is to identify potential flaws, biases, or gaps in reasoning and suggest improvements."
  },
  synthesizer: {
    name: "Synthesizer",
    description: "Combines insights into a coherent whole.",
    systemPrompt: "You are an expert synthesizer who brings together different perspectives. Your goal is to create a cohesive and comprehensive understanding of the topic by incorporating multiple viewpoints."
  }
};

async function main() {
  console.log("Tygent Multi-Agent Example");
  console.log("==========================");
  
  // Create a multi-agent orchestrator
  const orchestrator = new MultiAgentOrchestrator();
  
  // Add agents with their roles
  for (const [agentId, role] of Object.entries(roles)) {
    orchestrator.addAgent(agentId, role);
    console.log(`Added agent: ${role.name}`);
  }
  
  // Define query and optimization settings
  const query = "What are the potential benefits and risks of quantum computing?";
  
  const optimizationSettings: OptimizationSettings = {
    batchMessages: false,
    parallelThinking: true,  // Agents think in parallel
    sharedMemory: true,      // Agents share memory
    earlyStopThreshold: 0.0  // No early stopping
  };
  
  console.log(`\nExecuting conversation with query: '${query}'`);
  console.log("Optimization settings:");
  console.log(`- Parallel thinking: ${optimizationSettings.parallelThinking}`);
  console.log(`- Shared memory: ${optimizationSettings.sharedMemory}`);
  
  // Create the conversation DAG
  const dag = orchestrator.createConversationDag(query, optimizationSettings);
  
  // Find the critical path
  const criticalPath = orchestrator.findCriticalPath(dag);
  console.log(`\nCritical path in conversation DAG: ${criticalPath.join(' -> ')}`);
  
  // Execute the conversation
  console.log("\nExecuting conversation...");
  const results = await orchestrator.executeConversation(query, optimizationSettings);
  
  // Display results
  console.log("\nConversation results:");
  for (const [nodeId, result] of Object.entries(results)) {
    if (nodeId.startsWith("agent_")) {
      const agentId = nodeId.substring(6);  // Remove "agent_" prefix
      const role = roles[agentId];
      console.log(`\n== ${role.name}'s response ==`);
      if (result && typeof result === 'object' && 'response' in result) {
        console.log(result.response);
      }
    }
  }
  
  console.log("\nMulti-agent conversation completed successfully!");
}

main().catch(error => {
  console.error("Error executing multi-agent conversation:", error);
});