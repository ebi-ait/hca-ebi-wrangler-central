# Technology type metadata


### Library preparation protocol parameters


| Technology                                 | Cell barcode read | Cell barcode offset | Cell barcode length | Input nucleic acid | Library construction method ontology       | End bias    | Primer  | Strand    | Umi barcode read | Umi barcode offset | Umi barcode length |
|--------------------------------------------|-------------------|---------------------|---------------------|--------------------|--------------------------------------------------|-------------|---------|-----------|------------------|--------------------|--------------------|
| 10X 3' v2                                  | Read 1            | 0                   | 16                  | polyA RNA          | EFO:0009899                                      | 3 prime tag | poly-dT | first     | Read 1           | 16                 | 10                 |
| 10X 3' v3                                  | Read 1            | 0                   | 16                  | polyA RNA          | EFO:0009922                                      | 3 prime tag | poly-dT | first     | Read 1           | 16                 | 12                 |
| 10X 3' v1                                  | Read 1 / i7 Index | 0                   | 14                  | polyA RNA          | EFO:0009901                                      | 3 prime tag | poly-dT | first     | Read 1 / Read 2  | 14                 | 10                 |
| 10X 5' v2                                  | Read 1            | 0                   | 16                  | polyA RNA          | EFO:0009900                                      | 5 prime tag | poly-dT | first     | Read 1           | 16                 | 10                 |
| 10X 5' v1                                  | Read 1 / i7 Index | 0                   | 14                  | polyA RNA          | EFO:0011025                                      | 5 prime tag | poly-dT | first     | Read 1           | 14                 | 10                 |
| Drop-seq                                   | Read 1            | 0                   | 12                  | polyA RNA          | EFO:0008722                                      | 3 prime tag | poly-dT | first     | Read 1           | 12                 | 8                  |
| DroNc-seq                                  | Read 1            | 0                   | 12                  | polyA RNA          | EFO:0008720                                      | 3 prime tag | poly-dT | first     | Read 1           | 12                 | 8                  |
| inDrop                                     | Read 2            | 0                   | 8                   | polyA RNA          | EFO:0008780                                      | 3 prime tag | poly-dT | first     | Read 2           | 8                  | 6                  |
| Smart-seq2                                 | NA                | NA                  | NA                  | polyA RNA          | EFO:0008931                                      | full length | poly-dT | unstranded| NA               | NA                 | NA                 |   
| Smart-seq                                  | NA                | NA                  | NA                  | polyA RNA          | EFO:0008930                                      | full length | poly-dT | unstranded| NA               | NA                 | NA                 |
| Smart-like                                 | NA                | NA                  | NA                  | polyA RNA          | EFO:0010184                                      | full length | poly-dT | unstranded| NA               | NA                 | NA                 |
| Fluidigm C1-based library preparation      | NA                | NA                  | NA                  | polyA RNA          | EFO:0010058                                      | full length | poly-dT | unstranded| NA               | NA                 | NA                 |
| 10X scATAC-seq                             | i5 Index          | 0                   | 16                  | DNA                | EFO:0030007                                      | full length | random  | unstranded| NA               | NA                 | NA                 |
| scATAC-seq (Microfluidics)                 | i5 Index          | 0                   | 16                  | DNA                | EFO:0008904                                      | full length | random  | unstranded| NA               | NA                 | NA                 |
| CITE-seq (cell surface protein profiling)  | Read 1            | 0                   | 16                  | polyA RNA          | EFO:0030008                                      | 3 prime tag | poly-dT | first     | Read 1           | 16                 | 12                 |
| CITE-seq (sample multiplexing)             | Read 1            | 0                   | 16                   | polyA RNA         | EFO:0030009                                      | 3 prime tag | poly-dT | first     | Read 1           | 16                 | 12                 |
| CEL-seq                                    | Read 1            | 0                   | 16                  | polyA RNA          | EFO:0009294                                      | 3 prime tag | poly-dT | first     | Read 1           | 16                 | 12                 |
| CEL-seq2                                   | Read 1            | 6                   | 6                   | polyA RNA          | EFO:0010010                                      | 3 prime tag | poly-dT | first     | Read 1           | 0                  | 6                  |
| sci-RNA-seq                                | Read 1            | 8                   | 10                  | polyA RNA          | EFO:0010550                                      | 3 prime tag | poly-dT | first     | Read 1           | 0                  | 8                  |
| Seq-Well                                   | Read 1            | 0                   | 12                  | polyA RNA          | EFO:0008919                                      | 3 prime tag | poly-dT | first     | Read 1           | 12                 | 8                  |
|                                            |                   |                     |                     |                    |                                                  |             |         |           |                  |                    |                    |
| Visium Spatial Gene Expression             |i5 Index & i7 Index| 0                   | 10                  | polyA RNA          | EFO:0010961                                      | 3 prime tag | poly-dT | first     | Read 1           | 0 spatial,16 umi  | 16 spatial,10 umi   |      
|                                            |                   |                     |                     |                    |                                                  |             |         |           |                  |                    |                    |
| ATAC-seq                                   | NA                | NA                  | NA                  | DNA                | DNA library construction (EFO:0010172)         | full length | random  | unstranded| NA               | NA                 | NA                 |      
| RNA-seq                                   | NA                | NA                  | NA                  | polyA RNA            | cDNA library construction (EFO:0004187)         | full length | poly-dT | unstranded| NA               | NA                 | NA                 |

