def find_best_accuracy(results):
    max = 0
    best_model={}
    for model,result in results.items():
        accuracy = result['accuracy']
        print("{} : {}".format(model,accuracy))
        if accuracy>max:
            max = accuracy;best_model={}
            best_model[model] = accuracy
    print("""The best model is '{}' in terms of only accuracy : '{}' """.format(best_model.keys(),best_model.values())) 

def find_overall_best(results):
    max = 0
    best_model ={}
    for model,result in results.items():
        overall_perfomrance = sum(list(result.values()))/len(result)
        print("{} : {}".format(model,overall_perfomrance))
        if overall_perfomrance>max :
            max = overall_perfomrance;best_model={}
            best_model[model] = overall_perfomrance
    print("""The best model is '{}' with overall performance : '{}' """.format(best_model.keys(),best_model.values()))

def interpret_results(results):
    print(""" \t\tModels performance under differenct Metrics """)
    for model,result in results.items():
        print("{} : {}".format(model,result))
    print(""" \t\tBest Model in terms of only acucracy""")
    find_best_accuracy(results)
    print(""" \t\t Best Model in terms of overall performance""")
    find_overall_best(results)

