conversation_states = {}  # In-memory: {contact: {"state": "product", "data": {}}}


def handle_message(contact, message):
    if contact not in conversation_states:
        conversation_states[contact] = {"state": "product", "data": {}}

    state = conversation_states[contact]["state"]
    data = conversation_states[contact]["data"]

    if state == "product":
        data["product_name"] = message
        conversation_states[contact]["state"] = "name"
        return "What's your name?"
    elif state == "name":
        data["user_name"] = message
        conversation_states[contact]["state"] = "review"
        return f"Please send your review for {data['product_name']}."
    elif state == "review":
        data["product_review"] = message
        # Save to DB (we'll integrate this)
        conversation_states.pop(contact, None)  # Reset
        return f"Thanks {data['user_name']} -- your review for {data['product_name']} has been recorded."