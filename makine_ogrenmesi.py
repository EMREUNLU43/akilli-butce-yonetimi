from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def model_egit(X_train, X_test, y_train, y_test):
    # Karar Ağacı modeli
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Tahmin yapma
    y_pred = model.predict(X_test)

    # Model performansı
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Doğruluğu: {accuracy * 100:.2f}%")

    return model