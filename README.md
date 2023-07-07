# ground-penetrating-radar

The project focuses on processing Ground Penetrating Radar (GPR) 
data using a machine learning model to detect buried objects in the ground. 
Data collection involves using two Vivaldi antennas in bistatic mode, 
in conjunction with a Rohde & Schwarz Vector Network Analyzer (VNA). After obtaining the S-parameters using VNA, 
a logistic regression model is employed for classification. The resulting model achieves an 80% 
accuracy in detecting LiPo batteries buried at depths of 7-10 cm in the ground. The classification threshold 
can be adjusted to reduce false positives or false negatives. Several useful scripts were developed for this project, mainly in Python.
Libraries such as Pandas, Numpy, and Matplotlib were used for data processing and visualization, 
Sklearn for model training, and PyAutoGUI for automating data collection. This method gives promising results 
and encourages further research in this field.

[![GE Flag](https://flagcdn.com/16x12/ge.png)](./README-ge.md) [GE](./README-ge.md) | [![US Flag](https://flagcdn.com/16x12/us.png)](./README.md) US

**[Check out the full project report in PDF format](https://github.com/lnadi17/ground-penetrating-radar/blob/master/README.pdf)**

<img width="534" alt="Screenshot 2023-07-07 at 20 09 24" src="https://github.com/lnadi17/ground-penetrating-radar/assets/19193250/45ffadf4-0142-4d65-9780-6f297e9396a0">

### Literature (books, articles, videos, tables, graphs):

[Mine Action - The Research Experience of the Royal Military Academy of Belgium](https://www.intechopen.com/books/mine-action-the-research-experience-of-the-royal-military-academy-of-belgium/ground-penetrating-radar-for-close-in-mine-detection)\
[Radar Signatures of Complex Buried Objects in Ground Penetrating Radar](http://ijet.pl/old_archives/2011/1/01.pdf)\
[Overfitting vs. Underfitting: A Complete Example](https://towardsdatascience.com/overfitting-vs-underfitting-a-complete-example-d05dd7e19765)\
[Data Science Decal Fall 2017 Lecture 4: Logistic Regression and Regularization](https://www.youtube.com/watch?v=ehGMpLeVgPs&list=WL&index=75)\
[Stanford CS109 Handout #40: Logistic Regression](https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/pdfs/40%20LogisticRegression.pdf)\
[Speech and Language Processing, Daniel Jurafsky & James H. Martin, 2019](http://web.stanford.edu/~jurafsky/slp3/5.pdf)\
[The Neural Net Tank Urban Legend](https://www.gwern.net/Tanks)\
[Dielectric Constants for Earth materials](http://www.geo.umass.edu/faculty/wclement/dielec.html)\
[VSWR Conversion Table](https://www.everythingrf.com/tech-resources/vswr)\
[Buried Object Hyperbolic Shape Animation](https://www.geogebra.org/calculator/mayyj4kh)
