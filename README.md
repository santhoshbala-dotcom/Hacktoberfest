
# 🔍 Campus & Office Lost & Found Portal

> A lightweight, zero-dependency Python CLI tool that converts interactive terminal inputs into a clean, searchable web page for Lost & Found items.

---

## 📌 Problem Statement

Many colleges, student housing communities, and offices still rely on cluttered WhatsApp groups, Slack channels, or physical paper notices to post about lost items. Important messages quickly get buried in active group chats, making it frustrating and inefficient to track down lost property.

**Lost & Found Portal** solves this problem by allowing anyone to quickly log items through a simple terminal interface. The script automatically synthesizes these entries into a modern, responsive, single-page web directory (`index.html`) equipped with real-time search filtering.

---

## ✨ Features

- 🐍 **Zero External Dependencies**: Built strictly with standard Python 3 libraries—no `pip install`, Flask, or Jinja2 required.
- ⚡ **Instant HTML Generation**: Generates a self-contained `index.html` file in seconds.
- 🎨 **Modern Card Layout**: Clean CSS grid styling featuring color-coded status badges (**LOST** vs **FOUND**).
- 🔍 **Real-Time Client-Side Search**: Built-in vanilla JavaScript allows users to instantly search items by name, location, or status without reloading the page.
- 📱 **Fully Responsive**: Designed to display properly on desktop, tablet, and mobile browsers.

---

## 🛠️ Project Architecture

The application is contained within a single Python script (`python.py` or `app.py`) divided into four modular sections:

```
┌────────────────────────────────────────────────────────┐
│ SECTION 1: Embedded HTML, CSS & JavaScript Template    │
├────────────────────────────────────────────────────────┤
│ SECTION 2: Data Processing & HTML Card Compiler        │
├────────────────────────────────────────────────────────┤
│ SECTION 3: Terminal CLI Input & Validation Loop        │
├────────────────────────────────────────────────────────┤
│ SECTION 4: Main Application Execution                  │
└────────────────────────────────────────────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites

All you need is **Python 3.x** installed on your system.

### Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/lost-and-found-generator.git
   cd lost-and-found-generator
   ```

2. **Run the Script**
   ```bash
   python python.py
   ```

3. **Enter Item Details**
   Follow the interactive terminal prompts:
   - Enter the item name (e.g., `Blue Water Bottle`)
   - Select the status (`Lost` or `Found`)
   - Enter the location (e.g., `Library 2nd Floor`)
   - Provide contact info (e.g., `Desk 4 / Alex`)
   - Indicate whether to add another entry (`y/n`)

4. **View Your Web Page**
   Open the newly created `index.html` file directly in any web browser to view your portal!

---

## 🖥️ Sample CLI Workflow

```text
==================================================
           LOST & FOUND ENTRY CLI             
==================================================

--- NEW ENTRY ---
Enter Item Name: Blue Water Bottle
Status (Lost/Found): Found
Location/Place found/lost: Science Building Lab 3
Contact Info (Name/Email/Phone): Security Desk

✅ Item 'Blue Water Bottle' recorded successfully.

Add another entry? (y/n): n

Data collection finished. Processing files...
✅ Successfully generated web registry: /path/to/index.html
```

---

## 🤝 Contributing

Contributions make the open-source community an incredible place to learn, inspire, and create. Any contributions you make are **greatly appreciated**!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
