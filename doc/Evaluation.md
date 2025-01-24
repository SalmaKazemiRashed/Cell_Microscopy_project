# Evaluation

For evaluating the models we have used validation and test sets from  [Nuclei](https://www.sciencedirect.com/science/article/pii/S2352340922009726).

We have compared two metrics as pixel-based Jaccard index and object-based F1-score where the threshold for comparing two objects are 90%.

The metrics that we have used for both architectures are Jaccard Index and F1-score where they both are defind based on Intersection over Union (IOU),
The IoU measures the overlap of predicted and annotated objects and is calculated according to the following equation:

```math
IOU(A,B) = \dfrac {A \cap B }{A\cup B}
```

IoU determines Jaccard Index as a pixel-based index that can range from 0 to 1, from no overlap to identical objects. 
Since overlap of predicted and original objects is rarely 100\% we selected a few different thresholds for comparison (50\% to 90\%). This is for calculating F1-score which is an object-based index. F1-score measures how many out of all predictions were true positives as the geometric average between the recall and precision.


## U-Net evaluation

For evaluating U-Net models we have used our three best models as Model3, Model12, and Model14 where in the main manuscript we have mentioned 
the different training sets that they were trained on. 
The whole evaluation of U-Net models are described in evaluation/UNet/UNET_concise_Evaluation.ipynb
The required functions are mostly taken from  [carpenterlab](https://github.com/carpenterlab/unet4nuclei.git) repo and revised according to our models and data.
Besides, a classification of Tiny, Small, Normal and Large nuclei is also performed to see in which category the models work best.
Then Jaccard index were calculated based in IOU and then by assigning a threshold, F1-score were calculated.

The following table shows the results for each U-Net model.



    |F1_score_90   | Average Jaccard Index    | False Negatives  |  False Positives | True Positives  | Detected Objects  | False Discovery Rate |  Precision  | Recall |
|---|--------------|--------------------------|------------------|------------------|-----------------|-------------------|----------------------|-------------|--------|
|3  | 0.8099       | 0.87                     | 89               |   17             | 240             | 257               |  0.066               |    0.934    |  0.729 |
|12 | 0.8061       | 0.88                     | 98               |   9              | 231             | 240               |  0.038               |    0.962    |  0.702 |
|14 | 0.8461       | 0.88                     | 77               |   17             | 252             | 269               |  0.063               |    0.937    |  0.766 |