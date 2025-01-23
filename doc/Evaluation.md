# Evaluation

For evaluating the models we have used validation and test sets from  [Nuclei](https://www.sciencedirect.com/science/article/pii/S2352340922009726).

We have compared two metrics as pixel-based Jaccard index and object-based F1-score where the threshold for comparing two objects are 90%.


## U-Net evaluation

For evaluating U-Net models we have used our three best models 



|    |F1_score_90 |	Average Jaccard | Index |	False | Negatives |	False Positives |	True Positives |	Detected Objects |	False Discovery | Rate |	Precision |	Recall |
|3   | 	0.809952  | 0.871175        |	89.0  |	17.0  |	240.0 |	257.0     |	0.066148 |	0.933852 |   0.729483      |
|12| 	0.806144 	0.880613 	98.0 	9.0 	231.0 	240.0 	0.037500 	0.962500 	0.702128
14 	0.846058 	0.878350 	77.0 	17.0 	252.0 	269.0 	0.063197 	0.936803 	0.765957


| Item         | Price     | # In stock |
|--------------|-----------|------------|
| Juicy Apples | 1.99      | *7*        |
| Bananas      | **1.89**  | 5234       |