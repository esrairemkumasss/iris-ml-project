# 🌸 Iris Flower Classification (Machine Learning)

Bu proje, **Iris veri seti** kullanılarak çiçek türü tahmini yapan temel bir **Makine Öğrenmesi sınıflandırma** uygulamasıdır.  
Model olarak **Random Forest Classifier** kullanılmıştır.

---

## 🎯 Proje Amacı

- Denetimli öğrenme (Supervised Learning) sürecini uygulamak  
- Veri görselleştirme ile sınıflar arası farkları analiz etmek  
- Bir makine öğrenmesi modelini eğitmek, değerlendirmek ve yorumlamak  

---

## 📊 Veri Seti

- Kaynak: `sklearn.datasets.load_iris`
- Örnek sayısı: 150
- Sınıf sayısı: 3 (Setosa, Versicolor, Virginica)
- Özellikler:
  - Sepal Length
  - Sepal Width
  - Petal Length
  - Petal Width

---

## 🛠 Kullanılan Teknolojiler

- Python
- scikit-learn
- pandas
- matplotlib
- seaborn

---

## 🔍 Proje Akışı

- Veri seti yüklendi ve DataFrame’e dönüştürüldü  
- Pairplot ile keşifsel veri analizi yapıldı  
- Veri %80 eğitim, %20 test olarak ayrıldı  
- Random Forest modeli eğitildi  
- Accuracy ve Confusion Matrix ile performans ölçüldü  
- Yeni bir çiçek için tahmin yapıldı  
- Feature Importance analizi gerçekleştirildi  
- Model içindeki bir karar ağacı görselleştirildi  

---

## 📊 Model Çıktıları

### Pairplot
![Pairplot](outputs/pairplot.png)

### Confusion Matrix
![Confusion Matrix](outputs/confusion_matrix.png)

### Feature Importance
![Feature Importance](outputs/feature_importance.png)

### Decision Tree (Örnek)
![Decision Tree](outputs/decision_tree.png)

---

## 📈 Model Performansı

- Accuracy: %95+ (random state’e bağlı olarak değişebilir)

Model, Iris veri seti üzerinde yüksek doğruluk ile çalışmıştır.  
Özellikle **Petal Length** ve **Petal Width** özelliklerinin sınıflandırmada en etkili faktörler olduğu gözlemlenmiştir.

---

## 🚀 Geliştirme Fikirleri

- Farklı algoritmalarla karşılaştırma (KNN, SVM)
- Cross-validation
- Hyperparameter tuning
- Streamlit veya Flask ile web arayüzü

---

## 👩‍💻 Geliştirici

**Esra Kumas**  
Machine Learning & Software Development Enthusiast
