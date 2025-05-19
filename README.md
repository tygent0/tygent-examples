# Tygent Examples

This repository contains example code for using the Tygent packages in Python and TypeScript/JavaScript. These examples demonstrate how Tygent can optimize LLM agent execution using typed Directed Acyclic Graphs (DAGs).

## Python Examples

### Basic Usage
- [Basic Python Example](python_example.py) - Simple example of creating and executing a DAG with Tygent
- [Advanced Python Example](advanced_python_example.py) - Comprehensive customer support agent example showcasing parallel execution

### Integration Examples
- [LangChain Integration](langchain_integration.py) - Example showing how to use Tygent with LangChain
- [LangGraph Integration](langgraph_integration.py) - Example showing how to integrate Tygent with LangGraph

## TypeScript/JavaScript Examples

### Basic Usage
- [Basic TypeScript Example](nodejs_example.ts) - Simple example of creating and executing a DAG with Tygent
- [Advanced TypeScript Example](advanced_nodejs_example.ts) - Comprehensive product recommendation engine showcasing parallel execution

## Running the Examples

### Python

First, install the Tygent Python package:

```bash
pip install tygent
```

Then run any of the Python examples:

```bash
python python_example.py
```

### TypeScript/JavaScript

First, install the Tygent JavaScript package:

```bash
npm install tygent
```

Then run any of the TypeScript examples:

```bash
# Compile and run
npx ts-node nodejs_example.ts
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
