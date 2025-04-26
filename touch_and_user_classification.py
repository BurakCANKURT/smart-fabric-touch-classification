import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import streamlit as st

class TandUClassification:
    def __init__(self):
        self.df = pd.read_excel("03-Touch and User Classification from Smart Fabric.xlsx")
        self.feature_cols = [i for i in range(1, 3201)]
        self.X = self.df[self.feature_cols]
        self.y_user = self.df["user_id"]
        self.y_touch = self.df["touch_type"] if "touch_type" in self.df.columns else self.df["touch"]
        self.importances = None
        self.top_feats = None
        self.model = None

    def preprocessing(self):    
        scaler = StandardScaler()
        self.X = scaler.fit_transform(self.X)

    def RandomForest_user(self):
        X_train_user, X_test_user, y_train_user, y_test_user = train_test_split(self.X, self.y_user,test_size= 0.2, random_state= 42)
        self.model = RandomForestClassifier(n_estimators=100, random_state= 42)
        self.model.fit(X_train_user, y_train_user)
        y_pred_user = self.model.predict(X_test_user)
        print("User Accuracy :", accuracy_score(y_test_user, y_pred_user))
        print(classification_report(y_test_user, y_pred_user))

    def RandomForest_touch(self):
        X_train_user, X_test_user, y_train_user, y_test_user = train_test_split(self.X, self.y_touch,test_size= 0.2, random_state= 42)
        self.model = RandomForestClassifier(n_estimators=100, random_state= 42)
        self.model.fit(X_train_user, y_train_user)
        y_pred_user = self.model.predict(X_test_user)
        print("User Accuracy :", accuracy_score(y_test_user, y_pred_user))
        print(classification_report(y_test_user, y_pred_user))


    def importance(self):
        self.importances = self.model.feature_importances_
        self.top_feats = np.argsort(self.importances)[-100:]
        self.X = self.X.iloc[:, self.top_feats] 

    def visualize_touch(self, process_name):
        fig, ax = plt.subplots()
        ax.bar(range(100), self.importances[self.top_feats])
        ax.set_title("Top 100 Sensor (Touch Prediction)")
        ax.set_xlabel("Sensor No")
        ax.set_ylabel("Importance")
        st.pyplot(fig)
        fig.savefig(f"kmeans_model_{process_name}.png", bbox_inches='tight')
        plt.close(fig)

    def visualize_user(self, process_name):
        fig, ax = plt.subplots()
        ax.bar(range(100), self.importances[self.top_feats])
        ax.set_title("Top 100 Sensor (User Prediction)")
        ax.set_xlabel("Sensor No")
        ax.set_ylabel("Importance")
        st.pyplot(fig)
        fig.savefig(f"kmeans_model_{process_name}.png", bbox_inches='tight')
        plt.close(fig)

    def fullProcess_with_randomForest_touch(self):
        self.RandomForest_touch()
        self.importance()
        self.RandomForest_touch()
        self.visualize_touch("random_forest_touch")

    def fullProcess_with_randomForest_user(self):
        self.RandomForest_user()
        self.importance()
        self.RandomForest_user()
        self.visualize_user("random_forest_user")

if __name__ == "__main__":
    x = TandUClassification()
    x.preprocessing()
    x.fullProcess_with_randomForest_touch()
    x.fullProcess_with_randomForest_user()



