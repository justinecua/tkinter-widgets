import customtkinter as ctk
import time, os, subprocess, platform, webbrowser


def create_semi_final(root):
    # ==============================
    # Questions
    # ==============================
    questions = [
        {"title": "Calculator (Add/Subtract)", "points": 20,
        "content": "Create a basic calculator GUI.\n\nRequirements:\n• Addition and subtraction operations only\n• Buttons 0–9\n• Display input and result\n• Save as calculator.py"},
        
        {"title": "Rock-Paper-Scissors", "points": 15,
        "content": "Build a rock-paper-scissors game GUI.\n\nRequirements:\n• User and computer choice\n• Display winner\n• Save as rps.py"},
        
        {"title": "Login System", "points": 20,
        "content": "Build a simple login GUI.\n\nRequirements:\n• Register and login functionality\n• Store credentials in memory only\n• No password change\n• Save as login_system.py"},
        
        {"title": "Quiz (3 Questions, T/F)", "points": 20,
        "content": "Develop a quiz app GUI.\n\nRequirements:\n• 3 True/False questions\n• Show score at end\n• Save as quiz.py"},
        
        {"title": "To-Do List", "points": 20,
        "content": "Create a to-do list GUI.\n\nRequirements:\n• Add, mark complete, delete tasks\n• No file save needed\n• Save as todo.py"},
        
        {"title": "Random Password Generator", "points": 15,
        "content": "Create a random password generator.\n\nRequirements:\n• Select password length\n• Display generated password\n• Save as password_gen.py"},
        
        {"title": "Color Picker", "points": 15,
        "content": "Build a color picker GUI.\n\nRequirements:\n• Choose color button\n• Show selected color\n• Change window background color\n• Save as color_picker.py"},
        
        {"title": "Counter App", "points": 15,
        "content": "Make a counter GUI.\n\nRequirements:\n• Increment and decrement buttons\n• Show current count\n• Save as counter.py"},
        
        {"title": "Hello World Window", "points": 10,
        "content": "Create a simple GUI window.\n\nRequirements:\n• Show 'Hello World' message on button click\n• Save as hello_world.py"},
        
        {"title": "Stopwatch", "points": 20,
        "content": "Create a stopwatch GUI.\n\nRequirements:\n• Start, Stop, Reset buttons\n• Display time in seconds\n• Save as stopwatch.py"},
        
        {"title": "Digital Clock", "points": 20,
        "content": "Make a digital clock GUI.\n\nRequirements:\n• Display current time\n• Update every second\n• Save as digital_clock.py"},
        
        {"title": "Simple Image Viewer", "points": 15,
        "content": "Build an image viewer GUI.\n\nRequirements:\n• Load and display images\n• Next/Previous buttons\n• Save as image_viewer.py"},
        
        {"title": "Alarm Clock", "points": 15,
        "content": "Build a simple alarm clock GUI.\n\nRequirements:\n• Set alarm time\n• Show alert when alarm rings\n• Save as alarm_clock.py"},
        
        {"title": "Memory Match Game", "points": 20,
        "content": "Build a simple memory match game.\n\nRequirements:\n• Grid of cards\n• Click to reveal\n• Match pairs\n• Save as memory_game.py"},
        
        {"title": "File Opener", "points": 15,
        "content": "Create a file opener GUI.\n\nRequirements:\n• Open and display text files\n• Save as file_opener.py"}
    ]

    # ==============================
    # Layout Setup
    # ==============================
    main_frame = ctk.CTkFrame(root, fg_color="#f8fafb")
    main_frame.pack(fill="both", expand=True)

    left_nav = ctk.CTkFrame(main_frame, fg_color="#fefffe", width=280, border_width=1, border_color="#e0e0e0")
    left_nav.pack(side="left", fill="y")
    left_nav.pack_propagate(False)

    top_nav = ctk.CTkFrame(main_frame, fg_color="#fefffe", height=70, border_width=1, border_color="#e0e0e0")
    top_nav.pack(side="top", fill="x")
    top_nav.pack_propagate(False)

    content_frame = ctk.CTkFrame(main_frame, fg_color="#f8fafb")
    content_frame.pack(side="left", fill="both", expand=True)

    # ==============================
    # Fonts
    # ==============================
    button_font_normal = ctk.CTkFont(family="Arial", size=15, weight="normal")
    button_font_bold = ctk.CTkFont(family="Arial", size=15, weight="bold")

    # ==============================
    # Pre-Built Pages
    # ==============================
    pages = {}

    # ---- Home Page
    home_page = ctk.CTkFrame(content_frame, fg_color="#f8f9fa")

    info_card = ctk.CTkFrame(home_page, fg_color="white", corner_radius=5)
    info_card.pack(fill="x", pady=20, padx=20)
    ctk.CTkLabel(info_card, text="Instructions",
                 font=ctk.CTkFont(size=15, weight="bold"),
                 text_color="#2a3f5a").pack(anchor="w", padx=20, pady=(15, 0))
    ctk.CTkLabel(info_card,
                text=("You are allotted 2 hours and 30 minutes to complete your chosen projects totaling 70 points. "
                    "Select any combination of projects from the list, with each project worth 10, 15, or 20 points. "
                    "Save each project file using the specified filename. Carefully read all instructions before starting. "
                    "No external resources or internet access are allowed unless explicitly stated. "
                    "Focus on implementing the core requirements within the given time."),
                font=ctk.CTkFont(size=14),
                text_color="#444", justify="left", wraplength=1200
                ).pack(anchor="w", padx=20, pady=(5, 15))

    docs_card = ctk.CTkFrame(home_page, fg_color="white", corner_radius=5)
    docs_card.pack(fill="x", padx=20)
    ctk.CTkLabel(docs_card, text="Resources",
                 font=ctk.CTkFont(size=15, weight="bold"),
                 text_color="#2a3f5a").pack(anchor="w", padx=20, pady=15)

    def open_ctk_docs(): webbrowser.open("https://customtkinter.tomschimansky.com/documentation/widgets")
    def open_w3SchoolPython(): webbrowser.open("https://www.w3schools.com/python/")
    def open_local_pdf():
        pdf_path = os.path.abspath("assets/docs/reference2.pdf")
        if platform.system() == "Windows": os.startfile(pdf_path)
        elif platform.system() == "Darwin": subprocess.run(["open", pdf_path])
        else: subprocess.run(["xdg-open", pdf_path])

    ctk.CTkButton(docs_card, text="Open CustomTkinter Documentation", command=open_ctk_docs,
                  fg_color="#f8fafb", text_color="#38675d", hover_color="#e8eaeb",
                  height=40, corner_radius=8, font=ctk.CTkFont(weight="bold")).pack(fill="x", padx=20, pady=5)
    ctk.CTkButton(docs_card, text="Python W3School", command=open_w3SchoolPython,
                  fg_color="#f8fafb", text_color="#38675d", hover_color="#e8eaeb",
                  height=40, corner_radius=8, font=ctk.CTkFont(weight="bold")).pack(fill="x", padx=20, pady=5)
    ctk.CTkButton(docs_card, text="Building Modern GUIs with tkinter and Python (PDF)", command=open_local_pdf,
                  fg_color="#f8fafb", text_color="#38675d", hover_color="#e8eaeb",
                  height=40, corner_radius=8, font=ctk.CTkFont(weight="bold")).pack(fill="x", padx=20, pady=(0, 20))

    pages["Home"] = home_page
    
    # ---- Questions Page
    questions_page = ctk.CTkFrame(content_frame, fg_color="#f8f9fa")

    container = ctk.CTkFrame(questions_page, fg_color="#FFFFFF", corner_radius=12)
    container.pack(fill="both", expand=True, padx=20, pady=20)

    canvas = ctk.CTkCanvas(container, bg="#FFFFFF", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = ctk.CTkScrollbar(container, orientation="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    inner_frame = ctk.CTkFrame(canvas, fg_color="#FFFFFF")
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    def update_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"), width=event.width)
    inner_frame.bind("<Configure>", update_scroll)

    def on_mouse_wheel(event):
        if event.num == 0:
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        elif event.num == 4:
            canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            canvas.yview_scroll(1, "units")

    canvas.bind_all("<MouseWheel>", on_mouse_wheel)
    canvas.bind_all("<Button-4>", on_mouse_wheel)
    canvas.bind_all("<Button-5>", on_mouse_wheel)

    # === GRID DISPLAY
    cols = 3
    card_width = 350
    card_height = 280

    for i, q in enumerate(questions):
        row, col = divmod(i, cols)
        
        q_frame = ctk.CTkFrame(inner_frame, 
                            fg_color="#FFFFFF", 
                            corner_radius=12,
                            border_width=1,
                            border_color="#EAEDED",
                            width=card_width,
                            height=card_height)
        q_frame.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")
        q_frame.grid_propagate(False)  
        
        def on_enter(e, frame=q_frame): frame.configure(border_color="#D0D3D4")
        def on_leave(e, frame=q_frame): frame.configure(border_color="#EAEDED")
            
        q_frame.bind("<Enter>", on_enter)
        q_frame.bind("<Leave>", on_leave)
        
        content_container = ctk.CTkFrame(q_frame, fg_color="transparent")
        content_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        title_label = ctk.CTkLabel(content_container, text=q["title"], 
                                font=ctk.CTkFont(size=16, weight="bold"),
                                text_color="#2C3E50",
                                wraplength=card_width-40,  
                                justify="left")
        title_label.pack(anchor="w", pady=(0, 10))
        
        points_frame = ctk.CTkFrame(content_container, fg_color="#ECF7F6", corner_radius=4, height=24)
        points_frame.pack(anchor="center", pady=(0, 15))
        points_frame.pack_propagate(False)
        
        ctk.CTkLabel(points_frame, text=f"{q['points']} points", 
                    font=ctk.CTkFont(size=12, weight="bold"),
                    text_color="#449894").pack(padx=8, pady=4)
        
        content_frame = ctk.CTkFrame(content_container, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, pady=(0, 15))
        
        content_label = ctk.CTkLabel(content_frame, text=q["content"], 
                                    font=ctk.CTkFont(size=14),
                                    text_color="#34495E", 
                                    justify="left",
                                    wraplength=card_width-40,  
                                    height=100)  
        content_label.pack(anchor="nw", fill="both", expand=True)
      
    for c in range(cols):
        inner_frame.grid_columnconfigure(c, weight=1)

    pages["Questions"] = questions_page

    # ==============================
    # Show/Hide Pages
    # ==============================
    def show_page(name):
        for p in pages.values():
            p.pack_forget()
        pages[name].pack(fill="both", expand=True)

        for n, btn in buttons.items():
            btn.configure(fg_color="#fefffe", text_color="#78787e", font=button_font_normal)
        buttons[name].configure(fg_color="#f8fafb", text_color="#38675d", font=button_font_bold)

    # ==============================
    # Sidebar
    # ==============================
    ctk.CTkLabel(left_nav, text="OOP Semi Final Exam",
                 text_color="#2a3f5a", fg_color="transparent",
                 font=ctk.CTkFont(family="Arial", size=17, weight="bold")).pack(pady=25, padx=10)

    buttons = {}

    buttons["Home"] = ctk.CTkButton(left_nav, text="Home",
                                    fg_color="#fefffe", text_color="#78787e",
                                    hover_color="#f8fafb", width=200, height=40, anchor="w",
                                    font=button_font_normal, command=lambda: show_page("Home"))
    buttons["Home"].pack(pady=3, padx=20, fill="x")

    buttons["Questions"] = ctk.CTkButton(left_nav, text="Questions",
                                         fg_color="#fefffe", text_color="#78787e",
                                         hover_color="#f8fafb", width=200, height=40, anchor="w",
                                         font=button_font_normal, command=lambda: show_page("Questions"))
    buttons["Questions"].pack(pady=3, padx=20, fill="x")

    buttons["Exit"] = ctk.CTkButton(left_nav, text="Exit",
                                    fg_color="#fefffe", text_color="#78787e",
                                    hover_color="#f8fafb", width=200, height=40, anchor="w",
                                    font=button_font_normal, command=root.destroy)
    buttons["Exit"].pack(pady=3, padx=20, fill="x")

    # ==============================
    # Default Page
    # ==============================
    show_page("Home")
