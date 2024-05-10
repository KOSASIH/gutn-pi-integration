from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score

class Metrics:
    @staticmethod
    def accuracy(y_true, y_pred):
        return accuracy_score(y_true, y_pred)

    @staticmethod
    def f1(y_true, y_pred):
        return f1_score(y_true, y_pred, average='weighted')

    @staticmethod
    def precision(y_true, y_pred):
        return precision_score(y_true, y_pred, average='weighted')

    @staticmethod
    def recall(y_true, y_pred):
        return recall_score(y_true, y_pred, average='weighted')

    @staticmethod
    def roc_auc(y_true, y_pred):
        return roc_auc_score(y_true, y_pred, average='weighted')
