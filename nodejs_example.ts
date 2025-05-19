/**
 * Example usage of the Tygent Node.js package
 */

import { DAG, ToolNode, LLMNode, MemoryNode, Scheduler, AdaptiveExecutor } from 'tygent';

// Set your API key in environment variables
// process.env.OPENAI_API_KEY = 'your-api-key'; // Uncomment and set your API key

/**
 * Example search tool function
 */
async function searchFunction(inputs: any): Promise<any> {
  const query = inputs.query || 'default query';
  console.log(`Searching for: ${query}`);
  // In a real implementation, this would call a search API
  return { results: `Search results for '${query}'` };
}

/**
 * Example weather tool function
 */
async function weatherFunction(inputs: any): Promise<any> {
  const location = inputs.location || 'San Francisco';
  console.log(`Getting weather for: ${location}`);
  // In a real implementation, this would call a weather API
  return { 
    temperature: 72, 
    conditions: 'Sunny', 
    location 
  };
}

/**
 * Main execution function
 */
async function main() {
  // Create a DAG
  const dag = new DAG('example_workflow');
  
  // Create nodes
  const searchNode = new ToolNode('search', searchFunction);
  const weatherNode = new ToolNode('weather', weatherFunction);
  const processNode = new LLMNode(
    'process',
    'gpt-4o', // the newest OpenAI model is "gpt-4o" which was released May 13, 2024
    'Analyze the following information:\nSearch results: {search_results}\nWeather: {temperature}°F in {location}, conditions: {conditions}'
  );
  
  // Add nodes to the DAG
  dag.addNode(searchNode);
  dag.addNode(weatherNode);
  dag.addNode(processNode);
  
  // Connect nodes with edges
  dag.addEdge('search', 'process', { results: 'search_results' });
  dag.addEdge('weather', 'process', {
    temperature: 'temperature',
    conditions: 'conditions',
    location: 'location'
  });
  
  // Define a condition for optional edge traversal
  // This is an advanced feature that shows conditional execution paths
  const temperatureCheck = (outputs: Record<string, any>) => {
    // Only execute this path if the temperature is above 70°F
    return outputs.weather?.temperature > 70;
  };
  
  // Create an advanced scheduler that utilizes parallelism
  const executor = new AdaptiveExecutor(dag);
  
  try {
    // Execute the DAG with input data
    const result = await executor.execute({
      query: 'artificial intelligence advancements',
      location: 'New York'
    });
    
    // Print the results
    console.log('\n--- Execution Results ---');
    console.log(`Total execution time: ${result.totalTime.toFixed(2)} seconds`);
    
    console.log('\nNode execution times:');
    Object.entries(result.executionTimes).forEach(([nodeId, timeTaken]) => {
      console.log(`  - ${nodeId}: ${timeTaken.toFixed(2)} seconds`);
    });
    
    console.log('\nProcessed Result:');
    if (result.results.process) {
      const processResult = result.results.process;
      if ('response' in processResult) {
        console.log(processResult.response);
      } else if ('error' in processResult) {
        console.log(`Error: ${processResult.error}`);
      }
    }
  } catch (error: any) {
    console.error('Error executing DAG:', error.message);
  }
}

// Run the example
main().catch(console.error);