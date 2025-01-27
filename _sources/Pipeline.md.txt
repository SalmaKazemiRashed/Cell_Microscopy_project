# Full pipeline

After conducting accurate annotations published in [Nuclei](https://www.sciencedirect.com/science/article/pii/S2352340922009726) and [Cytosol](https://www.sciencedirect.com/science/article/pii/S2352340924011107),
training U-Net and HoVer-Net models for segmenting the nuclei channel, we have compared the top 3 best models from each architecture and at the end we have used the best U-Net model that we have trained on
our own annotated images as well as some images from [BBBC](https://bbbc.broadinstitute.org/) image set.
The model's performance on test set were validated where it had 85% F1-score on 90% overlapping threshold and 88% average Jaccard index.


The experiment were conducted in two Oxidative stress (A, B) and non-oxiditive stress (C,D) groups each group has one repetition all saved in 79 groups for almost 18000 genes.
The status of each group of raw data and how we proceeded to analyse is summarized in progress_log/plateProgress_done.xlsx file.
Some of plates were missing or there were several copies. We had to deal with missing or repeated data.


The overall process for each plate is as follows:
1)	Download from swestore
2)	Run extract_convert script over plate to extract only d0 channel.
3)	Normalize them to 8bit images using bash command
4)	Save the names in 4_filelist folder  and remove .C01 from  the folder and only keep .png ones (6144 images in each full plate) 
5)	Copy  and run prediction model over them
6)	Copy back to cluster storage
7)	Run area_size.py script over them and copy the file to A, or B, or C, or D 
8)	Run the plot over all of them




# Download and Extract

