from fpdf import FPDF

from services.integer_convert import message_for_row


class PDF(FPDF):

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, path):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, path, 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def chapter_body(self, txt, c):
        # Read text file

        # Times 12
        self.set_font('Times', '', 8)
        color = c.getRgb()
        self.set_fill_color(color[0], color[1], color[2])

        # Output justified text
        self.multi_cell(0, 5, txt, border=1, align="C", fill=True)
        # Line break
        self.ln(0)
        # Mention in italics
        self.set_font('', 'I')
        # self.cell(0, 5, '(end of excerpt)')


def print_to_pdf(listeDisplayedTrame, path):
    pdf = PDF(orientation='L')
    pdf.set_title("Unvell traffic")
    pdf.set_author('HOUSSENBAY Raoul Ammar')
    pdf.add_page()
    pdf.chapter_title(path)

    for count, trame in enumerate(listeDisplayedTrame):
        t, c = message_for_row(trame)
        pdf.chapter_body(t, c)

    pdf.output('export.pdf', 'F')
