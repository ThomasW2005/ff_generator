import tkinter as tk
import customtkinter as ctk
from templates import *
import locale
from datetime import datetime


class FahrzeugeFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.tlf = tk.BooleanVar()
        self.rs = tk.BooleanVar()
        self.mtf = tk.BooleanVar()
        self.vf = tk.BooleanVar()
        self.klf = tk.BooleanVar()
        self.wlf = tk.BooleanVar()

        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)  # sort of sticky="ew"

        self.fahrzeuge_tlf = ctk.CTkCheckBox(self, text="TLF", variable=self.tlf).grid(row=0, column=0, padx=5, pady=10)
        self.fahrzeuge_rs = ctk.CTkCheckBox(self, text="RF-S", variable=self.rs).grid(row=0, column=1, padx=5, pady=10)
        self.fahrzeuge_mtf = ctk.CTkCheckBox(self, text="MTF", variable=self.mtf).grid(row=0, column=2, padx=5, pady=10)
        self.fahrzeuge_vf = ctk.CTkCheckBox(self, text="VF", variable=self.vf).grid(row=0, column=3, padx=5, pady=10)
        self.fahrzeuge_klf = ctk.CTkCheckBox(self, text="KLF", variable=self.klf).grid(row=0, column=4, padx=5, pady=10)
        self.fahrzeuge_wlf = ctk.CTkCheckBox(self, text="WLF", variable=self.wlf).grid(row=0, column=5, padx=5, pady=10)

    def get_fahrzeuge(self):
        fahrzeuge = []
        if self.tlf.get():
            fahrzeuge.append("TLF")
        if self.rs.get():
            fahrzeuge.append("RF-S")
        if self.mtf.get():
            fahrzeuge.append("MTF")
        if self.vf.get():
            fahrzeuge.append("VF")
        if self.klf.get():
            fahrzeuge.append("KLF")
        if self.wlf.get():
            fahrzeuge.append("WLF")
        return fahrzeuge


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        locale.setlocale(locale.LC_TIME, "de_AT")

        # self.date = None

        # self.date = None

        self.title("FF-Bhk Einsatzgenerator v1.1")
        # self.geometry("950x900")
        # self.geometry("950x880")

        self.grid_columnconfigure((0, 1), weight=1)

        self.generator_entry = Generator(self)
        self.generator_entry.grid(row=0, column=0, sticky="news", padx=10, pady=10)

        self.output_entry = ctk.CTkTextbox(self, width=600)
        self.output_entry.grid(row=0, column=1, sticky="news", padx=(0, 10), pady=10)

        self.button_generate_full = ctk.CTkButton(self.generator_entry, text="Generate Full Article", command=self.generate).grid(row=15, column=0, sticky="ew", padx=10, pady=10)
        self.button_generate_minimal = ctk.CTkButton(self.generator_entry, text="Generate Homepage Snippet", command=self.generate_snippet).grid(row=15, column=1, sticky="ew", padx=10, pady=10)

    def write_out(self, data):
        self.error = False
        if data.startswith("F"):
            self.error = True

        t = tk.Tk()
        t.withdraw()
        t.clipboard_clear()
        t.clipboard_append(data)
        t.update()
        t.destroy()

        self.output_entry.delete(1.0, tk.END)
        self.output_entry.insert(tk.END, data)

    def check_input(self):
        try:
            self.generator_entry.level_entry.configure(values=([1, 2, 3, 4] if self.generator_entry.type.get() == "Brandeinsatz (B)" else [1, 2, 3]))

            self.eingesetzte_menner_text = self.generator_entry.eingesetzte_menner.get()

            if not self.eingesetzte_menner_text.isnumeric():
                self.write_out("Fehler: Eingesetzte Männer ist keine Zahl")
                return

            self.eingesetzte_menner = int(self.eingesetzte_menner_text)

            if not self.eingesetzte_menner:
                self.write_out("Fehler: Keine eingesetzten Männer angegeben")
                return

            self.date = self.generator_entry.date.get().replace(".", "")
            self.date_with_dots = self.generator_entry.date.get()
            if len(self.date) != 8:
                self.write_out("Fehler: Datum ist nicht korrekt")
                return

            date_obj = datetime.strptime(self.date, "%d%m%Y")
            self.weekday = date_obj.strftime("%A")

            self.uhrzeit = self.generator_entry.uhrzeit.get()
            if len(self.uhrzeit) != 5:
                self.write_out("Fehler: Uhrzeit ist nicht korrekt")
                return

            self.ort = self.generator_entry.einsatzort.get()
            if not self.ort:
                self.write_out("Fehler: Kein Einsatzort angegeben")
                return

            self.meldebild = self.generator_entry.einsatz_meldebild.get()
            if not self.meldebild:
                self.write_out("Fehler: Kein Meldebild ausgewählt")
                return

            self.alarmierung = ""
            if not self.generator_entry.pager.get() and not (self.generator_entry.sirene.get()):
                self.write_out("Fehler: Keine Alarmierung ausgewählt")
                return

            if self.generator_entry.pager.get():
                self.alarmierung += temp_pager
            if self.generator_entry.sirene.get():
                self.alarmierung += temp_sirene

            if (not self.generator_entry.type.get()) or (not self.generator_entry.level.get()):
                self.write_out("Fehler: Kein Einsatztyp ausgewählt")
                return
            self.type = self.generator_entry.type.get()[0] + str(self.generator_entry.level.get())

            if self.type == "T4" or self.type == "S4":
                self.write_out("Fehler: Einsatzstufe 4 ist nicht für Technische oder Schadstoffeinsätze möglich")
                return

            self.fahrzeuge_bild = ""
            self.fahrzeuge_text = ""
            self.fahrzeuge = self.generator_entry.fahrzeuge_entry.get_fahrzeuge()
            if not self.fahrzeuge:
                self.write_out("Fehler: Keine Fahrzeuge ausgewählt")
                return

            for fahrzeug in self.fahrzeuge:
                self.fahrzeuge_text += temp_auto_text_template.replace("[--fahrzeug--]", fahrzeug)
                if fahrzeug == "TLF":
                    self.fahrzeuge_bild += temp_auto_tlf
                elif fahrzeug == "RF-S":
                    self.fahrzeuge_bild += temp_auto_rf
                elif fahrzeug == "MTF":
                    self.fahrzeuge_bild += temp_auto_mtf
                elif fahrzeug == "VF":
                    self.fahrzeuge_bild += temp_auto_vf
                elif fahrzeug == "KLF":
                    self.fahrzeuge_bild += temp_auto_klf
                elif fahrzeug == "WLF":
                    self.fahrzeuge_bild += temp_auto_wlf

            self.bericht = self.generator_entry.einsatzbericht.get()
            if not self.bericht:
                self.write_out("Fehler: Kein Einsatzbericht angegeben")
                return

            self.andere_beteiligte = ""
            self.unsere_ff = f'FF Böheimkirchen - Markt ({len(self.fahrzeuge)} Fahrzeug{"" if len(self.fahrzeuge)==1 else "e"} + {self.eingesetzte_menner} Mann ‑ inkl. Bereitschaft)'
            self.andere_beteiligte += temp_andere_beteiligte.replace("[--andere--beteiligte--]", self.unsere_ff)

            self.andere_beteiligte_read = self.generator_entry.andere_beteiligte.get()
            if self.andere_beteiligte_read:
                for andere in self.andere_beteiligte_read.splitlines():
                    self.andere_beteiligte += temp_andere_beteiligte.replace("[--andere--beteiligte--]", andere)

            if self.type.startswith("T"):
                self.type_text = temp_t_image
            elif self.type.startswith("S"):
                self.type_text = temp_s_image
            elif self.type.startswith("B"):
                self.type_text = temp_b_image

            self.write_out("Erfolgreich generiert")

        except Exception as e:
            self.write_out("Fehler: " + str(e))

    def generate_snippet(self):
        try:
            self.check_input()
            if self.error == True:
                return
            template = open("template_snippet_do_not_touch.html", "r", encoding="utf-8")
            output = template.read()

            output = output.replace("[--insert--type--image--]", self.type_text)

            output = output.replace("[--insert--entire--date--]", self.weekday + ", " + self.date_with_dots)
            output = output.replace("[--insert--date--here--]", self.date)
            output = output.replace("[--insert--type--here--]", self.type)
            output = output.replace("[--insert--meldebild--here--]", self.meldebild)
            output = output.replace("[--insert--ort--here--]", self.ort)

            self.write_out(output)

        except Exception as e:
            self.write_out("Fehler: " + str(e))

    def generate(self):
        try:
            self.check_input()
            if self.error == True:
                return
            template = open("template_do_not_touch.html", "r", encoding="utf-8")
            output = template.read()
            output = output.replace("[--insert--date--here--]", self.date)
            output = output.replace("[--insert--type--here--]", self.type)
            output = output.replace("[--insert--meldebild--here--]", self.meldebild)
            output = output.replace("[--insert--date--with--dots--here--]", self.date_with_dots)
            output = output.replace("[--insert--uhrzeit--here--]", self.uhrzeit)
            output = output.replace("[--insert--ort--here--]", self.ort)
            output = output.replace("[--insert--alarmierung--here--]", self.alarmierung)
            output = output.replace("[--insert--fahrzeuge--text--here--]", self.fahrzeuge_text)
            output = output.replace("[--insert--fahrzeuge--bild--here--]", self.fahrzeuge_bild)
            output = output.replace("[--insert--bericht--here--]", self.bericht.replace("\n", "<br />"))
            output = output.replace("[--insert--andere--beteiligte--here--]", self.andere_beteiligte)

            self.write_out(output)

        except Exception as e:
            self.write_out(f"Fehler: {e}")


