cases = [
    ("billing", "billing", .97), 
    ("technical", "technical", .92),
    ("sales", "billing", .60), 
    ("general", "general", .81),
    ("billing", "technical", .55), 
    ("sales", "sales", .87),
    ("technical", "technical", .74), 
    ("general", "sales", .45),
]


for threshold in (.0, .7, .85, .95):
    handled = [(truth,pred) for truth,pred,confidence in cases if confidence >= threshold]
    coverage = len(handled)/len(cases)
    accuracy = sum(truth==pred for truth,pred in handled)/len(handled) if handled else 0
    print(f"threshold={threshold:.2f} coverage={coverage:.0%} selective_accuracy={accuracy:.0%} handled={len(handled)}")
