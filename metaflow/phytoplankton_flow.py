import sys
import os
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
        # Assuming load_dataset is correctly implemented and imported
        self.X_train, self.X_test, self.y_train, self.y_test = load_dataset('data/training/phyto_skye/phyto')
        print(f"Data loaded. Training samples: {len(self.X_train)}, Test samples: {len(self.X_test)}")
        self.next(self.train)

    @step
    def train(self):
        print("Training the model...")
        self.model = create_model(input_shape=self.X_train.shape[1:], num_classes=self.y_train.shape[1])
        self.model, self.history = train_model(self.model, self.X_train, self.y_train, self.X_test, self.y_test, epochs=10, batch_size=32)
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