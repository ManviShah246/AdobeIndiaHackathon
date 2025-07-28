## Approach Explanation – Round 1B: Connecting the Dots

### Objective

The goal of this solution is to process a set of academic or technical PDF documents and extract only the sections most relevant to a given persona and job-to-be-done. The solution is built to run fully offline, inside a Docker container, and outputs a structured `summary.json` file capturing relevant insights from the input PDFs.

---

### 1. Offline-First Design

To meet the offline constraints of the challenge, all required packages and models are bundled during Docker image build time. No online calls are made during runtime. The `sentence-transformers` library is installed in advance and used locally for semantic similarity scoring. The selected model (`all-MiniLM-L6-v2`) is lightweight and effective for matching textual content to the persona’s task.

---

### 2. Input and Metadata Extraction

All input PDFs are placed in the `input/` folder. Metadata such as file names, page numbers, and timestamps are collected at runtime and added to the `summary.json`. This ensures traceability and transparency of the extracted sections.

---

### 3. Section Detection and Ranking

PDFs are parsed using the PyMuPDF (`fitz`) library. The tool scans each page and detects section titles using heuristics based on font size and heading patterns (e.g., large bold text, numbered headings). The extracted text blocks are then semantically compared with the job-to-be-done using sentence embeddings from `sentence-transformers`.

Each section receives a **relevance score**, and only the most aligned sections are selected. These are added to the `extracted_sections` list along with their rank, title, and document location.

---

### 4. Subsection Summarization

For each extracted section, its body text is trimmed and cleaned, and added to the `subsection_analysis` part of the JSON. This provides detailed content that can be used by the persona (e.g., a PhD student) directly in their literature review or technical document.

---

### 5. Output Structure

The final `summary.json` has three main parts:
- `metadata`: Input document names, persona, job-to-be-done, and timestamp
- `extracted_sections`: A list of the most relevant sections across documents
- `subsection_analysis`: Refined text from each selected section for easy consumption

---

### Summary

The solution balances robustness with simplicity and complies with all offline and structural requirements. It is modular, easily extendable (e.g., to support other personas), and produces output that is immediately useful for academic or research-focused workflows.