class Generator(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.date = tk.StringVar()
        self.uhrzeit = tk.StringVar()
        self.einsatzort = tk.StringVar()
        self.einsatz_meldebild = tk.StringVar()
        self.pager = tk.BooleanVar()
        self.sirene = tk.BooleanVar()
        self.type = tk.StringVar()
        self.level = tk.IntVar()
        self.andere_beteiligte = tk.StringVar()
        self.einsatzbericht = tk.StringVar()
        self.eingesetzte_menner = tk.StringVar()

        self.grid_rowconfigure(0, pad=10)
        self.grid_columnconfigure((0, 1), weight=1, pad=10)

        # self.app_title = ctk.CTkLabel(self, text="FF-Generator", font=("Arial", 20)).grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        # self.button_generate = ctk.CTkButton(self, text="Generate", command=self.generate).grid(row=0, column=1, sticky="ew", padx=10, pady=10)

        # anzahl der eingesetzten männer
        self.eingesetzte_menner_label = ctk.CTkLabel(self, text="Eingesetzte Männer:").grid(row=0, column=0, sticky="we", padx=10, pady=10)
        self.eingesetzte_menner_entry = ctk.CTkEntry(self, textvariable=self.eingesetzte_menner).grid(row=0, column=1, sticky="ew", padx=10, pady=10)

        ## date
        self.date_label = ctk.CTkLabel(self, text="Datum:").grid(row=1, column=0, padx=10, pady=2)
        self.date_entry = ctk.CTkEntry(self, textvariable=self.date).grid(row=2, column=0, sticky="ew", padx=10, pady=2)

        # uhrzeit
        self.uhrzeit_label = ctk.CTkLabel(self, text="Uhrzeit:").grid(row=1, column=1, padx=10, pady=2)
        self.uhrzeit_entry = ctk.CTkEntry(self, textvariable=self.uhrzeit).grid(row=2, column=1, sticky="ew", padx=10, pady=2)

        # einsatzort
        self.einsatzort_label = ctk.CTkLabel(self, text="Einsatzort:").grid(row=3, column=0, padx=10, pady=2)
        self.einsatzort_entry = ctk.CTkEntry(self, textvariable=self.einsatzort).grid(row=4, column=0, sticky="ew", padx=10, pady=2)

        # meldebild
        self.meldebild_label = ctk.CTkLabel(self, text="Meldebil des Einsatzes:").grid(row=3, column=1, padx=10, pady=2)
        self.meldebild_entry = ctk.CTkEntry(self, textvariable=self.einsatz_meldebild).grid(row=4, column=1, sticky="ew", padx=10, pady=2)

        # alarmierung
        self.alarmierung_label = ctk.CTkLabel(self, text="Alarmierung:").grid(row=5, column=0, columnspan=2, padx=10, pady=2)
        self.alarmierung_sirene_entry = ctk.CTkCheckBox(self, text="Sirene", variable=self.sirene).grid(row=6, column=0, padx=10, pady=2)
        self.alarmierung_pager_entry = ctk.CTkCheckBox(self, text="Pager", variable=self.pager).grid(row=6, column=1, padx=10, pady=2)

        # art des einsatzes
        self.type_entry = ctk.CTkSegmentedButton(self, variable=self.type, values=["Brandeinsatz (B)", "Technischer Einsatz (T)", "Schadstoffeinsatz (S)"])
        # func = lambda event: self.level_entry.configure(values=([1, 2, 3, 4] if self.type.get() == "Brandeinsatz (B)" else [1, 2, 3]))
        # self.type_entry.bind("<KeyRelease>", func)
        self.type_entry.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        self.level_entry = ctk.CTkSegmentedButton(self, variable=self.level, values=[1, 2, 3, 4])
        self.level_entry.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
        # self.level_entry.configure(values=[1, 2, 3, 4])

        # fahrzeuge
        self.fahrzeuge_label = ctk.CTkLabel(self, text="Eingesetzte Fahrzeuge:").grid(row=9, column=0, columnspan=2, padx=10, pady=2)
        self.fahrzeuge_entry = FahrzeugeFrame(self)
        self.fahrzeuge_entry.grid(row=10, column=0, columnspan=2, padx=10, pady=2, sticky="ew")

        # andere beteiligte
        self.beteiligte_label = ctk.CTkLabel(self, text="Andere Beteiligte:").grid(row=11, column=0, columnspan=2, padx=10, pady=2)
        self.beteiligte_entry = ctk.CTkTextbox(self, height=100, font=("Arial", 12))
        self.beteiligte_entry.bind("<KeyRelease>", lambda event: self.andere_beteiligte.set(event.widget.get("1.0", "end-1c")))
        self.beteiligte_entry.grid(row=12, column=0, columnspan=2, sticky="nesw", padx=10, pady=2)

        # einsatzbericht
        self.einsatzbericht_label = ctk.CTkLabel(self, text="Einsatzbericht:").grid(row=13, column=0, columnspan=2, padx=10, pady=2)
        self.einsatzbericht_entry = ctk.CTkTextbox(self, font=("Arial", 12))
        self.einsatzbericht_entry.bind("<KeyRelease>", lambda event: self.einsatzbericht.set(event.widget.get("1.0", "end-1c")))
        self.einsatzbericht_entry.grid(row=14, column=0, columnspan=2, sticky="nesw", padx=10, pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
