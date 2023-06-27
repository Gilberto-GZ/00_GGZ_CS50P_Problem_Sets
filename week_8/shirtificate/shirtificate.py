from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 40)
        self._pdf.set_draw_color(150,0,0)
        self._pdf.cell(0, 30, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", border=1, align='C')
        self._pdf.image("shirtificate.png", w=self._pdf.epw, y=60)
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255,255,255)
        self._pdf.text(x=60, y=130, txt=f"{name} took CS50")

    def save(self, name):
        self._pdf.output(name)



name = input("Name: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")

