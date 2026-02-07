from fpdf import FPDF

class MedicalReport(FPDF):
    def header(self):
        # Design: Blue Header Bar
        self.set_fill_color(33, 150, 243) # Professional Blue
        self.rect(0, 0, 210, 40, 'F')
        self.set_font('Arial', 'B', 24)
        self.set_text_color(255, 255, 255)
        self.cell(0, 20, 'CLINICAL ENCOUNTER REPORT', 0, 1, 'C')
        self.ln(10)

    def patient_info_box(self, name, age, id_num):
        self.set_fill_color(240, 240, 240) # Light Gray Box
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, f" Patient: {name} | Age: {age} | ID: {id_num}", 1, 1, 'L', fill=True)
        self.ln(5)

def create_pdf():
    pdf = MedicalReport()
    pdf.add_page()
    
    # 1. Patient Details
    pdf.patient_info_box("John Doe", "45", "MD-99210")
    
    # 2. Clinical Findings (The Design Part)
    pdf.set_font('Arial', 'B', 14)
    pdf.set_text_color(33, 150, 243)
    pdf.cell(0, 10, "PRESENTING COMPLAINT & HISTORY", 0, 1)
    
    pdf.set_font('Arial', '', 11)
    pdf.set_text_color(50, 50, 50)
    history_text = ("Patient presents with acute onset of retrosternal chest pain radiating to the left arm. "
                    "History of hypertension and smoking. Currently experiencing diaphoresis.")
    pdf.multi_cell(0, 7, history_text)
    pdf.ln(5)
    
    # 3. Lab Results Table
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(40, 10, 'Test', 1)
    pdf.cell(40, 10, 'Result', 1)
    pdf.cell(40, 10, 'Reference', 1)
    pdf.ln()
    
    pdf.set_font('Arial', '', 11)
    data = [["Troponin I", "0.45 ng/mL", "< 0.04"], ["HbA1c", "6.2%", "4.0-5.6"]]
    for row in data:
        for item in row:
            pdf.cell(40, 10, item, 1)
        pdf.ln()

    pdf.output("Medical_Report_Sample.pdf")
    print("PDF Generated Successfully!")

if __name__ == "__main__":
    create_pdf()
