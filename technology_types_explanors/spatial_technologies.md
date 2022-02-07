# Spatial Technologies

## 10X spatial transcriptomics

### Method

Visium Spatial Gene Expression works with slides developed by 10x Genomics. Each slide contains 4 capture areas with 5,000 barcoded spots. Each spot contains millions of capture oligonucleotides. The fresh-frozen tissue sections are placed, fixed, stained, and permeabilized on the capture area of the slide. The permeabilization step releases the mRNA that then binds to spatially barcoded capture spots. cDNA is then synthesized from captured mRNA (reverse transcription), pooled and prepared into a sequencing library.

### Is visium a single cell method?

No. The barcoded spots capture 1-10 cells per spot. This allows you to link spatial information to a tissue section in great detail. However, 10x Genomics is working on Visium HD, a single-cell spatial transcriptomics solution and plans on releasing it Q1, 2022.

### Is visium compatible with staining?

The workflow is compatible with H&E staining which provides you with morphological context. The method does not support immunofluorescence staining.

### Aim

Map the whole transcriptome with morphological context in FFPE or fresh-frozen tissues.

### Input

Tissue section prepared on a slide with millions of capture oligos on 5,000 barcoded spots per capture area on the slide.

### Output

- Raw RNA sequencing data with a spatial barcode and umi barcode present in Read 1 (fastq files).

- Gene expression mtrix derived from raw RNA sequencing data.

- A list of spatial barcodes.

- An image file with barcoded spots. Each of these spots is assigned a set of coordinates.

**Example Visium Datasets:**

https://www.10xgenomics.com/resources/datasets?query=&page=1&configure%5Bfacets%5D%5B0%5D=chemistryVersionAndThroughput&configure%5Bfacets%5D%5B1%5D=pipeline

## **RNAScope**

RNAscope Technology is a novel in situ hybridization (ISH) assay for detection of target RNA within intact cells.

### Method

Tissue sections or cells are fixed onto slides and pre-treated with RNAscope® Pretreatment Kit to unmask target RNA and permeabilize cells. Designed with approx. 20 target-specific double Z probes, the probes hybridize to target RNA molecules. RNAScope detection reagents amplify the  hybridization signals via sequential hybridization of amplifiers and label probes. Each dot signal represents a single target RNA molecule and can be visualised with a microscope. Single molecule signals can be quantified on a cell-by-cell basis by manual counting or automated image analysis software.

### Is RNAScope a single cell method?

It is not a single-cell sequencing method. However, single molecule signals can be quantified by microscopy on a cell-by-cell basis by manual counting or automated image analysis software. This would include counts for the specific set of approx. 20 target-specific probes. Fluorescently-labelled morphology reagents can be used to visually or computationally elucidate the morphology of the tissue.

### Aim
Map a small set of target RNA molecules (target genes) with morphological context in FFPE or fresh-frozen tissues and quantify the counts of each target probe in spatial context.

### Input
Tissue section or cells prepared on a slide treated with RNAScope treatment kit and a panel of approx. 20 or less target-specific hybridisation probes. Additionally, fluorescently-labeled morphology reagents can be used to visually or computationally elucidate the morphology of the tissue.

### Output
Counts of specific target RNA molecules on a cell-by-cell basis generated by microscopy and image analysis.

### References
https://acdbio.com/science/how-it-works

## Digital Spatial Profiling (NanoString)

Digital Spatial Profiling (DSP) is a new technology which enables spatial analysis of RNA and protein in tissue specimens on slides.

### Method

Samples are stained with large panels of pre-mixed biological probes (each incorporating a unique, UV-cleavable DNA barcode) and fluorescently-labelled morphology reagents used to visually or computationally elucidate the morphology of the tissue. Using the fluorescent morphology reagents for guidance, defined regions of interest (ROIs) are illuminated with UV light and the cleaved barcodes from these ROIs are then quantified. This allows for high-plex RNA or protein quantitation from spatially-resolved regions within the tissue. The resulting counts constitute an expression profile of key targets across ROIs and elucidate the biology specific to that region. 

### Is DSP a single cell method?

No

### Is DSP compatible with staining?

Yes. Morphology markers are used to guide region of interest selection based on visual staining patterns. NanoString provides kits to profile common tissue morphology of interest. Each kit contains a nuclear stain and two fluorescently labelled antibodies against specific biological targets. This leaves an open fluorescent channel on the instrument for adding a third antibody for tissue visualization. This channel can be used for specific cell subtypes, unique architectural proteins, or other identifiers specific to your project. Alternatively, you can use just the nuclearstain from NanoString and customize the remaining three targets if the off the shelf kits do not work for your research question.

### Aim

A large panel of target RNA molecule probes are used for hybridization to a tissue specimen on a slide. Specific regions of interest (ROIs) are chosen based on morphological markers/immunofluorescence staining. Based on these ROIs, the hybridized probes from the specific ROIs can be cleaved by UV light, enabling their amplification and preparation for sequencing.

### Input

Tissue section or cells prepared on a slide and a large panel of UV cleavable hybridisation probes. Additionally, fluorescently-labeled morphology reagents can be used to visually or computationally elucidate the morphology of the tissue and define regions of interest (ROIs).

### Output

Gene expression data for a large panel of target genes for the defined spatial regions of interest (ROIs).

### References

https://www.nanostring.com/wp-content/uploads/2020/12/MAN-10108-01_GeoMx_DSP_Experimental_Design_Guideline.pdf
**Publication:** https://www.nature.com/articles/s41586-021-03570-8
**Example dataset google sheet:** https://docs.google.com/spreadsheets/d/1e-vEqEQpdlOtQX5iXOQphq2DE-ky_bEf/edit#gid=903163399