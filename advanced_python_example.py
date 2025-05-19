"""
Advanced Example: Customer Support Agent with Tygent
-------------------------------------------------
This example demonstrates how to build a customer support agent
using Tygent's DAG-based optimization capabilities.

The agent can:
1. Analyze customer questions
2. Search a knowledge base
3. Check customer purchase history
4. Generate personalized responses
5. Recommend related products

The DAG enables parallel execution of knowledge base search
and customer history lookup, optimizing response time.
"""

import os
import asyncio
import time
from typing import Dict, Any, List
import sys
sys.path.append('./tygent-py')
from tygent import DAG, ToolNode, LLMNode, MemoryNode, Scheduler, AdaptiveExecutor

# Set your API key - in production use environment variables
# os.environ["OPENAI_API_KEY"] = "your-api-key"  # Uncomment and set your API key

# Simulated database
KNOWLEDGE_BASE = {
    "product_return": "Products can be returned within 30 days with receipt for a full refund.",
    "shipping_time": "Standard shipping takes 3-5 business days. Express shipping takes 1-2 business days.",
    "account_reset": "You can reset your password by clicking 'Forgot Password' on the login page.",
    "product_warranty": "Our products come with a 1-year limited warranty covering manufacturing defects."
}

CUSTOMER_DATABASE = {
    "user123": {
        "name": "Jane Smith",
        "purchases": [
            {"product": "Wireless Headphones", "date": "2025-02-15", "order_id": "ORD-7891"},
            {"product": "Smart Speaker", "date": "2025-04-10", "order_id": "ORD-8567"}
        ],
        "subscription": "Premium",
        "account_created": "2024-12-01"
    },
    "user456": {
        "name": "John Doe",
        "purchases": [
            {"product": "Smartphone", "date": "2025-03-05", "order_id": "ORD-3245"},
        ],
        "subscription": "Basic",
        "account_created": "2025-01-15"
    }
}

PRODUCT_RECOMMENDATIONS = {
    "Wireless Headphones": ["Headphone Case", "Bluetooth Adapter", "Extended Warranty"],
    "Smart Speaker": ["Smart Bulbs", "Voice Remote", "Speaker Stand"],
    "Smartphone": ["Phone Case", "Screen Protector", "Wireless Charger"]
}

# Tool functions for our agent
async def analyze_question(inputs: Dict[str, Any]) -> Dict[str, Any]:
    """Analyze the customer question to determine intent and keywords."""
    question = inputs.get("question", "")
    print(f"Analyzing question: {question}")
    
    # In a real implementation, this would use an LLM or classifier
    # For demo purposes, using simple keyword matching
    keywords = []
    intent = "general"
    
    if "return" in question.lower() or "refund" in question.lower():
        keywords.append("return")
        keywords.append("refund")
        intent = "product_return"
    elif "shipping" in question.lower() or "delivery" in question.lower():
        keywords.append("shipping")
        keywords.append("delivery")
        intent = "shipping_time"
    elif "password" in question.lower() or "login" in question.lower() or "reset" in question.lower():
        keywords.append("password")
        keywords.append("account")
        intent = "account_reset"
    elif "warranty" in question.lower() or "broken" in question.lower():
        keywords.append("warranty")
        keywords.append("repair")
        intent = "product_warranty"
    
    # Add a simulated delay to represent real analysis time
    await asyncio.sleep(0.5)
    
    return {
        "intent": intent,
        "keywords": keywords,
        "confidence": 0.85
    }

async def search_knowledge_base(inputs: Dict[str, Any]) -> Dict[str, Any]:
    """Search for relevant information in the knowledge base."""
    intent = inputs.get("intent", "general")
    keywords = inputs.get("keywords", [])
    
    print(f"Searching knowledge base for intent: {intent}, keywords: {keywords}")
    
    # In a real implementation, this would use a vector search or database query
    # For demo purposes, using direct lookup based on intent
    knowledge_base_result = KNOWLEDGE_BASE.get(intent, "No specific information found.")
    
    # Add a simulated delay to represent real database query time
    await asyncio.sleep(0.7)
    
    return {
        "knowledge_result": knowledge_base_result,
        "sources": [f"knowledge_base:{intent}"]
    }

async def get_customer_history(inputs: Dict[str, Any]) -> Dict[str, Any]:
    """Retrieve customer purchase history and account information."""
    user_id = inputs.get("user_id", "")
    
    print(f"Getting customer history for user: {user_id}")
    
    # In a real implementation, this would query a customer database
    # For demo purposes, using a mock database lookup
    customer_info = CUSTOMER_DATABASE.get(user_id, {})
    
    # Add a simulated delay to represent real database query time
    await asyncio.sleep(0.8)
    
    if not customer_info:
        return {"error": "Customer not found"}
    
    return {
        "customer_name": customer_info.get("name", ""),
        "purchase_history": customer_info.get("purchases", []),
        "subscription_tier": customer_info.get("subscription", ""),
        "account_age": "5 months"  # In a real system, this would be calculated
    }

async def generate_product_recommendations(inputs: Dict[str, Any]) -> Dict[str, Any]:
    """Generate product recommendations based on purchase history."""
    purchases = inputs.get("purchase_history", [])
    
    recommendations = []
    for purchase in purchases:
        product = purchase.get("product", "")
        if product in PRODUCT_RECOMMENDATIONS:
            recommendations.extend(PRODUCT_RECOMMENDATIONS[product])
    
    # Deduplicate recommendations
    recommendations = list(set(recommendations))
    
    # Add a simulated delay
    await asyncio.sleep(0.3)
    
    return {
        "recommended_products": recommendations[:3]  # Top 3 recommendations
    }

