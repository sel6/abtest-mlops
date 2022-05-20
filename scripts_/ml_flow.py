import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import FunctionTransformer

# a class for machine learning processor
class ML_Processor:
    def __init__(self):
        pass

    #separates categorical and numerical columns
    def sep_cat_num(self, df):
        categorical_columns = df.select_dtypes(include='object').columns.tolist()
        numerical_columns = df.select_dtypes(exclude='object').columns.tolist()

        return categorical_columns, numerical_columns

    #encodes categgorical variable
    def cat_labeler(self, df, cat_cols):
        for column in cat_cols:
            encoder = LabelEncoder()
            df[column] = encoder.fit_transform(df[column])
        
        print(df.head())
        print("\n")

        return df

    #scales df
    def scaler(self, df):
        scaling = MinMaxScaler()
        df[:] = scaling.fit_transform(df[:])

        print("scaled")
        print(df.head())
        print("\n")
        
        return df

    #target and feautrue separator
    def target_feature(self, df, f_r, t):
        features = df.iloc[:,f_r[0]:f_r[1]].values
        target = df.iloc[:,t].values
        
        print("target_features output")
        print("features size: {}".format(features.shape))
        print("\n")

        return features, target
    
    #splits datasets
    def set_splitter(self, input, test, val, rand_state):
        features, target = input
        per_1 = test
        per_2 = (1-test)*val
        x_train, x_test, y_train, y_test = train_test_split(features, target,test_size= per_1,shuffle = True, random_state = rand_state )
        x_train, x_val, y_train, y_val = train_test_split(x_train, y_train,test_size= per_2, shuffle = True, random_state = rand_state)

        print("splitted outputt")
        print("X_train shape: {}".format(x_train.shape))
        print("y_train shape: {}".format(y_train.shape))
        print("x_test shape: {}".format(x_test.shape))
        print("y_test shape: {}".format(y_test.shape))
        print("X_val shape: {}".format(x_val.shape))
        print("y_val shape: {}".format(y_val.shape))


        return [x_train, y_train, x_test, y_test, x_val, y_val]
