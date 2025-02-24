import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def veri_hazirla():
    # Örnek veri seti
    veri = {
        'Gelir': [5000, 6000, 4500, 7000, 5500],
        'Gıda': [1000, 1200, 900, 1500, 1100],
        'Ulaşım': [500, 600, 400, 700, 550],
        'Eğlence': [300, 400, 200, 500, 350],
        'Kategori': ['Düşük', 'Orta', 'Düşük', 'Yüksek', 'Orta']
    }
    df = pd.DataFrame(veri)

    # Kategorik verileri sayısala çevirme
    label_encoder = LabelEncoder()
    df['Kategori'] = label_encoder.fit_transform(df['Kategori'])

    # Özellikler ve hedef değişken
    X = df.drop('Kategori', axis=1)
    y = df['Kategori']

    # Veri setini eğitim ve test olarak bölme
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test