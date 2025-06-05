# Tygent Examples

This repository contains example code for using the Tygent packages in Python and TypeScript/JavaScript. These examples demonstrate how Tygent can optimize LLM agent execution using typed Directed Acyclic Graphs (DAGs).

## Python Examples

### Basic Usage
- [Basic Python Example](python_example.py) - Simple `accelerate()` function example
- [Advanced Python Example](advanced_python_example.py) - Customer support agent with automatic parallelization
- [Multi-Agent Python Example](multi_agent_python_example.py) - Multiple agents working together with Tygent optimization

### Framework Integration Examples
- [LangChain Integration](langchain_integration.py) - Using `accelerate()` with LangChain agents
- [LangGraph Integration](langgraph_integration.py) - LangGraph workflow optimization
- [Dynamic DAG Example](dynamic_dag_example.py) - Runtime DAG modification and adaptation

### AI Platform Integration Examples  
- [Google AI Example](google_ai_example.py) - Gemini model integration with Tygent
- [Microsoft AI Example](microsoft_ai_example.py) - Azure AI Services with parallel execution
- [Salesforce Example](salesforce_example.py) - Salesforce Einstein integration

## TypeScript/JavaScript Examples

### Basic Usage
- [Basic TypeScript Example](nodejs_example.ts) - Simple `accelerate()` function example
- [Advanced TypeScript Example](advanced_nodejs_example.ts) - Product recommendation engine with parallelization
- [Multi-Agent TypeScript Example](multi_agent_nodejs_example.ts) - Multiple agents coordinated by Tygent

### AI Platform Integration Examples
- [Google AI TypeScript Example](google_ai_nodejs_example.ts) - Gemini model integration
- [Microsoft AI TypeScript Example](microsoft_ai_nodejs_example.ts) - Azure AI Services integration  
- [Salesforce TypeScript Example](salesforce_nodejs_example.ts) - Salesforce platform integration

## Running the Examples

### Setup Requirements

For examples that use external AI services, you'll need to set environment variables for API keys:

```bash
# For OpenAI examples
export OPENAI_API_KEY="your-openai-api-key"

# For Google AI examples  
export GOOGLE_AI_API_KEY="your-google-ai-api-key"

# For Microsoft Azure examples
export AZURE_OPENAI_API_KEY="your-azure-api-key"
export AZURE_OPENAI_ENDPOINT="your-azure-endpoint"

# For Salesforce examples
export SALESFORCE_USERNAME="your-username"
export SALESFORCE_PASSWORD="your-password"
export SALESFORCE_SECURITY_TOKEN="your-token"
```

### Python

Install dependencies and run examples:

```bash
# Install the Tygent Python package from the release
cd tygent-py
pip install .

# Run basic examples
python ../python_example.py
python ../advanced_python_example.py
python ../multi_agent_python_example.py

# Run integration examples
python ../langchain_integration.py
python ../dynamic_dag_example.py
```

### TypeScript/JavaScript

Install dependencies and run examples:

```bash
# Install the Tygent JavaScript package from the release
cd tygent-js
npm install
npm run build

# Run basic examples
npx ts-node ../nodejs_example.ts
npx ts-node ../advanced_nodejs_example.ts
npx ts-node ../multi_agent_nodejs_example.ts
```

## Environment Setup

For examples that use the OpenAI API, set your API key as an environment variable:

```bash
# For Python
export OPENAI_API_KEY=your-api-key

# For Node.js
OPENAI_API_KEY=your-api-key node your-script.js
```

## Performance Improvements

The examples demonstrate significant performance improvements when using Tygent's parallel execution capabilities:

- In the advanced Python example, parallel execution is typically 30-50% faster than sequential execution
- In the advanced TypeScript example, constraint-aware scheduling further improves performance by 20-40%

## Additional Resources

- [Tygent Python Package](https://github.com/tygent-ai/tygent-py)
- [Tygent JavaScript Package](https://github.com/tygent-ai/tygent-js)
- [Tygent Documentation](https://tygent.ai/docs)
