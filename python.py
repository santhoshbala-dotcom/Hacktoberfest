"<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lost & Found Inventory</title>
    <style>
        :root {{
            --bg-color: #f8fafc;
            --card-bg: #ffffff;
            --text-main: #0f172a;
            --text-muted: #64748b;
            --lost-color: #ef4444;
            --lost-bg: #fef2f2;
            --found-color: #10b981;
            --found-bg: #ecfdf5;
            --border: #e2e8f0;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }}

        body {{
            background-color: var(--bg-color);
            color: var(--text-main);
            padding: 2rem 1rem;
            max-width: 1100px;
            margin: 0 auto;
        }}

        header {{
            text-align: center;
            margin-bottom: 2rem;
        }}

        header h1 {{
            font-size: 2.25rem;
            margin-bottom: 0.5rem;
            color: #1e293b;
        }}

        header p {{
            color: var(--text-muted);
            font-size: 1rem;
        }}

        .search-container {{
            margin-bottom: 2rem;
            display: flex;
            justify-content: center;
        }}

        .search-input {{
            width: 100%;
            max-width: 500px;
            padding: 0.8rem 1.2rem;
            border: 2px solid var(--border);
            border-radius: 8px;
            font-size: 1rem;
            outline: none;
        }}

        .search-input:focus {{
            border-color: #3b82f6;
        }}

        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
        }}

        .card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        .card-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }}

        .item-name {{
            font-size: 1.25rem;
            font-weight: 600;
        }}

        .badge {{
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
        }}

        .badge-lost {{
            background-color: var(--lost-bg);
            color: var(--lost-color);
            border: 1px solid #fca5a5;
        }}

        .badge-found {{
            background-color: var(--found-bg);
            color: var(--found-color);
            border: 1px solid #6ee7b7;
        }}

        .card-body p {{
            font-size: 0.95rem;
            color: var(--text-muted);
            margin-bottom: 0.5rem;
        }}

        .empty-state {{
            text-align: center;
            grid-column: 1 / -1;
            padding: 3rem;
            color: var(--text-muted);
        }}
    </style>
</head>
<body>

    <header>
        <h1>🐾 Lost & Found Inventory</h1>
        <p>A dynamic registry powered by Python</p>
    </header>

    <div class="search-container">
        <input type="text" id="searchInput" class="search-input" placeholder="Search by item name or location..." onkeyup="filterItems()">
    </div>

    <div class="grid" id="itemGrid">
        {item_cards}
    </div>

    <script>
        function filterItems() {{
            const input = document.getElementById('searchInput').value.toLowerCase();
            const cards = document.getElementsByClassName('card');

            for (let i = 0; i < cards.length; i++) {{
                const text = cards[i].innerText.toLowerCase();
                cards[i].style.display = text.includes(input) ? "flex" : "none";
            }}
        }}
    </script>
</body>
</html>
def generate_item_card(item: Dict) -> str:
    status_class = "badge-lost" if item['status'].lower() == 'lost' else "badge-found"
    return f"""
        <div class="card">
            <div class="card-header">
                <span class="item-name">{item['name']}</span>
                <span class="badge {status_class}">{item['status']}</span>
            </div>
            <div class="card-body">
                <p><strong>📍 Location:</strong> {item['location']}</p>
                <p><strong>📞 Contact:</strong> {item['contact']}</p>
            </div>
        </div>"""

def generate_html_content(items: List[Dict]) -> str:
    if not items:
        cards_html = '<div class="empty-state"><h3>No items recorded yet.</h3></div>'
    else:
        cards_html = "\n".join([generate_item_card(item) for item in items])
    
    # Inject generated cards into the HTML template
    return HTML_TEMPLATE.format(item_cards=cards_html)

def save_html(content: str, filename: str = "index.html") -> None:
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n✅ Successfully generated web registry: {os.path.abspath(filename)}")
    except IOError as e:
        print(f"❌ Error writing file {filename}: {e}")
def get_validated_status() -> str:
    while True:
        status = input("Status (Lost/Found): ").strip().capitalize()
        if status in ["Lost", "Found"]:
            return status
        print("⚠️ Invalid input. Please enter 'Lost' or 'Found'.")

def run_cli_loop() -> List[Dict]:
    items: List[Dict] = []
    print("-" * 50)
    print("✨ Welcome to the Lost & Found Entry CLI ✨")
    print("-" * 50)

    while True:
        print("\n--- NEW ENTRY ---")
        item_name = input("Enter Item Name: ").strip()
        if not item_name:
            print("Item name is required. Skipping this entry.")
            continue

        status = get_validated_status()
        location = input("Location/Place found/lost: ").strip() or "Unknown Location"
        contact = input("Contact Info (Name/Email/Phone): ").strip() or "N/A"

        items.append({
            "name": item_name,
            "status": status,
            "location": location,
            "contact": contact
        })

        print(f"✅ Item '{item_name}' recorded successfully.")

        continue_choice = input("\nAdd another entry? (y/n): ").strip().lower()
        if continue_choice != 'y':
            break

    print("\n==========================================")
    print("💾 Data collection finished. Processing files...")
    print("==========================================")
    return items
def main():
    collected_items = run_cli_loop()
    if not collected_items:
        print("No items were entered. Exiting without generating HTML.")
        return

    html_content = generate_html_content(collected_items)
    save_html(html_content)

if _name_ == "_main_":
    main()
