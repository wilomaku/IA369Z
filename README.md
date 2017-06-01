# Corpus callosum's shape signature for segmentation error detection in large datasets

## Reproducible paper

This Readme file holds instructions for reproduction of the work **Corpus callosum's shape signature for segmentation error detection in large datasets**

This work was developed as part of a final project in the **Tools for reproducible research** subject. It is licensed under GNU v3 license, please refer to LICENSE.md for more details.

## Environment, used libraries and dependencies

* Python 2.7.6 (Be sure you have installed Python 2.7.x - Version Python 3.x presents some problems)
* Numpy 1.12.1
* Scipy 0.18.1
* Matplotlib 2.0.0
* bib_mri library (My library avaliable on: https://github.com/wilomaku/IA369Z/tree/master/dev)

## Files structure

This structure is located in the root of the git repository **wilomaku/IA369Z**:

* Deliver: Directory with main notebook .ipynb for execution and required PNG files for image visualization.
* Dev: It contains two elements: 1) bib_mri directory with Python script functions needed for execution of the reproducible paper and 2) Some old stuff under development (Not necessary).

## Instructions to execute notebook

Please, pay attention to these instructions and follow carefully

1. Make sure you have installed Jupyter Notebook with Python 2.7 (Instructions at http://jupyter.readthedocs.io/en/latest/install.html)
2. Create a local directory on location of your preference. This will be your **work_directory**
3. Write a email to wjgarciah@unal.edu.co requesting dataset link. You will get back the Dropbox link to download dataset (**dataset.zip**).
4. Download **dataset.zip**, copy it at your **work_directory** root and extract there (work_directory/dataset/). dataset directory has three directories (Seg_pixel/, Seg_ROQS/, Seg_Watershed/) containing binary masks (on .npy) and their labels (on .csv) for 153 subjects. For each diectory, masks are named as **mask_'method'_'number'.npy** where 'method' is the segmentation method that generate the mask and 'number' is the number assigned to that subject. The csv file, for each directory, has two columns: subject number and segmentation label (0 for correct segmentation and 1 for erroneous segmentation).
4. Copy the last version of main notebook (010617-WJGH-art_struc.ipynb) avaliable at https://github.com/wilomaku/IA369Z/tree/master/deliver and copy it to the **work_directory** root.
5. Run **jupyter notebook** from your **work_directory**
6. From Jupyter browser interface open main notebook (010617-WJGH-art_struc.ipynb) and run cells in order. You can check the intermediate results.

Questions? Suggestions? Please write to wjgarciah@unal.edu.co
