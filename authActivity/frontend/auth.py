import tkinter as tk
import customtkinter
from authActivity.backend.UserAccount import UserAccount
from PIL import Image, ImageTk

class Auth(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.user = UserAccount()
        self.pack(fill="both", expand=True)

        self.bg_image = Image.open("assets/images/bg3.jpg") 
        self.bg_image = self.bg_image.resize((master.winfo_screenwidth(),
                                              master.winfo_screenheight()))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(relx=0.5, rely=0.5, anchor="center")
        self.bg_label.lower()  

        self.notif_label = customtkinter.CTkLabel(
            self,
            text="",
            fg_color='transparent',  
            text_color="#000000",
            font=("Arial", 11),
            padx=20,
            pady=12,
            corner_radius=5
        )
        self.notif_label.place(relx=1.0, rely=1.0, anchor="se", y=-10, x=-10)
        self.notif_label.place_forget()  

        self.current_frame = None
        self.show_login()

    def show_notif(self, message):
        if message:
            self.notif_label.place(relx=1.0, rely=1.0, anchor="se", y=-10, x=-10)
            self.notif_label.configure(text=message, fg_color="#ffffff")  
            self.notif_label.lift()
            self.after(3000, self.clear_notif)
        else:
            self.clear_notif()

    def clear_notif(self):
        self.notif_label.place_forget()


    def clear_frame(self):
        if self.current_frame is not None:
            self.current_frame.destroy()
            self.current_frame = None

    def switch_to_register(self, event=None):
        self.show_register()

    def switch_to_login(self, event=None):
        self.show_login()

    def handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        message = self.user.login(username, password)
        self.show_notif(message) 
   
        if message == "Login successful":
            self.show_dashboard()  

    def handle_register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        message = self.user.register(username, password)
        self.show_notif(message)  

    def show_login(self):
        self.clear_frame()

        mainFrame = tk.Frame(self, bg="#ffffff", width=420, padx=40, pady=30, height=400)
        mainFrame.place(relx=0.5, rely=0.5, anchor="center")
        mainFrame.pack_propagate(False)

        tk.Label(mainFrame, text="Welcome Back", bg="#ffffff",
                 font=("Arial", 22, "bold"), fg="#2d3748").pack(pady=(0,2))
        tk.Label(mainFrame, text="Sign in to continue", bg="#ffffff",
                 font=("Arial", 10), fg="#718096").pack(pady=(0,20))

        customtkinter.CTkLabel(mainFrame, text="Username", font=("Arial", 13),
                               anchor="w", fg_color="transparent",
                               text_color="black").pack(fill="x")
        self.username_entry = customtkinter.CTkEntry(
            mainFrame, border_width=1, border_color="#e6e6e6", font=("Arial", 13),
            placeholder_text="Enter Username", placeholder_text_color="#a8a8a8",
            text_color="black", fg_color="#ffffff"
        )
        self.username_entry.pack(fill="x", pady=(0,15), ipady=8)

        tk.Label(mainFrame, text="Password", bg="#ffffff",
                 font=("Arial", 10), fg="#4a5568", anchor="w").pack(fill="x")
        self.password_entry = customtkinter.CTkEntry(
            mainFrame, border_width=1, border_color="#e6e6e6", font=("Arial", 13),
            placeholder_text="Enter Password", placeholder_text_color="#a8a8a8",
            text_color="black", fg_color="#ffffff", show="*"
        )
        self.password_entry.pack(fill="x", pady=(4,20), ipady=8)

        customtkinter.CTkButton(mainFrame, command=self.handle_login,
                                text="Login", hover_color="#003a92",
                                fg_color="#4c40f7", cursor="hand2").pack(fill="x", pady=(0,15), ipady=8)

        tk.Label(mainFrame, text="Don't have an account?", bg="#ffffff",
                 fg="#718096", font=("Arial", 9), anchor="c").pack(side="left", padx=(74,0))
        signuplabel = tk.Label(mainFrame, text="Sign up", bg="#ffffff",
                               fg="#4c40f7", font=("Arial", 9, "bold"), cursor="hand2")
        signuplabel.pack(side="left")
        signuplabel.bind("<Button-1>", self.switch_to_register)

        self.current_frame = mainFrame

    def show_register(self):
        self.clear_frame()

        mainFrame = tk.Frame(self, bg="#ffffff", width=420, padx=40, pady=30, height=400)
        mainFrame.place(relx=0.5, rely=0.5, anchor="center")
        mainFrame.pack_propagate(False)

        tk.Label(mainFrame, text="Create Account", bg="#ffffff",
                 font=("Arial", 22, "bold"), fg="#2d3748").pack(pady=(0,2))
        tk.Label(mainFrame, text="Sign in to continue", bg="#ffffff",
                 font=("Arial", 10), fg="#718096").pack(pady=(0,20))

        customtkinter.CTkLabel(mainFrame, text="Username", font=("Arial", 13),
                               anchor="w", fg_color="transparent",
                               text_color="black").pack(fill="x")
        self.username_entry = customtkinter.CTkEntry(
            mainFrame, border_width=1, border_color="#e6e6e6", font=("Arial", 13),
            placeholder_text="Enter Username", placeholder_text_color="#a8a8a8",
            text_color="black", fg_color="#ffffff"
        )
        self.username_entry.pack(fill="x", pady=(0,15), ipady=8)

        tk.Label(mainFrame, text="Password", bg="#ffffff",
                 font=("Arial", 10), fg="#4a5568", anchor="w").pack(fill="x")
        self.password_entry = customtkinter.CTkEntry(
            mainFrame, border_width=1, border_color="#e6e6e6", font=("Arial", 13),
            placeholder_text="Enter Password", placeholder_text_color="#a8a8a8",
            text_color="black", fg_color="#ffffff", show="*"
        )
        self.password_entry.pack(fill="x", pady=(4,20), ipady=8)

        customtkinter.CTkButton(mainFrame, command=self.handle_register,
                                text="Register", hover_color="#003a92",
                                fg_color="#4c40f7", cursor="hand2").pack(fill="x", pady=(0,15), ipady=8)

        tk.Label(mainFrame, text="Already have an account?", bg="#ffffff",
                 fg="#718096", font=("Arial", 9), anchor="c").pack(side="left", padx=(74,0))
        signuplabel = tk.Label(mainFrame, text="Login", bg="#ffffff",
                               fg="#4c40f7", font=("Arial", 9, "bold"), cursor="hand2")
        signuplabel.pack(side="left")
        signuplabel.bind("<Button-1>", self.switch_to_login)

        self.current_frame = mainFrame

    def show_dashboard(self):
        self.clear_frame()

        dashFrame = tk.Frame(self, bg="#ffffff", width=600, height=400)
        dashFrame.place(relx=0.5, rely=0.5, anchor="center")
        dashFrame.pack_propagate(False)

        tk.Label(dashFrame, text=f"Welcome, {self.user.current_user}!",
                bg="#ffffff", font=("Arial", 20, "bold"), fg="#2d3748").pack(pady=20)

        customtkinter.CTkButton(dashFrame, text="Logout", fg_color="#4c40f7",
                                hover_color="#003a92", command=self.show_login).pack(pady=10)

        self.current_frame = dashFrame
