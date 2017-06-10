# Corpus callosum's shape signature for segmentation error detection in large datasets

## Reproducible paper

This Readme file holds instructions for reproduction of the work **Corpus callosum's shape signature for segmentation error detection in large datasets**

This work was developed as part of a final project in the **Tools for reproducible research** course. It is licensed under GNU v3 license, please refer to LICENSE.md for more details.

## Environment, used libraries and dependencies

* Python 2.7.6 (Be sure you have installed Python 2.7.x - Version Python 3.x presents some problems)
* Numpy 1.12.1
* Scipy 0.18.1
* Matplotlib 2.0.0
* bib_mri library (My library avaliable on: https://github.com/wilomaku/IA369Z/tree/master/dev)

## Workflow

This project receives a binary mask, in .npy format, and return a binary value depending if it is erroneous segmentation (1) or correct segmentation (1). For constructing model (mean curvature generation and signature configuration), binary masks were passed (in .pny format).

![Alt text](figures/workflow_simp.png?raw=true "Title")

## Files structure

This structure is located in the root of the git repository **wilomaku/IA369Z**:

* Deliver: Directory with main notebook **'date'-WJGH-art_struc.ipynb** for execution. The **'date'** part in file name is formatted as day/month/year (last two digits). Please make sure you are using the last released notebook. Old versions of released notebooks are availables too, but they are not updated.
* Dev: It contains two elements: 1) bib_mri directory with Python script functions needed for execution of the reproducible paper and 2) Some old stuff under development (Not necessary).
* Images: Necessary images for notebook visualization. The user should not require to do anything here.

## Instructions to execute notebook

Please, pay attention to these instructions and follow carefully. Besides Jupyter notebook installed, you must have a work directory with three elements: dataset directory, ipyhton script and library directory with the necessary functions.

1. Make sure you have installed Jupyter Notebook with Python 2.7 (Instructions at http://jupyter.readthedocs.io/en/latest/install.html)
2. Create a local directory on location of your preference. This will be your **rep_directory**. If you already have a directory for repositories use it.
3. Clone the project's repository (available on https://github.com/wilomaku/IA369Z) directly on your **rep_directory**. Follow the next steps from your shell terminal or your prefered command line interface:
  - cd **rep_directory**
  - git clone https://github.com/wilomaku/IA369Z.git
4. Write a email to wjgarciah@unal.edu.co requesting dataset link. You will get back the Dropbox link to download dataset (**dataset.zip**).
5. Download **dataset.zip**, copy it at **rep_directory/IA369Z/** and extract there. dataset directory has three directories (Seg_pixel/, Seg_ROQS/, Seg_Watershed/) containing binary masks (on .npy) and their labels (on .csv) for 153 subjects. For each directory, masks are named as **mask_'method'_'number'.npy** where 'method' is the segmentation method that generate the mask and 'number' is the number assigned to that subject. The csv file, for each directory, has two columns: subject number and segmentation label (0 for correct segmentation and 1 for erroneous segmentation).
6. Run **jupyter notebook** from your **rep_directory/IA369Z/** directory.
7. From Jupyter browser interface open main notebook (the most recent one) in the deliver directory and run cells in order. You can check the intermediate results.

Questions? Suggestions? Please write to wjgarciah@unal.edu.co
