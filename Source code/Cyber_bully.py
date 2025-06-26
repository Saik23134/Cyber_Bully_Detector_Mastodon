import tkinter as tk
from tkinter import messagebox, scrolledtext
from better_profanity import profanity
from mastodon import Mastodon
import webbrowser
import re

# Mastodon API Setup
MASTODON_INSTANCE = 'https://mastodon.social'  # Change if using another instance
ACCESS_TOKEN = 'QEyRlshAo62PNteK7Flh5sfaiXPEFoXnOsMUUGRdQ38'  # Replace with your actual token

mastodon = Mastodon(
    access_token=ACCESS_TOKEN,
    api_base_url=MASTODON_INSTANCE
)

profanity.load_censor_words()

# Function to check posts
def get_bad_posts(username):
    try:
        account = mastodon.account_search(username)
        if not account:
            messagebox.showerror("Error", "User not found.")
            return []

        account_id = account[0]['id']
        statuses = mastodon.account_statuses(account_id, limit=50)
        bad_posts = []

        for status in statuses:
            text = status['content']
            clean_text = re.sub('<[^<]+?>', '', text)  # Remove HTML tags
            if profanity.contains_profanity(clean_text):
                bad_posts.append((clean_text, status['url']))

        return bad_posts

    except Exception as e:
        messagebox.showerror("Error", str(e))
        return []

# GUI
def display_results():
    username = entry.get().strip().lstrip('@')
    results_box.delete(1.0, tk.END)
    bad_posts = get_bad_posts(username)

    if not bad_posts:
        results_box.insert(tk.END, "No bad words found in recent posts.\n")
    else:
        for idx, (text, url) in enumerate(bad_posts, 1):
            results_box.insert(tk.END, f"{idx}. {text}\n")
            results_box.insert(tk.END, f"Link: {url}\n\n")

def open_link(event):
    index = results_box.index("@%s,%s" % (event.x, event.y))
    line = results_box.get(f"{index} linestart", f"{index} lineend")
    if line.startswith("Link: "):
        url = line.replace("Link: ", "").strip()
        webbrowser.open(url)

# Main window
root = tk.Tk()
root.title("Cyber Bully Detector")
root.geometry("600x500")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

check_button = tk.Button(root, text="Check Posts", command=display_results)
check_button.pack(pady=5)

results_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20)
results_box.pack(pady=10)
results_box.bind("<Button-1>", open_link)

root.mainloop()
