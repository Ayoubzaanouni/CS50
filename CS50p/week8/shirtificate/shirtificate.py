from fpdf import FPDF

class PDF(FPDF):

    def header(self):
        self.image("shirtificate.png", 10, 65, 190, 190)
        self.set_font("helvetica", "B", 45)
        self.text(45, 45, "CS50 Shirtificate")

    def footer(self):
        self.set_font("helvetica", "B", 25)
        self.set_text_color(255,255,255)
        self.text(72, 140, name + " took CS50")

name = input("what's your name? ")
pdf = PDF()
pdf.add_page()
pdf.footer()
pdf.output("shirtificate.pdf")



