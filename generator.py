import tkinter as tk
import customtkinter as ctk


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
        self.fahrzeuge_rs = ctk.CTkCheckBox(self, text="RS", variable=self.rs).grid(row=0, column=1, padx=5, pady=10)
        self.fahrzeuge_mtf = ctk.CTkCheckBox(self, text="MTF", variable=self.mtf).grid(row=0, column=2, padx=5, pady=10)
        self.fahrzeuge_vf = ctk.CTkCheckBox(self, text="VF", variable=self.vf).grid(row=0, column=3, padx=5, pady=10)
        self.fahrzeuge_klf = ctk.CTkCheckBox(self, text="KLF", variable=self.klf).grid(row=0, column=4, padx=5, pady=10)
        self.fahrzeuge_wlf = ctk.CTkCheckBox(self, text="WLF", variable=self.wlf).grid(row=0, column=5, padx=5, pady=10)
        self.grid(row=10, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    def get_fahrzeuge(self):
        return self.tlf.get(), self.rs.get(), self.mtf.get(), self.vf.get(), self.klf.get(), self.wlf.get()

    def print_test(self):
        print("test")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.date = tk.StringVar()
        self.uhrzeit = tk.StringVar()
        self.einsatzort = tk.StringVar()
        self.einsatz_meldebild = tk.StringVar()
        self.pager = tk.BooleanVar()
        self.sirene = tk.BooleanVar()
        self.type = tk.StringVar()
        self.level = tk.IntVar()

        self.title("FF-Bhk Einsatzgenerator")
        self.geometry("650x800")

        self.grid_rowconfigure(0, pad=10)
        self.grid_columnconfigure((0, 1), weight=1, pad=10)

        self.app_title = ctk.CTkLabel(self, text="FF-Generator", font=("Arial", 20)).grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        self.button_generate = ctk.CTkButton(self, text="Generate", command=self.generate).grid(row=0, column=1, sticky="ew", padx=10, pady=10)

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
        self.type_entry = ctk.CTkSegmentedButton(self, variable=self.type, values=["Brandeinsatz (B)", "Technischer Einsatz (T)", "Schadstoffeinsatz (S)"]).grid(row=7, column=0, columnspan=2, padx=10, pady=10)
        self.level_entry = ctk.CTkSegmentedButton(self, variable=self.level, values=[1, 2, 3, 4]).grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        # fahrzeuge
        self.fahrzeuge_label = ctk.CTkLabel(self, text="Eingesetzte Fahrzeuge:").grid(row=9, column=0, columnspan=2, padx=10, pady=2)
        self.fahrzeuge_entry = FahrzeugeFrame(self).grid(row=10, column=0, columnspan=2, padx=10, pady=2, sticky="ew")

    def generate(self):
        print(self.date.get())
        print(self.uhrzeit.get())
        print(self.einsatzort.get())
        print(self.einsatz_meldebild.get())
        print(self.pager.get())
        print(self.sirene.get())
        # print(self.type.get())
        # print(self.level.get())
        print(self.type.get()[0] + str(self.level.get()))
        # print(self.fahrzeuge_entry.get_fahrzeuge())
        print(self.fahrzeuge_entry.print_test())
        print(self.dataa)


# class fahrzeuge:
#     tlf = False
#     rs = False
#     mtf = False
#     vf = False
#     klf = False
#     wlf = False

#     def is_valid():
#         if fahrzeuge.tlf or fahrzeuge.rs or fahrzeuge.mtf or fahrzeuge.vf or fahrzeuge.klf or fahrzeuge.wlf:
#             return True
#         else:
#             return False


# class alarmierung:
#     sirene = False
#     pager = False

#     def is_valid():
#         return alarmierung.sirene | alarmierung.pager


# class einsatz_art:
#     type = None
#     level = None

#     def is_valid():
#         val = True

#         if einsatz_art.type == "":
#             val = False
#         if einsatz_art.level == 0:
#             val = False
#         if einsatz_art.level == 4 and (einsatz_art.type[0] == "S" or einsatz_art.type[0] == "T"):
#             val = False

#         return val

#     def get_short():
#         return (einsatz_art.type[0] if einsatz_art.type else "") + str(einsatz_art.level)


# def generate():
#     tmp_date = date_picked.get().replace(".", "")
#     date_picked.valid = tmp_date.isdigit() and len(tmp_date) == 8

#     alarmierung.sirene = sirene_used.get()
#     alarmierung.pager = pager_used.get()

#     einsatz_art.type = einsatz_type.get()
#     einsatz_art.level = einsatz_level.get()

#     einsatz_meldebild.valid = einsatz_meldebild.get() != ""

#     uhrzeit.valid = uhrzeit.get() != ""

#     einsatzort.valid = einsatzort.get() != ""

#     fahrzeuge.tlf = tlf_used.get()
#     fahrzeuge.rs = rs_used.get()
#     fahrzeuge.mtf = mtf_used.get()
#     fahrzeuge.vf = vf_used.get()
#     fahrzeuge.klf = klf_used.get()
#     fahrzeuge.wlf = wlf_used.get()

#     bericht.valid = bericht.get() != ""

#     andere_beteiligte.valid = andere_beteiligte.get() != ""

#     print(f'{"🟢" if date_picked.valid else "❌"} Date: {date_picked.get()}')
#     print(f'{"🟢" if uhrzeit.valid else "❌"} Uhrzeit: {uhrzeit.get()}')
#     print(f'{"🟢" if einsatzort.valid else "❌"} Einsatzort: {einsatzort.get()}')
#     print(f'{"🟢" if alarmierung.is_valid() else "❌"} Alarmierungsart: sirene={alarmierung.sirene}, pager={alarmierung.pager}')
#     print(f'{"🟢" if einsatz_art.is_valid() else "❌"} Einsatzart: {einsatz_art.get_short()}')
#     print(f'{"🟢" if einsatz_meldebild.valid else "❌"} Meldebild: {einsatz_meldebild.get()}')
#     print(f'{"🟢" if fahrzeuge.is_valid() else "❌"} Fahrzeuge: tlf={fahrzeuge.tlf}, rs={fahrzeuge.rs}, mtf={fahrzeuge.mtf}, vf={fahrzeuge.vf}, klf={fahrzeuge.klf}, wlf={fahrzeuge.wlf}')
#     print(f'{"🟢" if bericht.valid else "❌"} Bericht: {bericht.get()}')
#     print(f'{"🟢" if andere_beteiligte.valid else "❌"} Andere Beteiligte: {andere_beteiligte.get()}')

#     all_valid = (
#         date_picked.valid and alarmierung.is_valid() and einsatz_art.is_valid() and einsatz_meldebild.valid and uhrzeit.valid and einsatzort.valid and fahrzeuge.is_valid() and bericht.valid and andere_beteiligte.valid
#     )
#     print(f'{"🟢" if all_valid else "❌"}')

#     print("")


# # bericht, andere leute

# ###setup
# root = ctk.CTk()
# root.geometry("650x800")
# root.title("FF-Generator")
# date_picked = tk.StringVar()
# einsatz_type = tk.StringVar()
# sirene_used = tk.BooleanVar()
# pager_used = tk.BooleanVar()
# einsatz_level = tk.IntVar()
# einsatz_meldebild = tk.StringVar()
# uhrzeit = tk.StringVar()
# einsatzort = tk.StringVar()
# bericht = tk.StringVar()
# andere_beteiligte = tk.StringVar()

# tlf_used = tk.BooleanVar()
# rs_used = tk.BooleanVar()
# mtf_used = tk.BooleanVar()
# vf_used = tk.BooleanVar()
# klf_used = tk.BooleanVar()
# wlf_used = tk.BooleanVar()

# ### gloabl ui

# root.grid_rowconfigure(0, pad=10)
# root.grid_columnconfigure(0, weight=1)
# root.grid_columnconfigure(1, weight=1)

# label = ctk.CTkLabel(root, text="FF-Generator", font=("Arial", 20)).grid(row=0, column=0, sticky="ew", padx=10, pady=10)

# ###generate button
# button_generate = ctk.CTkButton(root, text="Generate", command=generate).grid(row=0, column=1, sticky="ew", padx=10, pady=10)

# ### date
# date_text = ctk.CTkLabel(root, text="Datum:").grid(row=1, column=0, padx=10, pady=2)
# date_entry = ctk.CTkEntry(root, textvariable=date_picked).grid(row=2, column=0, sticky="ew", padx=10, pady=2)


# ### uhrzeit
# uhrzeit_text = ctk.CTkLabel(root, text="Uhrzeit:").grid(row=1, column=1, padx=10, pady=2)
# uhrzeit_entry = ctk.CTkEntry(root, textvariable=uhrzeit).grid(row=2, column=1, sticky="ew", padx=10, pady=2)


# ### einsatzort
# einsatzort_text = ctk.CTkLabel(root, text="Einsatzort:").grid(row=3, column=0, padx=10, pady=2)
# einsatzort_entry = ctk.CTkEntry(root, textvariable=einsatzort).grid(row=4, column=0, sticky="ew", padx=10, pady=2)


# ### meldebild
# meldebild_text = ctk.CTkLabel(root, text="Meldebil des Einsatzes:").grid(row=3, column=1, padx=10, pady=2)
# meldebild_entry = ctk.CTkEntry(root, textvariable=einsatz_meldebild).grid(row=4, column=1, sticky="ew", padx=10, pady=2)


# # ### alarmierung
# ctk.CTkLabel(root, text="Alarmierung:").grid(row=5, column=0, columnspan=2, padx=10, pady=2)
# checkbox_sirene = ctk.CTkCheckBox(root, text="Sirene", variable=sirene_used).grid(row=6, column=0, padx=10, pady=2)
# checkbox_pager = ctk.CTkCheckBox(root, text="Pager", variable=pager_used).grid(row=6, column=1, padx=10, pady=2)


# ### art des einsatzes
# checkbox_type = ctk.CTkSegmentedButton(root, variable=einsatz_type, values=["Brandeinsatz (B)", "Technischer Einsatz (T)", "Schadstoffeinsatz (S)"]).grid(row=7, column=0, columnspan=2, padx=10, pady=10)
# checkbox_level = ctk.CTkSegmentedButton(root, variable=einsatz_level, values=[1, 2, 3, 4]).grid(row=8, column=0, columnspan=2, padx=10, pady=10)


# ### fahrzeuge
# fahrzeuge_text = ctk.CTkLabel(root, text="Eingesetzte Fahrzeuge:").grid(row=9, column=0, columnspan=2, padx=10, pady=2)
# FahrzeugeFrame = ctk.CTkFrame(root)
# FahrzeugeFrame.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)  # sort of sticky="ew"
# FahrzeugeFrame.fahrzeuge_tlf = ctk.CTkCheckBox(FahrzeugeFrame, text="TLF", variable=tlf_used).grid(row=0, column=0, padx=5, pady=10)
# FahrzeugeFrame.fahrzeuge_rs = ctk.CTkCheckBox(FahrzeugeFrame, text="RS", variable=rs_used).grid(row=0, column=1, padx=5, pady=10)
# FahrzeugeFrame.fahrzeuge_mtf = ctk.CTkCheckBox(FahrzeugeFrame, text="MTF", variable=mtf_used).grid(row=0, column=2, padx=5, pady=10)
# FahrzeugeFrame.fahrzeuge_vf = ctk.CTkCheckBox(FahrzeugeFrame, text="VF", variable=vf_used).grid(row=0, column=3, padx=5, pady=10)
# FahrzeugeFrame.fahrzeuge_klf = ctk.CTkCheckBox(FahrzeugeFrame, text="KLF", variable=klf_used).grid(row=0, column=4, padx=5, pady=10)
# FahrzeugeFrame.fahrzeuge_wlf = ctk.CTkCheckBox(FahrzeugeFrame, text="WLF", variable=wlf_used).grid(row=0, column=5, padx=5, pady=10)
# FahrzeugeFrame.grid(row=10, column=0, columnspan=2, sticky="ew", padx=10, pady=10)


# ### andere beteiligte
# beteiligte_text = ctk.CTkLabel(root, text="Andere Beteiligte:").grid(row=11, column=0, columnspan=2, padx=10, pady=2)
# # beteiligte_entry = ctk.CTkEntry(root, textvariable=andere_beteiligte, placeholder_text="CTkEntry").grid(row=12, column=0, columnspan=2, sticky="ew", padx=10, pady=2)
# beteiligte_entry = tk.Text(root, height=5, font=("Arial", 12), wrap="word", background="darkgray")
# beteiligte_entry.bind("<KeyRelease>", lambda event: andere_beteiligte.set(event.widget.get("1.0", "end-1c")))
# beteiligte_entry.grid(row=12, column=0, columnspan=2, sticky="ew", padx=10, pady=2)


# # ### bericht
# bericht_text = ctk.CTkLabel(root, text="Bericht:").grid(row=13, column=0, columnspan=2, padx=10, pady=2)
# bericht_entry = tk.Text(root, height=10, font=("Arial", 12), wrap="word", background="darkgray")
# bericht_entry.bind("<KeyRelease>", lambda event: bericht.set(event.widget.get("1.0", "end-1c")))
# bericht_entry.grid(row=14, column=0, columnspan=2, sticky="ew", padx=10, pady=2)


# root.mainloop()

if __name__ == "__main__":
    app = App()
    app.mainloop()
