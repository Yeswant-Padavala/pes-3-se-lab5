"""Cleaned Inventory System Module
This module provides functions to manage an inventory system, including adding/removing items,
loading/saving data, and printing reports. It includes error handling"""
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Global variable
stock_data = {}

def addItem(item="default", qty=0, logs=[]):
    """Adds an item to the stock_data with the specified quantity and logs the action."""
    if logs is None:
        logs = []
    
    if not item or not isinstance(item, str):
        logger.warning(f"Invalid item name: {item}")
        return
    
    if not isinstance(qty, int):
        logger.warning(f"Invalid quantity type for {item}: {type(qty)}")
        return
    
    stock_data[item] = stock_data.get(item, 0) + qty
    log_message = f"{datetime.now()}: Added {qty} of {item}"
    logs.append(log_message)
    logger.info(log_message)

def removeItem(item, qty):
    """Removes the specified quantity of an item from stock_data."""
    if not isinstance(item, str) or not isinstance(qty, int):
        logger.warning(f"Invalid types: item={type(item)}, qty={type(qty)}")
        return False
    
    try:
        if item not in stock_data:
            logger.warning(f"Item '{item}' not found in inventory")
            return False
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            logger.info(f"Item '{item}' removed from inventory (quantity reached 0)")
        return True
    except KeyError as e:
        logger.error(f"KeyError when removing {item}: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error removing {item}: {e}")
        return False

def getQty(item):
    """Returns the quantity of the specified item in stock_data."""
    return stock_data[item]

def loadData(file="inventory.json"):
    """Loads stock data from a JSON file into stock_data."""
    global stock_data
    try:
        with open(file, "r") as f:
            stock_data = json.load(f)
        logger.info(f"Data loaded from {file}")
        return True
    except FileNotFoundError:
        logger.warning(f"File {file} not found, starting with empty inventory")
        stock_data = {}
        return False
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in {file}: {e}")
        return False
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        return False

def saveData(file="inventory.json"):
    """Saves the current stock_data to a JSON file."""
    try:
        with open(file, "w") as f:
            json.dump(stock_data, f, indent=2)
        logger.info(f"Data saved to {file}")
        return True
    except IOError as e:
        logger.error(f"Error saving data to {file}: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error saving data: {e}")
        return False

def printData():
    """Prints a report of all items in stock_data."""
    print("\n=== Items Report ===")
    if not stock_data:
        print("Inventory is empty")
        return
    
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")
    print("=" * 20)

def checkLowItems(threshold=5):
    """Returns a list of items with quantities below the specified threshold."""
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    # Load existing data
    loadData()
    
    # Valid operations
    addItem("apple", 10)
    
    # Invalid operations (will be logged but not crash)
    addItem("banana", -2)  # Negative quantity
    addItem(123, "ten")  # Invalid types - will be rejected
    
    # Remove items
    removeItem("apple", 3)
    removeItem("orange", 1)  # Item doesn't exist - handled gracefully

    # Query data
    print(f"Apple stock: {getQty('apple')}")
    print(f"Low items: {checkLowItems()}")
    
    # Save and display
    saveData()
    printData()
    
    # Removed dangerous eval()

main()
