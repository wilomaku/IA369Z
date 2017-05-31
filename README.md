# Corpus callosum's shape signature for segmentation error detection in large datasets

## Reproducible paper

This Readme file holds instructions for reproduction of the work **Corpus callosum's shape signature for segmentation error detection in large datasets**

This work was done as part of the final project in the **Tools for reproducible research** subject. It is licensed under GNU v3 license, please refer to LICENSE.md for more details.

## Environment and used libraries and dependencies

* Python 2.7
* Numpy 1.12.1
* Scipy 0.18.1
* Matplotlib 2.0.0
* Nibabel 2.0.1
* bib_mri library (My library avaliable on: )

## Files structure

This structure is located in the root of the git repository **wilomaku/IA369Z**:

* Deliver: Directory with main notebook .ipynb for execution and required PNG files for image visualization.
* Dev: It contains two elements: 1) bib_mri directory with Python script functions needed for execution of the reproducible paper and 2) Not required notebooks did during development of the project.

## Instructions to execute notebook

Please, pay attention to these instructions and follow carefully

1. Make sure you have installed Jupyter Notebook with Python 2.7 (Instructions at http://jupyter.readthedocs.io/en/latest/install.html)
2. Install Nibabel through Anaconda: pip install nibabel (Instructions at http://nipy.org/nibabel/installation.html)
3. Create a local directory on location of your preference. This will be your work_directory
4. Download the dataset directories availables at **XDEF** and copy each one at the work_directory root:
  * Three directories (Seg_pixel/, Seg_ROQS/, Seg_Watershed/) containing binary masks (on .npy) and their labels (on .csv) for the three segmentation methods and the 153 subjects. For each diectory, masks are named as mask_'method'_'number'.npy where 'method' is the segmentation method that generate the mask and 'number' is the number assigned to that subject. The csv file has two columns: subject number and segmentation label (0 for correct segmentation and 1 for erroneous segmentation).
  * One directory (dif_mri/) containing nifti diffusion files (on .nii) for 1 subject
5. Download the last version of main notebook (.ipynb) avaliable at https://github.com/wilomaku/IA369Z/tree/master/dev and copy it to the work_directory
6. Move to the work_directory and run **jupyter notebook**
7. From Jupyter browser interface open main notebook (.ipynb) and run cells in order. You can check the intermediate results.
