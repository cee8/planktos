from metaflow import FlowSpec, step

class PhytoplanktonClassificationFlow(FlowSpec):

    @step
    def start(self):
        # Load data
        self.X_train, self.X_test, self.y_train, self.y_test = load_dataset('data/processed/phyto_skye/phyto')
        self.next(self.train_model)

    @step
    def train_model(self):
        # Train your model here
        self.next(self.end)

    @step
    def end(self):
        # Final step
        pass

if __name__ == '__main__':
    PhytoplanktonClassificationFlow()
