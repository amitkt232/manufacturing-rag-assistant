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


Issue:
Broad maintenance queries retrieved partially relevant chunks without explicit interval information.

Impact:
LLM produced fallback response despite semantically related retrieval.

Potential Fix:
Hybrid retrieval or metadata filtering later.

Issue:
Troubleshooting-focused queries retrieved highly relevant procedural chunks.

Impact:
Grounded responses significantly improved.

Observation:
Technical procedural queries performed better than broad operational queries.


Observation:
Cross-encoder reranking improved relevance ordering for troubleshooting queries.

Observation:
BM25 improved exact technical keyword matching while semantic retrieval improved conceptual matching.