### Sequencing protocol parameters

| Technology                                 | Paired end  | Sequencing method                      | Sequencing method ontology
|--------------------------------------------|-------------|----------------------------------------|----------------------------|
| 10X 3' v2                                  | no          | tag based single cell RNA sequencing   | EFO:0008440                |                 
| 10X 3' v3                                  | no          | tag based single cell RNA sequencing   | EFO:0008440                |                 
| 10X 3' v1                                  | no          | tag based single cell RNA sequencing   | EFO:0008440                |                 
| 10X 5' v2                                  | no          | tag based single cell RNA sequencing   | EFO:0008440                |                 
| 10X 5' v1                                  | no          | tag based single cell RNA sequencing   | EFO:0008440                |    
| Drop-seq                                   | no          | tag based single cell RNA sequencing   | EFO:0008440                | 
| DroNc-seq                                  | no          | tag based single cell RNA sequencing   | EFO:0008440                |                 
| inDrop                                     | no          | tag based single cell RNA sequencing   | EFO:0008440                |             
| Smart-seq2                                 | yes         | full length single cell RNA sequencing | EFO:0008441                |          
| Smart-seq                                  | yes         | full length single cell RNA sequencing | EFO:0008441                |                 
| Smart-like                                 | yes         | full length single cell RNA sequencing | EFO:0008441                |                 
| Fluidigm C1-based library preparation      | yes         | full length single cell RNA sequencing | EFO:0008441                |      
| 10X scATAC-seq                             | yes         | scATAC-seq                             | EFO:0010891                | 
| scATAC-seq (Microfluidics)                 | yes         | scATAC-seq                             | EFO:0010891                | 
| CITE-seq (cell surface protein profiling)  | no          | tag based single cell RNA sequencing   | EFO:0008440                |       
| CITE-seq (sample multiplexing)             | no          | tag based single cell RNA sequencing   | EFO:0008440                |     
| CEL-seq                                    | no          | tag based single cell RNA sequencing   | EFO:0008440                |                 
| CEL-seq2                                   | no          | tag based single cell RNA sequencing   | EFO:0008440                |     
| sci-RNA-seq                                | no          | tag based single cell RNA sequencing   | EFO:0008440                |    
| Seq-Well                                   | no          | tag based single cell RNA sequencing   | EFO:0008440                | 
|                                            |             |                                        |                            | 
| Visium Spatial Gene Expression             | no          | Visium Spatial Gene Expression         | EFO:0010961                |
|                                            |             |                                        |                            | 
| ATAC-seq                                   | no          | ATAC-seq                               | EFO:0007045                | 
| RNA-Seq                                    | no          | RNA-Seq                                | EFO:0008896                | 
