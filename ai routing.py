def slade_response(query): keywords = ["status", "danger", "help", "location", "time"] if any(k in query.lower() for k in keywords): return local_slade_brain(query) else: return ask_openai(query)
