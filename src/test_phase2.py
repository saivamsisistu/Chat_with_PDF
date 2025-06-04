from pdf_loader import extract_text_from_pdf, split_text_into_chunks

def test_phase2():
    # Step 1: Path to a sample PDF file
    pdf_path = "src\Sai_Vams_Resume.pdf"  # Replace with your actual test file name

    # Step 2: Extract text
    text = extract_text_from_pdf(pdf_path)
    print("\n--- Extracted Text Preview ---\n")
    print(text[:1000])  # Show first 1000 characters

    # Step 3: Split into chunks
    chunks = split_text_into_chunks(text)
    print(f"\n✅ Total Chunks: {len(chunks)}\n")
    print("--- First Chunk ---")
    print(chunks[0])

if __name__ == "__main__":
    test_phase2()
