# ground-penetrating-radar
პროექტი არის GPR-ის (Ground Penetrating Radar) მონაცემების მანქანური სწავლების
გამოყენებით დამუშავების მეთოდის და ამით მიწაში დამარხული ობიექტების აღმოჩენის
შესახებ. მონაცემების შეგროვებისთვის გამოყენებულია ორი ვივალდის ანტენა ბისტატიკურ
რეჟიმში, Rohdze-Schwarz ფირმის ვექტორულ ქსელურ ანალიზატორთან (VNA) ერთად. 
VNA-ით S-პარამეტრების შეგროვების შემდეგ გამოყენებულია ლოგისტიკური რეგრესიის მოდელი მათი კლასიფიცირებისთვის.
მიღებულ მოდელი არის cross-validated და შედეგად 80% სიზუსტით შეუძლია მიწაში
7-10სმ-ზე დამარხული LiPo ბატარიების აღმოჩენა. ბუნებრივია, კლასიფიკაციის ბარიერის
ცვლილება შეიძლება რათა შევამციროთ ცრუ დადებითი ან ცრუ უარყოფითი მონაცემების
რაოდენობა. პროექტის შექმნისას ბევრი გამოსადეგი სკრიპტი დაიწერა, ძირითადად Python-ში. 
ბიბლიოთეკები, როგორებიცაა Pandas, Numpy და Matplotlib გამოყენებული იყო მონაცემების დამუშავებისთვის და
ვიზუალიზაციისთვის, Sklearn ბიბლიოთეკა მოდელის მორგებისთვის, PyAutoGUI მონაცემთა
შეგროვების ავტომატიზაციისთვის და ა.შ. ეს მეთოდი დამაიმედებელ შედეგს იძლევა უფრო
ფართო გამოყენებისთვის და მიზნად ისახავს უფრო მეტი კვლევის წარმოებას ამ
მიმართულებით.

**[იხილეთ პროექტის ანგარიშის pdf ვერსია](https://github.com/lnadi17/ground-penetrating-radar/blob/master/README.pdf)**

<img width="534" alt="Screenshot 2023-07-07 at 20 09 24" src="https://github.com/lnadi17/ground-penetrating-radar/assets/19193250/45ffadf4-0142-4d65-9780-6f297e9396a0">

### ლიტერატურა (ნაშრომები, სტატიები, ვიდეოები, ცხრილები, გრაფიკები):

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
