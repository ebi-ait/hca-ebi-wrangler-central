# Overview of NanoString Digital Spatial Profiling and RNAScope

## NanoString Digital Spatial Profiling

### Method

Digital Spatial Profiling (DSP) is a new technology which enables spatial analysis of RNA and protein in tissue specimens on slides. Samples are
stained with large panels of pre-mixed biological probes (each incorporating a unique, UV-cleavable DNA barcode) and fluorescently-labelled
morphology reagents used to visually or computationally elucidate the morphology of the tissue. Using the fluorescent morphology reagents for
guidance, defined regions of interest (ROIs) are illuminated with UV light and the cleaved barcodes from these ROIs are then quantified.
This allows for high-plex RNA or protein quantitation from spatially-resolved regions within the tissue. The resulting counts constitute an
expression profile of key targets across ROIs and elucidate the biology specific to that region. 

### Is DSP a single cell method?

No.

### Is DSP compatible with staining?

Yes. Morphology markers are used to guide region of interest selection based on visual staining patterns. NanoString provides kits to profile
common tissue morphology of interest. Each kit contains a nuclear stain and two fluorescently labelled antibodies against specific biological
targets. This leaves an open fluorescent channel on the instrument for adding a third antibody for tissue visualization. This channel can be used
for specific cell subtypes, unique architectural proteins, or other identifiers specific to your project. Alternatively, you can use just the
nuclearstain from NanoString and customize the remaining three targets if the off the shelf kits do not work for your research question.

### Aim

To quantify gene expression levels of a large panel of target genes using a panel of RNA moleculer hybridisation probes. These gene expression levels
are linked to specific regions of interest (ROIs) which are identified using morphological markers or immunofluorescence staining.

### Input

Tissue section or cells prepared on a slide and a large panel of UV cleavable hybridisation probes. Fluorescently-labeled morphology reagents can
be used to visually or computationally elucidate the morphology of the tissue and highlight regions of interest (ROIs).

### Output

- A file listing gene/transcript counts for each target gene/transcript in each region of interest (ROI), defined either by a morphological or
  fluorescence marker.

### References

See [NanoString GeoMx DSP Guidelines](https://www.nanostring.com/wp-content/uploads/2020/12/MAN-10108-01_GeoMx_DSP_Experimental_Design_Guideline.pdf).

See this [NanoString DSP publication](https://www.nature.com/articles/s41586-021-03570-8).

## RNAScope

### Method

RNAscope Technology is a novel in situ hybridization (ISH) assay for detection of target RNA within intact cells. Tissue sections or cells are
fixed onto slides and pre-treated with RNAscope® Pretreatment Kit to unmask target RNA and permeabilize cells. Designed with approx.
20 target-specific double Z probes, the probes hybridize to target RNA molecules. RNAScope detection reagents amplify the  hybridization signals
via sequential hybridization of amplifiers and label probes. Each dot signal represents a single target RNA molecule and can be visualised with
a microscope. Single molecule signals can be quantified on a cell-by-cell basis by manual counting or automated image analysis software.

### Is RNAScope a single cell method?

No. However, single molecule signals can be quantified by microscopy on a cell-by-cell basis by manual counting or automated image analysis software.
This would include counts for the specific set of approx. 20 target-specific probes. Fluorescently-labelled morphology reagents can be used to
visually or computationally elucidate the morphology of the tissue.

### Aim

Map a small set (<= 20) of target RNA molecules with morphological context in FFPE or fresh-frozen tissues and quantify the counts of each target
probe in spatial context. Note it is **not high-throughput** and **not a sequencing method**. The technique can be used to complement other spatial profiling
technques. For example, it can help to guide region of interest (ROI) selection prior to NanoString Digital Spatial Profiling. 

### Input

Tissue section or cells prepared on a slide treated with RNAScope treatment kit. Fluorescently-labeled morphology reagents can be used to
visually or computationally elucidate the morphology of the tissue.

### Output

Gene expression counts for the specific target RNA molecules within specific Regions of Interest (ROIs) or on a cell-by-cell basis if cells can
be distinguished manually using microscopy.

### References

See [https://acdbio.com/science/how-it-works](https://acdbio.com/science/how-it-works)
