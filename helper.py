import pandas as pd
import pickle

class Operations:

    def process_gender(gender, df):
        if gender == "M":
            df['gender_F'] = [0]
            df['gender_M'] = [1]
        else:
            df['gender_F'] = [1]
            df['gender_M'] = [0]
        
        return df
    
    def process_tenure(tenure, df):
        df['tenure'] = [tenure]

        return df
    
    def process_internet(internet, df ):
        df['internet'] = [internet]

        return df
    
    def process_online_sec(os, df):
        df['online_sec'] = [os]

        return df
    
    def process_multi_lines(mlines, df):
        df['multi_lines'] = [mlines]

        return df

    def process_contract(contract, df):
        if contract == "m":
            df['contract_m'] = [1]
            df['contract_ty'] = [0]
            df['contract_oy'] = [0]
        elif contract == "ty":
            df['contract_m'] = [0]
            df['contract_ty'] = [1]
            df['contract_oy'] = [0]
        else:
            df['contract_m'] = [0]
            df['contract_ty'] = [0]
            df['contract_oy'] = [1]
        
        return df
    
    def make_predictions(df):
        #load the model
        with open("model/model.pkl", 'rb') as file:
            model = pickle.load(file)
        #get predictions
        pred = model.predict(df)
        pred = pred.tolist()[0]
        
        if pred == 0:
            return "Will Not Churn"
        else:
            return "Will Churn"

    def get_predictions(
        tenure, multi_lines, internet, 
        online_sec, gender, contract):
        colnames = ['tenure', 'multi_lines', 'internet', 
            'online_sec', 'gender_F', 'gender_M', 
            'contract_m', 'contract_oy', 'contract_ty']
        df = pd.DataFrame(columns=colnames)
        #get tenure
        df = Operations.process_tenure(tenure, df)
        #get mlines
        df = Operations.process_multi_lines(multi_lines, df)
        #get internet
        df = Operations.process_internet(internet, df)
        #get online security
        df = Operations.process_online_sec(online_sec, df)
        #get gender
        df = Operations.process_gender(gender, df)
        #get contract
        df = Operations.process_contract(contract, df)

        #get the predictions
        pred = Operations.make_predictions(df)

        return pred
    
