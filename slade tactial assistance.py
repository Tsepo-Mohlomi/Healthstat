    self.chat_log = tk.Text(root, bg="#1e1e1e", fg="lime", font=("Consolas", 10))
    self.chat_log.pack(expand=True, fill=tk.BOTH)

    self.entry = tk.Entry(root, bg="#333", fg="#fff", insertbackground='white')
    self.entry.pack(fill=tk.X, padx=5, pady=5)
    self.entry.bind("<Return>", self.send_message)

    self.btn_frame = tk.Frame(root, bg="#1e1e1e")
    self.btn_frame.pack(fill=tk.X, pady=5)

    self.send_btn = tk.Button(self.btn_frame, text="Send", command=self.send_message)
    self.send_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

    self.worm_btn = tk.Button(self.btn_frame, text="WormGPT", command=self.worm_send)
    self.worm_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

    self.time_label = tk.Label(root, fg="gray", bg="#1e1e1e", font=("Consolas", 9))
    self.time_label.pack(side=tk.BOTTOM, pady=3)
    self.update_time()

    if speech_available:
        self.voice_btn = tk.Button(root, text="🎤 Voice", command=self.voice_input)
        self.voice_btn.pack(side=tk.BOTTOM, pady=5)

    self.chat_log.insert(tk.END, "Slade: Tactical AI online. Type your command.\n\n")

def update_time(self):
    now = datetime.datetime.now().strftime("🕒 %H:%M:%S")
    self.time_label.config(text=now)
    self.root.after(1000, self.update_time)

def send_message(self, event=None):
    user_input = self.entry.get()
    if not user_input.strip():
        return
    self.chat_log.insert(tk.END, f"You: {user_input}\n")
    response = slade_response(user_input)
    self.chat_log.insert(tk.END, f"Slade: {response}\n\n")
    self.entry.delete(0, tk.END)
    slade_voice.say(response)
    slade_voice.runAndWait()

def worm_send(self):
    user_input = self.entry.get()
    if not user_input.strip():
        return
    response = send_to_wormgpt(user_input)
    self.chat_log.insert(tk.END, f"WormGPT: {response}\n\n")
    self.entry.delete(0, tk.END)

def voice_input(self):
    if not speech_available:
        return
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        self.chat_log.insert(tk.END, "Listening...\n")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            self.entry.insert(0, text)
            self.send_message()
        except Exception as e:
            self.chat_log.insert(tk.END, "Slade: I didn't catch that, boss.\n\n")
