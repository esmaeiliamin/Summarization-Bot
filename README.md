# This function helps to break down the summarization task into smaller 
# parts using the map-reduce paradigm from LangChain,processes each
# part with the LLm, and then combines the results into a final summary.
# This implementation can handle large documents by splitting them into 
# smaller chunks and processing them parallely.