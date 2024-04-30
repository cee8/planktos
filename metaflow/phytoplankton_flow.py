import sys
import os
import json  # Import json to handle saving of the label dictionary
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from metaflow import FlowSpec, step
from src.model import create_model, train_model, evaluate_model
from src.data_loader import load_dataset

class PhytoplanktonClassificationFlow(FlowSpec):

    @step
    def start(self):
        print("Starting the flow...")
        # Load data or perform initial actions
        print("Loading data...")
        # Load data along with the label dictionary to ensure consistency in labels
        self.X_train, self.X_test, self.y_train, self.y_test, self.class_labels = load_dataset('data/training/phyto_skye/phyto')
        print(f"Data loaded. Training samples: {len(self.X_train)}, Test samples: {len(self.X_test)}")
        self.next(self.train)

    @step
    def train(self):
        print(f"Current Working Directory: {os.getcwd()}")
        print("Training the model...")
        self.model = create_model(input_shape=self.X_train.shape[1:], num_classes=self.y_train.shape[1])
        self.model, self.history = train_model(self.model, self.X_train, self.y_train, self.X_test, self.y_test, epochs=10, batch_size=32)
        model_directory = 'models'
        os.makedirs(model_directory, exist_ok=True)
        model_save_path = os.path.join(model_directory, 'model.keras')
        self.model.save(model_save_path)
        # Save the class labels to a JSON file to ensure they can be used consistently at prediction time
        label_save_path = os.path.join(model_directory, 'labels.json')
        with open(label_save_path, 'w') as f:
            json.dump(self.class_labels, f)
        print(f"Model saved to {model_save_path} and labels saved to {label_save_path}")
        print("Model training complete.")
        self.next(self.evaluate)

    @step
    def evaluate(self):
        print("Evaluating the model...")
        metrics = evaluate_model(self.model, self.X_test, self.y_test)
        print("Model evaluation complete.")
        print("Accuracy:", metrics['accuracy'])
        print("Precision:", metrics['precision'])
        print("Recall:", metrics['recall'])
        print("F1 Score:", metrics['f1_score'])
        self.next(self.end)

    @step
    def end(self):
        print("Phytoplankton classification flow completed.")

if __name__ == '__main__':
    PhytoplanktonClassificationFlow()
