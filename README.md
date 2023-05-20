## How to use

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the script

```bash
python main.py
```

# Use case

This program takes an invoice and extracts the desired information from it using Azure services.

## Input

The invoices are in folders that are organized by year, then country and finally (in some cases) category, e.g.

```
├── 2019
│   ├── de
│   │   ├── **/*.pdf
│   ├── uk
│   │   ├── **/*.pdf
│   ├── es
│   │   ├── public transport
│   │   │   ├── **/*.pdf
├── 2020
│   ├── de
│   │   ├── cafe
│   │   │   ├── **/*.pdf
│   │   ├── hotel
│   │   │   ├── **/*.pdf
│   ├── pl
│   │   ├── restaurant
│   │   │   ├── **/*.pdf
```

## Output

The final product is a csv with the following information:

- File name
- Vendor's name
- Vendor's address
- Country where it was emitted
- Address where it was emitted
- Date
- Payment type
- Subtotal
- Total taxes
- Total
- Quantity of items
- Category of bought items (food, transportation, etc)

This information is translated to spanish before being saved.

## Invoices

You can find the invoices in `./resources`
