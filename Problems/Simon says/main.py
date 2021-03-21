def what_to_do(instructions):
    if instructions.startswith("Simon says"):
        return "I " + instructions[len("Simon says") + 1:]
        # Another solution 1
        # return f"I {instructions[11:]

    elif instructions.endswith("Simon says"):
        return "I " + instructions[:len(instructions) - len("Simon says")]
        # Another solution 1
        # return f"I {instructions[:-11]}

    return "I won't do it!"

    # Another solution 2
    # if instructions.startswith("Simon says") or instructions.endswith("Simon says"):
    #     return f"I {instructions.replace("Simon says", "").strip()}
    # return "I won't do it!"
