import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_products():
    """Reads product data from a JSON file."""
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def read_csv_products():
    """Reads product data from a CSV file."""
    products = []
    try:
        with open("products.csv", "r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                try:
                    row["id"] = int(row["id"])
                    row["price"] = float(row["price"])
                    products.append(row)
                except (ValueError, KeyError):
                    continue  # Skip invalid rows
        return products
    except (FileNotFoundError, csv.Error):
        return None


@app.route("/products")
def products_list():
    """
    Displays products from JSON or CSV based on the 'source' query parameter.
    Filters by 'id' if provided.
    """
    source = request.args.get("source")
    product_id = request.args.get("id")

    data = None
    error = None

    if source == "json":
        data = read_json_products()
    elif source == "csv":
        data = read_csv_products()
    else:
        error = "Wrong source. Please specify 'json' or 'csv'."

    if data is None and error is None:
        error = "Could not load data from the specified source."

    if data and product_id:
        try:
            product_id = int(product_id)
            filtered_data = [p for p in data if p["id"] == product_id]
            if not filtered_data:
                error = "Product not found."
            data = filtered_data
        except ValueError:
            error = "Invalid product ID. ID must be an integer."
            data = None

    return render_template("product_display.html", products=data, error=error)


if __name__ == "__main__":
    app.run(debug=True, port=5000)