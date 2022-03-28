## 10X Spatial Transcriptomics

### Method

Visium Spatial Gene Expression works with slides developed by 10x Genomics. Each slide contains 4 capture areas with 5,000 barcoded spots. Each spot contains millions of capture oligonucleotides. The fresh-frozen tissue sections are placed, fixed, stained, and permeabilized on the capture area of the slide. The permeabilization step releases the mRNA that then binds to spatially barcoded capture spots. cDNA is then synthesized from captured mRNA (reverse transcription), pooled and prepared into a sequencing library.

### Is visium a single cell method?

Not yet to date. The barcoded spots capture 1-10 cells per spot. This allows you to link spatial information to a tissue section in great detail. However, 10x Genomics is working on Visium HD, a single-cell spatial transcriptomics solution and plans on releasing it Q1, 2022.

### Is visium compatible with staining?

The workflow is compatible with H&E staining which provides you with morphological context. The method does not support immunofluorescence staining.

### Aim

Map the whole transcriptome with morphological context in FFPE or fresh-frozen tissues.

### Input

Tissue section prepared on a slide with millions of capture oligos on 5,000 barcoded spots per capture area on the slide.

### Output

- Raw RNA sequencing data with a spatial barcode and umi barcode present in Read 1 (fastq files).

- Gene expression mtrix derived from raw RNA sequencing data.

- A list of spatial barcodes that can be mapped to spatial coordinates in the image file.

- An image file with barcoded spots. Each of these spots is assigned a set of coordinates.

### Example Visium Datasets

https://www.10xgenomics.com/resources/datasets?query=&page=1&configure%5Bfacets%5D%5B0%5D=chemistryVersionAndThroughput&configure%5Bfacets%5D%5B1%5D=pipeline