async def generate_response(inputs: Dict[str, Any]) -> Dict[str, Any]:
    """Generate a personalized response to the customer question."""
    question = inputs.get("question", "")
    knowledge_result = inputs.get("knowledge_result", "")
    customer_name = inputs.get("customer_name", "")
    subscription_tier = inputs.get("subscription_tier", "")
    recommended_products = inputs.get("recommended_products", [])
    
    # In a real implementation, this would use an LLM with a prompt
    # For demo purposes, using template-based generation
    
    # Personalized greeting
    response = f"Hello {customer_name}, thanks for contacting our support team.\n\n"
    
    # Answer to question
    response += f"Regarding your question about '{question}':\n{knowledge_result}\n\n"
    
    # Subscription tier message
    if subscription_tier == "Premium":
        response += "As a Premium member, you have access to our priority support line at 1-800-555-HELP.\n\n"
    
    # Product recommendations
    if recommended_products:
        response += "Based on your previous purchases, you might also be interested in:\n"
        for product in recommended_products:
            response += f"- {product}\n"
    
    # Add a simulated delay to represent generation time
    await asyncio.sleep(0.5)
    
    return {
        "response_text": response,
        "response_sentiment": "helpful",
        "response_length": len(response)
    }

async def main():
    print("Creating Customer Support Agent with Tygent...\n")
    
    # Define our customer query scenario
    customer_query = "Can I return the headphones I bought last month?"
    customer_id = "user123"
    
    print(f"Customer query: \"{customer_query}\"")
    print(f"Customer ID: {customer_id}\n")
    
    # Create a DAG for our customer support workflow
    dag = DAG("customer_support_agent")
    
    # Create nodes for each step of the workflow
    analyze_node = ToolNode("analyze", analyze_question)
    knowledge_node = ToolNode("knowledge", search_knowledge_base)
    customer_node = ToolNode("customer", get_customer_history)
    recommend_node = ToolNode("recommend", generate_product_recommendations)
    response_node = ToolNode("response", generate_response)
    
    # Add nodes to the DAG
    dag.add_node(analyze_node)
    dag.add_node(knowledge_node)
    dag.add_node(customer_node)
    dag.add_node(recommend_node)
    dag.add_node(response_node)
    
    # Define the workflow connections
    # analyze_question -> search_knowledge_base
    dag.add_edge("analyze", "knowledge", {
        "intent": "intent",
        "keywords": "keywords"
    })
    
    # customer_history is independent of question analysis
    # No edge needed between analyze and customer
    
    # get_customer_history -> generate_product_recommendations
    dag.add_edge("customer", "recommend", {
        "purchase_history": "purchase_history"
    })
    
    # All information flows to the response generation
    dag.add_edge("analyze", "response", {})  # Just to pass the original question
    dag.add_edge("knowledge", "response", {
        "knowledge_result": "knowledge_result"
    })
    dag.add_edge("customer", "response", {
        "customer_name": "customer_name",
        "subscription_tier": "subscription_tier"
    })
    dag.add_edge("recommend", "response", {
        "recommended_products": "recommended_products"
    })
    
    # Create a parallel executor
    executor = AdaptiveExecutor(dag)
    
    print("=== Running Sequential Execution for comparison ===")
    sequential_start = time.time()
    
    # Simulate sequential execution manually
    query_analysis = await analyze_question({"question": customer_query})
    kb_results = await search_knowledge_base(query_analysis)
    customer_info = await get_customer_history({"user_id": customer_id})
    product_recs = await generate_product_recommendations(customer_info)
    
    # Combine all inputs for response generation
    response_inputs = {
        "question": customer_query,
        "knowledge_result": kb_results["knowledge_result"],
        "customer_name": customer_info["customer_name"],
        "subscription_tier": customer_info["subscription_tier"],
        "recommended_products": product_recs["recommended_products"]
    }
    
    final_response = await generate_response(response_inputs)
    sequential_time = time.time() - sequential_start
    
    print(f"\nSequential execution time: {sequential_time:.2f} seconds\n")
    
    print("=== Running Parallel Execution with Tygent ===")
    # Execute the DAG with input data
    result = await executor.execute({
        "question": customer_query,
        "user_id": customer_id
    })
    
    # Extract the final response
    tygent_response = result["results"]["response"]["response_text"]
    tygent_time = result["total_time"]
    
    print(f"\nTygent parallel execution time: {tygent_time:.2f} seconds")
    print(f"Performance improvement: {((sequential_time - tygent_time) / sequential_time * 100):.1f}%\n")
    
    print("=== Final Response ===")
    print(tygent_response)
    
    print("\n=== Node Execution Times ===")
    for node_id, exec_time in result["execution_times"].items():
        print(f"{node_id}: {exec_time:.2f} seconds")
    
    print("\n=== Execution Graph Analysis ===")
    print("Sequential path: analyze -> knowledge -> response")
    print("Parallel path 1: customer -> recommend -> response")
    print(f"Critical path: {max(result['execution_times'].items(), key=lambda x: x[1])[0]}")

if __name__ == "__main__":
    asyncio.run(main())