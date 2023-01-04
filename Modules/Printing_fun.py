def printing_models(designs, printed_models):
    """Print a list of designs"""    
    while designs:
        current_design = designs.pop()
        print("Printing " + current_design)
        printed_models.append(current_design)
    return printed_models

def show_models(printed_models):
    """Show a list of models printed"""
    print("Those models were printed:")    
    for model in printed_models:
        print("- " + model)
