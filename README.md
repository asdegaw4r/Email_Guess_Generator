# Email_Guess_Generator


A small Python tool that's perfect for reaching that company guy you're trying to get an internship from through email BCC. creates up to 100 possible email address formats for a given first name, last name, and domain.
Useful for lead research, internal directory reconstruction, or verifying possible contact formats before using any email verification or outreach tools.

📦 Features

Generates 100 plausible email address permutations using common naming patterns (first.last, f.last, firstl, etc.).

Saves results to a clean CSV file in your Documents folder.

Requires only Python 3 — no external libraries.

⚙️ Installation

Clone or copy this repository:

git clone https://github.com/yourusername/email_guess_generator.git
cd email_guess_generator


(Optional) Make the script executable:

chmod +x generate_guesses.py


Verify Python 3 is installed:

python3 --version


If not, install from python.org
 or via Homebrew:

brew install python

🚀 Usage

From the terminal, run:

python3 generate_guesses.py First Last domain.com


Example:

python3 generate_guesses.py John Doe example.com


This creates:

~/Documents/john_doe_email_guesses.csv

🧾 Output Example
email
john@example.com

j.doe@example.com

john.doe@example.com

johnd@example.com

jdoe@example.com

john.doe1@example.com

johndoe01@example.com

... (up to 100 entries)
📂 Output Location

Generated files are automatically written to:

~/Documents/<first>_<last>_email_guesses.csv

⚠️ Ethical & Legal Use

This script only generates potential email formats — it does not send or verify messages.
If you plan to contact anyone using guessed emails:

Always verify addresses with a trusted service (e.g., Hunter.io, ZeroBounce).

Do not mass-email or BCC unverified addresses.

Respect privacy laws such as CAN-SPAM (US) and GDPR (EU).

Use responsibly for professional outreach, never for spam or unsolicited messaging.

🧠 Author Notes

This project was designed to simplify the process of generating predictable corporate email structures safely and locally, without relying on cloud APIs.
You own and control all generated data.

🛠 Example Workflow

Generate guesses:

python3 generate_guesses.py Jane Smith company.com


Verify output CSV with an email verifier API.

Manually confirm valid addresses before any outreach.

🧩 License

MIT License — free for personal and commercial use with attribution.
