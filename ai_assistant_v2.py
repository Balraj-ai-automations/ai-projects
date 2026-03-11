question = input("Ask AI something: ")

print("\nAI Assistant is thinking...")

if "ai" in question.lower():
    answer = "AI stands for Artificial Intelligence. It allows computers to perform tasks that normally require human intelligence."

elif "automation" in question.lower():
    answer = "Automation means using technology to perform tasks automatically without human effort."

else:
    answer = "That is an interesting question. In real AI systems this would be answered by a large language model."

print("\nAI Assistant:", answer)