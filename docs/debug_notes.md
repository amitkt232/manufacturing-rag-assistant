Issue:
Repeated headers appeared across multiple pages.

Impact:
Could introduce retrieval noise.

Potential Fix:
Header/footer removal preprocessing later.


Issue:
Repeated document headers appeared across most pages.

Impact:
Could introduce retrieval duplication noise.

Potential Fix:
Header/footer cleaning during preprocessing.

Issue:
OCR quality reduced on diagram-heavy pages.

Impact:
Potential retrieval inaccuracies.

Potential Fix:
Azure Document Intelligence or layout-aware OCR later.


Issue:
Table structures were partially flattened during extraction.

Impact:
Potential retrieval ambiguity for structured maintenance values.

Potential Fix:
Table-aware parsers or layout-aware extraction later.


Issue:
Engineering diagrams/images were not semantically extracted.

Impact:
Visual maintenance context unavailable to retriever.

Potential Fix:
Multimodal pipeline or Azure Document Intelligence later.


Issue:
Some maintenance queries retrieved generic operational chunks.

Impact:
Reduced retrieval precision.

Potential Fix:
Hybrid search or reranker later.

Issue:
Table-heavy chunks reduced semantic clarity.

Impact:
Embedding quality degraded for structured content.

Potential Fix:
Table-aware chunking later.