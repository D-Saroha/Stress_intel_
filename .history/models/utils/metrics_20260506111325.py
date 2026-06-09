from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


def calculate_classification_metrics(
    y_true,
    y_pred
):

    metrics = {
        "accuracy": accuracy_score(
            y_true,
            y_pred
        ),

        "precision": precision_score(
            y_true,
            y_pred,
            average="weighted"
        ),

        "recall": recall_score(
            y_true,
            y_pred,
            average="weighted"
        ),

        "f1_score": f1_score(
            y_true,
            y_pred,
            average="weighted"
        ),

        "confusion_matrix": confusion_matrix(
            y_true,
            y_pred
        ).tolist(),

        "classification_report": classification_report(
            y_true,
            y_pred,
            output_dict=True
        )
    }

    return metrics