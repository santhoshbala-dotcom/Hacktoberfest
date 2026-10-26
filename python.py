def generate_item_card(item: Dict) -> str:
    """Generates the HTML card structure for a single item."""
    status_class = f"status-{item['status'].lower()}"

    # Sanitize data for display
    name = item['name'].strip()
    location = item['location'].strip()
    contact = item['contact'].strip()

    return f"""
    <div class="item-card" data-name="{name.lower()}" data-location="{location.lower()}">
        <span class="status-badge {status_class}">{item['status']}</span>
        <h3>{name}</h3>
        <div class="detail-row">
            <strong>Location/Place:</strong> {location}
        </div>
        <div class="detail-row">
            <strong>Contact Info:</strong> {contact if contact else 'N/A'}
        </div>
    </div>
    """

def generate_html_content(items: List[Dict]) -> str:
    """
    Takes a list of item dictionaries and compiles them into the final HTML body content.
    """
    # Generate all the individual cards
    item_cards = "\n".join([generate_item_card(item) for item in items])

    # Inject the cards into the main template
    return HTML_TEMPLATE.format(item_cards=item_cards)

def save_html(content: str, filename: str = "index.html") -> None:
    """Writes the generated HTML string to a specified file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n✅ Successfully generated web registry: {os.path.abspath(filename)}")
    except IOError as e:
        print(f"❌ Error writing file {filename}: {e}")

def get_validated_status() -> str:
    """Prompts user for status and validates against 'Lost' or 'Found'."""
    while True:
        status = input("Status (Lost/Found): ").strip().capitalize()
        if status in ["Lost", "Found"]:
            return status
        print("⚠️ Invalid input. Please enter 'Lost' or 'Found'.")

def run_cli_loop() -> List[Dict]:
    """Main loop for collecting user input."""
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

        # Collect required fields
        status = get_validated_status()
        location = input("Location/Place found/lost: ").strip()
        contact = input("Contact Info (Name/Email/Phone): ").strip()

        # Store data
        items.append({
            "name": item_name,
            "status": status,
            "location": location,
            "contact": contact
        })

        print(f"\n✅ Item '{item_name}' recorded successfully.")

        # Check for termination condition
        continue_choice = input("\nAdd another entry? (y/n): ").lower()
        if continue_choice != 'y':
            break

    print("\n=======================================")
    print("💾 Data collection finished. Processing files...")
    print("=======================================")
    return items
def main():
    """The entry point for the application."""

    # 1. Collect data via CLI
    collected_items = run_cli_loop()

    if not collected_items:
        print("No items were entered. Exiting without generating HTML.")
        return

    # 2. Generate HTML content
    html_content = generate_html_content(collected_items)

    # 3. Save file
    save_html(html_content)

if __name__ == "__main__":
    main()