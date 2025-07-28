import os
import json
import fitz  # PyMuPDF
from datetime import datetime

INPUT_DIR = "input"
OUTPUT_DIR = "output"

def extract_sections(pdf_path):
    doc = fitz.open(pdf_path)
    results = []

    for page_num, page in enumerate(doc):
        text = page.get_text()
        if "method" in text.lower():  # Just a placeholder logic
            results.append({
                "document": os.path.basename(pdf_path),
                "page_number": page_num + 1,
                "section_title": "Method Section",
                "importance_rank": 1,
                "refined_text": text.strip()
            })

    return results

def main():
    result = {
        "metadata": {
            "input_documents": [],
            "persona": "PhD in Computational Biology",
            "job_to_be_done": "Write literature review on GNNs for Drug Discovery",
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": [],
        "subsection_analysis": []
    }

    for file in os.listdir(INPUT_DIR):
        if file.endswith(".pdf"):
            path = os.path.join(INPUT_DIR, file)
            result["metadata"]["input_documents"].append(file)
            sections = extract_sections(path)

            for sec in sections:
                result["extracted_sections"].append({
                    "document": sec["document"],
                    "page_number": sec["page_number"],
                    "section_title": sec["section_title"],
                    "importance_rank": sec["importance_rank"]
                })
                result["subsection_analysis"].append({
                    "document": sec["document"],
                    "page_number": sec["page_number"],
                    "refined_text": sec["refined_text"]
                })

    with open(os.path.join(OUTPUT_DIR, "summary.json"), "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)

if __name__ == "__main__":
    main()
