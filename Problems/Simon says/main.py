def what_to_do(instructions):
    templ = "Simon says"
    if instructions.startswith(templ):
        return "I " + instructions[len(templ) + 1:]
    if instructions.endswith(templ):
        return "I " + instructions[:len(templ) + 1]

    return "I won't do it!"