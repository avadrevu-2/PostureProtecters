import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
import joblib


GOOD_POSTURE_FILENAME = 'real_data_good.csv'
GOOD_POSTURE_2_FILENAME = 'real_data_good_2.csv'

BAD_POSTURE_FILENAME = 'real_data_bad.csv'
BAD_POSTURE_2_FILENAME = 'real_data_bad_2.csv'

RANDOM_FOREST_FILENAME = 'test_2_random_forest_model.pkl'


def preprocess_data(good_csv_file: str, bad_csv_file: str) -> tuple[np.ndarray, pd.Series]:
    # Load the good posture data from the CSV file
    good_df = pd.read_csv(GOOD_POSTURE_2_FILENAME, skiprows=0)
    # good_df.append(pd.read_csv(GOOD_POSTURE_2_FILENAME, skiprows=1))
    good_df['posture_label'] = 1  # Add posture label column and set it as 1

    # Load the bad posture data from the CSV file
    bad_df = pd.read_csv(BAD_POSTURE_2_FILENAME, skiprows=0)
    # bad_df.append(pd.read_csv(BAD_POSTURE_2_FILENAME, skiprows=1))
    bad_df['posture_label'] = 0  # Add posture label column and set it as 1

    # Concatenate the good and bad dataframes
    df = pd.concat([good_df, bad_df])

    # Separate features and labels
    features = df.drop(columns=['posture_label'])
    print(features)
    labels = df['posture_label']

    # Perform min-max scaling on the features
    scaler = MinMaxScaler()
    scaled_features = scaler.fit_transform(features)
    return scaled_features, labels



def train_random_forest(features: np.ndarray, labels: pd.Series) -> RandomForestClassifier:
    x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.25, random_state=42)
    
    # Initialize and fit the Random Forest classifier
    rf = RandomForestClassifier(n_estimators=1000, random_state=42)
    rf.fit(x_train, y_train)

    # Evaluate the performance
    y_pred = rf.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(12, 12))
    img = sns.heatmap(cm, annot=True, annot_kws={"size": 20}, fmt='d', cmap='Blues', cbar=False, xticklabels=['Bad Posture', 'Good Posture'], yticklabels=['Bad Posture', 'Good Posture'])
    img.set_xticklabels(img.get_xmajorticklabels(), fontsize = 20)
    img.set_yticklabels(img.get_ymajorticklabels(), fontsize = 20)
    plt.title("Confusion Matrix", fontsize=35)
    plt.xlabel("Predicted Labels", fontsize=30)
    plt.ylabel("True Labels", fontsize=30)
    plt.show()

    print(f"Accuracy: {accuracy}")
    return rf


if __name__ == '__main__':
    print('Preprocessing Data...')
    features, labels = preprocess_data(GOOD_POSTURE_FILENAME, BAD_POSTURE_FILENAME)
    print('Fitting Random Forest Model...')
    rf_model = train_random_forest(features, labels)
    print('Saving Model to Pkl file...')
    joblib.dump(rf_model, RANDOM_FOREST_FILENAME)
