import warnings
from validation import validate_data

warnings.filterwarnings("ignore")
data,status = validate_data('diabetes.csv')

if status :
    from eda import explore_data
    explore_data(data=data)
    
    from preprocessing import preprocessor
    x,y,pbm_type = preprocessor(data)
    
    from splitter import train_test_validation_splitter
    xtrain,xval,ytrain,yval = train_test_validation_splitter(x,y,pbm_type)
    print("Training Data shape : {} ; {}".format(xtrain.shape,ytrain.shape))
    print("Validation Data shape : {} ; {}".format(xval.shape,yval.shape))

    from classification_models import model_fitter
    all_estimators,results = model_fitter(xtrain,ytrain,xval,yval)

    print(all_estimators)
    print(results)

    from interpret_results import interpret_results
    interpret_results(results)
    
else :
    print("""Dataset didn't pass the criterions.Please make sure you have followed the guidelines properly.
    Data doesn't have sufficient rows and columns""")